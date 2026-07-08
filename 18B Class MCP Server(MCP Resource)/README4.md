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
Class18B Work 
#####################################################

Gemini ko ye prompt dia
Create a json file consists of librrary books data. Keep it to only 3 Create a directory named mock_data and keep the file inside it.

#####################################################
server.py (main.py ki jaga ye name rakha)
#####################################################

from fastmcp import FastMCP 
import json

with open("mock_data/library_books.json") as r: #("mock_data/library_books.json" ye folder or file hai jo hum ny prompt dy 
                                                # kar banwaye tha. as r means read) 
                                                # (Es line ka matlb hai ky jis json ki file mein mera data hai os ko yaha py 
                                                #  main open kar rha hon. kis form mein read krne ky form mein.)


   books_data = json.load(r)  # (books_data ye variable bnaya hai. json jo upper import kia tha osko load kia or r ye wo he variable
                              # hai jo upper wali line mein create kia tha.) 
                              # (Es line ka matlb hai upper line wali file open kro or jis chez ko tum read kar rhy ho osko load
                              # kar do/ mere pass data ly kar ao. Yani ye JSON format data ko Pyhton ki Dictionary main convert
                              # karta hai.)

mcp = FastMCP() 

################## Tools ##################

@mcp.tool() 
async def get_my_ip_address():
    return "192.0.0.1" 

@mcp.tool()
async def get_my_emails():
    return [                  # [] list create ki or os ky andar {} object/dictionary hai
        {"from": "ahmed@gmail.com",
         "to": "ali@gmail.com",
         "body": "This is an Testing Email"
        }
] 

################## Resources ##################

@mcp.resource("data://books_data") # ("data://books_data" Es ko hum kah sktey hain ky ye Protocol//Address hai.) 
def get_all_books():
    return json.dump(books_data)   # (books_data ye upper server.py/main.py ki file mein variable ka name rakha tha. dump means 
                                   #  Ye Python ki dictionary ko dubara json form main convert kar dy ga.)

if __name__ == "__main__":
   mcp.run()

#####################################################
MCP RESOURCES (TOday Class Topic Start)
#####################################################

FastMCP (Ye google py search kia then Welcome to FastMCP Es url py click kar ky es ko open kia tw application open ho gai.
         Yaha side bar mein Core Components py click kia then Resources py click kia tw yaha resources k detail hogi or code bhi hoga.)


Resources & Templates:

Resources represent data or file that an MCP client can read.
(Resources wo data ya wo file hoti hain jis ko MCP client read krta hai.)

(MCP resources main hmra data ki he bat ho rhi hai chahy wo hmare database ka data ho chahy wo kisi local file mein/claude py rakha hua data ho.)

What Are Resources:

Resources provide read-only access to data for LLM or client application. 
(Resources means resources mein data ki he bat hoti hai. read-only means jis ko main sirf parh skta hn osko modify/change/update nhi kar skta.
Resources kia hota hai apky LLM Model ky liye wo data hota hai jo sirf or sirf read ho. 
Jasey hum restaurent gaye waha jo menu hota hai os ko hum sirf read kar skty change/update nhi kar skty.)

MCP Tool mein bhi sirf data ki bat hoti hai or resources mein bhi sirf data ki bat hoti hai. Yani dono mein same bat ye hai ky data ki bat ho rhi.
lekin in dono main difference ye hai ky mcp.tool mein ap chezon/data ko modify/change/update kar skty ho or Resources mein ap chezon/data ko sirf read-only kar skty ho modify/change/update nhi kar skty.

-----------------------------------------------------

What are MCP Resources?
1-MCP Resources consists of Data.
(Yani MCP Resources mein only data ki bat hoti hai.)

2-MCP Resources can only access Read-only data.
(Yani main sirf or sirf data ko read kar skta hn. modify/change/update nhi kar skty.)

3-MCP Resources are similar to GET requests.   
(GET requests means Jab hum server sy data ko mangwaty hain. Tw osko hum modify/change/update nhi kar skty. Jasey hum restaurent mein gaye or waiter ko kaha menu ly ao yani hum ny get request ki but hum menu change nhi kar skty.)


-----------------------------------------------------

Books API: https://simple-books-api.click OR 03021210812 

Protocol//Address:

Protocol:  https:                         OR 03
Address:   //simple-books-api.click       OR 021210812


@mcp.resource("data://books_data") # ("data://books_data" Es ko hum kah sktey hain ky ye Protocol//Address hai.) 
def get_all_books():
    return json.dump(books_data)   # (books_data ye upper server.py/main.py ki file mein variable ka name rakha tha. dump means 
                                   #  Ye Python ki dictionary ko dubara json form main convert kar dy ga.)

(Ye bhiserver.py/main.py ki file ka code hai)
-----------------------------------------------------

uv add fastmcp (Ye terminal/cmd py run karni hai)

(Upper wali command terminal/cmd mein run karne ky bad hum pyproject.toml ki file main dekh skty hain hum ky dependencies ky array ki list mein fastmcp install ho gaya hai.)

