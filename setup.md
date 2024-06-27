
# Setup Instructions

Make sure the cluster and the nodes are up and running before proceeding.

## Enable OIDC for the cluster


```bash
eksctl utils associate-iam-oidc-provider --region ${REGION} --cluster ${CLUSTER_NAME} --approve
```

## Install the Metrics API

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Setup GPU Metrics collection

Remove NVIDIA device plugin

```bash
kubectl -n kube-system delete daemonset nvidia-device-plugin-daemonset
```

Install  NVIDIA GPU Operator


```bash
kubectl create namespace gpu-operator
curl https://raw.githubusercontent.com/NVIDIA/dcgm-exporter/main/etc/dcp-metrics-included.csv > dcgm-metrics.csv
kubectl create configmap metrics-config -n gpu-operator --from-file=dcgm-metrics.csv
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update

helm install --wait \
	--generate-name -n gpu-operator \
	--create-namespace nvidia/gpu-operator \
	--set "dcgmExporter.config.name"=metrics-config \
	--set "dcgmExporter.env[0].name"=DCGM_EXPORTER_COLLECTORS \
	--set "dcgmExporter.env[0].value"=/etc/dcgm-exporter/dcgm-metrics.csv \
	--set toolkit.enabled=false
```


Make sure the logs in the following commands's output say "Starting webserver".
```bash
kubectl -n gpu-operator logs -f $(kubectl -n gpu-operator get pods | grep dcgm | cut -d ' ' -f 1 | head -n 1)
```


## Enable S3 Read Only access

create a policy for read-only s3 access for a specific bucket

```bash
aws iam create-policy \
    --policy-name S3ListEMLOS19 \
    --policy-document file://01_iam-s3-test-policy.json
```

Create IRSA for the above policy    

```bash
eksctl create iamserviceaccount \
  --name s3-list-sa \
  --cluster ${CLUSTER_NAME} \
  --attach-policy-arn arn:aws:iam::${ACCOUNT_ID}:policy/S3ListEMLOS19 \
  --approve \
  --region ${REGION}
```


```bash
kubectl describe sa s3-list-sa
```

## (Optional) Enable EBS Access

Create IRSA for EBS

```bash
eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster ${CLUSTER_NAME} \
  --role-name AmazonEKS_EBS_CSI_DriverRole \
  --role-only \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --region ${REGION}
```

Create the EBS CSI Driver Addon
```bash
eksctl create addon --name aws-ebs-csi-driver --cluster ${CLUSTER_NAME} --service-account-role-arn arn:aws:iam::${ACCOUNT_ID}:role/AmazonEKS_EBS_CSI_DriverRole --region ${REGION} --force
```


## Istio Installation

```bash
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

kubectl create namespace istio-system
helm install istio-base istio/base -n istio-system --set defaultRevision=default --wait
helm install istiod istio/istiod -n istio-system --wait
kubectl create namespace istio-ingress
```



```bash
helm install istio-ingress istio/gateway -n istio-ingress \
  --set "labels.istio=ingressgateway" \
  --set service.annotations."service\beta\.kubernetes\.io/aws-load-balancer-type"="nlb" \
  --set service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-scheme"="internet-facing" \
  --set service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-attributes"="load_balancing.cross_zone.enabled=true" \
  --wait

kubectl rollout restart deployment istio-ingress -n istio-ingress
```


## Install Addons

```bash
for ADDON in kiali jaeger prometheus grafana
do
    ADDON_URL="https://raw.githubusercontent.com/istio/istio/1.19.3/samples/addons/$ADDON.yaml"
    kubectl apply -f $ADDON_URL
done
```


Modify Prometheus to collect logs from DGCA (lines added and the resulting file is already present in repo)
```bash
kubectl apply -f 02_prometheus.yaml
```
## Create DCGM Dashboard in Grafana

Download DCGM Grafana Dashboard JSON from [grafana.com](https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/) and create dashboard.


## Enable SideCar Injection

```bash
kubectl label namespace default istio-injection=enabled
```

## Install the Gateway CRDs

```bash
kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v0.8.0" | kubectl apply -f -; }
```


## Install KServe

```bash
kubectl apply -f 04_istio-kserve-ingress.yaml	
```



## Install Cert Manager
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.1/cert-manager.yaml
```

## Install KServe Manifest
```bash
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.1/kserve.yaml
```
## Install KServe Runtime
```bash
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.1/kserve-runtimes.yaml

kubectl patch configmap/inferenceservice-config -n kserve --type=strategic -p '{"data": {"deploy": "{\"defaultDeploymentMode\": \"RawDeployment\"}"}}'
```

## Create 'Secret' for S3 Access

```bash
eksctl create iamserviceaccount \
	--cluster=${CLUSTER_NAME} \
	--name=s3-read-only \
	--attach-policy-arn=arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
	--override-existing-serviceaccounts \
	--region ${REGION} \
	--approve
	
kubectl apply -f 05_s3-secret.yaml

kubectl patch serviceaccount s3-read-only -p '{"secrets": [{"name": "s3-secret"}]}'
```

