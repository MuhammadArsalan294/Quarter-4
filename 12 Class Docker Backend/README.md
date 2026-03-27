############################################
CLASS 12 DOCKER BACKEND
############################################

Jasey phle USB ka use karty thy videos aik laptop sy dusre laptop main save asey he Docker web application ky liye use hota hai.
Agar kisi ny apko apna project dia Tw os main ye masla ho sakta hai jo nechy likha hai tw docker wo masla thik karta hai.

-Application Code 
-Packages with their Particular Version
-Same Plateform agnostic  (Yani agar kisi ky pass linux ho or kisi ky pass window tw ye masla bhi docker solve karta hai)
-Difference of version introducing error called Breaking Changes (Jasey version ka masla ata 13 chl rha 14 a agya tw docker ye masla thik krta hai)


Docker Image:
-It is a blueprint or a compressor version of our application. (Frontent/Backend/Database/)
-Image is as same as Class in OOP.
-It contains all the stuff like, Appliction code, libraries with their version.

Docker Container:
-It is as same as Object in OOP.
-When up and running my application in docker container.

----------------------------------------------------------

What is Dockerfile:
-The thing that is used to create a image is called Dockerfile.
-It shold be at the root level of your application code.
(Wo kon c chez hai hai jo image bnaey gi wo hai dockerfile. Ye file Project ky root py hogi. root mtlb jaha pyproject.toml ya main.py file hogi waha)

Docker hub is just like a playstore for Docker.
(Ye image hum docker hub sy import kar rhy hain. Docker hub kia hai docker playstore hai jaha sari chezein rakhi hui hoti hain)

Dockerfile keywords: 
(Dockerfile keywords ko hum Dockerfile main use krne wale function bhi kah skty hain or ye function ko call kr rha hon mein or jab call krty tw aurguments bhi pass karty hain)

FROM
COPY
RUN
EXPOSE
CMD

----------------------------------------------------------

user("ali", "ahmed")
COPY /requirements.txt .

def COPY(apnaLaptop, dockerContainer):
return ....

