import asyncio
import logging
from src.fetch_data.fetcher import get_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataEmitter")


class Exporter:
    def __init__(self, sio):
        self.sio = sio

    async def emit_data_forever(self):
        try:
            logger.info("Sending data to the main server with!")
            while True:
                data = await get_data() if asyncio.iscoroutinefunction(get_data) else get_data()
                await self.sio.emit("prefData", data) # emiting data to client
                await asyncio.sleep(1) # additional halt for next one sec to provide each time data
        except asyncio.CancelledError:
            logger.info("Emission task cancelled. Cleaning up...")    