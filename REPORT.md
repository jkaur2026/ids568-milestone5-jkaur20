1. Introduction

In this project, I built a FastAPI-based inference system that is able to handle multiple requests efficiently. The goal of this system is to improve performance by using batching and caching techniques, while also supporting concurrent requests. This helps reduce response time and makes the system more scalable when handling higher workloads.

2. System Design

The system is designed to improve efficiency using three main components: batching, caching, and asynchronous processing. Batching groups multiple incoming requests together and processes them at once, which reduces overhead and improves performance. Caching is used to store previously generated responses so that repeated requests can be returned instantly without recomputing the result. In addition, asynchronous processing allows the system to handle multiple requests at the same time instead of waiting for each one to finish before starting the next.

3. Implementation

The system was implemented using FastAPI to create an API endpoint for text generation. A load generator script was created to simulate multiple requests being sent to the server, and a benchmark script was used to measure performance under different workloads and concurrency levels. These tools helped test how well the system performs when handling multiple requests at once and allowed for collecting metrics such as total processing time and average latency.

4. Results & Performance Evaluation

To evaluate the performance of the system, I tested it using different numbers of requests (5, 10, and 20) along with different concurrency levels (1, 2, and 5). The results show that increasing concurrency improves performance. When the concurrency level was set to 1, the system took longer to process all requests because they were handled more sequentially. As the concurrency increased to 2 and 5, the total processing time decreased since multiple requests were processed at the same time.

Another key observation is that the average latency remained relatively low across all tests. This means that even with more parallel requests, the response time for each request did not increase significantly. Overall, the system handles higher workloads more efficiently with increased concurrency and is able to scale well without causing major delays.

5. Conclusion

Overall, the system successfully demonstrates how batching, caching, and asynchronous processing can improve performance in an inference pipeline. The results show that the system can handle multiple requests efficiently and scale better as concurrency increases. This approach makes the system more practical for real-world applications where many users may send requests at the same time.
