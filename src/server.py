from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

from src.caching import InferenceCache
from src.batching import DynamicBatcher
from src.config import MODEL_NAME, MAX_NEW_TOKENS

app = FastAPI()

generator = pipeline("text-generation", model=MODEL_NAME)

cache = InferenceCache()

class PromptRequest(BaseModel):
    prompt: str

async def batched_infer(prompts):
    return [
        generator(
            prompt,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False
        )[0]["generated_text"]
        for prompt in prompts
    ]

batcher = DynamicBatcher(batched_infer)

@app.post("/generate")
async def generate(request: PromptRequest):
    cached = cache.get(request.prompt)
    if cached is not None:
        return {"response": cached}

    result = await batcher.add_request(request.prompt)
    cache.set(request.prompt, result)
    return {"response": result}
