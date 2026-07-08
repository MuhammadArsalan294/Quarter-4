from fastmcp import Client
import asyncio
from rich import print

async def main():
    client = Client("http://127.0.0.1:8000/sse")

    async with client:
        tools = await client.list_tools()
        print("Available Tools:", tools)


if __name__ == "__main__":
    asyncio.run(main())
