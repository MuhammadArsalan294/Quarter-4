#################### Fundamental Prompt Technique ####################
______________________________________________________________________________________________________________________________

1- Zero Shot Prompting(Zero means without shot means example / Zero shot without example )

Yani hum ny LLM ko koi bhi example provide nahi ki or answer a gaya / ya hmein LLM sy direct bat karni ho.
Example hum es liye provide karty hain LLM ko jab hum chahty hain LLM wo he response krey jo hamare mind mein hai.
Prompt that does not contains any examples

OR 
Zero-Shot Prompting ka matlab hota hai AI ko bina kisi example diye task karwana.

Prompt:

"I love learning AI." "مجھے مصنوعی ذہانت سیکھنا پسند ہے۔"
______________________________________________________________________________________________________________________________

2- One Shot Prompting (One Example Promption)

Yani hum LLM ko one example provide karty hain.
Prompt that contains only one example

OR
Jab hum LLM ko ek example dete hain, aur uske baad usi example ki tarah ka naya kaam karne ko kehte hain.

Prompt:

Example:
"I love learning AI." → "مجھے مصنوعی ذہانت سیکھنا پسند ہے۔"
______________________________________________________________________________________________________________________________

3- Few shot Prompting

Yani hum LLM ko multiple example provide karty hain.
Prompt that contains 3-5 examples.

OR
Jab hum LLM ko (2 ya zyada) examples dete hain, taake wo pattern samajh kar usi style mein naya jawab de.

Prompt:

Example 1:
"I love learning AI." "مجھے مصنوعی ذہانت سیکھنا پسند ہے۔"

Example 2:
"He plays football." "وہ فٹبال کھیلتا ہے۔"
_______________________________________________________________________________________________________________________________

4- Role and System Prompting

Apne Agent ko prompt do instruction mein jis mein behavior btaya jaye. Yani apne agent ya system ko instructions main btana ky behave es trha karna hai.
Role + System Prompting can be used together.

"You are a Software engineer your expertise lies in writing APIS in Python FASTPI. Your task is to give highly optimize solution for the endpoints I request. The APIS should cover timeouts and rate limiting."

OR
1️⃣ Role Prompting

Jab hum LLM ko ek role assign karte hain (jaise teacher, developer, writer, doctor, etc.) taake wo usi role ke hisaab se jawab de — to ise Role Prompting kehte hain.

Example:

Prompt:
You are a professional blog writer.
Write an engaging blog post about Artificial Intelligence for beginners

2️⃣ System Prompting

System Prompt wo instruction hoti hai jo model ke system level par set ki jati hai, jisse AI ka overall behavior aur style control hota hai.

Example:

system_prompt = """
You are a helpful and knowledgeable AI assistant.
Always explain concepts clearly and in simple language.
"""

_______________________________________________________________________________________________________________________________

What is Chain of Thoughts

Chain of thought mein hum kahty hain ky soch samjh ky step by step jawab dena.Yani LLM sochta hai.

1- Step by step reasoning for complex problems
2- Think before answering
3- Show working

Example:
1- Maths Problem (Algebra problem)
2- Making a Dish
3- Trip to Northern Area
4- Buying a car
5- Telling doctor about your symptoms,
6- Relationship chain: apke mama kay bete ki mami ki ammi ki behn ka beta ka dost ka bhai apka kya hua?, When I was 4 my friend was half my age now I am 20 what is the age of my friend

Prompts:
1- Buying a car
2- Telling doctor about your symptoms,
3- Relationship chain: apke mama kay bete ki mami ki ammi ki behn ka beta ka dost ka bhai apka kya hua?, When I was 4 my friend was half my age now I am 20 what is the age of my friend

Prompt:
"I want to invest in crypto but keeping the market trends and fluctuations in mind. Think step by step: First, check current trends. Second, look at risks. Third, suggest safe options."

Prompt 2:
"For any investment query, think step by step: 1. Analyze trends. 2. Check risks. 3. Suggest options." This helps the agent avoid rushed, bad decisions."

OR

Chain of Thought ka matlab hota hai AI ka apna reasoning process,
jisme model step-by-step soch kar final answer tak pohanchta hai —
bilkul insaan ki tarah, jo sochta hai “pehle ye samjho, phir ye, phir answer nikalo.”

Example (Without Chain of Thought)

Prompt:

What is 12 × 13?

Output:

156
Yahan model ne seedha answer diya,
but reasoning (steps) nahi dikhayi.

Example (With Chain of Thought)

Prompt:

Let's think step by step.
What is 12 × 13?

Output:

