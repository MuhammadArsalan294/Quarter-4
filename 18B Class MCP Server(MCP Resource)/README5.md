#####################################################
Class18C Work 
#####################################################

Model Context Protocol (MCP)

Q- Who uses the tool?
Ans- LLM uses the tool. 
(Yani LLM tool ko use karta hai.)

Q- What happens when a tool is being used?
Ans- Tokens are being consumed when LLM perform its duty. 
(Yani LLM Jab bhi duty perform karta hai tw os ky liye tokens khrch hoty hain.)
(LLM py get request jati nhi hai tw resources call kar ky cost effective ho skty hai. Es he liye hum MCP server use kar rhy 
ta ky cost sy bacha ja skey.)

call/tool
list/tool
(Yani tool ya tw call hoga/ list hoga)

call/resources
list/resources
(Yani resources ya tw call hoga/ list hoga)


Done: (Ye kam hum kar chuky hain last class mein)
1-MCP Servers
  Tool
  Resources

2-MCP Client
  FASTMCP (from fastmcp import Client) 
  OpenAI agents SDK

#####################################################
CHATGPT
#####################################################

✅ Q1: Who uses the tool?

LLM directly khud se tools use nahi karta, balkay developer ke defined system (jaise MCP server ya agent framework) ke through tool call hota hai.
OR
LLM decide karta hai ke tool use karna hai ya nahi.
Lekin actual call system karta hai (backend / MCP server).


✅ Q2: What happens when a tool is being used?


Jab LLM kaam karta hai (chahe text generate kare ya tool call kare), tab tokens consume hotay hain — aur isi par cost depend karti hai.

Jab LLM bina tool ke kaam karta hai:

Har cheez khud sochta hai
Zyada tokens use hotay hain
Cost zyada hoti hai

Jab tool use hota hai (MCP server etc):

LLM sirf instruction deta hai
Heavy kaam tool karta hai (database, API, calculation etc)
Tokens kam lagte hain
Cost kam hoti hai

#####################################################
PROMPT OR MCP PROMPT
#####################################################

Prompt:
Prompt wo tareeqa hota hai jisse hum LLM se baat karte hain (instruction ya command).

MCP Prompt:
In MCP context prompts are pre-crafted templates/order for LLM. MCP Prompts are provided by the server to the client. 
(MCP mein prompts pre-built templates hote hain jo pehle se ready hote hain. 
Developer ya server ko pehle se pata hota hai ke client ko kya chahiye. Is liye wo ready-made prompts (templates) bana kar client ko de deta hai. Client ko khud likhne ki zaroorat nahi hoti bas select/click karta hai aur kaam ho jata hai.)

Important Point:
MCP Prompts hamesha server provide karta hai or Client unhein use karta hai select/click kar ky. 
Yani kisi application main aik box bana hua hai os mein MCP prompt hota hai jo server provide krta hai hum just click karty hain tw action perform ho jata hai.

Simple Comparison:
ChatGPT: User khud prompt likhta hai.
MCP: Server pehle se prompt bana kar deta hai.


#####################################################
JSON-RPC?
#####################################################

What is JSON-RPC?

JSON- JavaScript Object Notation
RPC- Remote Procedure Call

Think of your MCP Client as a person walking into a shop (MCP Server) to ask for something. The way they ask and receive — that specific language — is JSON-RPC.
JSON-RPC is the communication protocol used between MCP Client and MCP Server. Every interaction — listing tools, calling a tool, reading resources — happens through JSON-RPC.

Frontend / Next.JS(Client) -> HTTP Request -> Backend / FASTAPI(Server). 
(User frontend sy backend py bat HTTP Request ky zariye kar rha hota hai.
Yani humne frontend next.js py bnaya or backend fastapi py bnaya. Yani hmara frontend bat kar rha hai hmarey backend sy. Jab apki web application apky backend sy bat krti hai tw kis language ka istmal hota hai JSON ka. Yani JSON tw hota he hai but aik or concept hai http ka. Yani Jab apka Next.js apky backend sy bt krta hai tw kis shkl mein bt karta hai http ki shkl mein.)


