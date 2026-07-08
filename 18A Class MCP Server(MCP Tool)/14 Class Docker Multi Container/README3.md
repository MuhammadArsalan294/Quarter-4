####################################################
CLASS 14 (CREATE A DOCKER FRONTEND & BACKEND PROJECT)
####################################################

####################################################
PROMPT 1 (FRONTEND)
####################################################

Create a simple frontend project using Next.js (latest version) with App Router and Tailwind CSS enabled.

Requirements:
- The project should have a single page.
- Display "Hello World" in the center of the screen.
- Use modern React functional components.
- Apply basic Tailwind CSS styling (centered text, large font).
- Keep the code clean and minimal.
- Provide folder structure and main file code (app/page.tsx).
- Also include steps to run the project locally.

Output should be well-structured and beginner-friendly.

---------------------------------------------------

hello-world-app ki jaga frontend-nextjs kar do

####################################################
PROMPT 2 (BACKEND)
####################################################

Create a simple backend project using FastAPI (Python).

Requirements:
- Create a basic FastAPI app.
- Add one GET endpoint "/" that returns JSON:
  { "message": "Hello from FastAPI 🚀" }

- Enable CORS so that a frontend (e.g., Next.js running on localhost:3000) can access the API.
- Use clean and minimal code.

Project Structure:
- Include main.py
- Include requirements.txt

Docker:
- Add a Dockerfile to containerize the FastAPI app.
- The app should run on port 8000.
- Use uvicorn as the server.

Output:
- Provide complete code for:
  1. main.py
  2. requirements.txt
  3. Dockerfile
- Provide step-by-step instructions to run locally and with Docker.

Keep the explanation beginner-friendly and well-structured.

-----------------------------------------------------------

(Ye prompt claude ko dena hai)
You are inside a frontend-nextjs and backend-fastapi app router project.You are a docker expert and your task is to create a simple docker image for my frontend-nextjs and backend-fastapi project.
Create a simple docker image my goal is to create an image and run a container locally Donot do anything related to production great docker
or k8s

(Jab upper wala prompt dia claude ko tw os ny Dockerfile bna di frontend or backend ki or code bhi likh dia)
(Jab upper wala prompt dia claude ko tw os ny project ky root py docker-compose.yaml file bhi bna di or code bhi likh dia os mein yani docker-compose.yaml file frontend or backend ky nechy ban gai)

-----------------------------------------------------------

1. Create an Image: (Docker ky side bar mein images mein ye image bney gi)

docker open 
(Ye command  terminal/cmd mein run karni hai vs code ky)

cd "D:\QUARTER-4-PROMPT-ENGINEERING\14 Class Docker Multi Container\frontend-nextjs" (Terminal 1)
docker build -t frontend-nextjs . 
&
cd "D:\QUARTER-4-PROMPT-ENGINEERING\14 Class Docker Multi Container\backend-fastapi" (Terminal 2)
docker build -t backend-fastapi .

-----------------------------------------------------------

2. Run the Container:

(Ye prompt claude ko dena hai) 
I have created an image now i want to create a container give me command for it. Donot run by yourself just give me the command.


(Ye command  terminal/cmd mein run karni hai vs code ky)
docker run -d -p 3000:3000 --name frontend-container frontend-nextjs  (Terminal 1)
&
docker run -d -p 8000:8000 --name backend-container backend-fastapi   (Terminal 2)

(Agar container successfully run krey ga tw wo return krey ga id id yani number.)

----------------------------------------------------------

Mainey claude ko kaha mjhe watch mood enable karna hai tw tum mjhe command do tw is ny nechy wali command di tw wo mainey terminal py run ki

docker compose watch (Claude ny es trha ki command di thi termial py run krne ky liye) 


docker open kia container py aye backend py click kar ky backend run kia ab vs code open kia main.py ki file mein jo bhi change krein gay wo docker py bhi automatic change hoga.
docker open kia container py aye frontend py click kar ky frontend run kia ab vs code open kia page.tsx ki file mein jo bhi change krein gay wo docker py bhi automatic change hoga.

Docker py project asey hoga:

14classdockermulticontainer (es py click kia tw es ky andar frontend or backend dono hon gay)
fastapi-backend
nextjs-frontend