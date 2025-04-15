import click
import logging
import asyncio
from src.export_data.exporter import Client

#Logging Setup 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DataEmitter")

# instanciating socket.io client for connecting and sending data
perf_client = Client()

#  CLI Definition
@click.group()
def cli():
    """Performance Client CLI"""
    pass

@cli.command(name="connect")
@click.option('--auth_key', required=True, help='Authentication key')
@click.option('--host_url', required=True, help='Host URL to connect to')
def connect_command(auth_key: str, host_url: str):
    """Connect to the server and start emitting data."""
    try:
        asyncio.run(perf_client.run_client(auth_key, host_url))
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received. Shutting down...")

@cli.command(name="disconnect")
def disconnect_command():
    """Disconnect from the Socket.IO server."""
    asyncio.run(perf_client.disconnect_client())

# Entry Point
if __name__ == '__main__':
    cli()