MCP Client -> JSON RPC -> MCP Server 
(Jab bhi apka MCP Client wo FASTMCP ho / OpenAI agents SDK ho wo jab bhi apky MCP server sy bt krey gay tw JSON RPC ky zariye krey ga.
Yani main client hon mjhe sahri ka saman chahiye tw main bakry py gaya or jo sahri ka saman provide krey ga wo kon hai apka server tw phir wo bole ga apka 500 ka bill hua tw hum ny kis language mein bt ki urdu. Asey he jab apka MCP Client apky MCP Server sy bat krey ga tw JSON RPC ky zariye krey ga.)

(Apka MCP Client apky MCP Server sy kia bat krey ga wo listing tools yani tools ki list mangwa skta hai or calling a tool yani tool ko call kar skta hai or reading resources yani resources ko read kr skta hai / resources ki list mngwa skta hai / resources ko call kar skta hai kis ky throw JSON-RPC ky throw.)

#####################################################
Client Or Server kaise connect hote hain?
#####################################################

Jab MCP Client, MCP Server se baat karta hai, to wo JSON-RPC naam ki special format/language use kar ky bat karta hai.
Jaise hum normal zindagi mein Urdu ya English mein baat karte hain, waise hi Client aur Server JSON-RPC mein baat karte hain.

Client aur Server kaise connect hote hain?

MCP mein 2 main tareeqay hain:

1- STDIO (Standard Input/Output) — Local
Jab server apni machine (local) par chal raha ho tw.
Request jati hai → Standard Input se.
Response aata hai → Standard Output se.

Simple:
Jaise tum khud ja kar saman le kar aao (face-to-face / local)

2- SSE (Server-Sent Events) — Remote / Online
Jab server online / remote ho (jaise internet par)
Client aur server internet ke through connected hote hain.

Simple:
Jaise online baat karna (remote access)

Final One-line Idea:
MCP Client aur Server JSON-RPC mein baat karte hain, aur connect hone ke 2 tareeqay hain.
STDIO (local) aur SSE (online).

----------------------------------------------------

1- Request

The client asks the server to do something. (Jab client request bhejta hai server ko.)

{
  "jsonrpc": "2.0",                     (Always same will never change)
  "id": 1,                              (There will always be an id attribute.vWill always be unique in the entire 
                                         request response cycle)
  "method": "tools/call",               (read_resource) (Client tells the server what client wants)
  "params": { "name": "get_weather" }   (This attribute is responsible to call an actual function.)
}

kasey pta chly ga ky ye Object/JSON hai. 
key-value pairs jo hain wo single/double qutation/string mein hain means ye JSON hai.

"jsonrpc": "2.0",
Jab bhi MCP Client, MCP Server ko request bhejta hai, to request mein jo ye "jsonrpc" field hoti hai, us ki key aur value hamesha same rehti hai. Iski value "2.0" hoti hai jo string format mein hoti hai. Ye kabhi change nahi hoti.
Ye ("2.0") float/decimal nahi hoti. Ye string hoti hai. Hum kah sktey hain string ky andar float/decimal number.

"id": 1,
Jab bhi MCP Client, MCP Server ko request bhejta hai, to us request ki ek "id" hoti hai.
Ye "id" har request ke liye unique hoti hai, yani har nayi request ki alag id hoti hai.

"method": "tools/call", 
jab bhi MCP Client, MCP server sy bt krey ga tw JSON-RPC ky through krey ga. kia bat krey ga tool/resource sy related bt krey ga.
Jab bhi MCP Client, MCP server ko request bhejy ga ya tw tool call krey ga ya tw tool ko list krey ga or ya tw resource read krey ga ya tw resource call krey ga ya tw resource ko list krey ga. 
method field mein client server ko yeh specify karta hai ke actual mein kaunsa action perform karna hai, yani tool se related kaam hai ya resource se related.

"params": { "name": "get_weather" } 
method batata hai ke kya karna hai jaise tool call karna (tools/call).
params batata hai ke kis tool ko chalana hai. Agar get_weather ek tool (function) hai, to params server ko ye batata hai.
Is get_weather tool ko run karo.

----------------------------------------------------

2- Resonse 

The server replies back. (Jab server reply karta hai client ko.)

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": { "temp": "30°C" }
}

"jsonrpc": "2.0",
Jab bhi MCP mein request ka response aata hai, to us mein "jsonrpc": "2.0" zaroor hota hai.
Ye hamesha same rehta hai aur kabhi change nahi hota.

