Container is an instance that runs you application .
(Container hmari application ko docker ky environment mein chlata hai.)

###############################################
KUBERNETES
###############################################

Mere laptop ka aik feature hai jis mein 8GB RAM hai, Yani mere laptop mein space hai tw mein es mein application install kron ga
jasey application install hogi tw space bhi kam ho jaye gi. Jasey space full hone lgay gi tw hum unneccessary chezon ko hata dein gay.
Asey he application install karty rhy tw space full ho gai ab hum kia karein gay RAM increase karwa lein gay 16GB RAM krwa lein gay.Jab 16GB RAM bhi full ho jaye gi tw hum 32GB RAM karwa lein gay.Yani abhi tak hum RAM ko increase kiye ja rhy hein.

Jo hum ny local/vs code ya docker py container run kiye thy tw wo kia karty thy mere machine/laptop ki resources/RAM OR CPU ko istamal krty thy. Yani Container kia krty hain mere machine/laptop ki resources/RAM or CPU ka use karty hain.

(Sir ny likhwaya)
(Jitne users application use karty hain tou container par load jata hai aur container machine/laptop ki resources/RAM ko use karty hain.)

Main chata hn jasey he mere resources/RAM or CPU full hn tw aik or machine/laptop khud he start ho jaye ya phir mein khud manually ye kam kron. Yani main 365 day machine/laptop ly kar beitha raha AWS, Azure, Google cloud khol kar ya phir ye kam khud ho jaye automatic.

Jasey ky Hmari application container py hai or india or pak ka match hai tw users a gaye aik sath 1 lac tw space full ho gai tw asey hmari application crash ho jaye gi ya down ho jaye gi over traffic ki waja sy.
Yani hmari application crash nhi honi chahiye es ky liye ya 24 hour beithy raho apne resources/RAM or CPU ko barhaney liye taky agar users mere
container par aye or container py load prey tw hmari application kbhi bhi crash naw ho or ye cheez posible nhi hai ky main 24 hours machine/laptop ly kar beitha rahon. Ya phir mjhe koi asa software mil jaye jo ye resources/RAM or CPU ky process ko automate kar dy es process ka name hai kubernetes.

Why Kubernetes?
-Kubernetes is a system that manage scalling, healing and load balancing across containers.
(Yani mere application hai os py users a rhy hain or load par rha hai tw kia ho ga ya mere application crash hogi agar ap chahty 
ky ye kbhi crash yani down naw ho tw hmein resources/RAM or CPU increase krne hongay es k liye aik automatic tool hai
jis ka name kubernetes hai.)

Yani hum ny resources rent ki hain jab koi bhi chez rent py lety tw os ki cost ati hai.
Scaling: Yani india or pak ka match tha wo khtm ho gaya ya jab application py users ka traffic aya tha tw container py resources/RAM or CPU increase ho gaye thy or ab wo sara traffic ticket khareed kar chla gaya ab kia hoga wo resources/RAM or CPU tw khtm ho gaye es ko khty hain scalling jab kubernetes py koi traffic ata hai tw kubernetes khud he es ko scale up karta hai yani resources/RAM or CPU ko increase karta hai or jasey he traffic chla jaye tw os ko khud he scale down karta hai kyu ky resources/RAM or CPU farig ho gai ab. Ye sari chez kubernetes khud handle krta hai.
Healing: Yani agar koi container crash ho rha tw os ko dubara up karna. Ye sari chez kubernetes khud handle krta hai.
Load balanceing:  Jab load aye ga ap ki application py os ko bhi ye balance krey ga. Ye sari chez kubernetes khud handle krta hai.  

Container ki automatic management ky liye kubernetes bana hai. Yani mere software ka khyal rakhne k liye bnaya gaya hai kubernetes


What are pods?

-Container lives inside pods in k8s/kubernetes.
(kubernetes mein container kaha hoty hain pods ky andar es ka mtlb kubernetes jab bhi bt krey ga wo apky pod sy krey ga.)

- 99% of the times there is only one Container in a pod.
(1 container mein hmesha aik he pod hoga.)

1-Container aik Residents hai yani society/colony 
2-Pod aik Apartment hai yani flat

###############################################
CHATGPT
###############################################

🚀 Kubernetes Short Notes:

Docker containers humare laptop/machine ki RAM aur CPU use karte hain.

Agar users zyada aa jayein (high traffic), to:

-Load barh jata hai
-RAM/CPU full ho jata hai
-Application crash ya down ho sakti hai

Is problem ka solution Kubernetes hai.

----------------------------------------------

🤖 Kubernetes kya karta hai?

1. Scaling 📈📉

Traffic zyada ho → resources increase (scale up)
Traffic kam ho → resources decrease (scale down)

2. Healing 🔄

Agar container crash ho jaye → automatically restart ho jata hai

3. Load Balancing ⚖️

Traffic ko different containers mein divide/balance karta hai

----------------------------------------------

📦 Pods
Kubernetes mein container Pod ke andar hota hai
Usually 1 Pod = 1 Container

👉 Simple Example:

Container = Resident
Pod = Apartment

----------------------------------------------

🧠 Conclusion

Kubernetes ek automatic system hai jo:

Application ko crash hone se bachata hai
Resources (RAM/CPU) manage karta hai
Manual monitoring ki zarurat kam karta hai

