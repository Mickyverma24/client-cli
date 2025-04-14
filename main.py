import socketio
import asyncio
import logging
import typer
# from fetch_data import get_data
# Setup logging
from exporter import emit_data_forever

app = typer.Typer()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataEmitter")

# Create Socket.IO async client
sio = socketio.AsyncClient(reconnection=True)

# Connection events
@sio.event
async def connect():
    logger.info("Connected to server.")

@sio.event
async def disconnect():
    logger.info("Disconnected from server.")

@app.command()
def set(auth: str):
    print("Setting auth of the client")

@app.command()
def connect():
    print("Connecting to the client")

@app.command()
def disconnect():
    """Disconnects the socket."""
    if sio.connected:
        asyncio.run(sio.disconnect())
        logger.info("Disconnected manually.")
    else:
        logger.warning("Socket is already disconnected.")

async def main():
    await sio.connect('http://localhost:3000', auth={'token': "aaeygaotohmodihe"}, transports=['websocket'])
    
    emit_task = asyncio.create_task(emit_data_forever(sio))

    try:
        await sio.wait()  # Keeps client alive and listening
    except KeyboardInterrupt:
        logger.info("Received exit signal. Disconnecting...")
        emit_task.cancel()
        await sio.disconnect()


@app.command()
def start():
    asyncio.run(main())
   
if __name__ == "__main__":
    app()
