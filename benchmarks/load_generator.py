import asyncio
import time
import httpx

API_URL = "http://127.0.0.1:8001/generate"


async def make_request(client, text_input):
    start_time = time.time()

    response = await client.post(API_URL, json={"prompt": text_input})

    end_time = time.time()

    return {
        "input_text": text_input,
        "status": response.status_code,
        "latency_sec": end_time - start_time,
        "output": response.json()
    }


async def run_async_load(requests_list, concurrency_level=1):
    limiter = asyncio.Semaphore(concurrency_level)

    async with httpx.AsyncClient(timeout=120.0) as client:

        async def limited_request(text_input):
            async with limiter:
                return await make_request(client, text_input)

        tasks = [limited_request(text) for text in requests_list]

        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    demo_inputs = [f"Test prompt {i}" for i in range(5)]

    results = asyncio.run(run_async_load(demo_inputs, concurrency_level=2))

    for r in results:
        print(r)
