# Qwen setup with claude 
 
1.Open Windows Powershell
  
  npm install -g @qwen-code/qwen-code@latest
  
2.Verify Installation :
  
  qwen --version

3.Install Claude Code Router
 
  npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

  Close the window

##########################################################################

window ky search bar py cmd open krna waha qwen likh kar chla dena hai
4.Qwen OAuth (enter and login gmail)
  close window

  1.From Laptop SearchBar Open cmd:
    code .

5.See the folders 
      
  1).claude
  2).claude-code-router
  
    if not then create it manually 


6.Go to .claude-code-router/config.json 

  and paste this : 
            
{  
  "LOG": true,  
  "LOG_LEVEL": "info",  
  "HOST": "127.0.0.1",  
  "PORT": 3456,  
  "API_TIMEOUT_MS": 600000,  
  "Providers": [  
    {  
      "name": "qwen",  
      "api_base_url": "https://portal.qwen.ai/v1/chat/completions",  
      "api_key": "YOUR_QWEN_ACCESS_TOKEN_HERE",  
      "models": [  
        "qwen3-coder-plus",  
        "qwen3-coder-plus",  
        "qwen3-coder-plus"  
      ]  
    }  
  ],  
  "Router": {  
    "default": "qwen,qwen3-coder-plus",  
    "background": "qwen,qwen3-coder-plus",  
    "think": "qwen,qwen3-coder-plus",  
    "longContext": "qwen,qwen3-coder-plus",  
    "longContextThreshold": 60000,  
    "webSearch": "qwen,qwen3-coder-plus"  
  }  
}


7.Go to .qwen/oauth_creds.json folder: 
         
  Copy the access token and paste in .claude-code-router/config.json

  """"""api_key": "YOUR_QWEN_ACCESS_TOKEN_HERE",""""""" 

  Close the Window 

8.Open cmd 
 
  ccr start  / ccr restart
  close the window
 
  open cmd again:
   
  ccr code  

  ### The Setup is done successfully✅ ###
  close the window

##########################################################################

ReAuthenticate Qwen: (Yani agar laptop close kar ky open kia ya api ka masla aya tw ye setup karna lazmi hoga har bar)

Laptop ky search py cmd open kia or code . kar k VS Code open kia
.qwen ky folder ko delete kia vs code main sy
qwen (ye cmd main likh kar enter krein gay tw vs code main .qwen ka folder ban jaye ga)

1.Qwen OAuth (enter and login gmail) agar ye aya tw thik warna agay nechy wala karo km
 
Go to .qwen/oauth_creds.json folder:

Copy the access token and paste in .claude-code-router/config.json

""""""api_key": "YOUR_QWEN_ACCESS_TOKEN_HERE",""""""" 


ccr restart
ccr code


##########################################################################

### Starting the Project ###

Go TO Folder: 

1.Open CMD
 
2.specifyplus init .

It will ask questions: 
--> firstly pess y 
--> then select claude
--> ps
--> code .

Close the Terminal

3.Open the cmd again 
 
--> ccr start
close the terminal

4.Open cmd again
   
--> ccr code 

5.### verify specifyplus setup ### 

type / you will see sp commands below --> Successfull✅
 
6.Paste your /sp.specify command

 

