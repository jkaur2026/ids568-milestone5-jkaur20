import asyncio
from src.config import BATCH_SIZE, BATCH_TIMEOUT_MS


class DynamicBatcher:
    def __init__(self, model_infer_fn):
       
        self.model_infer_fn = model_infer_fn
        self.queue = []
        self.lock = asyncio.Lock()
        self.batch_task = None

    async def add_request(self, prompt: str):
      
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        async with self.lock:
            self.queue.append((prompt, future))

           
            if len(self.queue) >= BATCH_SIZE:
                batch = self.queue[:]
                self.queue.clear()
                asyncio.create_task(self._process_batch(batch))

          
            elif self.batch_task is None or self.batch_task.done():
                self.batch_task = asyncio.create_task(self._wait_and_process())

        return await future

    async def _wait_and_process(self):
      
      
        await asyncio.sleep(BATCH_TIMEOUT_MS / 1000)

        async with self.lock:
            if not self.queue:
                return

            batch = self.queue[:]
            self.queue.clear()

        await self._process_batch(batch)

    async def _process_batch(self, batch):
      
        prompts = [item[0] for item in batch]
        futures = [item[1] for item in batch]

        try:
            results = await self.model_infer_fn(prompts)

            for future, result in zip(futures, results):
                if not future.done():
                    future.set_result(result)

        except Exception as e:
            for future in futures:
                if not future.done():
                    future.set_exception(e)
