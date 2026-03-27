#################### Essential Configuration Settings ####################


#################### Temperature(0-1) ####################

Ye control karta hai AI ke creativity level ko. OR Yeh parameters AI ke jawab dene ke andaaz ko control karte hain:

1- Low Temperature

Low(0-0.3) Yani jo kah raha hon wohi kam karna hai or kuch nahi karna. Low yani jo kah raha hon wo he likho zyada nahi socho.
Compromises the creativity of LLM. 
OR 
Low (0-0.3): Focused, consistent, deterministic responses

Example: Temperature 0: Math problems, factual questions, Law, Medical, Personal Organization Data collection
Example: Agar aap equation solve karne ko kaho, toh ye sirf correct step-by-step calculation karega.

2- Medium Temperature

Medium(0.4-0.7) Yani khelo bhi or parho bhi.
Creativity + Valid. 
OR 
Medium (0.4-0.7): Balanced creativity and consistency

Example: Temperature 0.7: Creative writing, brainstorming, Easy Writing, Email Writing, Summerize, Re-write(repharse)


3- High Temperature

High(0.8-1.0) Khelo bas parho nahi. 
Creativity + Relevancy could compromise. 
OR 
High (0.8-1.0): Creative, diverse, but potentially unpredictable

Example: Temperature 0.9: Poetry, experimental content, India Media 
Example: Agar aap story likhne ko kaho, toh ye har baar alag style aur unexpected twists ke sath likhega


#################### Output Length / Token Limits ####################

Token Limits(Token means words) es ka matlb hai LLM ky response ko chota karna. OR Ye decide karta hai ke AI ka jawab kitne words ya characters tak ja sakta hai.
Agar limit 200 hai to AI 200 tokens (roughly 150 words) ke baad ruk jayega.
Control the output lenght of the LLM response.

Example:
1- Two paragraph summary
2- Generate minutes of the meetings in 10 bullet points 


#################### Top-k and Top-P (Nucleus Sampling) ####################

'''''Top-K'''''

Top-k (K means number or ye static hoty hain) 
Top ky 10 student class mein sy picnic py jayein gay.
OR 
Ye setting AI ko batati hai ke jab wo next word predict kare, to wo sirf top k options me se choose kare.

Example:
Top-k = 2 (always prefer top 2 words) Sirf top 2 likely words consider karega.

Aj mosam boht
Acha
Bura
Thanda
Garam

Start ky do select hon ky kyu ky ye static hain 


'''''Top-P'''''

Top-P (ye dynamic hoty hain. Top-P is dynamic )
Jasey barish ky 50% chances hain.
Top P means wo student jin ki percentage 70% sy zyada hai wo picnic py jayein gay.
OR 
Ye “probability-based” control hota hai.
AI unhi words me se choose karta hai jinki combined probability ek limit (p) tak hoti hai.
In Top-P we set the threshold

Example:
Top-P = 0.8 (Yani 80% sy zyada )

Ah mosam boht
Acha  (50%)
Bura  (30%)
Thanda
Garam

Ye combine probability ko ly ga yani acha bura dono
When selecting a next word combine probability from the threshold will be nominated.



########## How Temperature, TopK and TopP work together ##########

1-Conservative (means focused): Temperature = 0.1, Top-P = 0.9, Top-K = 20

Temperature (Supreme Controller): Low
Top-P = 90% (Second Preference): High
Top-K = 20  (Least Preference): Low

2-Balanced: Temperature 0.2, Top-P 0.95, Top-K 30
3-Creative: Temperature 0.9, Top-P 0.99, Top-K 40