###################################################################
FASTAPI POWERED AUTHENTICATION AND AUTHORIZATION (USE FOR SECURITY)
###################################################################

Ai Native Application:       Means wo application jis main ai involve ho.
Cloud Native Development:    Means apni application ko docker mein containerize kia and kubernetes sy python ki image ko chlaya.
Cloud Native Ai Application: Means apni application ko start/first day sy he docker main chlao or start/first day sy he os mein ai
                             integrete kro or start/first day sy he os ko containerize kar do.

Native:                      Means start sy he os main cloud or ai lgao.Jasey mein karachi pada hua or karachi mein he prha or ab
                             job/bussiness bhi karachi mein he kar rha hn tw mein karachi ka he native hon.
Kubernetes:                  Means Kubernetes ka kia maqsad hai billion of user ko handle karna.

#############################################

Authentication:              Means Who are you.
Signup and Login Means jab bhi application py user ata hai tw wo ye btata hai ky main kon hon.
OR
Ap kisi bhi application py ja kar apni aik jaga bnaty ho yani ap kisi application py gaye waha ja kar as a user jaga bnai yani hum as a user register ho gaye jasey hum ny uni/school mein admission lia yani form fill kia form mein kia likha apne barey mein ky who are you.

#############################################

name: ali
password: ali@456 (Agar database main ye password jaye ga tw user ky liye ye security thread hai asey koi bhi user application ka user 
                   nhi bney ga es he liye nechy password hashing wala kam krty hain.)

Password Hashing: (Means user ka ali@456 ye same password kbhi bhi database mein store nhi karty. Yani es password ko lambi string/code 
                  word mein convert kar k database mein bhejty hain kyu ky database mein company ka data store hota hai agr hum password hashing nhi krein gay tw koi bhi hacker data nkl skta hai or application hack bhi kar skta hai)
password:         2hjjh342343bvhvj222222222v3h4   (password hashing ky bad database mein ye password jaye ga.)

#############################################

Edge Case:
Edge Case kia hota hai application main koi kharbi naw ho jaye es liye os ko phle sy handle karty hain.
Agar user already singup hai tw os ko aik message a jaye user already signup hai.

#############################################

JWT Tokens/Access Token
J- Json
W- Web
T- Token

Signup:
1- Password Hashing

Login Scenario:
1- Password Verify
2- Application will assign a JWT/Access Token.      (J-Json, W-Web, T-Token)
 - Login API "Depends" on form_data.                ( form_data  Yani user ny jo form fill kia os ka data la kar do)
 - create_access_token that return JWT/Access Token.

Jab user Sign up karta hai tw password hash hota hai.
Sign up ky bad user login karta hai login karty waqt apko 2 chezon ka khyal rakhna hai.
1- Password verify  (Yani password verify hoga. kyu ky database mein user ka alag password hota hai string mein lamba sa or user ky
                     pass alag password hai jo os ny rakha hua hai )
2- JWT/Access Token (Jab user signin ya login krta hai tw apki application user ko aik token assign/issue karti hai. Yani user jitni
                    bar login hoga apki application os ko har bar new token assign krey gi. JWT/access token har baar naya generate hota hai, same nahi hota.)

#############################################

Authentication: Means who are you.
Authentication main user sign up or sign in karta hai. Authentication ky bad hum user ko btaty hain ky apky pass application ko use karne
ki kitni authority/power hai.

Authorization: Means apky pass kia kia Authority/power hai OR Means Authority ya kisi bhi chez ki hadood ko btana.
Authorization hmesha Authentication ky bad hogi.

Example:
Hum ny governor house mein admission lia mtlb hum ny Authentication ki.Yani hum ny form fill kar ky btaya ky main kon hon.
Ab Sir ali jawad kisi bhi student ko remove nhi kar skty ye kam sirf sir Ameen ka hai. Yani sir ali jawad ko os ki power/Authority/hadood ka idea hai.

#############################################

(Ye Vs Code mein main.py ki file mein kam kia hai.)

1- Created a Pydantic Model for the user.
2- Created a fake_users_db list/array .
3- Handle the Edge case for already existing user.
4- Created a signup endpoint.
5- Hashed the password.

---------------------------------------------

(Hum ny main.py ki file main jo end point bnaye thy wo browser sy asey check karne hain ky thik chl rhy ya nhi)

http://127.0.0.1:8000/docs browser py ja kar es url py gaye Post /register py click kia then Try it out on click then 
("username": "string",) es ki jaga ("username": "abc",) ye likha or ("password": "string") es ki jaga ("password": "abc123") ye likha then Execute on click tw Response body py ye print ho gaya {"message": "User abc registered successfully"}. 

upper register ka kam check krna ky bad GET /me Get Current User py click kia then Try it out on click then Execute on click tw Response body main  {"username": "abc", or  "password": "$2b$12$gOo.VQWLnk3PndeJf9nJTetiHb0XzkDE2xgs4rsX24ykW8CFSMQF2"} ye aye ga.
Yani user ny password abc rakha or data base mein hmara password string mein lamba sa save hai yani application thik work kar rhi.

for loop: Jab bhi apko same kam karna ho repeatively tw waha hum loop ka use karty hain jbhi yaha for ka use kia hai. loop do hoty hain for loop or while loop.

#############################################

httsp:fastapi.tiangolo.com (Ye google py search kia or es web ky andar chly gaye es py click kar ky)

---------------------------------------------

httsp:fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
es url par web search perform karo or mjhe 2 paragraph ki summary extract kar ky dedo. Vocabulary ko easy rakhna.main aik engineer hon.

Sir ny browser py Fastapi ki app open ki or es ky andar chatbot icon ky upper click kr ky chatbot open kia waha ja kar upper wale url or line ko likh kar enter kia then

OAuth2 with Password (and hashing), Bearer with JWT tokens 
fastapi.tiangolo.com/tutorial

(Ye box a gaya es py click kia yaha main.py file ka code hoga. Sir ny bhi yaha sy he code ko copy paste kia tha.)
(Lekin main asey kam nhi karon ga main cloud ko prompt dy kar he os sy kam krwaon ga )

#############################################

Jab Project ban gaya tw mainey apni main.py ki file clear ki or sir ki copy paste ki tw error a gaya mere pass phir mainey cloud ko kha ky error thik kar do.
