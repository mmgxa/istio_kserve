```
NAMESPACE       NAME                                                                  READY   STATUS      RESTARTS      AGE
cert-manager    pod/cert-manager-cainjector-65c7bff89d-zv42n                          1/1     Running     0             42m
cert-manager    pod/cert-manager-cbcf9668d-wbx7w                                      1/1     Running     0             42m
cert-manager    pod/cert-manager-webhook-594cb9799b-chhgd                             1/1     Running     0             42m
default         pod/torchserve-predictor-58f6699b89-r5skg                             2/2     Running     0             38m
gpu-operator    pod/gpu-feature-discovery-qmpn9                                       1/1     Running     0             49m
gpu-operator    pod/gpu-operator-1697535794-node-feature-discovery-master-6d6fknn7q   1/1     Running     0             49m
gpu-operator    pod/gpu-operator-1697535794-node-feature-discovery-worker-7jvhb       1/1     Running     0             49m
gpu-operator    pod/gpu-operator-1697535794-node-feature-discovery-worker-lj98q       1/1     Running     0             49m
gpu-operator    pod/gpu-operator-1697535794-node-feature-discovery-worker-szjbh       1/1     Running     0             49m
gpu-operator    pod/gpu-operator-59bfbb6bdc-4fsfj                                     1/1     Running     0             49m
gpu-operator    pod/nvidia-cuda-validator-d9nkl                                       0/1     Completed   0             49m
gpu-operator    pod/nvidia-dcgm-exporter-2m9vg                                        1/1     Running     0             49m
gpu-operator    pod/nvidia-device-plugin-daemonset-zxng2                              1/1     Running     0             49m
gpu-operator    pod/nvidia-operator-validator-bknlf                                   1/1     Running     0             49m
istio-ingress   pod/istio-ingress-96c4d5694-vcz9v                                     1/1     Running     0             44m
istio-system    pod/grafana-b8bbdc84d-k8p5q                                           1/1     Running     0             43m
istio-system    pod/istiod-54f986b554-qg6j8                                           1/1     Running     0             45m
istio-system    pod/jaeger-7d7d59b9d-dqqlg                                            1/1     Running     0             43m
istio-system    pod/kiali-58d8c9c978-hctmh                                            1/1     Running     0             43m
istio-system    pod/prometheus-db8b4588f-t2qhd                                        2/2     Running     0             43m
kserve          pod/kserve-controller-manager-5d995bd58-28q5w                         2/2     Running     1 (39m ago)   41m
kube-system     pod/aws-node-7ns2h                                                    2/2     Running     0             53m
kube-system     pod/aws-node-lmzv6                                                    2/2     Running     0             53m
kube-system     pod/aws-node-zzvnm                                                    2/2     Running     0             53m
kube-system     pod/coredns-59754897cf-675dc                                          1/1     Running     0             60m
kube-system     pod/coredns-59754897cf-cf2m8                                          1/1     Running     0             60m
kube-system     pod/ebs-csi-controller-846fc648c9-5hw9l                               6/6     Running     0             45m
kube-system     pod/ebs-csi-controller-846fc648c9-dfszj                               6/6     Running     0             45m
kube-system     pod/ebs-csi-node-4ngx6                                                3/3     Running     0             45m
kube-system     pod/ebs-csi-node-kmqnz                                                3/3     Running     0             45m
kube-system     pod/ebs-csi-node-p4xdj                                                3/3     Running     0             45m
kube-system     pod/kube-proxy-bl47q                                                  1/1     Running     0             53m
kube-system     pod/kube-proxy-gnklp                                                  1/1     Running     0             53m
kube-system     pod/kube-proxy-zllgg                                                  1/1     Running     0             53m
kube-system     pod/metrics-server-fbb469ccc-22n9c                                    1/1     Running     0             50m

NAMESPACE       NAME                                                            TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)                                          AGE
cert-manager    service/cert-manager                                            ClusterIP      10.100.49.118    <none>                                                                    9402/TCP                                         42m
cert-manager    service/cert-manager-webhook                                    ClusterIP      10.100.31.223    <none>                                                                    443/TCP                                          42m
default         service/kubernetes                                              ClusterIP      10.100.0.1       <none>                                                                    443/TCP                                          61m
default         service/torchserve-predictor                                    ClusterIP      10.100.216.216   <none>                                                                    80/TCP                                           38m
gpu-operator    service/gpu-operator                                            ClusterIP      10.100.242.87    <none>                                                                    8080/TCP                                         49m
gpu-operator    service/gpu-operator-1697535794-node-feature-discovery-master   ClusterIP      10.100.86.193    <none>                                                                    8080/TCP                                         49m
gpu-operator    service/nvidia-dcgm-exporter                                    ClusterIP      10.100.230.176   <none>                                                                    9400/TCP                                         49m
istio-ingress   service/istio-ingress                                           LoadBalancer   10.100.9.82      af095ccc95c874abcb7a8410b9e84b37-1042384974.us-west-2.elb.amazonaws.com   15021:32637/TCP,80:30686/TCP,443:32556/TCP       44m
istio-system    service/grafana                                                 ClusterIP      10.100.155.209   <none>                                                                    3000/TCP                                         43m
istio-system    service/istiod                                                  ClusterIP      10.100.185.102   <none>                                                                    15010/TCP,15012/TCP,443/TCP,15014/TCP            45m
istio-system    service/jaeger-collector                                        ClusterIP      10.100.188.162   <none>                                                                    14268/TCP,14250/TCP,9411/TCP,4317/TCP,4318/TCP   43m
istio-system    service/kiali                                                   ClusterIP      10.100.68.55     <none>                                                                    20001/TCP,9090/TCP                               43m
istio-system    service/prometheus                                              ClusterIP      10.100.245.189   <none>                                                                    9090/TCP                                         43m
istio-system    service/tracing                                                 ClusterIP      10.100.121.168   <none>                                                                    80/TCP,16685/TCP                                 43m
istio-system    service/zipkin                                                  ClusterIP      10.100.124.225   <none>                                                                    9411/TCP                                         43m
kserve          service/kserve-controller-manager-metrics-service               ClusterIP      10.100.46.35     <none>                                                                    8443/TCP                                         41m
kserve          service/kserve-controller-manager-service                       ClusterIP      10.100.207.160   <none>                                                                    8443/TCP                                         41m
kserve          service/kserve-webhook-server-service                           ClusterIP      10.100.255.9     <none>                                                                    443/TCP                                          41m
kube-system     service/kube-dns                                                ClusterIP      10.100.0.10      <none>                                                                    53/UDP,53/TCP                                    60m
kube-system     service/metrics-server                                          ClusterIP      10.100.181.184   <none>                                                                    443/TCP                                          50m

NAMESPACE      NAME                                                                   DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                                      AGE
gpu-operator   daemonset.apps/gpu-feature-discovery                                   1         1         1       1            1           nvidia.com/gpu.deploy.gpu-feature-discovery=true   49m
gpu-operator   daemonset.apps/gpu-operator-1697535794-node-feature-discovery-worker   3         3         3       3            3           <none>                                             49m
gpu-operator   daemonset.apps/nvidia-dcgm-exporter                                    1         1         1       1            1           nvidia.com/gpu.deploy.dcgm-exporter=true           49m
gpu-operator   daemonset.apps/nvidia-device-plugin-daemonset                          1         1         1       1            1           nvidia.com/gpu.deploy.device-plugin=true           49m
gpu-operator   daemonset.apps/nvidia-driver-daemonset                                 0         0         0       0            0           nvidia.com/gpu.deploy.driver=true                  49m
gpu-operator   daemonset.apps/nvidia-mig-manager                                      0         0         0       0            0           nvidia.com/gpu.deploy.mig-manager=true             49m
gpu-operator   daemonset.apps/nvidia-operator-validator                               1         1         1       1            1           nvidia.com/gpu.deploy.operator-validator=true      49m
kube-system    daemonset.apps/aws-node                                                3         3         3       3            3           <none>                                             60m
kube-system    daemonset.apps/ebs-csi-node                                            3         3         3       3            3           kubernetes.io/os=linux                             45m
kube-system    daemonset.apps/ebs-csi-node-windows                                    0         0         0       0            0           kubernetes.io/os=windows                           45m
kube-system    daemonset.apps/kube-proxy                                              3         3         3       3            3           <none>                                             60m

NAMESPACE       NAME                                                                    READY   UP-TO-DATE   AVAILABLE   AGE
cert-manager    deployment.apps/cert-manager                                            1/1     1            1           42m
cert-manager    deployment.apps/cert-manager-cainjector                                 1/1     1            1           42m
cert-manager    deployment.apps/cert-manager-webhook                                    1/1     1            1           42m
default         deployment.apps/torchserve-predictor                                    1/1     1            1           38m
gpu-operator    deployment.apps/gpu-operator                                            1/1     1            1           49m
gpu-operator    deployment.apps/gpu-operator-1697535794-node-feature-discovery-master   1/1     1            1           49m
istio-ingress   deployment.apps/istio-ingress                                           1/1     1            1           44m
istio-system    deployment.apps/grafana                                                 1/1     1            1           43m
istio-system    deployment.apps/istiod                                                  1/1     1            1           45m
istio-system    deployment.apps/jaeger                                                  1/1     1            1           43m
istio-system    deployment.apps/kiali                                                   1/1     1            1           43m
istio-system    deployment.apps/prometheus                                              1/1     1            1           43m
kserve          deployment.apps/kserve-controller-manager                               1/1     1            1           41m
kube-system     deployment.apps/coredns                                                 2/2     2            2           60m
kube-system     deployment.apps/ebs-csi-controller                                      2/2     2            2           45m
kube-system     deployment.apps/metrics-server                                          1/1     1            1           50m

NAMESPACE       NAME                                                                               DESIRED   CURRENT   READY   AGE
cert-manager    replicaset.apps/cert-manager-cainjector-65c7bff89d                                 1         1         1       42m
cert-manager    replicaset.apps/cert-manager-cbcf9668d                                             1         1         1       42m
cert-manager    replicaset.apps/cert-manager-webhook-594cb9799b                                    1         1         1       42m
default         replicaset.apps/torchserve-predictor-58f6699b89                                    1         1         1       38m
gpu-operator    replicaset.apps/gpu-operator-1697535794-node-feature-discovery-master-6d6fcf875b   1         1         1       49m
gpu-operator    replicaset.apps/gpu-operator-59bfbb6bdc                                            1         1         1       49m
istio-ingress   replicaset.apps/istio-ingress-55d9c6654b                                           0         0         0       44m
istio-ingress   replicaset.apps/istio-ingress-96c4d5694                                            1         1         1       44m
istio-system    replicaset.apps/grafana-b8bbdc84d                                                  1         1         1       43m
istio-system    replicaset.apps/istiod-54f986b554                                                  1         1         1       45m
istio-system    replicaset.apps/jaeger-7d7d59b9d                                                   1         1         1       43m
istio-system    replicaset.apps/kiali-58d8c9c978                                                   1         1         1       43m
istio-system    replicaset.apps/prometheus-db8b4588f                                               1         1         1       43m
kserve          replicaset.apps/kserve-controller-manager-5d995bd58                                1         1         1       41m
kube-system     replicaset.apps/coredns-59754897cf                                                 2         2         2       60m
kube-system     replicaset.apps/ebs-csi-controller-846fc648c9                                      2         2         2       45m
kube-system     replicaset.apps/metrics-server-fbb469ccc                                           1         1         1       50m

NAMESPACE       NAME                                                       REFERENCE                         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
default         horizontalpodautoscaler.autoscaling/torchserve-predictor   Deployment/torchserve-predictor   0%/80%    1         1         1          38m
istio-ingress   horizontalpodautoscaler.autoscaling/istio-ingress          Deployment/istio-ingress          3%/80%    1         5         1          44m
istio-system    horizontalpodautoscaler.autoscaling/istiod                 Deployment/istiod                 0%/80%    1         5         1          45m
```
