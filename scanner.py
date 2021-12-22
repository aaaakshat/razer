#!/usr/bin/env python3

import asyncio
from bleak import BleakScanner

uuid = "251385E1-E5B1-A22A-70C1-BC056642B5B9"

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)


asyncio.run(main())
