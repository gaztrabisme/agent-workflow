# Production Thinking

Use this reference when deciding whether an ML inference pipeline can meet its latency, throughput, capacity, and reliability needs. `dev` owns its implementation code.

## Production decisions start below the API

For each production-critical technology, identify the operations hidden below its API calls. [book:designing-ai-interfaces], User Experience in the AI Era. Map where data physically resides at each pipeline step, identify every device transition, and determine what moves data between CPU, GPU, disk, and network. Compare transfer requirements with measured ceilings on the actual target hardware. [book:ai-engineering-huyen], Computational bottlenecks

An API call can conceal a GPU-to-host copy, a synchronization barrier, serialization, or queueing. A NumPy slice between two GPU models may look cheap while forcing a GPU-to-CPU transfer, host operation, and upload back to the GPU. Avoid CPU access in a hot path when the runtime would serialize the work—but verify the runtime and I/O binding before assuming every CPU touch creates an extra synchronization. (Senior engineer review of a client inference pipeline.)

If an API's lower layer is unclear, name the blind spot and investigate when performance is unexpectedly poor. Learn from internals documentation, performance guides, postmortems, and hot-path source code rather than stopping at API tutorials.

## Draw the pipeline and reduce data movement

Draw an inference pipeline as a graph: operations are nodes; data handoffs and device boundaries are edges. Reduce unnecessary moving edges, keep adjacent operations on the same device when possible, and fuse neighboring stages when measurement supports it. [book:designing-ml-systems-huyen], Model optimization

To avoid GPU-to-CPU-to-GPU round trips, consider merging sequential models into one graph, moving crops or preprocessing onto the GPU, or simplifying the design to one model. When a boundary is necessary, send the smallest useful payload.

Aim for Level 2–3 pipeline fusion in production and investigate why a pipeline remains at prototype-level 0–1. Fuse operators to avoid redundant memory access, including adjacent preprocessing and postprocessing when possible. Eliminate intermediate materialization unless it is needed for debugging or fan-out. Fusion can be described as a ladder—from separate processes to a merged graph or custom kernel. Higher fusion can reduce observability, fault isolation, portability, and cost efficiency, so validate those trade-offs against measured service needs.

Where the design calls for graph changes, use the appropriate mechanism: `onnx.compose` to merge sequential ONNX models, ONNX Runtime custom operations for CPU logic between GPU passes, `onnx-graphsurgeon` to edit exported nodes, TensorRT plugins for custom CUDA kernels when runtime custom operations are too slow, and NVIDIA DALI when preprocessing is the bottleneck.

CUDA streams can overlap GPU computation and data transfers when pipelining frames. [book:machine-learning-production-systems], NVIDIA Triton Inference Server

## Load, scale, and hardware

Assess what happens when production components run together, not only one at a time. Inventory shared GPU memory, PCIe bandwidth, CPU, memory bandwidth, network, and disk resources. [book:machine-learning-production-systems], Ensemble Serving Considerations Benchmarks using an exclusive GPU are not production latency; test realistic concurrency and profile the whole system. [book:machine-learning-production-systems], NVIDIA Triton Inference Server; [book:software-engineering-at-google], Performance, Load, and Stress testing; [book:ai-engineering-huyen], Throughput and goodput

An isolated pipeline once summed three fast components to predict about 71 frames per second. With ten cameras on one shared GPU, contention, transfer waits, CPU serialization, and alert bursts brought observed throughput closer to 25 frames per second on a good day and 15 during storms. The lesson is to measure the combined system under production-like traffic and topology, since load behavior emerges from the whole system. [book:software-engineering-at-google], Performance, Load, and Stress testing

Under load, bound queues or define backpressure and frame-drop behavior; identify the queue that acts as the pressure valve. Classify threaded work by GIL behavior: multiprocessing or GIL-releasing extensions can help CPU-bound work; threads suit I/O-bound work, and some numerical and inference libraries release the GIL.

Before deployment, project the design to 10× the expected load. Identify O(1) and O(N) operations, determine which per-item work dominates, and note resources that accumulate over time and how each is cleaned up. [book:hands-on-site-reliability-engineering], Purging of database tables. Establish the blast radius if one component fails and isolate failures so one camera or dependency cannot wedge the pipeline. [book:hands-on-site-reliability-engineering], Circuit breaker. Mentally simulate 10× cameras, frame rate, alerts, and runtime duration, then prioritize the scale failures most likely to bite first. [book:hands-on-site-reliability-engineering], Introducing chaos engineering

ML pipeline problems often have equivalents in databases, networking, and operating systems. Reuse their patterns where they fit: co-locate models that currently communicate through CPU glue; skip unchanged frames or use temporal differencing; time-slice shared GPU work and batch across cameras where suitable; use rate limits and backpressure for alert storms; preload models and warm up kernels; move preprocessing to the GPU when it is the bottleneck; consider a shared inference server when multiple containers load the same model; slow producers or drop frames when queues grow.

