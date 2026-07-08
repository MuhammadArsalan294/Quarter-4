Sir Ny Ye Kam Class Mein Nhi Kia But Apni Repo Mein Kia Hai Ye Mainey Repo Sy Copy Paste Kia Hai.

###############################################
Folder (agents_client) & File (main.py)
###############################################

import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerSse

load_dotenv()
async def main():
    async with MCPServerSse(
        name="Library Server",
        params={"url": "http://localhost:8000/sse"},
    ) as server:

        agent = Agent(
            name="Librarian",
            instructions="You are a helpful library assistant. Use the available tools to issue and return books.",
            mcp_servers=[server],
        )

        # Issue a book
        print("\n--- Issuing Book 1 ---")
        result = await Runner.run(agent, "Issue book with id 1")
        print(result.final_output)

        # Try issuing the same book again
        print("\n--- Issuing Book 1 Again ---")
        result = await Runner.run(agent, "Issue book with id 1")
        print(result.final_output)

        # Return the book
        print("\n--- Returning Book 1 ---")
        result = await Runner.run(agent, "Return book with id 1")
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())


###############################################
File (server.py/main.py)
###############################################

import json
from fastmcp import FastMCP

mcp = FastMCP()

with open("data/books.json") as f:
    books_data = json.load(f)

with open("data/rules.json") as r:
    rules = json.load(r)

######
################## Resources ##################
######

@mcp.resource("data://books")
async def get_all_books():
    return json.dumps(books_data)

@mcp.resource("data://books/{id}")
async def get_book_by_id(id: int):
    for book in books_data["books"]:
        if book["id"] == id:
            return json.dumps(book)
    return json.dumps({"error": f"Book with id {id} not found"})

@mcp.resource("data://rules")
async def get_rules():
    return json.dumps(rules)

######
################## Tools ##################
######

@mcp.tool()
async def issue_book(book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            if not book["available"]:
                return json.dumps({"error": f"'{book['title']}' is already issued"})
            book["available"] = False
            return json.dumps({"success": f"'{book['title']}' has been issued"})
    return json.dumps({"error": f"Book with id {book_id} not found"})

@mcp.tool()
async def return_book(book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            if book["available"]:
                return json.dumps({"error": f"'{book['title']}' is not issued"})
            book["available"] = True
            return json.dumps({"success": f"'{book['title']}' has been returned"})
    return json.dumps({"error": f"Book with id {book_id} not found"})

######
################## Prompts ##################
######

@mcp.prompt()
def book_recommendation(genre: str) -> str:
    available_books = [book for book in books_data["books"] if book["available"] and book["genre"].lower() == genre.lower()]
    if not available_books:
        return f"No available books found in the '{genre}' genre. Suggest some popular {genre} books the library should add."
    book_list = "\n".join([f"- {b['title']} by {b['author']} ({b['published_year']})" for b in available_books])
    return f"Here are available books in the '{genre}' genre:\n{book_list}\nRecommend which one the user should read and why."

@mcp.prompt()
def overdue_notice(user_name: str, book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            return f"Write a polite overdue notice for {user_name} who has not returned '{book['title']}' by {book['author']}. Remind them of library rules and ask them to return it soon."
    return f"Write a general overdue notice for {user_name} reminding them to return their overdue library book."

if __name__ == "__main__":
    mcp.run()


###############################################
File (client.py)
###############################################

import asyncio
from fastmcp import Client
import rich

client = Client("http://127.0.0.1:8000/sse")

async def main():
    async with client:
        # Read all books
        all_books = await client.read_resource("data://books")
        rich.print("All Books:", all_books)

        # Read a single book by id
        book = await client.read_resource("data://books/1")
        rich.print("Book 1:", book)

        # Read rules
        rules = await client.read_resource("data://rules")
        rich.print("Rules:", rules)

        rich.print("========================================== Tools: ========================================== ")

        # Issue a book
        issue_result = await client.call_tool("issue_book", {"book_id": 1})
        rich.print("Issue Book 1:", issue_result)

        # Try issuing the same book again (should fail)
        issue_again = await client.call_tool("issue_book", {"book_id": 1})
        rich.print("Issue Book 1 again:", issue_again)

        # Return the book
        return_result = await client.call_tool("return_book", {"book_id": 1})
        rich.print("Return Book 1:", return_result)

        rich.print("========================================== Prompts: ========================================== ")

        # Book recommendation prompt
        recommendation = await client.get_prompt("book_recommendation", {"genre": "Programming"})
        rich.print("Book Recommendation:", recommendation)

        # Overdue notice prompt
        overdue = await client.get_prompt("overdue_notice", {"user_name": "Ali", "book_id": 3})
        rich.print("Overdue Notice:", overdue)

if __name__ == "__main__":
    asyncio.run(main())