"id": 1,
id ek number hota hai jo har request ko alag pehchan deta hai. 
Jab client server ko request bhejta hai, to us request ki ek id hoti hai.
Jab server response deta hai, to woh usi same id ke sath jawab deta hai.
jasey exam ky question or Answer ky number dono same hoty hain.

"result": { "temp": "30°C" }
result woh actual reply hota hai jo server client ko deta hai.
Function mein jo bhi data ya object return hota hai, woh result ke attribute mein aa jata hai.

----------------------------------------------------

3- Error

If something goes wrong:

{
  "jsonrpc": "2.0",  
  "id": 1,           
  "error": { "code": -32601, "message": "Method not found" } 
}

Har request successful nahi hoti, kabhi fail bhi ho jati hai. Agar fail ho jaye to server "error" bhejta hai, jo client ko milta hai.


"jsonrpc": "2.0",
Ye hamesha same hota hai aur MCP/JSON-RPC protocol show karta hai.

"id": 1,
Ye usi request ki id hoti hai jiske liye error aya hai.
Is se pata chalta hai ke kaunsi request fail hui.
Yani apki kis request py error aya hai id ky throw ptaa chla ky kon c request fail ho rhi hai.

"error": { "code": -32601, "message": "Method not found" }
Jab MCP request fail hoti hai to response mein "error" aata hai, jisme error ka code aur message hota hai.
"id" same request ki hoti hai taake pata chale kaunsi request fail hui hai.
"Method not found" ka matlab hai ke jo method call kiya gaya wo exist nahi karta.
 

----------------------------------------------------

4- Common JSON-RPC Error Codes

These are the standard errors you may encounter during the MCP request-response cycle:

Code	Name	           When does it happen?
-32700	Parse Error        Server received invalid JSON (broken syntax, missing brackets, etc.) 
                           (Jab server ko invalid JSON mile jaise syntax galat ho, brackets missing hon, etc.)

Code	Name	           When does it happen?
-32600	Invalid Request	   JSON is valid but not a proper JSON-RPC request (missing method, wrong jsonrpc version) 
                           (JSON theek hota hai lekin valid JSON-RPC request nahi hoti jaise method missing ho ya jsonrpc version galat ho.)

Code	Name	           When does it happen?
-32601	Method Not Found   The method you called doesn't exist on the server (e.g. typo in tool name)     
                           (Ap jo method/tool call karte ho wo server par exist hi nahi karta jaise name galat likh diya ho.)

Code	Name	           When does it happen?
-32602	Invalid Params	   Method exists but the params you sent are wrong (missing required param, wrong type)
                           (Method exist karta hai lekin jo params aap ne bheje hain wo galat hain jaise required value missing ho ya type wrong ho.)

Code	Name	           When does it happen?
-32603	Internal Error	   Something broke inside the server while processing your request                        
                           (Jab server ke andar koi problem ho jaye request process karte waqt.4)

----------------------------------------------------

5- MCP-Specific Errors

On top of standard JSON-RPC errors, MCP defines additional error scenarios:

Code	Name	                When does it happen?
-32001	Tool Execution Error	The tool was found but crashed or failed during execution
                                (Tool mil gaya lekin chalate waqt fail ho gaya ya crash ho gaya.)

Code	Name	                When does it happen?
-32002	Resource Not Found	    The resource URI you requested doesn't exist on the server
                                (Jo resource aap ne manga hai wo server par exist nahi karta.)

Code	Name	                When does it happen?
-32003	Prompt Not Found	    The prompt template you requested doesn't exist on the server
                                (Jo prompt aap ne manga hai wo server par exist nahi karta.)

Code	Name	                When does it happen?
—	    Transport Error	        Connection lost — server crashed, pipe broke, or SSE stream dropped
                                (Jab connection toot jaye jaise server band ho jaye, connection break ho jaye, ya stream disconnect ho jaye.)

Code	Name	                When does it happen?
—	    Timeout	                Server took too long to respond and the client gave up
                                (Jab server bohat der laga de aur client wait karna band kar de.)

Code	Name	                When does it happen?
—	    Initialization Failed	Client-server handshake failed (version mismatch, capability issue)
                                (Jab client aur server connect na ho saken jaise version ya capability match na kare.)


