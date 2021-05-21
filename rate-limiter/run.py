import fire
from typing import *

from collections import defaultdict

from dataclasses import dataclass, field
import numpy as np

import time


import asyncio
loop = asyncio.get_event_loop()


@dataclass
class Request:
    ip: str
    data: Any

async def some_function(request):
    print(f"Processing request from {request.ip}")
    await asyncio.sleep(0.1)
    print(f"Done processing request!")


@dataclass
class RateLimiter:
    # e.g. 60 seconds
    bucket_size_ms: int 
    limit_per_bucket: float

    max_buckets: int = 5

    def __post_init__(self):
        self._buckets: List[Dict[str, int]] = [defaultdict(lambda: 0)] * self._max_buckets
        self._last_update = int(time.time() * 1000)
        self._last_bin = -1
        self._bucket_expiries = List[int] = [0] * self._max_buckets

    def check_limit(request: Request) -> bool:
        now_ms = int(time.time() * 1000)
        bin_id = (now_ms // self.bucket_size_ms) % self.max_buckets

        # Can use a sliding window with previous bucket
        prev_bin_id = bin_id - 1
        if prev_bin_id < 0:
            prev_bin_id = self.max_buckets - 1

        if now_ms > self._bucket_expires[bin_id]:
            self._buckets[bin_id] = defaultdict(lambda: 0)
            # bucket_expiry is start of bin + 2*bin_width 
            self._bucket_expires[bin_id] = int(now_ms // self.bucket_size_ms + 2)*self.bucket_size_ms

        if now_ms > self._bucket_expires[prev_bin_id]:
            self._buckets[prev_bin_id] = defaultdict(lambda: 0)
            # for prev bin_id bucket_expiry is start of bin + bin_width 
            self._bucket_expires[bin_id] = int(now_ms // self.bucket_size_ms + 1)*self.bucket_size_ms

        self._tidy_up(bin_id, prev_bin_id, now_ms)

        self._buckets[bin_id][request.ip] += 1

        ms_in_bin = now_ms - (now_ms // self.bucket_size_ms)
        pct_in_bin = float(ms_in_bin) / self.bucket_size_ms

        rate = (
            (1. - pct_in_bin) * self._buckets[prev_bin_id][request.ip]
            + self._buckets[bin_id][request.ip]
        )

        return self._buckets[bin_id] < limit_per_bucket


if __name__ == '__main__':
    fire.Fire(run)

