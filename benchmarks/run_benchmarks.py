import asyncio
import time
import json
import os
from load_generator import run_async_load

RESULTS_DIR = "benchmarks/results"


async def benchmark():
    os.makedirs(RESULTS_DIR, exist_ok=True)

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

            output = {
                "requests": size,
                "concurrency": concurrency,
                "total_time": total_time,
                "average_latency": avg_latency,
                "results": results
            }

            filename = f"{RESULTS_DIR}/results_{size}_c{concurrency}.json"

            with open(filename, "w") as f:
                json.dump(output, f, indent=2)

            print("=" * 50)
            print(f"Saved: {filename}")
            print(f"Requests: {size}, Concurrency: {concurrency}")
            print(f"Total Time: {total_time:.2f} sec")
            print(f"Average Latency: {avg_latency:.2f} sec")


if __name__ == "__main__":
    asyncio.run(benchmark())
