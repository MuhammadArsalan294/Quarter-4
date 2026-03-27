from fastapi import FastAPI # fastapi ky package/module main sy FASTAPI ki class ko import kia.ye class hai kyu ky es ka phla letter Capital hai.

app = FastAPI() #  yaha class ko initialize kia ya call kia () bracket lga kar. Jab bhi class bnti hai tw os ka aik object/instance/constructor bnta hai. or wo app ky variable main rakh dia

@app.get("/")     # ye aik decorator hai. Yani nechy wala function es app ka return statment ban jaye ga or .get method hai jo data ko ly kar ata hai read krne ky liye. / slash ka mtlb hai home page. Agar hum ny yaha /welcome likha tw phir server py bhi http://localhost:8000/welcome likhein ky tw he print hoga 
def read_root():  # ye function hai or os ka name hai 
    return {"Hello": "World"} # ye python ki aik dictionary hai 
 