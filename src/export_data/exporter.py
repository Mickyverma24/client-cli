import logging
import asyncio
import socketio
from src.export_data.exporter_service import Exporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataEmitter")


class Client:
    def __init__(self):
        self.sio = socketio.AsyncClient(reconnection=True)
        self.exporter = Exporter(sio=self.sio)

    async def run_client(self, auth_key: str, host_url: str) -> None:
        try:
            await self.sio.connect(
                host_url,
                auth={'token': auth_key, 'clientType':'cli'},
                transports=['websocket']
            )

            emit_task = asyncio.create_task(self.exporter.emit_data_forever())

            try:
                await self.sio.wait()
            except asyncio.CancelledError:
                logger.info("Emission task cancelled.")
            finally:
                await self.sio.disconnect()

        except socketio.exceptions.ConnectionError as e:
            logger.error(f"Failed to connect to {host_url}: {e}")

    async def disconnect_client(self):
        if self.sio.connected:
            await self.sio.disconnect()
            logger.info("Disconnected manually.")
        else:
            logger.warning("Socket already disconnected.")
