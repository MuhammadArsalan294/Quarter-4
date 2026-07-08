from fastmcp import FastMCP 

mcp = FastMCP() 

@mcp.tool()
def get_ip_address():
    return "My IP address is 192.168.1.1"

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
   mcp.run() 
