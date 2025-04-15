import asyncio
from src.export_data.exporter import Client

perf_client = Client()

async def main():
    auth = "**"
    host = "**"
    await perf_client.run_client(auth_key=auth, host_url=host)

if __name__ == "__main__":
    asyncio.run(main())