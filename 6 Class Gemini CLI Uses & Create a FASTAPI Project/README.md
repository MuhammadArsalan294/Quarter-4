Class 5

Book Referece:

https://ai-native.panaversity.org/

Book on click
Part 2: AI Tool Landscape on click
Chapter 6: Google Gemini CLI: Open Source and Everywhere on click
Installation Authentication & First Steps on click

OR

https://geminicli.com/

Docs on click
Gemini CLI Quickstart on click 

##################################################

Node.js Install:

Open terminal/Command Prompt/CMD/Powershell, type: node --version or node -v

npm Package manager (comes with Node.js): Open terminal, type: npm --version or npm -v  

###################################################

Gemini CLI installation:

Method 1: Global Installation (Recommended)

npm install -g @google/gemini-cli (ye laptop ky cmd / terminal / command prompt main run karni hai )

OR

Method 2: Run Without Installing (npx)

npx @google/gemini-cli


Verify Installation: 

After installation completes (or when using npx), verify it worked:(Check install or not install)

If installed globally
gemini -v (es sy check krein gay install hua ya nhi)
0.13.0    (asey likha hua aya tw means install hai)

If using npx
npx @google/gemini-cli --version

###################################################

gemini       (phir laptop ky cmd main he gemini likh kar enter krna hai tw tw gemini cli open ho jaye ga)
/help        (jab gemini open hoga os ky search bar main /help likhein gay tw help command a jayein gi ouski)



Do Login:

Google login (free tier: 60 requests/min, 1,000 requests/day - Google AI Studio, 2025).
Gemini API Key (requires API setup).
Vertex AI (requires Google Cloud Project).

_________________________________________________________________________________________________________________________________________

Class 6


Basic Commands for GEMINI-CLI:

/auth: to authenticate the user (Yani gemini ky search bar main /auth likh kar enter kia tw authentication method a jaye gay ky login kis trha krna hai)
/memory: to show, add, refresh and list memory (Yani gemini CLI ky search bar main  /memory list likh kar enter ya click kia tw GEMINI.md ki file jaha jaha hai wo list a jaye gi ky kitni file bani hui hain ) or (/memory refresh sy refresh ho jaye gi)
/clear: Clear the screen and conversation history
/model: To change the model

-----------------------------------------------------------------

Memory or Context:

Jab bhi bat memory or context ki ho tw hmarey mind main GEMINI.md ani chahiye.
context ka mtlb hota hai information memory ka mtlb hota hai yad rakhna.Hmarey LLM statless hoty hai yani wo purani btein yad nhi rakhty.jbhi es ka use krty hain hum.

When talking about memory or the context it is a know fact that we are talking about GEMINI.md
memory or context = GEMINI.md

-----------------------------------------------------------------

Destinations for Gemini.md:

GEMINI.md hum apne project main 3 ya 5 jaga py likh skty hain.
There are 3-5 levels where we can define GEMINI.md file

1.Root/Home Directory GEMINI.md

Yani jab hum ny gemini install ki tw c drive main phir users main phir Dell main .gemini ka folder hai ye kahlata hai root/Home directory or yaha aye gi aik GEMINI.md ki file or ye phle sy bani hui nhi ho gi hum ko create krni hogi.
Jo root level py GEMINI.md hoti hai os ka kam hota hai ap ky har os project ko impact karna jo gemini CLI use kar rha hai.yani es trha ki file main hum coding standard define karty hain means comment karty hain. 
C:\Users\Dell\.gemini\GEMINI.md - It impacts every project that user GEMINI-CLI. It is mainly used to define the rules that should be applied on every project.

2.Project Level GEMINI.md 

Dusri GEMINI.md project level py hogi or ye sirf es  project ko impact krey gi.  
Only impacts the particular project.

3.Module Level GEMINI.md 

Tesri GEMINI.md ki file aik project ky kisi folder main ho skti hai or ye sirf es folder ko impact krey gi or baki ky kisi folder ko impact nhi krey gi.
Beneficial to give GEMINI-cli instructions related to a module/feature.
Features like Tech Stack, Test cases, Multi lingual etc can be written in project specific GEMINI.md.

-----------------------------------------------------------------

Create a Project Use FASTAPI

1.Initialize a Projects through UV  
2.Create/activate a virtual env(optional)
3.Start making Instances and endpoint (do this by prompt)

Prompt Work:

ye google gemini ky search bar m likhna hai. tw ye 3 kam khud kar dy ga 
1.Initialize a project with UV package manager. (Control + Enter sy new line main a jayein gay.)
2.Make a virtual environment using UV.
3.Also activate the virtual environment. (then enter press)

--------------------------------------------
Prompt Work:

In main.py initialize the fastapi server. (phir ye gemini CLI ky search bar py likh kar enter press karna hai. Es ny hmein fastapi ka main.py ki file main aik server bhi initialize kar ky dia or aik end point bhi bana kar dia. Yani coding likh kr di)

-------------------------------------------
Prompt Work:

Now your task is to spin up the FASTAPI SERVER.Make sure to include --reload flag in your  command. (Ye FASTAPI ko up krne ki command hai.Phir ye gemini CLI ky search bar mein likh kar enter press karna hai. Ye hmari file ko run krey ga server py )

Start the Server: uv run uvicorn main:app --reload (Ye terminal py khud sy bhi likh skty hain project run karne k liye baki es ko gemini py nhi likha)

(uv aik package manager hai. uv run file ko server py run krey ga. uvicorn khud sy server hai jo FASTAPI ki application ko sambhalne ka zimadar hai. main file ka name hai. app mere instance ky variable ka name hai. --reload es ka mtlb agar main.py main kuch bhi changes krein gay tw wo khud server py chly jayein gi jasey {"Hello":"World"} likha hua tha es ki jaga {"Hello":"Ali"} likha tw ye sever py gaya or server refresh kia tw {"Hello":"Ali"} chl jaye ga server py)

1 uv = Package Manager
2 uv run = file run on server
3 Uvicorn = The server that actually runs and serves your FastAPI app to users
4 main = your Python file name (main.py)
5 app = the FastAPI instance variable name
6 --reload = auto-restart on code changes

-------------------------------------------

To Access FASTAPI ENDPOINTS:

1.http://localhost:8000 (ye server py ja kar likhna hai. {"Hello":"World"} ye print ho kar a gaya server py )

2.For docs: http://localhost:8000/docs (server py ja kar ye likha or enter kia tw FASTAPI ki window open hogai or phir icon/errow py click kia or phir try it out py click kia phir Execute py click kia tw kuch details a jayein gi. Code means Status.agar koi chez success hai tw 200 / etc code status/no atty hain. Agar user ki trf sy masla ho tw 400 code status/no aty hain or agar server ki trf sy masla ho tw 500 code status/no aty hain. )

1 To request the endpoint expand the Bar
2 Click on Try it out
3 Click on execute

-------------------------------------------
Assignment:

Deposit Module

Prompt for the deposit module
Create an endpoint for deposit asking users the amount to deposit. Make sure to update the bank_balance after depositing


HOMEWORK:

1.Make an API route with the endpoint /authenticate.

2.The user should be asked for his/her name and pin_number

3.Make an endpoint named /bank-transfer

4.The user should be asked for the receipents_name and the amount to trnasfer

5.After transfering the amount, the amount should be deducted from the sender and should be added to the receiver's accounts.

6.After bank-transfer hit the authenticate with route again with the name of the person to whom you have transfered the amount.

7.After authenticating from the receiver's account you should be able to see the amount added to the person bank_balance

