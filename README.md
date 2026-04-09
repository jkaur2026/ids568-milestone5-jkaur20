# IDS 568 - Milestone 5: LLM Inference Optimization

## Overview
In this project, I built a FastAPI-based model serving system that can handle multiple text generation requests efficiently. The goal was to simulate a real-world machine learning API that supports batching, caching, and concurrent request handling. The system uses a HuggingFace text generation model and exposes an endpoint that takes in prompts and returns generated responses.

## System Design
The system is built using FastAPI for handling API requests and the HuggingFace pipeline for text generation.

Two main optimizations were implemented:

- **Batching:** Multiple incoming requests are grouped together and processed at once instead of individually. This helps reduce repeated model calls and improves efficiency.
- **Caching:** Previously processed prompts are stored so that if the same input is received again, the response can be returned instantly without recomputing.

These components work together to improve performance and reduce unnecessary computation, especially under higher workloads.

## Benchmarking Approach
To evaluate system performance, I tested different combinations of request loads and concurrency levels.

The system was tested with:
- request sizes of 5, 10, and 20
- concurrency levels of 1, 2, and 5

This made it possible to observe how the system behaves under both low and high traffic conditions. The benchmarks measured total execution time and average latency for each configuration.

## Results & Performance Evaluation
The results show that increasing concurrency generally improves performance. When concurrency was set to 1, the system processed requests more sequentially, which led to longer total execution times. As concurrency increased to 2 and 5, multiple requests were handled at the same time, which reduced the overall processing time.

At the same time, average latency remained relatively stable across most tests. This shows that even when handling more requests in parallel, the system maintained consistent response times. At higher request loads, there was a slight increase in latency due to additional processing overhead and queuing. Overall, the system demonstrates good scalability and is able to handle increased workloads efficiently.

## Visualization
A latency comparison chart was generated using the benchmark results to visualize how performance changes across different configurations. The chart makes it easier to compare average latency across request sizes and concurrency levels.

## Project Structure
```text
src/
benchmarks/
  run_benchmarks.py
  load_generator.py
  results/
analysis/
  plot_results.py
  visualizations/
README.md
REPORT.md
requirements.txt

How to Run:
Start the server: python3 -m uvicorn src.server:app --reload --port 8001

Run Benchmarks:python3 benchmarks/run_benchmarks.py

Generate Visualspython3 analysis/plot_results.py

Conclusion

This project demonstrates how batching and caching can improve the performance of a machine learning API. The system is able to scale with increasing request loads while maintaining reasonable latency, making it a strong foundation for higher-load deployment scenarios.
