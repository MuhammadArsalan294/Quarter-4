from fastmcp import FastMCP 
import json

with open("mock_data/library_books.json") as r: 
   books_data = json.load(r) 
      
mcp = FastMCP() 

################## Tools ##################

@mcp.tool() 
async def get_my_ip_address():
    return "192.0.0.1" 

@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
async def get_my_emails():
    return [                 
        {"from": "ahmed@gmail.com",
         "to": "ali@gmail.com",
         "body": "This is an Testing Email"
        }
] 
################## Resources ##################

@mcp.resource("data://books_data") 
def get_all_books():
    return json.dumps(books_data)  

if __name__ == "__main__":
   mcp.run()
