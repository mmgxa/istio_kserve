```
2023-10-17T10:13:21,920 [INFO ] epollEventLoopGroup-3-3 TS_METRICS - ts_inference_requests_total.Count:1.0|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537601
2023-10-17T10:13:21,921 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req.cmd PREDICT to backend at: 1697537601921
2023-10-17T10:13:21,922 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - Backend received inference at: 1697537601
2023-10-17T10:13:21,923 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - received text: 'a cat programming on a beach'
2023-10-17T10:13:21,957 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 
2023-10-17T10:13:22,752 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   0%|          | 0/50 [00:00<?, ?it/s]
2023-10-17T10:13:23,588 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   2%|▏         | 1/50 [00:00<00:38,  1.26it/s]
2023-10-17T10:13:24,428 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   4%|▍         | 2/50 [00:01<00:39,  1.22it/s]
2023-10-17T10:13:25,270 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   6%|▌         | 3/50 [00:02<00:38,  1.21it/s]
2023-10-17T10:13:26,104 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   8%|▊         | 4/50 [00:03<00:38,  1.20it/s]
2023-10-17T10:13:26,939 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  10%|█         | 5/50 [00:04<00:37,  1.20it/s]
2023-10-17T10:13:27,769 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  12%|█▏        | 6/50 [00:04<00:36,  1.20it/s]
2023-10-17T10:13:28,610 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  14%|█▍        | 7/50 [00:05<00:35,  1.20it/s]
2023-10-17T10:13:29,447 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  16%|█▌        | 8/50 [00:06<00:35,  1.20it/s]
2023-10-17T10:13:30,290 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  18%|█▊        | 9/50 [00:07<00:34,  1.20it/s]
2023-10-17T10:13:31,135 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  20%|██        | 10/50 [00:08<00:33,  1.19it/s]
2023-10-17T10:13:31,977 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  22%|██▏       | 11/50 [00:09<00:32,  1.19it/s]
2023-10-17T10:13:32,820 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  24%|██▍       | 12/50 [00:10<00:31,  1.19it/s]
2023-10-17T10:13:33,667 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  26%|██▌       | 13/50 [00:10<00:31,  1.19it/s]
2023-10-17T10:13:34,517 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  28%|██▊       | 14/50 [00:11<00:30,  1.19it/s]
2023-10-17T10:13:35,367 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  30%|███       | 15/50 [00:12<00:29,  1.18it/s]
2023-10-17T10:13:36,217 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  32%|███▏      | 16/50 [00:13<00:28,  1.18it/s]
2023-10-17T10:13:37,065 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  34%|███▍      | 17/50 [00:14<00:27,  1.18it/s]
2023-10-17T10:13:37,917 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  36%|███▌      | 18/50 [00:15<00:27,  1.18it/s]
2023-10-17T10:13:38,768 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  38%|███▊      | 19/50 [00:15<00:26,  1.18it/s]
2023-10-17T10:13:39,623 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  40%|████      | 20/50 [00:16<00:25,  1.18it/s]
2023-10-17T10:13:40,472 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  42%|████▏     | 21/50 [00:17<00:24,  1.17it/s]
2023-10-17T10:13:41,319 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  44%|████▍     | 22/50 [00:18<00:23,  1.18it/s]
2023-10-17T10:13:42,171 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  46%|████▌     | 23/50 [00:19<00:22,  1.18it/s]
2023-10-17T10:13:43,024 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  48%|████▊     | 24/50 [00:20<00:22,  1.18it/s]
2023-10-17T10:13:43,881 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  50%|█████     | 25/50 [00:21<00:21,  1.18it/s]
2023-10-17T10:13:44,734 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  52%|█████▏    | 26/50 [00:21<00:20,  1.17it/s]
2023-10-17T10:13:45,587 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  54%|█████▍    | 27/50 [00:22<00:19,  1.17it/s]
2023-10-17T10:13:46,442 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  56%|█████▌    | 28/50 [00:23<00:18,  1.17it/s]
2023-10-17T10:13:47,296 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  58%|█████▊    | 29/50 [00:24<00:17,  1.17it/s]
2023-10-17T10:13:48,154 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  60%|██████    | 30/50 [00:25<00:17,  1.17it/s]
2023-10-17T10:13:49,008 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  62%|██████▏   | 31/50 [00:26<00:16,  1.17it/s]
2023-10-17T10:13:49,865 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  64%|██████▍   | 32/50 [00:27<00:15,  1.17it/s]
2023-10-17T10:13:50,725 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  66%|██████▌   | 33/50 [00:27<00:14,  1.17it/s]
2023-10-17T10:13:51,602 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  68%|██████▊   | 34/50 [00:28<00:13,  1.17it/s]
2023-10-17T10:13:51,636 [INFO ] pool-3-thread-1 TS_METRICS - CPUUtilization.Percent:50.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,639 [INFO ] pool-3-thread-1 TS_METRICS - DiskAvailable.Gigabytes:24.714950561523438|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - DiskUsage.Gigabytes:55.273311614990234|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUUtilization.Percent:100.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,640 [INFO ] pool-3-thread-1 TS_METRICS - MemoryAvailable.Megabytes:11113.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,641 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUsed.Megabytes:4230.41796875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:51,641 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUtilization.Percent:29.2|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537631
2023-10-17T10:13:52,447 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  70%|███████   | 35/50 [00:29<00:12,  1.16it/s]
2023-10-17T10:13:53,308 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  72%|███████▏  | 36/50 [00:30<00:12,  1.17it/s]
2023-10-17T10:13:54,164 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  74%|███████▍  | 37/50 [00:31<00:11,  1.16it/s]
2023-10-17T10:13:55,029 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  76%|███████▌  | 38/50 [00:32<00:10,  1.17it/s]
2023-10-17T10:13:55,892 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  78%|███████▊  | 39/50 [00:33<00:09,  1.16it/s]
2023-10-17T10:13:56,750 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  80%|████████  | 40/50 [00:33<00:08,  1.16it/s]
2023-10-17T10:13:57,616 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  82%|████████▏ | 41/50 [00:34<00:07,  1.16it/s]
2023-10-17T10:13:58,479 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  84%|████████▍ | 42/50 [00:35<00:06,  1.16it/s]
2023-10-17T10:13:59,338 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  86%|████████▌ | 43/50 [00:36<00:06,  1.16it/s]
2023-10-17T10:14:00,206 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  88%|████████▊ | 44/50 [00:37<00:05,  1.16it/s]
2023-10-17T10:14:01,067 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  90%|█████████ | 45/50 [00:38<00:04,  1.16it/s]
2023-10-17T10:14:01,927 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  92%|█████████▏| 46/50 [00:39<00:03,  1.16it/s]
2023-10-17T10:14:02,794 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  94%|█████████▍| 47/50 [00:39<00:02,  1.16it/s]
2023-10-17T10:14:03,656 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  96%|█████████▌| 48/50 [00:40<00:01,  1.16it/s]
2023-10-17T10:14:04,515 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  98%|█████████▊| 49/50 [00:41<00:00,  1.16it/s]
2023-10-17T10:14:04,515 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.16it/s]
2023-10-17T10:14:04,515 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.17it/s]
2023-10-17T10:14:06,482 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - generated images: [<PIL.Image.Image image mode=RGB size=1024x1024 at 0x7F922C2487C0>]
2023-10-17T10:14:07,176 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]HandlerTime.Milliseconds:45253.1|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537647,d718bc20-1a63-4582-bc77-9a909420452a, pattern=[METRICS]
2023-10-17T10:14:07,176 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - HandlerTime.ms:45253.1|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:d718bc20-1a63-4582-bc77-9a909420452a,timestamp:1697537647
2023-10-17T10:14:07,177 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]PredictionTime.Milliseconds:45253.35|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537647,d718bc20-1a63-4582-bc77-9a909420452a, pattern=[METRICS]
2023-10-17T10:14:07,177 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - PredictionTime.ms:45253.35|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:d718bc20-1a63-4582-bc77-9a909420452a,timestamp:1697537647
2023-10-17T10:14:11,296 [INFO ] W-9000-sdxl_1.0 ACCESS_LOG - /127.0.0.1:46314 "POST /v1/models/sdxl:predict HTTP/1.1" 200 49376
2023-10-17T10:14:11,296 [INFO ] W-9000-sdxl_1.0 TS_METRICS - Requests2XX.Count:1.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537651
2023-10-17T10:14:11,296 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_inference_latency_microseconds.Microseconds:4.9299189976E7|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537651
2023-10-17T10:14:11,296 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_queue_latency_microseconds.Microseconds:144.923|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537651
2023-10-17T10:14:11,296 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.job.Job - Waiting time ns: 144923, Backend time ns: 49374929543
2023-10-17T10:14:11,296 [INFO ] W-9000-sdxl_1.0 TS_METRICS - QueueTime.Milliseconds:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537651
2023-10-17T10:14:11,297 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - sent a reply, jobdone: true
2023-10-17T10:14:11,297 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 49298
2023-10-17T10:14:11,297 [INFO ] W-9000-sdxl_1.0 TS_METRICS - WorkerThreadTime.Milliseconds:78.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537651
2023-10-17 10:14:12.288 kserve.trace requestId: aa3a4e77-a74d-4053-903f-18a7520694db, preprocess_ms: 0.01335144, explain_ms: 0, predict_ms: 50371.350765228, postprocess_ms: 0.004291534
2023-10-17 10:14:19.104 uvicorn.access INFO:     127.0.0.6:38773 10 - "POST /v1/models/sdxl%3Apredict HTTP/1.1" 200 OK
2023-10-17 10:14:19.116 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 57.19968938827515
2023-10-17 10:14:19.116 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 7.800679000000002
2023-10-17T10:14:38,294 [INFO ] epollEventLoopGroup-3-4 TS_METRICS - ts_inference_requests_total.Count:1.0|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537678
2023-10-17T10:14:38,295 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req.cmd PREDICT to backend at: 1697537678295
2023-10-17T10:14:38,297 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - Backend received inference at: 1697537678
2023-10-17T10:14:38,297 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - received text: 'a cat playing football on a beach'
2023-10-17T10:14:38,333 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 
2023-10-17T10:14:39,150 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   0%|          | 0/50 [00:00<?, ?it/s]
2023-10-17T10:14:39,987 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   2%|▏         | 1/50 [00:00<00:40,  1.22it/s]
2023-10-17T10:14:40,838 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   4%|▍         | 2/50 [00:01<00:39,  1.21it/s]
2023-10-17T10:14:41,686 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   6%|▌         | 3/50 [00:02<00:39,  1.19it/s]
2023-10-17T10:14:42,535 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   8%|▊         | 4/50 [00:03<00:38,  1.19it/s]
2023-10-17T10:14:43,378 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  10%|█         | 5/50 [00:04<00:38,  1.18it/s]
2023-10-17T10:14:44,216 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  12%|█▏        | 6/50 [00:05<00:37,  1.18it/s]
2023-10-17T10:14:45,060 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  14%|█▍        | 7/50 [00:05<00:36,  1.19it/s]
2023-10-17T10:14:45,900 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  16%|█▌        | 8/50 [00:06<00:35,  1.19it/s]
2023-10-17T10:14:46,748 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  18%|█▊        | 9/50 [00:07<00:34,  1.19it/s]
2023-10-17T10:14:47,594 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  20%|██        | 10/50 [00:08<00:33,  1.19it/s]
2023-10-17T10:14:48,439 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  22%|██▏       | 11/50 [00:09<00:32,  1.18it/s]
2023-10-17T10:14:49,287 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  24%|██▍       | 12/50 [00:10<00:32,  1.18it/s]
2023-10-17T10:14:50,135 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  26%|██▌       | 13/50 [00:10<00:31,  1.18it/s]
2023-10-17T10:14:51,002 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  28%|██▊       | 14/50 [00:11<00:30,  1.18it/s]
2023-10-17T10:14:51,638 [INFO ] pool-3-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,639 [INFO ] pool-3-thread-1 TS_METRICS - DiskAvailable.Gigabytes:24.714908599853516|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,639 [INFO ] pool-3-thread-1 TS_METRICS - DiskUsage.Gigabytes:55.273353576660156|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,639 [INFO ] pool-3-thread-1 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - GPUUtilization.Percent:100.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - MemoryAvailable.Megabytes:11108.28515625|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUsed.Megabytes:4235.1328125|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,640 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUtilization.Percent:29.2|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537691
2023-10-17T10:14:51,845 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  30%|███       | 15/50 [00:12<00:29,  1.17it/s]
2023-10-17T10:14:52,688 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  32%|███▏      | 16/50 [00:13<00:28,  1.18it/s]
2023-10-17T10:14:53,534 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  34%|███▍      | 17/50 [00:14<00:27,  1.18it/s]
2023-10-17T10:14:54,385 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  36%|███▌      | 18/50 [00:15<00:27,  1.18it/s]
2023-10-17T10:14:55,239 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  38%|███▊      | 19/50 [00:16<00:26,  1.18it/s]
2023-10-17T10:14:56,087 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  40%|████      | 20/50 [00:16<00:25,  1.18it/s]
2023-10-17T10:14:56,934 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  42%|████▏     | 21/50 [00:17<00:24,  1.18it/s]
2023-10-17T10:14:57,783 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  44%|████▍     | 22/50 [00:18<00:23,  1.18it/s]
2023-10-17T10:14:58,634 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  46%|████▌     | 23/50 [00:19<00:22,  1.18it/s]
2023-10-17T10:14:59,479 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  48%|████▊     | 24/50 [00:20<00:22,  1.18it/s]
2023-10-17T10:15:00,324 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  50%|█████     | 25/50 [00:21<00:21,  1.18it/s]
2023-10-17T10:15:01,181 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  52%|█████▏    | 26/50 [00:21<00:20,  1.18it/s]
2023-10-17T10:15:02,033 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  54%|█████▍    | 27/50 [00:22<00:19,  1.18it/s]
2023-10-17T10:15:02,887 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  56%|█████▌    | 28/50 [00:23<00:18,  1.18it/s]
2023-10-17T10:15:03,743 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  58%|█████▊    | 29/50 [00:24<00:17,  1.17it/s]
2023-10-17T10:15:04,599 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  60%|██████    | 30/50 [00:25<00:17,  1.17it/s]
2023-10-17T10:15:05,452 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  62%|██████▏   | 31/50 [00:26<00:16,  1.17it/s]
2023-10-17T10:15:06,307 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  64%|██████▍   | 32/50 [00:27<00:15,  1.17it/s]
2023-10-17T10:15:07,163 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  66%|██████▌   | 33/50 [00:27<00:14,  1.17it/s]
2023-10-17T10:15:08,015 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  68%|██████▊   | 34/50 [00:28<00:13,  1.17it/s]
2023-10-17T10:15:08,872 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  70%|███████   | 35/50 [00:29<00:12,  1.17it/s]
2023-10-17T10:15:09,729 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  72%|███████▏  | 36/50 [00:30<00:11,  1.17it/s]
2023-10-17T10:15:10,585 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  74%|███████▍  | 37/50 [00:31<00:11,  1.17it/s]
2023-10-17T10:15:11,440 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  76%|███████▌  | 38/50 [00:32<00:10,  1.17it/s]
2023-10-17T10:15:12,301 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  78%|███████▊  | 39/50 [00:33<00:09,  1.17it/s]
2023-10-17T10:15:13,159 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  80%|████████  | 40/50 [00:33<00:08,  1.17it/s]
2023-10-17T10:15:14,023 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  82%|████████▏ | 41/50 [00:34<00:07,  1.17it/s]
2023-10-17T10:15:14,882 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  84%|████████▍ | 42/50 [00:35<00:06,  1.16it/s]
2023-10-17T10:15:15,747 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  86%|████████▌ | 43/50 [00:36<00:06,  1.16it/s]
2023-10-17T10:15:16,606 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  88%|████████▊ | 44/50 [00:37<00:05,  1.16it/s]
2023-10-17T10:15:17,469 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  90%|█████████ | 45/50 [00:38<00:04,  1.16it/s]
2023-10-17T10:15:18,333 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  92%|█████████▏| 46/50 [00:39<00:03,  1.16it/s]
2023-10-17T10:15:19,193 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  94%|█████████▍| 47/50 [00:40<00:02,  1.16it/s]
2023-10-17T10:15:20,059 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  96%|█████████▌| 48/50 [00:40<00:01,  1.16it/s]
2023-10-17T10:15:20,925 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  98%|█████████▊| 49/50 [00:41<00:00,  1.16it/s]
2023-10-17T10:15:20,926 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.16it/s]
2023-10-17T10:15:20,926 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.17it/s]
2023-10-17T10:15:22,907 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - generated images: [<PIL.Image.Image image mode=RGB size=1024x1024 at 0x7F922C2480D0>]
2023-10-17T10:15:23,767 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]HandlerTime.Milliseconds:45469.86|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537723,0a5a5bcd-bda4-4b1b-b5c3-a54308f35503, pattern=[METRICS]
2023-10-17T10:15:23,767 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - HandlerTime.ms:45469.86|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:0a5a5bcd-bda4-4b1b-b5c3-a54308f35503,timestamp:1697537723
2023-10-17T10:15:23,767 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]PredictionTime.Milliseconds:45470.11|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537723,0a5a5bcd-bda4-4b1b-b5c3-a54308f35503, pattern=[METRICS]
2023-10-17T10:15:23,768 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - PredictionTime.ms:45470.11|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:0a5a5bcd-bda4-4b1b-b5c3-a54308f35503,timestamp:1697537723
2023-10-17T10:15:27,707 [INFO ] W-9000-sdxl_1.0 ACCESS_LOG - /127.0.0.1:59894 "POST /v1/models/sdxl:predict HTTP/1.1" 200 49413
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 TS_METRICS - Requests2XX.Count:1.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537727
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_inference_latency_microseconds.Microseconds:4.9340985769E7|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537727
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_queue_latency_microseconds.Microseconds:164.284|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537727
2023-10-17T10:15:27,708 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.job.Job - Waiting time ns: 164284, Backend time ns: 49412842463
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 TS_METRICS - QueueTime.Milliseconds:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537727
2023-10-17T10:15:27,708 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - sent a reply, jobdone: true
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 49340
2023-10-17T10:15:27,708 [INFO ] W-9000-sdxl_1.0 TS_METRICS - WorkerThreadTime.Milliseconds:73.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537727
2023-10-17 10:15:28.648 kserve.trace requestId: 9dd79815-3c70-4011-9ef1-077f2756abcb, preprocess_ms: 0.012397766, explain_ms: 0, predict_ms: 50357.427358627, postprocess_ms: 0.004291534
2023-10-17 10:15:35.277 uvicorn.access INFO:     127.0.0.6:60453 10 - "POST /v1/models/sdxl%3Apredict HTTP/1.1" 200 OK
2023-10-17 10:15:35.290 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 56.99935531616211
2023-10-17 10:15:35.290 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 7.56701
2023-10-17T10:15:51,053 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.714977264404297|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.273284912109375|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,054 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,055 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:11112.85546875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,055 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4230.55859375|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:15:51,055 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:29.2|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537751
2023-10-17T10:16:03,293 [INFO ] epollEventLoopGroup-3-1 TS_METRICS - ts_inference_requests_total.Count:1.0|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537763
2023-10-17T10:16:03,293 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req.cmd PREDICT to backend at: 1697537763293
2023-10-17T10:16:03,294 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - Backend received inference at: 1697537763
2023-10-17T10:16:03,294 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - received text: 'a cat looking at its reflection in water'
2023-10-17T10:16:03,329 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 
2023-10-17T10:16:04,153 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   0%|          | 0/50 [00:00<?, ?it/s]
2023-10-17T10:16:05,001 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   2%|▏         | 1/50 [00:00<00:40,  1.21it/s]
2023-10-17T10:16:05,871 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   4%|▍         | 2/50 [00:01<00:40,  1.19it/s]
2023-10-17T10:16:06,734 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   6%|▌         | 3/50 [00:02<00:40,  1.17it/s]
2023-10-17T10:16:07,597 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   8%|▊         | 4/50 [00:03<00:39,  1.17it/s]
2023-10-17T10:16:08,463 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  10%|█         | 5/50 [00:04<00:38,  1.16it/s]
2023-10-17T10:16:09,325 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  12%|█▏        | 6/50 [00:05<00:37,  1.16it/s]
2023-10-17T10:16:10,180 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  14%|█▍        | 7/50 [00:05<00:37,  1.16it/s]
2023-10-17T10:16:11,045 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  16%|█▌        | 8/50 [00:06<00:36,  1.16it/s]
2023-10-17T10:16:11,910 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  18%|█▊        | 9/50 [00:07<00:35,  1.16it/s]
2023-10-17T10:16:12,773 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  20%|██        | 10/50 [00:08<00:34,  1.16it/s]
2023-10-17T10:16:13,639 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  22%|██▏       | 11/50 [00:09<00:33,  1.16it/s]
2023-10-17T10:16:14,504 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  24%|██▍       | 12/50 [00:10<00:32,  1.16it/s]
2023-10-17T10:16:15,373 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  26%|██▌       | 13/50 [00:11<00:31,  1.16it/s]
2023-10-17T10:16:16,237 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  28%|██▊       | 14/50 [00:12<00:31,  1.16it/s]
2023-10-17T10:16:17,099 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  30%|███       | 15/50 [00:12<00:30,  1.16it/s]
2023-10-17T10:16:17,967 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  32%|███▏      | 16/50 [00:13<00:29,  1.16it/s]
2023-10-17T10:16:18,836 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  34%|███▍      | 17/50 [00:14<00:28,  1.16it/s]
2023-10-17T10:16:19,707 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  36%|███▌      | 18/50 [00:15<00:27,  1.15it/s]
2023-10-17T10:16:20,578 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  38%|███▊      | 19/50 [00:16<00:26,  1.15it/s]
2023-10-17T10:16:21,446 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  40%|████      | 20/50 [00:17<00:26,  1.15it/s]
2023-10-17T10:16:22,315 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  42%|████▏     | 21/50 [00:18<00:25,  1.15it/s]
2023-10-17T10:16:23,185 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  44%|████▍     | 22/50 [00:18<00:24,  1.15it/s]
2023-10-17T10:16:24,056 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  46%|████▌     | 23/50 [00:19<00:23,  1.15it/s]
2023-10-17T10:16:24,925 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  48%|████▊     | 24/50 [00:20<00:22,  1.15it/s]
2023-10-17T10:16:25,795 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  50%|█████     | 25/50 [00:21<00:21,  1.15it/s]
2023-10-17T10:16:26,663 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  52%|█████▏    | 26/50 [00:22<00:20,  1.15it/s]
2023-10-17T10:16:27,534 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  54%|█████▍    | 27/50 [00:23<00:19,  1.15it/s]
2023-10-17T10:16:28,403 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  56%|█████▌    | 28/50 [00:24<00:19,  1.15it/s]
2023-10-17T10:16:29,274 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  58%|█████▊    | 29/50 [00:25<00:18,  1.15it/s]
2023-10-17T10:16:30,143 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  60%|██████    | 30/50 [00:25<00:17,  1.15it/s]
2023-10-17T10:16:31,013 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  62%|██████▏   | 31/50 [00:26<00:16,  1.15it/s]
2023-10-17T10:16:31,882 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  64%|██████▍   | 32/50 [00:27<00:15,  1.15it/s]
2023-10-17T10:16:32,748 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  66%|██████▌   | 33/50 [00:28<00:14,  1.15it/s]
2023-10-17T10:16:33,618 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  68%|██████▊   | 34/50 [00:29<00:13,  1.15it/s]
2023-10-17T10:16:34,486 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  70%|███████   | 35/50 [00:30<00:13,  1.15it/s]
2023-10-17T10:16:35,357 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  72%|███████▏  | 36/50 [00:31<00:12,  1.15it/s]
2023-10-17T10:16:36,226 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  74%|███████▍  | 37/50 [00:32<00:11,  1.15it/s]
2023-10-17T10:16:37,096 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  76%|███████▌  | 38/50 [00:32<00:10,  1.15it/s]
2023-10-17T10:16:37,964 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  78%|███████▊  | 39/50 [00:33<00:09,  1.15it/s]
2023-10-17T10:16:38,831 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  80%|████████  | 40/50 [00:34<00:08,  1.15it/s]
2023-10-17T10:16:39,703 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  82%|████████▏ | 41/50 [00:35<00:07,  1.15it/s]
2023-10-17T10:16:40,570 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  84%|████████▍ | 42/50 [00:36<00:06,  1.15it/s]
2023-10-17T10:16:41,440 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  86%|████████▌ | 43/50 [00:37<00:06,  1.15it/s]
2023-10-17T10:16:42,305 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  88%|████████▊ | 44/50 [00:38<00:05,  1.15it/s]
2023-10-17T10:16:43,177 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  90%|█████████ | 45/50 [00:38<00:04,  1.15it/s]
2023-10-17T10:16:44,045 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  92%|█████████▏| 46/50 [00:39<00:03,  1.15it/s]
2023-10-17T10:16:44,913 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  94%|█████████▍| 47/50 [00:40<00:02,  1.15it/s]
2023-10-17T10:16:45,782 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  96%|█████████▌| 48/50 [00:41<00:01,  1.15it/s]
2023-10-17T10:16:46,651 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  98%|█████████▊| 49/50 [00:42<00:00,  1.15it/s]
2023-10-17T10:16:46,652 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:43<00:00,  1.15it/s]
2023-10-17T10:16:46,652 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:43<00:00,  1.15it/s]
2023-10-17T10:16:48,637 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - generated images: [<PIL.Image.Image image mode=RGB size=1024x1024 at 0x7F922C248100>]
2023-10-17T10:16:49,332 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]HandlerTime.Milliseconds:46037.6|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537809,22a02389-6d96-4910-b553-e839a194895b, pattern=[METRICS]
2023-10-17T10:16:49,332 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - HandlerTime.ms:46037.6|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:22a02389-6d96-4910-b553-e839a194895b,timestamp:1697537809
2023-10-17T10:16:49,332 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]PredictionTime.Milliseconds:46037.85|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537809,22a02389-6d96-4910-b553-e839a194895b, pattern=[METRICS]
2023-10-17T10:16:49,333 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - PredictionTime.ms:46037.85|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:22a02389-6d96-4910-b553-e839a194895b,timestamp:1697537809
2023-10-17T10:16:51,532 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,532 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.714847564697266|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,532 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.273414611816406|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:10877.59765625|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4465.8203125|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:51,533 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:30.7|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537811
2023-10-17T10:16:54,059 [INFO ] W-9000-sdxl_1.0 ACCESS_LOG - /127.0.0.1:47078 "POST /v1/models/sdxl:predict HTTP/1.1" 200 50766
2023-10-17T10:16:54,060 [INFO ] W-9000-sdxl_1.0 TS_METRICS - Requests2XX.Count:1.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537814
2023-10-17T10:16:54,060 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_inference_latency_microseconds.Microseconds:5.0684798324E7|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537814
2023-10-17T10:16:54,060 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_queue_latency_microseconds.Microseconds:139.341|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537814
2023-10-17T10:16:54,061 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.job.Job - Waiting time ns: 139341, Backend time ns: 50767124754
2023-10-17T10:16:54,061 [INFO ] W-9000-sdxl_1.0 TS_METRICS - QueueTime.Milliseconds:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537814
2023-10-17T10:16:54,061 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - sent a reply, jobdone: true
2023-10-17T10:16:54,061 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 50684
2023-10-17T10:16:54,061 [INFO ] W-9000-sdxl_1.0 TS_METRICS - WorkerThreadTime.Milliseconds:84.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537814
2023-10-17 10:16:55.220 kserve.trace requestId: 8030efdb-6c17-45e1-8fca-f988505640f0, preprocess_ms: 0.012874603, explain_ms: 0, predict_ms: 51929.763793945, postprocess_ms: 0.004053116
2023-10-17 10:17:02.019 uvicorn.access INFO:     127.0.0.6:42159 10 - "POST /v1/models/sdxl%3Apredict HTTP/1.1" 200 OK
2023-10-17 10:17:02.027 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 58.73757791519165
2023-10-17 10:17:02.027 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 7.968180000000004
2023-10-17T10:17:36,011 [INFO ] epollEventLoopGroup-3-2 TS_METRICS - ts_inference_requests_total.Count:1.0|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537856
2023-10-17T10:17:36,011 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req.cmd PREDICT to backend at: 1697537856011
2023-10-17T10:17:36,013 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - Backend received inference at: 1697537856
2023-10-17T10:17:36,014 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - received text: 'a cat talking on a mobile phone'
2023-10-17T10:17:36,046 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 
2023-10-17T10:17:36,861 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   0%|          | 0/50 [00:00<?, ?it/s]
2023-10-17T10:17:37,699 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   2%|▏         | 1/50 [00:00<00:39,  1.23it/s]
2023-10-17T10:17:38,550 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   4%|▍         | 2/50 [00:01<00:39,  1.21it/s]
2023-10-17T10:17:39,400 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   6%|▌         | 3/50 [00:02<00:39,  1.19it/s]
2023-10-17T10:17:40,247 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   8%|▊         | 4/50 [00:03<00:38,  1.19it/s]
2023-10-17T10:17:41,086 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  10%|█         | 5/50 [00:04<00:38,  1.18it/s]
2023-10-17T10:17:41,929 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  12%|█▏        | 6/50 [00:05<00:37,  1.19it/s]
2023-10-17T10:17:42,767 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  14%|█▍        | 7/50 [00:05<00:36,  1.19it/s]
2023-10-17T10:17:43,611 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  16%|█▌        | 8/50 [00:06<00:35,  1.19it/s]
2023-10-17T10:17:44,461 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  18%|█▊        | 9/50 [00:07<00:34,  1.19it/s]
2023-10-17T10:17:45,310 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  20%|██        | 10/50 [00:08<00:33,  1.18it/s]
2023-10-17T10:17:46,159 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  22%|██▏       | 11/50 [00:09<00:32,  1.18it/s]
2023-10-17T10:17:47,009 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  24%|██▍       | 12/50 [00:10<00:32,  1.18it/s]
2023-10-17T10:17:47,856 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  26%|██▌       | 13/50 [00:10<00:31,  1.18it/s]
2023-10-17T10:17:48,705 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  28%|██▊       | 14/50 [00:11<00:30,  1.18it/s]
2023-10-17T10:17:49,556 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  30%|███       | 15/50 [00:12<00:29,  1.18it/s]
2023-10-17T10:17:50,406 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  32%|███▏      | 16/50 [00:13<00:28,  1.18it/s]
2023-10-17T10:17:51,302 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  34%|███▍      | 17/50 [00:14<00:28,  1.18it/s]
2023-10-17T10:17:51,634 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.714763641357422|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.27349853515625|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:100.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:11106.13671875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,635 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4237.28125|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:51,636 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:29.2|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537871
2023-10-17T10:17:52,142 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  36%|███▌      | 18/50 [00:15<00:27,  1.16it/s]
2023-10-17T10:17:52,991 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  38%|███▊      | 19/50 [00:16<00:26,  1.17it/s]
2023-10-17T10:17:53,841 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  40%|████      | 20/50 [00:16<00:25,  1.17it/s]
2023-10-17T10:17:54,699 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  42%|████▏     | 21/50 [00:17<00:24,  1.17it/s]
2023-10-17T10:17:55,555 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  44%|████▍     | 22/50 [00:18<00:23,  1.17it/s]
2023-10-17T10:17:56,420 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  46%|████▌     | 23/50 [00:19<00:23,  1.17it/s]
2023-10-17T10:17:57,277 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  48%|████▊     | 24/50 [00:20<00:22,  1.17it/s]
2023-10-17T10:17:58,140 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  50%|█████     | 25/50 [00:21<00:21,  1.17it/s]
2023-10-17T10:17:59,003 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  52%|█████▏    | 26/50 [00:22<00:20,  1.16it/s]
2023-10-17T10:17:59,858 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  54%|█████▍    | 27/50 [00:22<00:19,  1.16it/s]
2023-10-17T10:18:00,723 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  56%|█████▌    | 28/50 [00:23<00:18,  1.16it/s]
2023-10-17T10:18:01,581 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  58%|█████▊    | 29/50 [00:24<00:18,  1.16it/s]
2023-10-17T10:18:02,445 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  60%|██████    | 30/50 [00:25<00:17,  1.16it/s]
2023-10-17T10:18:03,308 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  62%|██████▏   | 31/50 [00:26<00:16,  1.16it/s]
2023-10-17T10:18:04,168 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  64%|██████▍   | 32/50 [00:27<00:15,  1.16it/s]
2023-10-17T10:18:05,035 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  66%|██████▌   | 33/50 [00:28<00:14,  1.16it/s]
2023-10-17T10:18:05,904 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  68%|██████▊   | 34/50 [00:28<00:13,  1.16it/s]
2023-10-17T10:18:06,771 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  70%|███████   | 35/50 [00:29<00:12,  1.16it/s]
2023-10-17T10:18:07,641 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  72%|███████▏  | 36/50 [00:30<00:12,  1.16it/s]
2023-10-17T10:18:08,509 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  74%|███████▍  | 37/50 [00:31<00:11,  1.15it/s]
2023-10-17T10:18:09,379 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  76%|███████▌  | 38/50 [00:32<00:10,  1.15it/s]
2023-10-17T10:18:10,248 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  78%|███████▊  | 39/50 [00:33<00:09,  1.15it/s]
2023-10-17T10:18:11,116 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  80%|████████  | 40/50 [00:34<00:08,  1.15it/s]
2023-10-17T10:18:11,986 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  82%|████████▏ | 41/50 [00:35<00:07,  1.15it/s]
2023-10-17T10:18:12,854 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  84%|████████▍ | 42/50 [00:35<00:06,  1.15it/s]
2023-10-17T10:18:13,728 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  86%|████████▌ | 43/50 [00:36<00:06,  1.15it/s]
2023-10-17T10:18:14,595 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  88%|████████▊ | 44/50 [00:37<00:05,  1.15it/s]
2023-10-17T10:18:15,462 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  90%|█████████ | 45/50 [00:38<00:04,  1.15it/s]
2023-10-17T10:18:16,332 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  92%|█████████▏| 46/50 [00:39<00:03,  1.15it/s]
2023-10-17T10:18:17,207 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  94%|█████████▍| 47/50 [00:40<00:02,  1.15it/s]
2023-10-17T10:18:18,074 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  96%|█████████▌| 48/50 [00:41<00:01,  1.15it/s]
2023-10-17T10:18:18,943 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  98%|█████████▊| 49/50 [00:42<00:00,  1.15it/s]
2023-10-17T10:18:18,943 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.15it/s]
2023-10-17T10:18:18,943 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.17it/s]
2023-10-17T10:18:20,939 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - generated images: [<PIL.Image.Image image mode=RGB size=1024x1024 at 0x7F922C2482E0>]
2023-10-17T10:18:21,803 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]HandlerTime.Milliseconds:45790.57|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537901,f0d0022c-252b-48b5-9c5a-d627c60e4480, pattern=[METRICS]
2023-10-17T10:18:21,804 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - HandlerTime.ms:45790.57|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:f0d0022c-252b-48b5-9c5a-d627c60e4480,timestamp:1697537901
2023-10-17T10:18:21,804 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]PredictionTime.Milliseconds:45790.8|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537901,f0d0022c-252b-48b5-9c5a-d627c60e4480, pattern=[METRICS]
2023-10-17T10:18:21,804 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - PredictionTime.ms:45790.8|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:f0d0022c-252b-48b5-9c5a-d627c60e4480,timestamp:1697537901
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 ACCESS_LOG - /127.0.0.1:35818 "POST /v1/models/sdxl:predict HTTP/1.1" 200 49727
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 TS_METRICS - Requests2XX.Count:1.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537905
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_inference_latency_microseconds.Microseconds:4.9659544584E7|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537905
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_queue_latency_microseconds.Microseconds:157.101|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537905
2023-10-17T10:18:25,738 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.job.Job - Waiting time ns: 157101, Backend time ns: 49727033506
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 TS_METRICS - QueueTime.Milliseconds:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537905
2023-10-17T10:18:25,738 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - sent a reply, jobdone: true
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 49659
2023-10-17T10:18:25,738 [INFO ] W-9000-sdxl_1.0 TS_METRICS - WorkerThreadTime.Milliseconds:68.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537905
2023-10-17 10:18:26.763 kserve.trace requestId: cabe2103-c4b1-4027-800d-4df118d169c6, preprocess_ms: 0.012397766, explain_ms: 0, predict_ms: 50754.44984436, postprocess_ms: 0.003576279
2023-10-17 10:18:33.396 uvicorn.access INFO:     127.0.0.6:47731 10 - "POST /v1/models/sdxl%3Apredict HTTP/1.1" 200 OK
2023-10-17 10:18:33.402 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 57.39452242851257
2023-10-17 10:18:33.403 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 7.648676999999999
2023-10-17T10:18:51,065 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,065 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.71460723876953|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.27365493774414|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:11045.66796875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4297.75390625|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:18:51,066 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:29.6|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537931
2023-10-17T10:19:07,941 [INFO ] epollEventLoopGroup-3-3 TS_METRICS - ts_inference_requests_total.Count:1.0|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537947
2023-10-17T10:19:07,942 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req.cmd PREDICT to backend at: 1697537947942
2023-10-17T10:19:07,943 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - Backend received inference at: 1697537947
2023-10-17T10:19:07,943 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - received text: 'a cat staring at a chicken'
2023-10-17T10:19:07,977 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 
2023-10-17T10:19:08,791 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   0%|          | 0/50 [00:00<?, ?it/s]
2023-10-17T10:19:09,633 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   2%|▏         | 1/50 [00:00<00:39,  1.23it/s]
2023-10-17T10:19:10,482 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   4%|▍         | 2/50 [00:01<00:39,  1.20it/s]
2023-10-17T10:19:11,332 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   6%|▌         | 3/50 [00:02<00:39,  1.19it/s]
2023-10-17T10:19:12,181 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -   8%|▊         | 4/50 [00:03<00:38,  1.19it/s]
2023-10-17T10:19:13,024 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  10%|█         | 5/50 [00:04<00:38,  1.18it/s]
2023-10-17T10:19:13,863 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  12%|█▏        | 6/50 [00:05<00:37,  1.18it/s]
2023-10-17T10:19:14,705 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  14%|█▍        | 7/50 [00:05<00:36,  1.19it/s]
2023-10-17T10:19:15,553 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  16%|█▌        | 8/50 [00:06<00:35,  1.19it/s]
2023-10-17T10:19:16,405 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  18%|█▊        | 9/50 [00:07<00:34,  1.18it/s]
2023-10-17T10:19:17,256 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  20%|██        | 10/50 [00:08<00:33,  1.18it/s]
2023-10-17T10:19:18,107 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  22%|██▏       | 11/50 [00:09<00:33,  1.18it/s]
2023-10-17T10:19:18,956 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  24%|██▍       | 12/50 [00:10<00:32,  1.18it/s]
2023-10-17T10:19:19,803 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  26%|██▌       | 13/50 [00:10<00:31,  1.18it/s]
2023-10-17T10:19:20,660 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  28%|██▊       | 14/50 [00:11<00:30,  1.18it/s]
2023-10-17T10:19:21,508 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  30%|███       | 15/50 [00:12<00:29,  1.18it/s]
2023-10-17T10:19:22,354 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  32%|███▏      | 16/50 [00:13<00:28,  1.18it/s]
2023-10-17T10:19:23,204 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  34%|███▍      | 17/50 [00:14<00:28,  1.18it/s]
2023-10-17T10:19:24,059 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  36%|███▌      | 18/50 [00:15<00:27,  1.18it/s]
2023-10-17T10:19:24,912 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  38%|███▊      | 19/50 [00:16<00:26,  1.18it/s]
2023-10-17T10:19:25,769 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  40%|████      | 20/50 [00:16<00:25,  1.17it/s]
2023-10-17T10:19:26,620 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  42%|████▏     | 21/50 [00:17<00:24,  1.17it/s]
2023-10-17T10:19:27,474 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  44%|████▍     | 22/50 [00:18<00:23,  1.17it/s]
2023-10-17T10:19:28,330 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  46%|████▌     | 23/50 [00:19<00:23,  1.17it/s]
2023-10-17T10:19:29,190 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  48%|████▊     | 24/50 [00:20<00:22,  1.17it/s]
2023-10-17T10:19:30,043 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  50%|█████     | 25/50 [00:21<00:21,  1.17it/s]
2023-10-17T10:19:30,903 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  52%|█████▏    | 26/50 [00:22<00:20,  1.17it/s]
2023-10-17T10:19:31,758 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  54%|█████▍    | 27/50 [00:22<00:19,  1.17it/s]
2023-10-17T10:19:32,618 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  56%|█████▌    | 28/50 [00:23<00:18,  1.17it/s]
2023-10-17T10:19:33,473 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  58%|█████▊    | 29/50 [00:24<00:18,  1.17it/s]
2023-10-17T10:19:34,331 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  60%|██████    | 30/50 [00:25<00:17,  1.17it/s]
2023-10-17T10:19:35,194 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  62%|██████▏   | 31/50 [00:26<00:16,  1.17it/s]
2023-10-17T10:19:36,056 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  64%|██████▍   | 32/50 [00:27<00:15,  1.16it/s]
2023-10-17T10:19:36,914 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  66%|██████▌   | 33/50 [00:28<00:14,  1.16it/s]
2023-10-17T10:19:37,779 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  68%|██████▊   | 34/50 [00:28<00:13,  1.16it/s]
2023-10-17T10:19:38,636 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  70%|███████   | 35/50 [00:29<00:12,  1.16it/s]
2023-10-17T10:19:39,504 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  72%|███████▏  | 36/50 [00:30<00:12,  1.16it/s]
2023-10-17T10:19:40,370 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  74%|███████▍  | 37/50 [00:31<00:11,  1.16it/s]
2023-10-17T10:19:41,229 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  76%|███████▌  | 38/50 [00:32<00:10,  1.16it/s]
2023-10-17T10:19:42,092 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  78%|███████▊  | 39/50 [00:33<00:09,  1.16it/s]
2023-10-17T10:19:42,954 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  80%|████████  | 40/50 [00:34<00:08,  1.16it/s]
2023-10-17T10:19:43,816 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  82%|████████▏ | 41/50 [00:34<00:07,  1.16it/s]
2023-10-17T10:19:44,683 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  84%|████████▍ | 42/50 [00:35<00:06,  1.16it/s]
2023-10-17T10:19:45,545 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  86%|████████▌ | 43/50 [00:36<00:06,  1.16it/s]
2023-10-17T10:19:46,409 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  88%|████████▊ | 44/50 [00:37<00:05,  1.16it/s]
2023-10-17T10:19:47,277 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  90%|█████████ | 45/50 [00:38<00:04,  1.16it/s]
2023-10-17T10:19:48,146 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  92%|█████████▏| 46/50 [00:39<00:03,  1.16it/s]
2023-10-17T10:19:49,017 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  94%|█████████▍| 47/50 [00:40<00:02,  1.15it/s]
2023-10-17T10:19:49,886 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  96%|█████████▌| 48/50 [00:41<00:01,  1.15it/s]
2023-10-17T10:19:50,802 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG -  98%|█████████▊| 49/50 [00:41<00:00,  1.15it/s]
2023-10-17T10:19:50,803 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.13it/s]
2023-10-17T10:19:50,804 [WARN ] W-9000-sdxl_1.0-stderr MODEL_LOG - 100%|██████████| 50/50 [00:42<00:00,  1.17it/s]
2023-10-17T10:19:51,732 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,733 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.682151794433594|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,734 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.30611038208008|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,735 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,735 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,736 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,736 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:100.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,736 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:11044.19140625|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,736 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4299.21875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:51,736 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:29.6|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537991
2023-10-17T10:19:52,778 [INFO ] W-9000-sdxl_1.0-stdout MODEL_LOG - generated images: [<PIL.Image.Image image mode=RGB size=1024x1024 at 0x7F922C2480A0>]
2023-10-17T10:19:53,624 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]HandlerTime.Milliseconds:45680.8|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537993,a2bcda0d-0a77-48bf-b307-c60f4a5fa2e1, pattern=[METRICS]
2023-10-17T10:19:53,624 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - HandlerTime.ms:45680.8|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:a2bcda0d-0a77-48bf-b307-c60f4a5fa2e1,timestamp:1697537993
2023-10-17T10:19:53,624 [INFO ] W-9000-sdxl_1.0-stdout org.pytorch.serve.wlm.WorkerLifeCycle - result=[METRICS]PredictionTime.Milliseconds:45681.03|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,1697537993,a2bcda0d-0a77-48bf-b307-c60f4a5fa2e1, pattern=[METRICS]
2023-10-17T10:19:53,624 [INFO ] W-9000-sdxl_1.0-stdout MODEL_METRICS - PredictionTime.ms:45681.03|#ModelName:sdxl,Level:Model|#hostname:torchserve-predictor-58f6699b89-r5skg,requestID:a2bcda0d-0a77-48bf-b307-c60f4a5fa2e1,timestamp:1697537993
2023-10-17T10:19:57,759 [INFO ] W-9000-sdxl_1.0 ACCESS_LOG - /127.0.0.1:39276 "POST /v1/models/sdxl:predict HTTP/1.1" 200 49818
2023-10-17T10:19:57,760 [INFO ] W-9000-sdxl_1.0 TS_METRICS - Requests2XX.Count:1.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537997
2023-10-17T10:19:57,760 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_inference_latency_microseconds.Microseconds:4.9745944062E7|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537997
2023-10-17T10:19:57,760 [INFO ] W-9000-sdxl_1.0 TS_METRICS - ts_queue_latency_microseconds.Microseconds:160.44|#model_name:sdxl,model_version:default|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537997
2023-10-17T10:19:57,760 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.job.Job - Waiting time ns: 160440, Backend time ns: 49818513790
2023-10-17T10:19:57,760 [INFO ] W-9000-sdxl_1.0 TS_METRICS - QueueTime.Milliseconds:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537997
2023-10-17T10:19:57,760 [DEBUG] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - sent a reply, jobdone: true
2023-10-17T10:19:57,761 [INFO ] W-9000-sdxl_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 49745
2023-10-17T10:19:57,761 [INFO ] W-9000-sdxl_1.0 TS_METRICS - WorkerThreadTime.Milliseconds:74.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697537997
2023-10-17 10:19:59.178 kserve.trace requestId: 5628c194-37f7-4550-8cc1-f6c1aa60c6c9, preprocess_ms: 0.012636185, explain_ms: 0, predict_ms: 51239.856481552, postprocess_ms: 0.003814697
2023-10-17 10:20:05.843 uvicorn.access INFO:     127.0.0.6:58377 10 - "POST /v1/models/sdxl%3Apredict HTTP/1.1" 200 OK
2023-10-17 10:20:05.854 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 57.91600704193115
2023-10-17 10:20:05.854 kserve.trace kserve.io.kserve.protocol.rest.v1_endpoints.predict: 8.075919999999996
2023-10-17T10:20:51,074 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,075 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:24.68233871459961|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,075 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:55.30592346191406|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,075 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:69.1|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,075 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:84.16015625|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,076 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:12927.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,076 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0.0|#Level:Host,DeviceId:0|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,076 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:11038.1875|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,076 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4305.23828125|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
2023-10-17T10:20:51,076 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:29.7|#Level:Host|#hostname:torchserve-predictor-58f6699b89-r5skg,timestamp:1697538051
```
