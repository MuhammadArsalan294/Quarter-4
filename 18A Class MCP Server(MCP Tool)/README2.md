#####################################################
PROMPT (Ye prompt claude ko dy kar project bnana hai)
#####################################################

Create a complete backend starter project using Python (FastAPI).

Requirements:
- Do NOT automatically create a virtual environment
- Assume the user will manually create and activate the virtual environment
- Use uv only for dependency management (not for venv creation)

Project setup:
- Include clean folder structure
- main.py as entry point

Code:
- Create one GET route "/"
- It should return "Hello World"
- Keep code simple and beginner friendly
- Add comments for explanation

Also include:
- Step-by-step instructions where user manually:
  1. Creates virtual environment using python -m venv
  2. Activates it
  3. Installs dependencies
- Commands to run the project
- Brief explanation of each step

-----------------------------------------------------

1-Sab sy phle uv ka project initialize hoga uv init ki command sy then
2-Virtual Environment create hoga then
3-Virtual Environment activate hoga

uv venv                 (Ye terminal/cmd py run karni hai then)
.venv\Scripts\activate  (Ye terminal/cmd py run karni hai)

#####################################################
Class Work
#####################################################

Claude code docs mcp servers (Ye google py search kia)
Connect Claude Code to tools via MCP (Es url py click kia)

Remote MCP Server: (Ye sab remote mcp server hain. Nechy scroll kia tw kafi sarey mcp server mojood hain.)
-Slack  (Slack mcp server office ya personal communication ky liye hota hai)
-Figma
-Canva  (Agar koi graphic designer hai tw es ko connect kar skta hai)
-Linear
-Vercel
-Hugging Face

Ab Agar apne Remote MCP Server/External Resources connect karna hai tw inki command ko yaha sy copy karo or ye command Chatgpt/Deepseek ko do os ko bolo mjhe Claude/Qwen/Gemini use karna hai tw mere es command ko Claude/Qwen/Gemini ky hisab sy bna kar do or phir tum ye command Chatgpt/Deepseek sy copy karo or apne terminal/cmd py la kar paste karo. 
kia ap apna MCP Server bna sktey hain ji ap apna MCP Server bna sktey hain.

#####################################################

Create Custom MCP server:

1-Framework: FasTMCP 
(Hum ye wala frame work use krein gay. Jasey FasTAPI python ka frame work hai. Asey he FasTMCP MCP Server create krne ka frame work hai.
Or
FatTAPI API bnane mein kam ata hai or FasTMCP MCP bnane mein kam ata hai)

FastMCP (ye google py search kia then Welcome to FastMCP Es url py click kar ky es ko open kia tw application open ho gai.
        Yaha side bar mein Installation py click kia tw yaha FastMCP ki installation ki command hongi. Again side bar mein Quickstart py click kia tw yaha FastMCP Server create krne ka code hoga.)

2-@mcp.tool  
(Phle hum ny Quarter 3 mein @funtion_tool dekha or abhi hum Quarter 4 mein @mcp.tool dekhein gay.)
(Tool main hum apni personal chezein/real time chezen jo hmrey LLM ky pass maujod nhi hoti wo rakhty hain. 
historical data/purani chezon py hmara LLM train hai jbhi hum personal data/real time data provide kar rhy hain.)


#####################################################
main.py 
#####################################################

from fastmcp import FastMCP # (fastmcp ye package ka name hai or FastMCP ye class ka name hai)

mcp = FastMCP() # (mcp ka variable bnaya or phir FastMCP() class likhi.Class ka instance / Class ka object. Ye dono aik he bat 
                #  hai kuch bhi bolein.)

@mcp.tool()    
def get_ip_address():
    return "My IP address is 192.168.1.1"

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
   mcp.run()  (Es ka mtlb hai Mere MCP Server ko chlao)

-----------------------------------------------------

uv add fastmcp (Ye terminal/cmd py run karni hai)

-----------------------------------------------------

fastmcp run main.py --transport sse --port 8000 
(Ye command terminal/cmd py run karni hai es sy FastMCP Server run hoga. Ye command run karne sy terminal/cmd mein http://127.0.0.1:8000/sse  ye url aye ga es ko yaha sy copy karna hai or browser py paste karna hai.)

event: endpoint
data: /messages/?session_id=9362c77f5ea7474f93284901258495e8
(Agar Browser/server es trha sy dekh rha hai tw means sab kuch thik hai)

-----------------------------------------------------

npx @modelcontextprotocol/inspector 
(Ye command new termial/cmd py run karni hai. Es ko run karne ky bad browser py khud he url open hoga. Yaha side bar py Connect py click kia then upper navigation bar main Tools py click kia then List Tools py click kia tw waha py get_ip_address or add_numbers likha aye ga yani ye do tools hain jo tool hum ny main.py ki file mein bnaye thy or Tool main do chezein hoti hain ya tw Tool list hota hai ya phir Call hota hai. Then History ky andar tools/list py click kia tw waha Response ky andar tools ky list ki history ho gi jo array/list or dictionary mein hogi.)

#####################################################
client.py
#####################################################

(Create a file client.py. Client es liye bna rhy kyu ky har server ky liye aik client zarori hota hai) 

from fastmcp import Client
import asyncio
from rich import print

async def main():
    client = Client("http://127.0.0.1:8000/sse")
    #ye 127.0.0.1 es ka mtlb local host hota he. Yaha client ka aik variable bnaya or phir Client ka aik instance/object create kia or os ky andar aik url pass kia FastMCP server ky browser ka ya jo FastMCP run kia tha browser/server py os ka url. Asan word mein yani mainey jo main.py ky project ko browser/server py run kia tha ye os ka url hai.

    async with client: #(async means Asyncronous function.Yaha mera client sever ko request kar rha hai. Es liye jab bhi client
                       # sy server py request jati hai tw asyncronous hota hai)

        tools = await client.list_tools() # (async ky sath await lgta hai Es ka mtlb hai ky ye certain line of code hai jis
                                          # main apko time lgy ga thora ruk jao. list_tools ye aik funtion hai jo hum ny upper
                                          # dekha tha browser main ja kar.)
                                          # (Yani client/client.py ny call kia mere server/backend/main.py ko or mere server
                                          # mein aik function moujood hai. OR
                                          # Yani client sy server py request ja rhi or or client server ko kah rha ky app ky
                                          # pass mere jitne bhi tools hain naw unki mjhe list provide kro.)
        print(Available Tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())

-----------------------------------------------------

uv add asyncio   (ye terminal py run kia)
uv add rich      (ye terminal py run kia) 
uv run client.py (ye terminal py run kia)

-----------------------------------------------------

Answer:

Available Tools:
[
    Tool(
        name='get_ip_address',
        title=None,
        description=None,
        inputSchema={'additionalProperties': False, 'properties': {}, 'type': 'object'},
        outputSchema=None,
        icons=None,
        annotations=None,
        meta={'fastmcp': {'tags': []}},
        execution=None
    ),
    Tool(
        name='add_numbers',
        title=None,
        description=None,
        inputSchema={
            'additionalProperties': False,
            'properties': {'a': {'type': 'integer'}, 'b': {'type': 'integer'}},
            'required': ['a', 'b'],
            'type': 'object'
        },
        outputSchema={'properties': {'result': {'type': 'integer'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True},   
        icons=None,
        annotations=None,
        meta={'fastmcp': {'tags': []}},
        execution=None
    )
]