### Hardware and capacity

Profile to identify the capacity limit rather than guessing. Compute-bound and memory-bandwidth-bound workloads need different fixes; a profiler roofline chart can distinguish them. [book:ai-engineering-huyen], Computational bottlenecks

Use the profiler's roofline view to classify compute versus memory-bandwidth limits. Track model FLOPs utilization (MFU) against the chip's theoretical peak throughput. For an approximate latency floor, estimate compute time from operations divided by peak compute and data-movement time from bytes divided by memory bandwidth; the slower bound sets the lower limit. [book:ai-engineering-huyen], Computational bottlenecks; Utilization, MFU, and MBU

When movement limits the workload, consider smaller batches or quantization. Do not pay for FP32 unless the task requires it; use FP16 when accuracy permits and calibrate before using INT8. [book:ai-engineering-huyen], Computational bottlenecks; Inference quantization

## Failures, observability, and recovery

For each component, ask how it can fail at 3 a.m. and whether operators will know. Distinguish loud failures such as crashes from silent failures such as degraded predictions, missing alerts, or a stream that slows down without an error. Ensure monitoring catches performance degradation, not only process health. [book:designing-ml-systems-huyen], Alerts; Causes of ML System Failures

Specify what happens when an external dependency is unavailable: route to a fallback, retry within a defined bound, degrade, or fail explicitly. Define the recovery path after a crash and whether it is automatic or needs a person. [book:ai-engineering-huyen], Gateway; [book:hands-on-site-reliability-engineering], Automated remediation

Provision a full-capacity fallback for a fast cached path so losing the cache raises latency rather than causing an outage. If full capacity is not viable, define a deliberate graceful-degradation mode, such as reducing inference rate while preserving other service functions. [book:software-engineering-at-google], Managing State

Give distinct terminal status labels to distinct failure endings so callers can respond correctly. For each component, define healthy, degraded, and failed signals, the notification path, and whether recovery is automatic or manual. [book:real-world-software-development], Modeling Errors; [book:ai-engineering-huyen], Summary

Monitor model quality as well as service health. Watch input and output distributions with descriptive statistics so shifts and failures can be investigated; distribution shifts can degrade a model after deployment. [book:machine-learning-production-systems], What Should You Monitor?; [book:designing-ml-systems-huyen], Causes of ML System Failures

Monitor gradual VRAM growth and plan memory cleanup, pools, or reloads. For inference-time creep, profile on the target system and consider periodic restarts only if measurements justify them. Use the scheduler's resource requests and bin-packing to place replicas and isolate tenants; when startup memory still exceeds capacity, consider a shared inference server. [book:software-engineering-at-google], Containerization and Multitenancy

For queues, monitor depth and alert on fill-ups from slow subscribers or high publisher volume; a bounded queue alone does not explain why it fills. Use a bounded queue with a deliberate drop policy where required. On stream reconnect, cancel, join, and restart the old thread explicitly. Use monotonic time for intervals and UTC for timestamps. For FFmpeg workers, inspect return codes and terminate a process that exceeds its timeout. [book:hands-on-site-reliability-engineering], MQ monitoring

## Launch, learn, and optimize

Set service-level indicators and objectives for the deployed model, with a documented error budget policy that says what may ship while the objective is met and what stops when it is missed. [book:hands-on-site-reliability-engineering], Key metrics for SRE

Use bounded chaos experiments to test recovery: define steady state, hypothesize that it will continue during an injected failure, inject a limited fault, verify behavior, and remediate findings. Prioritize faults by severity. [book:hands-on-site-reliability-engineering], Build a hypothesis; Introducing chaos engineering

Use a canary deployment to route part of production traffic to the new model version and verify it before directing full traffic. [book:hands-on-site-reliability-engineering], Canary deployments

After a production incident, hold a blameless postmortem that turns the incident into resilience actions. Use a shared account of the timeline, impact, contributing causes, and actions rather than assigning blame. [book:hands-on-site-reliability-engineering], Blameless postmortems

Before launch, complete the data-movement, system-interaction, scale, hardware, and operations checks. [book:hands-on-site-reliability-engineering], Skill set of SREs

Optimize the largest measured bottleneck, not the most interesting component. Profile the pipeline and model first: in one logged example, inference took 1.65 seconds while vector search took 123 milliseconds, so model optimization mattered more than search tuning. [book:building-reliable-ai-systems], 10.3.2 Logging what matters; [book:ai-engineering-huyen], Computational bottlenecks

Periodically, and when adopting a new technology, audit whether you understand each production component's lower layer and failure modes.