COPY("/requirement.txt  ".") 

----------------------------------------------------------

Create A Dockerfile on VS CODE

# Base Image Of Python
From python:3.12-slim 
(Ye image hum docker hub sy import kar rhy hain. Docker hub kia hai docker ka playstore hai jaha sari chezein rakhi hui hoti hain or ye project ky root py hogi root mtlb jaha project hoga waha base py ye file hogi yani hum kah skty hain Dockerfile wo camera hai jo image bnata hai)

# Copy The Application Code (class 14) OR Set Working Directory In Container (class 15)
WORKDIR /app 
(WORKDIR es ka mtlb hai hum docker ky function ko call kar rhy hain or /app ka mtlb hai hum directory/folder ko target kar rhy hain or kah skty docker ky container mein app name ka folder hoga jaha mere puri application pari hogi) 
 
# Copying The Application Dependencies File OR Copy requirements file (Class 15)
COPY /requirements.txt . 
(COPY ye function hai or requirements.txt ye first argumemt hai es ka mtlb hota hai wo tmam file/folder jo hmarey local system/apna laptop ky upper hai or . second argument es ka mtlb jo bhi docker container ky andar hai ya cuurent directory. Jasey hum code . karty hain yani current folder ko open karo)
 
# Install Dependencies
RUN pip install --no-cache-dir -r requirement

# Copy Application Code
COPY . . 
(Es ka mtlb hota hai mere tmam file ko copy karo or rakho docker container py yani phla argument local ko or dusra docker ko target krey ga)

# Expose port 8000
EXPOSE 8000 
(Ye python backend hai jbhi 8000 or agar frontend hota tw 3000 hota)

# Run The Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "-post", "8000"] 
(CMD means command prompt open karo or mere python fastapi ki application ko run kro)

###############################################
CLASS 13 DOCKER FRONTEND
###############################################

###############################################
INSTALLATION
###############################################

docker install
laptop restart then docker open
wsl --update (Ye laptop ky terminal/cmd mein run kar ky wsl ko install karna hai)

###############################################
PROMPT 1
###############################################

Your task is to create a simple Next.js App Router project from scratch.

Requirements:
1. Create a basic Next.js project using App Router.
2. Inside the main page (app/page.tsx), display a simple paragraph.
3. The paragraph should say: "This is my first Next.js app running successfully."
4. Keep the code simple and beginner-friendly.
5. Do not add any extra styling or complex features.

Also provide the commands to run the project locally.

###############################################
PROMPT 2
###############################################

Make sure the project works perfectly with npm install and npm run dev.


############################################
CLASS 13
############################################

(Ye prompt claude ko dena hai)
You are inside a nextjs app router project.You are a docker expert and your task is to create a simple docker image for my nextjs project.
Create a simple docker image my goal is to create an image and run a container locally Donot do anything related to production great docker
or k8s

(Jab upper wala prompt dia claude ko tw os ny Dockerfile bhi bna di or nechy wala code bhi Dockerfile mein likh kar dy dia)

# Simple Dockerfile for Next.js
FROM node:20-alpine

WORKDIR /app

# COPY package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy all project files
COPY . .

# Build the Next.js app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the app
CMD ["npm", "run", "start"]

-----------------------------------------------------------

1. Create an Image:

(Ye command  terminal/cmd mein run karni hai vs code ky)
docker build -t nextjs-app . (Ye terminal py run ki es sy sy docker image bney gi yani docker ky andar aik image bney gi)


-----------------------------------------------------------

2. Run the Container:

(Ye prompt claude ko dena hai) 
I have created an image now i want to create a container give me command for it. Donot run by yourself just give me the command.

To run a container from Image:
docker run -d -p 3000:3000 --name my-container <image-name> 

-d (means detached)
-p (means port)
-image-name: (Name of the image)

What is Dtached Mode?
When you run a container with detached mode (-d) it only returns a container. (Jab hum ny container run kia tw os ny id return ki )

(Ye command  terminal/cmd mein run karni hai vs code ky)
docker run -d -p 3000:3000 --name nextjs-container nextjs-app  (<image-name> es ki jaga sir ny docker ky andr sy docker image ka name copy kar ky paste kia jasey ye nextjs-app.)
(Agar container successfully run krey ga tw wo return krey ga id id yani number.)


(Docker main ja kar side bar mein containers py click krey gay tw waha container ban gaya ho ga or port(3001:3000) py click kia tw localhost:3000 open ho gaya yani application ab docker py chl rhi hai.)
(Name ky nechy nextjs-container py click kia tw hum logs mein a gaye yani jaha hum application bnty thy vs code py waha a gaye then hum files py click krein gay tw files a jayein gi WORKDIR main jis ka name /app rakha tha wo yaha a gai hogi yaha open file editor py click krein gay tw code a jaye ga vs code ka.)

(Ab agar hum apne vs code main kuch bhi change krein gay agar wo file container main bhi hai tw wo change nhi ho gi file kyu ky container main file isolated hoti hain.)

-----------------------------------------------------------

3. Run the Container with .env:

(Agar docker ko .env file ky environment deny hon tw wo bhi asey dy skty hain.)

(Ye command terminal/cmd mein run karni hai vs code ky)
docker run -d -p 8000:8000 --env-file .env --name my-fastapi-container my-first-image

-----------------------------------------------------------

Why Bind Mountings?
-Aplication running inside docker containers are isolated/soundproof.
(Application jo docker container main hoti hai wo isolated hoti hain Yani bahir jo bhi ho rha ho os ka mere application py koi frk nhi prta)

BIND MOUNT: (Means Sync Connection/files)
(Yani jo kam bhi main local machine yani vs code py karon wo kam docker py bhi hoty rahy sath sath.
Yani vs code mein page.tsx ki file main change kron tw wo docker py bhi change ho)


Name of the file to work with volumes: 
(Ye file bnani hogi bind mount karne k liye ta ku jo changing vs code main karon wo real time docker main bhi ho)
docker-compose.yml OR docker-compose.yaml
-Watch Mode
-To enable watch mode: press "w"

(Ye claude ko deni hai prompt)
I want to enable bind mounts inside my project. Your task is to create a docker-compose.yaml file with minimal instruction to enable watch
mode. Keep the file simple and easy as I will only run this on my docker desktop no need to do anything related production or k8s.

----------------------------------------------------------

What does watch mode do?
(jab upper wala prompt dia claude ko tw os ny mjhe ye code dia claude py he)

  ✦ I've created the docker-compose.yaml file with bind mounts for local development. Let me explain the configuration to the user.

  ✦ Created docker-compose.yaml with:

     - Bind mount (./:/app) — Your local code synced to container
     - node_modules volume — Prevents overwriting container's node_modules
     - Dev mode — Runs npm run dev for hot reloading

    Commands:

     1 # Start the container
     2 docker-compose up
     3
     4 # Start in detached mode (background)
     5 docker-compose up -d
     6
     7 # Stop the container
     8 docker-compose down

    Access your app at http://localhost:3000. Code changes will automatically reload.
  
OR

Created docker-compose.yaml with watch mode enabled. Heres what it does:

- sync - Syncs changes from ./app and ./public folders to the container without rebuilding
- rebuild - Rebuilds the container when package.json changes (new dependencies)
- command: npm run dev - Overrides the Dockerfile to run in dev mode (required for hot reload)

to run with watch mode:
docker compose watch

or run detached:
docker compose watch -d

--------------------------------------------------------

Summary for watch mode:
1-Create a docker-compose.yaml file to enable watch mode.
2-sync your machine/laptop app and public directory with docker app and public directory.
3-Run command docker-compose.yaml
4-Docker compose itself creates 

docker-compose.yaml (ye file create ho gai vs code main nechy wala code bhi hoga es file mein)

services:
  nextjs:
    build:
      context: .
      target: builder
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    command: npm run dev

OR

develop:
watch:
  action:sync
  path: /app # local app directory name (yani jo mere vs code main app file hai os ko target krwa rha hon)
  target: /app/app                      (ye dono docker ky andar hain jaha target ho rha)


(Then ye prompt claude ko dena hai)
do i need to another new image? please also tell me a reason regardless of yes or no

Answer: No, you don't need a new image.
OR
Answer: Yes a new image will be built automatically when you run docker compose watch.
(ye prompt dy kar hum ny pucha ky new image bney ki zarorat hai tw os ny kaha yes ye automatically khud he image generate kar leta 
hai jab ap docker-compose run karty hain tw)

(Ye command terminal/cmd mein run karni hai vs code ky)
docker compose watch  
(Ye command run karne ky bad agar error aye tw docker mein container ky andar sy file delete krni hai phir dubara apne vs code ky terminal/cmd mein docker compose watch ki command run karni hai then docker mein ja kar side bar sy container open karna hai or port py click kr ky run krna hai)

(docker compose watch terminal py run kia tha tw os ky nechy ye kuch line thi jo copy ki hain or nechy paste ki hain)
class15-app                Built
Network Class15_default    C
Container class15-app-1    S
Watch enabled
----------------------------------------------------------

(Ab ye prompt dena hai claude ko )
(docker compose watch jis terminal/cmd  py kia tha os ky nechy kuch logs thy enable wgera ky wo copy kar ky paste kiye claude py or nechy wala prompt bhi) 

(Jab docker compose watch terminal py run kia tha tw os ky nechy ye kuch line thi jo copy ki hain or yaha paste ki)
class15-app                Built
Network Class15_default    C
Container class15-app-1    S
Watch enabled
I have created a docker-compose.yaml file and above i have pasted the fresh logs tell me if my watch mode is enabled correctly.
Does any file and folder changes will reflect immeditaley?

(Jo first time docker run kia tha os ko he open kar k rakhna hai then page.tsx ki file mein change kia waha ja kar dekho tw waha bhi change hoga)




