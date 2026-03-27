

Bash On Windows with WSL2 + Ubuntu:

1-Install WSL(1 Command) M

  wsl --install (Ye laptop ky windows main powershell main Run as Administrator mein run karni hai)


2-Install WSL Core Components

  wsl --install --no-distribution

  Restart your system after this step.

3-Install Ubuntu on WSL  M

  wsl --install -d Ubuntu

  When Ubuntu opens: kia pta ye open ho jaye khud agar nhi hua tw laptop ky search bar main Ubuntu likh kar open karo
  Create a username:                 arsalan
  Create a password(input hidden):   arsalan123
  
4-Verify Bash Installation

  bash --version (laptop ky search bar main Ubuntu likh kar open karo or ubunto main ye run karo)

5-Access Windows Files From Bash

  cd /mnt
  ls
  cd c
  ls
  cd Users





UBUNTO/WSL Complete Hackathon Development Setup:

1.Install Node.js inside WSL(Recommended):

  sudo apt update (update package)
  sudo apt install -y nodejs npm (Install Node.js(LTS)
  node -v (Verify Installation)
  npm -v (Verify Installation)

2.Installing Node.js 20 Using NVM (Best Practice):

  curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash (Install NVM)
  source ~/.bashrc (Reload Terminal)
  nvm --version    (Verify NVM Installation)

3.Install & Upgrade Node.js to Version 20:

  nvm install 20       (Install Node.js v20)
  nvm use 20           (Use Node.js v20)
  nvm alias default 20 (Set Node.js v20 as Default)
  node -v              (Verify Node.js 20 as Default)
  npm -v               (Verify Node.js 20 as Default)

4.Installing Python,Pip And Virtual Environment

  sudo apt install -y python3 python3-pip pyhton-venv (Install Python & pip)
  python3 --version (Verify Python & pip)
  pip3 --version    (Verify Python & pip)
  python3 -m venv --help (Ye chatgpt ny di kyu k error a rha tha mere pass)

5.Enable python and pip Commands(Optional but Recommended)

  sudo apt install -y python-is-python3 
  python --version (Verify)
  pip --version    (Verify)
  
---------------
Virtual Environment:

python3 -m venv venv
source venv/bin/activate
(venv) arsalan@DESKTOP-SG2GDHI:~$ 

pip install specifyplus


Install Claude Code:

npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

Install Bonsai CLI

npm install -g @bonsai-ai/cli
   



  
