import time
import hashlib
from collections import OrderedDict
from src.config import CACHE_TTL_SECONDS, CACHE_MAX_ENTRIES, MODEL_NAME


class InferenceCache:
    def __init__(self, ttl=CACHE_TTL_SECONDS, max_entries=CACHE_MAX_ENTRIES):
        self.ttl = ttl
        self.max_entries = max_entries
        self.store = OrderedDict()

    def _make_key(self, prompt: str) -> str:
       
        raw = f"{prompt}|{MODEL_NAME}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def get(self, prompt: str):
        key = self._make_key(prompt)

        if key not in self.store:
            return None

        value, created_at = self.store[key]

   
        if time.time() - created_at > self.ttl:
            del self.store[key]
            return None

        # Move to end
        self.store.move_to_end(key)
        return value

    def set(self, prompt: str, value: str):
        key = self._make_key(prompt)

       
        if key in self.store:
            del self.store[key]

        # max size
        elif len(self.store) >= self.max_entries:
            self.store.popitem(last=False)

        
        self.store[key] = (value, time.time())

    def clear(self):
        self.store.clear()
