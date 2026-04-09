# IDS 568 – Milestone 5: Model Serving & Benchmarking

## Overview
In this project, I built a FastAPI-based model serving system that can handle multiple text generation requests efficiently. The goal was to simulate a real-world machine learning API that supports batching, caching, and concurrent request handling. The system uses a HuggingFace text generation model and exposes an endpoint that takes in prompts and returns generated responses.

## System Design
The system is built using FastAPI for handling API requests and the HuggingFace pipeline for text generation. Two key optimizations were implemented:

- **Batching:** Multiple incoming requests are grouped together and processed at once instead of individually. This helps reduce repeated model calls and improves efficiency.
- **Caching:** Previously processed prompts are stored so that if the same input is received again, the response can be returned instantly without recomputing.

These components work together to improve performance and reduce unnecessary computation, especially under higher workloads.

## Benchmarking Approach
To evaluate system performance, I tested different combinations of request loads and concurrency levels. Specifically, I ran experiments with:
- Request sizes: 5, 10, and 20 requests
- Concurrency levels: 1, 2, and 5

This allowed me to observe how the system behaves under both low and high traffic conditions. The benchmarks measure total execution time and average latency for each configuration.

## Results & Performance Evaluation
The results show that increasing concurrency generally improves performance. When concurrency was set to 1, the system processed requests more sequentially, leading to longer total execution times. As concurrency increased to 2 and 5, multiple requests were handled simultaneously, which reduced overall processing time.

At the same time, average latency remained relatively stable across most tests. This indicates that even when handling multiple requests in parallel, the system maintained consistent response times. However, at higher request loads, there was a slight increase in latency due to additional processing overhead and queuing effects.

Overall, the system demonstrates good scalability. It is able to handle increased workloads efficiently while maintaining stable performance. The batching mechanism helps reduce repeated model execution, and caching further improves efficiency by avoiding redundant computations.

## Visualization
A latency comparison chart was generated using the benchmark results to visualize how performance changes across different configurations. The chart highlights how latency varies with increasing request sizes and concurrency levels, making it easier to compare system behavior under different conditions.

## Project Structure
src/ # API server implementation
benchmarks/ # Benchmark scripts
benchmarks/results/ # Saved benchmark outputs
analysis/ # Visualization scripts
analysis/visualizations/ # Generated charts
README.md
requirements.txt


## How to Run
1. Start the server:python3 -m uvicorn src.server:app --reload --port 8001

2. Run benchmarks (in a new terminal):python3 benchmarks/run_benchmarks.py


3. Generate visualization:python3 analysis/plot_results.py


## Conclusion
This project demonstrates how batching and caching can significantly improve the performance of a machine learning API. The system is able to scale with increasing request loads while maintaining reasonable latency, making it a strong foundation for real-world deployment scenarios.
