######################################################
TODO APP SIGNUP/SIGNIN FORM
######################################################

Auth/register.tsx (Folder or File)

Email             (Input Field)
Password          (Input Field)

Register          (Button) 

######################################################

await fetch('/api/registration') (Frontend Server / api url) (Yani api ky end point ko hum kah skty hain phone number)

@app.post('/api/registration')   (Backend/Fastapi Server / api url) (Yani api ky end point ko hum kah skty hain phone number)
@app.post('/api/registration/')  (Trailing Slash)
OR 
@app.post('/api/signup')         (Agar asa kia tw error aye ga kyu ky Frontend or Backend ky same end point/phone number hoone chahiye 
                                  yaha hum ny end point/phone number change kar dia tw error aye ga)

#####################################################

Rate Limiting:  (USE FOR SECURITY)
Yani hum kis context mein bat kar rhy hain. Hum API context mein bat kar rhy.
Rate Limiting bhi bhi hum Security ky liye krty hain ta ky hacker sy bach skein. hacker kasey hack karty hain wo aik python py assi script likhein gay ky apki api py within 5 second 1 lac request aye gi tw in sab sy bachny ky liye hum rate limiting lgaty hain.

Yani rate limiting ap ki API py apply hoti hai.Api kon c jo hum fastapi mein build karty hain un sari api py rate limit lgay ga.
Abhi tak hum ny kisi bhi user ko restrict nhi kia tha ap es had tak hmari api ko use kar skty ho.Jasey hum ny Todo App bnai thi waha hum ny kisi bhi user ko restrict nhi kia tha ky ap es had tak api ko use kar skty ho.

Yani jab bhi hum api bnaty hain tw hum user ko kbhi bhi unlimited access nhi dety.Yani wo API ki bat kar rhy hain sir jo server/database
main request karti hain.
Rate limit kia hota hai apki jo particular api jo server ya database main request karti ho ap un py rate limit lgaty hain. 

In terms of Server and Database.
Kisi bhi API ko ek specific time frame ky liye accessible bnana.

@app.post(/create)
@app.post(/read)
Yani ye api data base py request kar rhi es py hum rate limit lgaty hain.
Yani kisi bhi aik kam ko specific time mein he karna/specific time tak krna rate limiting kahlata hai.
OR (Own Wording)
Yani Api py rate limit lgana ta ky user aik time tak es ko use krey.
Jasey ramadan mein hum 30 rozey rakhty hain tw hmara 24 hours roza nhi hota roza fajar sy magrib tak hota. 
Jasey GEMINI/QWEN/CLOUDE ki api key jin main bhi rate limiting lagi hui hoti hai ta ky es ko user aik time tak he use krey jasey 10 hours use krey. 

#####################################################
Main.py
#####################################################

main.py (nechy wala sara kam main.py ki file main kia hai)

limiter =  
Limiter(key_func=get_remote_address)  (Aik variable bnaya limiter ka or Limiter ki Class ko call kia then key_func=get_remote_address 
                                       ka function pass kia jo kia krey ga user ky data/information ko track krey ga .)

app.state.limiter = limiter (upper wale limiter ko fastapi main ja kar store kar dia or jo chez fastapi ky pass hogi naw tw wo osy khud 
                             apne pass sy utha kar use kr ly ga.)

-----------------------------------------------------

@app.exception_handler(RateLimitExceeded) (Ye error handling ho rhi hai or RateLimitExceeded slowapi ky packages sy a rha hai)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Too Many Requests",
            "message": "You have exceeded the rate limit. Please slow down and try again later.",
        },
    )

-----------------------------------------------------

@app.get("/read") (Ye simple Api hai yaha rate limit nhi lgai.)
async def read():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]

-----------------------------------------------------

@app.get("/login")                 (Ye Api bnai/end point bnaya hai or nechy es py rate limit lgaya hai.)
@limiter.limit(3/minute)           (Number of request sab sy phle aye ga ky bhai kitni request allow karni hai then time frame aye ga jo 
                                   /sec/min/hours mein ho skta hai. Yani user 1 minute mein kitni bar login kar skta hai or agar 
                                   /second/minute/hours likha hai tw wo by default 1 consider hoga OR Yani agar koi number nhi hai tw wo by default 1 consider hoga.)
async def login(request: Request): (Agar rate limit lgani hai tw Request ka parameter hmesha pass krna prey ga agar nhi pass kia tw 
                                    error aye ga or ye fastapi ki library sy a rha hai.)
    return {"message": "Login successful"}

Browser py ja kar es url http://127.0.0.1:8000/docs py gaye waha fastapi ky end point GET /login py click kia then Try it out on click then Execute on click tw Response body mein Login successful print hua yani asey 3 bar karne sy Login successful print ho kar aye ga os ky bad Internal Server Error aye ga. Yani 1 minute ky andar bas 3 bar request kar skty hum 4 bar Internal Server Error aye ga.

-----------------------------------------------------

1- Create an endpoint named claude-code.
2- Rate limit this api to 2 request per 5 hours cycle.

@app.post("/claude-code")
@limiter.limit(2/5 hours) 
async def claude_code(request: Request): 
    return {"message": "Claude code executed successfully"}

Browser py ja kar es url http://127.0.0.1:8000/docs py gaye waha fastapi ky end point POST /claude-code py click kia then Try it out on click then Execute on click tw Response body mein Claude code executed successfully print hua yani asey 2 bar karne sy Claude code executed successfully print ho kar aye ga os ky bad Internal Server Error aye ga. Yani 5 hours ky andar bas 2 bar request kar skty hum 3 bar Internal Server Error aye ga.

-----------------------------------------------------

APIs browser ke Inspect → Network tab me visible hoti hain, jahan se koi bhi un requests ko dekh ya copy kar sakta hai. Isi liye hum rate limiting use karte hain taake API par excessive requests (spam ya abuse) ko control kiya ja sake. Lekin sirf rate limiting security ke liye kaafi nahi hoti; proper authentication aur authorization bhi zaroori hote hain.