12 × 10 = 120
12 × 3 = 36
120 + 36 = 156
So, the answer is 156.
Yahaan model ne step-by-step reasoning batayi —
yehi process Chain of Thought kehlata hai.
______________________________________________________________________________________________________________________________

What is Tree of Thoughts(TOT)?

LLM TOT main bhi sochy ga or yaha wo multiple possible ways main sochy ga.
Chain of thought main 1 possible ways main sochy ga or TOT main multiple possible ways main sochy ga ye difference hai in dono mein.

1- Explore MULTIPLE paths or possible ways.
2- Thinks in different paths
3- We could say Tell us 3 possible ways
4- Thinks Pros and Cons

Example:

1- How to control Air Pollution?
2- Tax Collection Problem: Country developing Solution: Tax Collection (50%)

Solution One:

1- High Class (50%)
2- Middle Class: 8%
3- Lower Class 1%

Prompt: I want to improve tax collection using a Tree of Thoughts approach, while considering taxpayer compliance and economic factors. Think 3 approaches for: First, analyze current revenue data. Second, identify common evasion methods. Third, propose three possible ways to implement a tax: a progressive income tax, a value-added tax on goods, and a property tax based on location and value.

OR

Tree of Thoughts ka matlab hai — AI ek hi line mein sochne ke bajaye bohat saari soch ki lines (branches) banata hai.
Yani AI ek se zyada possible ideas try karta hai — aur phir best idea choose karta hai.
Bilkul tree ki tarah, jisme ek stem se multiple branches nikalti hain

Example:

Socho tum AI ko bolte ho:

"Write a blog title about Artificial Intelligence."

Ab AI ke paas bohat saare ideas aa sakte hain:

“How Artificial Intelligence is Changing the World”
“The Future of AI: Smarter Machines Ahead”
“AI Revolution: Redefining Human Potential”

Ab AI har ek idea ko analyze karega:

Kya ye title attractive hai?
Kya ye SEO-friendly hai?
Kya ye topic se match karta hai?

Phir AI best title choose karega ✅

________________________________________________________________________________________________________________________________

What is Self-Consistency?

Yani hum friend sy puchty hain bar bar confirm karne k liye ky dinner py jana hai naw. Means kisi bhi cheez ki conformation lena.
OR
jab sir dard ho to hum 3 alag alag doctor ky pass jaty hain jo confirm kar dein ky migraine hai 

1- Need confirmation of a particular thing Example:
2- Buying a house
3- Confirming 3 different doctors to confirm that disease is actually a Migraine.
4- Asking a friend again and again to confirm about a dinner.
5- Consulting different mechanics about car engine.

Prompt: You are a tax auditor reviewing a business's financial records. To ensure self-consistency in your final report, you must cross-verify the reported annual revenue from three independent sources before confirming the figure.

Check the following three sources for consistency:

The official Income Statement submitted by the company.
The total deposits recorded in the company's primary bank statements for the year.
The sum of all sales invoices issued and logged in their internal accounting software.

OR

Self-Consistency ek aisi technique hai jisme AI ek hi question ke multiple answers generate karta hai,
phir un sab answers ko analyze karke sabse common ya logical answer choose karta hai

Example:

Socho tum AI se poochte ho:

“What is 25 + 37?”

AI agar normal “Chain of Thought” use kare to ek hi answer dega:
→ 62

Lekin agar hum Self-Consistency use karein, to AI multiple reasoning paths try karega 👇

Path 1:
25 + 30 = 55, 55 + 7 = 62 ✅

Path 2:
25 + 37 = (20 + 30) + (5 + 7) = 50 + 12 = 62 ✅

Path 3:
25 + 37 = 25 + 35 + 2 = 60 + 2 = 62 ✅

Sab answers same aaye — so AI ka logic self-consistent hai.
Agar ek path galat hota, to AI usko reject karke majority answer (62) ko choose karta.

________________________________________________________________________________________________________________________________

What is ReAct?

Re (Reasoning/Thoughts) 
Act (Action) 

Jab bhi LLM ky pass query jaye gi wo ous ko sochy ga phir os py react krey ga.

i.  Analyze the Query/Prompt Act (Action) 
ii. Call a tool/API


Prompt: Analyze this taxpayer's query about deduction eligibility. First, reason through the specific tax rules involved. Then, call the API to fetch their latest transaction history. Finally, provide a clear answer based on the combined data.

OR

What is ReAct?
Full Form:

ReAct = Reasoning + Acting

Yani AI sirf sochta (reasoning) nahi, balki kaam bhi karta hai (acting).

Example:

Prompt:

“Find the capital of the country where the Eiffel Tower is located.”

Step 1 – Reasoning (Soch)

