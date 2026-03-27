Write a book using Docusaurus

Coding Agents: GEMINI-CLI/CLAUDE CODE

Prompt using SpeckitPlus

Primitive of SpeckitPlus:
  
1.Constitution(For the entire Project) yani constitution entire project ky liye hota hai contitution means kisi chez ka core maqsad jasey hum E-Commerce website bna rhy hain tw os ka maqsad hai user online shoping kar skey or agar blog website bna rhy tw os ka purpose user online news parh skey
Restaurent khul raha tw oska constitution hoga khana bechna custumer ko

2.Feature Development

1.Specifiation - spec.md (Flow of your Application)(Ky btao os project mein karna kia kia hai / Ya project kia bney Yani agar hmari aik E-commerce aplication ka os ka flow kia hoga. user aye ga wo product dekh skta hai add to cart py click krey ga tw ye hoga payment py click krey ga tw ye hoga)
Restaurent mein custumer yaha sy enter hoga or family ky table yaha lgein gay parking waha hogo or weter es trha aye ga. or khana asey deliver hoga or payment asey hogi

2.Plan - plan.md (Technical Planning) Yani frontend next.js ka lgy ga or backend python ka lgy ga database qterland ka lgy ga or gemini cli/ claude/ qwen hmara query agent hoga 
Restaurent ka plan ky bhi mennu kia hoga shaf kis trha hire hon gay itne table ka order dena hai

3.Task - task.md (Job Details )(Jis planning face mein apne jin shaf ko hire kia tha or weter ko hire kia tha jin parking walon ko hire kia tha ab unko task btein gay )

4.Implement - implement.md (start doing the task)(Jab Specification hogai planning ho gai task dy dia ab wo apna kam karn)


/clear

Api key system variable sy bhi check kar skty laptop ky search bar sy

Coding Agent: Qwen 

1. Use Context management carefully
2. Read the error carefully
3. Use Qwen


RAG CHATBOT 
RAG: Retrieval-Augmented Generation (Yani jo apky pdf sy jawab dy skein / jo apki organization ky database sy jawab dy skein)

1.Vector/Numbers Databasese (Database yaha hmara data store ho vector means number )
0.1 Normal Database stores data in text format. (Jasey Food panda  ki wesite hai os py agar biryani likha. or agar Food panda ky database mein exit ye query hogi biryani tw he wo data la kar dy ga warna kah dy ga food item not found)
0.2 Vector database stores data numbers.
0.2.1Vector database focuses on meaning or intent. (Vector data base meaning ya intent py kam karty hain. jasey yaha py likhein perfume or mere e-commerce website py kahi perfume likha he nhi hai jo likha hai os ky brand ka name likha or ab user aya user ny llikha perfume or mere e-commerce website py perfume ky branda ky name hain tw user jasey he perfume likhy ga osko sari chezein mil jayein g kyu ky wo perfume or brand ky name  ky meanings/intent same hain) 

2.Gemini/ Openai Embeddings Models Embedding models are responsible for converting text to vectors/numbers (ap ky vector data base mein data store hota hai numbers mein or hmari book ka content tw english mein hai tw os ko number mein kasey convert krein. number mein convert krna hmari zemadari nhi hai ye zemadari hai gemini ky embedding model ki )    


3. We will be using Qdrant Database


Hackathon 2

1.CLI based FASTAPI TODO APPLICATION
2.Clone the template from class09
3.Run two servers
0.1 NextJS: npm run dev/ pnpm run dev
0.2 FASTAPI: uv run uvicorn [filename]:[instancevariable --reload]
uv run uvicorn main:app --reload
pnpm run dev



