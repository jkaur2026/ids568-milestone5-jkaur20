import asyncio
import time
from load_generator import run_async_load


async def benchmark():
    test_sizes = [5, 10, 20]
    concurrency_levels = [1, 2, 5]

    for size in test_sizes:
        for concurrency in concurrency_levels:
            inputs = [f"Benchmark prompt {i}" for i in range(size)]

            start = time.time()

            results = await run_async_load(inputs, concurrency_level=concurrency)

            end = time.time()

            total_time = end - start
            avg_latency = sum(r["latency_sec"] for r in results) / len(results)

            print("=" * 50)
            print(f"Requests: {size}")
            print(f"Concurrency: {concurrency}")
            print(f"Total Time: {total_time:.2f} sec")
            print(f"Average Latency: {avg_latency:.2f} sec")


if __name__ == "__main__":
    asyncio.run(benchmark())
