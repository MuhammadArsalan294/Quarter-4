Class 5

#################### Coding Aents ####################

1- Claude Code ($20)
2- Gemini-CLI  (Free)

____________________________________________________________________________________________________________________________

#################### AI Driven Development ####################

Means AI sy madad lena. Yani wo coding/development jis main hum AI sy madad lein.
Yani AI coding krey ga or hum manage krein gay code ko context or prompt ko or review krein gay.

1- AI agents like claude code will do the coding.
2- Developers will now be managers and telling the AI agent What TO DO.
3- The condition is to have in depth understanding of prompt and context Engineering.
4- Developer will be reviewing the code and reviewers are those who are expert themselves.

OR

AI Driven Development ka matlab hai ke Artificial Intelligence (AI) ab software banane mein developers ki madad karta hai.
Pehle sirf insaan code likhta tha, ab AI code likhne, samajhne aur test karne mein help karta hai.

Example:

AI tools jaise ChatGPT, GitHub Copilot, ya Code Llama trained hote hain lakhon code examples par.

_____________________________________________________________________________________________________________________________

#################### AI Native Application ####################

Wo application jo khud powered hon. Yani wo bnda ya wo chez jo jaha sy belong karta ho jasey residence.
Or
Yani wo application jis main LLM or model AI ka use krein. Yani wo application jis main khud AI use ho rha ho.
jasey Quarter 2 main aik Blog application bnai or Quarter 4 main AI ka use karwa dia os Appication main tw wo AI Powered Application ban gai.

1- AI powered applications.
2- Application that are using LLM or models themselves.

OR

AI Native Application woh app hoti hai jo AI par hi depend karti hai — matlab uska main feature ya function Artificial Intelligence se chal raha hota hai.

Example:

ChatGPT → pura AI par based hai (user se baat karne ke liye).
Grammarly → AI se text check karta hai.
Notion AI → likhe hue notes ko summarize aur rewrite karta hai.
Midjourney / DALL·E → text se images banata hai.

In sab ka main feature AI ke bina kaam hi nahi karta — isiliye ye AI Native Apps hain.

______________________________________________________________________________________________________________________________

#################### Spec Driven Development ####################

1- Spec means/full form is Specification.
2- Specification means documenting/paper work.
3- Markdown files:

OR

Spec Driven Development (SDD) ka matlab hai. 
Code likhne se pehle hum specifications (yaani detailed plan / document) likhte hain — aur poora development usi spec ke hisaab se hota hai.

Matlab — pehle decide kar lo “kya banana hai aur kaise kaam karega,” phir us plan ke according code likho.


Specification ek clear written guide hoti hai jo batati hai:

App ya system kya karega
Har feature ka behavior kya hoga
Inputs kya lenge aur outputs kya denge
Errors ya exceptions kaise handle honge

Example:

Agar tum ek Login System bana rahe ho, to spec mein likhoge:
User apna email aur password dalega
Agar galat password ho to “Invalid password” message aayega
Agar login sahi ho to dashboard open hoga

Ye likhne ke baad hi tum code likhna start karoge.

_______________________________________________________________________________________________________________________________

Class 8(Part A)

Book Referece:

https://ai-native.panaversity.org/

Book on click
Part 2: AI Tool Landscape on click
Chapter 5: How It All Started __ The Claude Code.. on click
Free Claude Code Setup with Google Gemini on click

-----------------------------------------------------------

#################### Claude Code + Gemini Full Setup(Windows Guide) ####################


Step 0: Confirm Node.js

Windows Powershell open krein (Yani laptop ky search bar sy Windows Powershell/Command Prompt open karo )

node --version OR node -v (Ye command run karo)

-----------------------------------------------------------

Step 1: Get Your Free Google API KEY

Goto: https://aistudio.google.com
Get API Key on click
Create API Key on click
name your key (koi bhi name likhna hai)
name your project (koi bhi name likhna hai)
create key on click
key copy kar lein


-----------------------------------------------------------

Step 2: Install Tools

Windows Powershell Open 
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router (Ye command run karo)

-----------------------------------------------------------

Step 3: Create Config Directories

Windows Powershell Open 
mkdir $HOME/.claude-code-router 
OR
mkdir "$HOME/.claude-code-router" -Force (Ye run ki thi)

mkdir $HOME/.claude
OR
mkdir "$HOME/.claude" -Force  (Ye run ki thi)

-----------------------------------------------------------

Step 4: Create Config.json (Windows Version)

Windows Powershell Open 
notepad "$HOME/.claude-code-router/config.json"   (Ye command run karo es sy notepad open hoga )

(ye config.json ki file main set krni hai )
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "AIzaSyAR-mTmm40NcpMf-zA_uQCsfvAwmd4jJO8", (Ye key Generate ki hai wo hai)
      "models": [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
      ],
      "transformer": {
        "use": ["gemini"]
      }
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash",
    "background": "gemini,gemini-2.5-flash",
    "think": "gemini,gemini-2.5-flash",
    "longContext": "gemini,gemini-2.5-flash",
    "longContextThreshold": 60000
  }
}
(Jo key Generate ki hai wo yaha paste ki hai upper)

code . (Yani mrzi hai ye notepad main setting set kar lo ya phir vs code open kar ky config.json ki file ky andr)

-----------------------------------------------------------

Step 5: Set Your API KEY (Windows Method )

Windows PowerShell Open (Run as Administrator)
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'YOUR_KEY_HERE', 'User')
OR
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'AIzaSyAkwynK7fX4rgt2vlWcywB-2KOUGmv7hUg', 'User')
(Ye paste karni hai kyu ky yaha api key generate kar ky lga di hai)

Verify the key (yani jo uper key set ki hai os ko check kar skty set hui hai ya nhi )

closed Windows Powershell -> Open a new Windows Powershell -> run:
echo $env:GOOGLE_API_KEY

-----------------------------------------------------------

Step 6: Verify Setup Worked

Windows Powershell Open
claude --version           (Ye command run karni hai check karne ky liye ky installation hui hai ya nahi)
ccr version                (Ye command run karni hai check karne ky liye ky installation hui hai ya nahi)  
echo $env:GOOGLE_API_KEY   (Ye command run karni hai check karne ky liye ky installation hui hai ya nahi)

-----------------------------------------------------------

Step 7: Daily Workflow

Terminial 1- Start router First

Windows Powershell Open 
ccr start  (Ye command run karo)
Wait for: ✅ Service started successfully

Terminal 2 - THEN use Claude (after router is ready)

Windows Powershell Open
ccr code  (Ye command run karo claude use karne ky liye ye apne Window Powershell main)
OR 
claude (ye paid ky liye hai)
