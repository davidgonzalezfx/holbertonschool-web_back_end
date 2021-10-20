#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
