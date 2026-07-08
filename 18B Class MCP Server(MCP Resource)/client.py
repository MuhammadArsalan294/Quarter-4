from fastmcp import Client
import asyncio
from rich import print

async def main():
    # Connecting to the server
    client = Client("http://127.0.0.1:8000/sse")

    async with client:
        # 1. List and call Tools
        print("--- Listing Tools ---")
        tools = await client.list_tools()
        print(tools)

        print("\n--- Calling 'get_my_ip_address' ---")
        ip = await client.call_tool("get_my_ip_address")
        print(f"IP Address: {ip}")

        print("\n--- Calling 'get_my_emails' ---")
        emails = await client.call_tool("get_my_emails")
        print(f"Emails: {emails}")

        # 2. List and read Resources
        print("\n--- Listing Resources ---")
        resources = await client.list_resources()
        print(resources)

        print("\n--- Reading Resource 'data://books_data' ---")
        books = await client.read_resource("data://books_data")
        print(f"Books Data: {books}")

if __name__ == "__main__":
    asyncio.run(main())
