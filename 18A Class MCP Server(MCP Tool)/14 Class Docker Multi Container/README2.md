######################################################
CLASS 14 MULTI CONTAINERS
######################################################

Multi Containers:

Multi container main 2 chezein hoti hain aik microservice architecture or dusra two/three tier architecture.
1- Microservice Architecture 
2- Two/Three Tier Architecture

######################################################

1- Microservice Architecture:

Micro:                       means small.
Service:                     means koi bhi asa feature jo apki application apko provide kar rhi hai.

MicroService:                means aik idea hai / Architecture ka name hai.
Multi Container:             means ye os idea ki implementation.

Todo App Features: (FASTAPI) (Ye hum ny Application bnai thi nechy os ky features hain. Yani 3 features hain es ky tw 3 container bhi bney gay)
1- Signin / Login
2- Dashboard (Todo Features)
3- Free Tier / Premium Tier  


What is Microservice:
1-Number of feature are equal to number of FastAPI application.
2-different features means different containers.
3-different containers communicate through network.

Microservice main kia hota hai jitne feature utni Fastapi ki application/container. Upper 3 feature hain tw fastapi ki 3 application/container bney gay.
Microservice aik orctehecer hai jis mein kia hota hai apki jitni application ky features hon gay naw wo alag alag bney gay kbhi bhi aik sath 
nhi bney gay.
Microservice ka sab sy zyada faida ye hai ky agar application ki aik service/feature bhi down ho tw baki ki kisi application py os ka empact nhi
parta. Jasey whatsapp or facebook or instagram teno alag alag application hain. Yani alag alag container bney gay inky.
Apka bhi phone hai mera bhi hai kisi or ka bhi hai yani sab ky pass alag alag phone hai. Yani multi container consider krty hain hum es ko
agar mere phone sy kisi or ky phone py bat krni ho tw es ky liye sab sy zyada zarori network hota hai jazz/ufone/telenore/zong.
Agar network nhi hai tw hum appas mein bt nhi kr skty. 


Microservice One Line Answer:
Application ky jitne feature utne he containers bhi.
OR
Microservice kia hota hai jitne features utni he apki application/container.

######################################################

2- Two/Three Tier Architecture:

Technology based decision: (Yani 2 technology hain es ki tw 2 container bhi bney gay)
1- Frobtend: Nextjs 
2- Backend: Fastapi
OR 
Storage: Postgres
Caching: Redis

Jab bhi Two/Three Tier Architecture ki bat hogi tw ap technology base decision lein gay yani backend ky 10 feature hain tw 1 container bney ga
or Jab Microservice Architecture  ki bt hoti hai tw decision ap application ky feature ky hisab sy lety hain yani 3 features hain tw 3 container bney gay

######################################################
CHATGPT
######################################################

Multi Containers (Short)

Multi-container ka matlab:
Ek app ko multiple containers mein run karna

-----------------------------------------------------

1. Microservice Architecture

Rule:
Jitne features utne containers

Example:
Login     →  1 container
Dashboard →  1 container
Premium   →  1 container

Simple:
Har feature alag app/container hota hai
Sab network se connect hote hain

----------------------------------------------------
2. Two / Three Tier Architecture

Rule:
Jitni technologies utne containers

Example:
Frontend (Next.js)   →  1 container
Backend  (FastAPI)   →  1 container
Database (Postgres)  →  1 container

----------------------------------------------------

Final Difference:
Microservice: feature base (zyada containers)
Tier Architecture: technology base (kam containers)

One Line Yaad Rakhna:
Microservice = Features wise containers
Tier = Technology wise containers

######################################################
YE SIR KY LECTURE SY COPY KIA
######################################################

dockerfile frontend or backend dono ky andr hogi 
docker-compose.yml ye root level py hogi mtlb frontend or backend ky nechy he

(Ye prompt dena hai claud ko)
Create a docker compose file with watch mode. I want to run my backend fastapi and frontend nextjs in docker.
Donot do anything related to k8s or  production grade docker.I only want to run this in docker desktop.

docker compose up (ye sir ny termial py run ki hai )

docker open kia container py aye backend py click kar ky backend run kia then backend ka url hoga http://localhost:8000 es ky sath /docs likh kar dekhna hai work kar rha ya nhi then.
try it out on click then
Execute on click then
Response body py Hello world a gaya

docker open kia container py aye backend py click kar ky backend run kia ab vs code open kia main.py ki file mein jo bhi change krein gay wo docker py bhi automatic change hoga.
docker open kia container py aye frontend py click kar ky frontend run kia ab vs code open kia page.tsx ki file mein jo bhi change krein gay wo docker py bhi automatic change hoga.

Docker py project asey hoga:

14classdockermulticontainer (es py click kia tw es ky andar frontend or backend dono hon gay)
fastapi-backend
nextjs-frontend