AI sochta hai:

“Eiffel Tower Paris mein hai, aur Paris France mein hai.”

Step 2 – Action

AI ek action leta hai:

“Search for the capital of France.”

Step 3 – Observation

AI search ka result dekhta hai:

“The capital of France is Paris.”

Step 4 – Final Answer

AI soch ke kehta hai:

“The capital of the country where the Eiffel Tower is located is Paris.” ✅

________________________________________________________________________________________________________________________________

How to write an Effective Prompts

1- Be specific and clear
2- Use Action Verbs
3- Tell AI/Agent what to do. Avoid telling AI what NOT to do.
4- Provide examples: Providing the specific design reference to Lovable/vo.dev (Platform to convert design to code)
5- Use variables.

Prompt: Write an API in Python. Implement all the best practices like Rate-Limiting and spamming. The API should be optimize. The API should be have the POST method. The parameters should be from Pydantic class

Prompt with Variables: Write an API in {prog_language}. Implement all the best practices like Rate-Limiting and spamming. The API should be optimize. The API should be have the {api_method} method. The parameters should be from {validation} class

1. Be Clear & Specific 

AI ko exactly batao ke tum chahte kya ho.
Agar tum (ghuma phira) likhoge, AI bhi confuse ho jayega.

Example:

✅ “Write a 300-word blog about how Artificial Intelligence is transforming education, in a friendly tone.”
❌ “Write about AI.”

2. Give Context

AI ko background samjhao — kis audience ke liye likhna hai, kya purpose hai, kis style mein chahiye.

Example:

“You are a tech blogger. Write a detailed blog about AI tools for students in a friendly tone.”


3. Define the Role

AI ko ek role ya persona do — taake wo usi mindset se soch sake.

Example:

“You are a professional web developer. Explain Tailwind CSS to a beginner in simple words.”


4. Specify the Format

AI ko batao result kis format mein chahiye (text, HTML, markdown, bullet points, etc.)

Example:

“Give the answer in bullet points.”
“Return the blog in HTML format with headings and paragraphs.”



5. Set the Tone & Style 

Batana zaroori hai ke likhne ka style kaisa ho — friendly, professional, funny, serious, etc.

Example:

“Write in a conversational and friendly tone.”


6. Use Step-by-Step Instructions

Complex task ho to steps mein likho.

Example:

“Explain Prompt Engineering in 3 parts:

1."Definition"
2."Examples"
3."Benefits for developers.”

7. Give Examples (Few-Shot Prompting)

Agar AI ko pattern samjhana hai to ek ya do examples zaroor do.

Example:

“Example:
Input: Write a slogan for a fruit shop.
Output: Freshness You Can Taste!
Now write one for an online bookstore.”

8. Add Constraints (Rules) 

Kabhi kabhi AI ko boundaries dena useful hota hai.

Example:

“Use only 100 words.
Do not use difficult English words.”

Ye output ko clean aur controlled banata hai.

9. Ask for Improvement

Tum AI se keh sakte ho:

“Now improve this blog for SEO.”
“Make this explanation simpler.”



10. Test & Iterate

Prompt likhne ke baad agar result perfect nahi aaye — thoda modify karo, aur dobara try karo. Yehi Prompt Iteration process hai.

Example:

“You are a professional content writer.
Write a 500-word SEO blog about ‘AI in Healthcare’ in a friendly tone.
Include headings (H2), keywords naturally, and return in HTML format.”

In One Line:

“An effective prompt is clear, specific, contextual, and tells the AI who it is, what to do, how to do it, and in what style or format.”


###################Helping Prompts to Learn and Practice for the exams and homework############################

Prompt You are a prompt engineering expert. Your task is to make the fundamentals and complex prompt engineering concept easy to understand. I would be pasting the text from a Highly maintained Github Repo. Keep your vocabulary simple and easy to understand.
After your explanation I would provide a summary of what I have understand. Rate my summary out of 10 so I would get a better idea that where I am standing.



############# Project Related Discussion ############

FrontEnd: NextJS Backend: Python (Programming language) Backend Framework: FASTAPI

1- Make a FASTAPI endpoint
2- In the FASTAPI endpoint initialize the Agent and initialize the Runner
3- Return the Response to the Frontend

Javascript

export async function POST(){}
export async function GET(){}

Projects

1- AI Powered Blog website
2- AI powered Resume chatbot
3- AI powered ECommerce
4- Share on LinkedIn


NEXTJS + FASTAPI starter plate code

npx create-next-app --example https://github.com/vercel-labs/ai-sdk-preview-python-streaming ai-sdk-preview-python-streaming-example