-----------------------------------------------------

uv run fastmcp run server.py --transport sse --port 8000  (Important)
(Ye command terminal/cmd py run karni hai es sy FastMCP Server run hoga. Ye command run karne sy terminal/cmd mein http://127.0.0.1:8000/sse  ye url aye ga es ko yaha sy copy karna hai or browser py paste karna hai.)

event: endpoint
data: /messages/?session_id=9362c77f5ea7474f93284901258495e8
(Agar Browser/server es trha sy dekh rha hai tw means sab kuch thik hai)


-----------------------------------------------------

1-Created Mock Data from Books
2-Loaded json (json.load) into .py file
3-Created Read Only Resource
4-@mcp.resources(protocol://address)
5.Convertiong python dictionary to JSON again through JSON.dump()

#####################################################
client.py 
#####################################################

(Ye sir ny kaha mere project sy copy paste kar lo but maine ye claude sy likhwai hai os ko kaha mere server.py ki file ko dekh kar client.py ki file edit kar do.)

Client sy agar resource ko read karna ho tw hum kon sa function call krein gay client.read_resource("data://library_books_data") ka bracket ky andar wo he aye ga jo hum ny @mcp.resource ky tool ky andr likha tha server.py/main ki file mein.


#####################################################

@mcp.tool agar hmein koi chez modify/change/update/transfer krni hai tw es k liye hum mcp tool ka use krein gay.
@mcp.resource read only hai agar hmein koi chez only read krni hoto hum resources ka use krein gaye.
jasey hum ny prompt dy kar claude sy 3 book bnai agar hum in books mein changing krein 3 books ki jaga 1 books kar dein ya phir book ka name change kar dein tw ye resources sy nhi hoga kyu k resources read only hoty hain agar hum ko in books mein koi action perform karna hai yani kuch changes karni hai tw es ky liye hum mcp tool ka use krein gay.

-----------------------------------------------------

uv add asyncio   (ye terminal py run kia)
uv add rich      (ye terminal py run kia) 

-----------------------------------------------------

npx @modelcontextprotocol/inspector       (Important)
(Ye command new termial/cmd py run karni hai. Es ko run karne ky bad browser py khud he url open hoga. Yaha side bar py Connect py click kia then upper navigation bar main Tools py click kia then List Tools py click kia tw waha py get_ip_address or add_numbers likha aye ga yani ye do tools hain jo tool hum ny main.py ki file mein bnaye thy or Tool main do chezein hoti hain ya tw Tool list hota hai ya phir Call hota hai. Then History ky andar tools/list py click kia tw waha Response ky andar tools ky list ki history ho gi jo array/list or dictionary mein hogi.)
(npx @modelcontextprotocol/inspector ye command terminal/cmd main run karne sy inspector install ho jata hai or inspector aik tool hai jo apky browser py ja kar apko apki tamam chezein list kr ky la kar dy deta hai)

Aik hum ny upper wala kam inspector ky zariye kia or dusra ye he kam hum ny apni file main bhi kia hai coding kar ky.


-----------------------------------------------------

uv run client.py (ye terminal py run kia)  (Important)

-----------------------------------------------------

Answer:

--- Listing Tools ---
[
    Tool(
        name='get_my_ip_address',
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
        outputSchema={
            'properties': {'result': {'type': 'integer'}},
            'required': ['result'],
            'type': 'object',
            'x-fastmcp-wrap-result': True
        },
        icons=None,
        annotations=None,
        meta={'fastmcp': {'tags': []}},
        execution=None
    ),
    Tool(
        name='get_my_emails',
        title=None,
        description=None,
        inputSchema={'additionalProperties': False, 'properties': {}, 'type': 'object'},
        outputSchema=None,
        icons=None,
        annotations=None,
        meta={'fastmcp': {'tags': []}},
        execution=None
    )
]

--- Calling 'get_my_ip_address' ---
IP Address: CallToolResult(content=[TextContent(type='text', text='192.0.0.1', annotations=None, meta=None)], 
structured_content=None, meta=None, data=None, is_error=False)

--- Calling 'get_my_emails' ---
Emails: CallToolResult(content=[TextContent(type='text', text='[{"from":"ahmed@gmail.com","to":"ali@gmail.com","body":"This is an 
Testing Email"}]', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False)

--- Listing Resources ---
[
    Resource(
        name='get_all_books',
        title=None,
        uri=AnyUrl('data://books_data'),
        description=None,
        mimeType='text/plain',
        size=None,
        icons=None,
        annotations=None,
        meta={'fastmcp': {'tags': []}}
    )
]

--- Reading Resource 'data://books_data' ---
Books Data: [TextResourceContents(uri=AnyUrl('data://books_data'), mimeType='text/plain', meta=None, text='[{"id": 1, "title": "ToKill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": 1960}, {"id": 2, "title": "The Great Gatsby", "author": 
"F. Scott Fitzgerald", "genre": "Classic", "year": 1925}, {"id": 3, "title": "1984", "author": "George Orwell", "genre": 
"Dystopian", "year": 1949}]')]


