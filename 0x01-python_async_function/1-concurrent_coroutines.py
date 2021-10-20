#!/usr/bin/env python3
""" The basics of async """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    """
    queue, array = [], []

    # for _ in range(n):
    #     queue.append(asyncio.create_task(wait_random(max_delay)))

    # array.append(await asyncio.gather(*queue))

    # for q in asyncio.as_completed(queue):
    #     array.append(await q)

    for _ in range(n):
        queue.append(wait_random(max_delay))

    for q in asyncio.as_completed(queue):
        result = await q
        array.append(result)

    return array
