import logging
import asyncio
from fetch_data import get_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataEmitter")

async def emit_data_forever(sio):
    try:
        while True:
            data = await get_data() if asyncio.iscoroutinefunction(get_data) else get_data()
            await sio.emit("prefData", data)
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        logger.info("Emission task cancelled. Cleaning up...")