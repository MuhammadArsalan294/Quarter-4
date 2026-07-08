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

