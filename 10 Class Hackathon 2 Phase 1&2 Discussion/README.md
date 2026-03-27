Frontend (Jo user ko dekhai deti hai or frontend bt krta hai backend sy address ky throw ya API ky throw )


Backend API (FASTAPI API Means Application Programming Interface) FastAPI python ka framework hai jo ky API bnata hai or endpoint apne pass rakhta hai. Frontend request krey ga apne backend sy backend ky pass koi naw koi endpoint hoga endpoint means address hoga.Means frontend bt krta hai backend sy address ky throw ya API ky throw. 

 
SQL Model (Backebd py endpoint hoga ous endpoint py sql ka section hoga or wo hmare database mein record ja kar insert ya update kr dy ga)
Hum python mein object oriented programming likhein gay or SQL Model model ko provide kr dein gay or SQL Model hamare database mein recode insert ya update kar dy ga.
SQL Model kia krey ka python ly ga or database ko provide krey ga

Database (Neon Postgress) id, task


FrontEnd Nextjs URL (localhost:3000)
FASTAPI backend URL (localhost:8000)
Frontend or Backend Asynchronous hon gay kyu ky server sy jb communication hota hai tw response aney mein time lgta hai.Ye hmesha Asynchronous rhy gi.



Backend Setup:

1.Initial a uv project
2.Create a virtual environment and activate it
3.Install package:
  uv add fastapi
  uv add pydantic
  uv add sqlmodel
  uv add psycopg2   (ye python or sql ky between communication ky liye hoti hai)
  uv add uuid
  uv add python-dotenv
  uv add unicorn

Backend Server Run:

uv run uvicorn main:app --reload (uv venv then ye command chly gi)

localhost:8000/docs

Code 200 (Means ok)
Code 400 (Means User/Developer Error)
Code 500 (Means Server  Error)


main.py (file)

1.Loaded Environment Variable
2.SQL Model Class
3.Create A Function To Create A Database And Table

Frontend Setup:

Create a NextJS app router project: npx create-next-app@16.0.10


Database Setup:

1.Goto Vercel and click on Storage then Create Database on click
2.Select Neon and click Continue
3.Name your Database and Click on Continue/Done  (name ye rakha tha neon-pink-book)
4.Copy snippet the Credentials.
5.Create a file named .env at the root of your Python FastAPI project and paste the Credentials you copied.
6.Goto Neon Official website(https://neon.com/) to see the Table and record (Neon Database )


Neon Official website(https://neon.com/):

Login
Vercel py jo name tha wo khud a jaye ga yaha or os ky upper click kia
Sidebar scrool and tables on click 