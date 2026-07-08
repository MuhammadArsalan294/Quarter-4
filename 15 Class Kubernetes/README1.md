###############################################
KUBERNETES INSTALLATION AND PRACTICE
###############################################

1- What is kubectl?

-Kubectl is a command line/CLI tools for kubernetes/k8s.

Command: winget install kubernetes.kubectl     (Jaha docker wala kam kia tha vs code mein waha terminal/cmd mein ye command run krni hai)
Verify installation:  kubectl version --client

(winget windows ka paystaore hai jaha application pari hoti hai.)

###############################################

2- MiniKube: (Minikube aik cluster hota hai jis py hum kubernetes sy related kam kar rhy hoty hain)

Command: winget install Kubernetes.minikube    (Jaha docker wala kam kia tha  vs code mein waha terminal/cmd mein ye command run krni hai)
verify installtion: minikube version           (Ye run karne sy phle laptop restart kia)

###############################################

3- Create Kubernetes cluster inside a Docker:

Command: minikube start --driver=docker        (Jaha docker wala kam kia tha vs code mein waha terminal/cmd mein ye command run krni hai)

Run commands after the Installtion:

minikube status
minikube dashboard  (Jab upper wali 3 installation ho jayein gi tw ye wali command run krey gay tw khud he kubernetes ka page browser
                    py open hoga means successfully installation ho gai hai)

http://127.0.0.1:54316/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/workloads?namespace=default
(kubernetes ka link hai ye jo browser py khud open hua tha)

NOTE: Incase the Installation fails run these commands and try again: 
(Agar error aya tw ye wala kam karna hai but mere pass error nhi aya tha tw mainey ye kam nahi kia means nechy wali command)

minikube delete
docker rm -f minikube-preload-sidecar
docker rm -f minikube
docker system prune -f (This will remove everything in from your docker)
docker volume rm minikube
minikube start --driver=docker

###############################################

(Ab kubernetes ky andar side bar py Pods py click krna hai yaha dekhein gay tw aik pod already hoga Running agar nhi hai tw nechy wali command dy kr banwa lein gay) 

pods ky andar 
1- Pyhton image     (Yani image ka container chlta hai hmesha)
2- Container
3- Pods             (Yani container Pods main chlta hai direct nhi chlta)
3.1 kubelet         (ye pod ky andar aik cheez hoti hai kubelet or ye kubernetes sy instruction leti hai)
3.2 containerd      (Ye container ka enginee hota hai)

(Ab ye cloud sy puchna hai)
Main kis trha already running pod ko delete karon? mjhe command do is sy related.

kubetcl delete pod my-first-pod 
(my-first-pod ye kubernetes main side bar main Pods py click kia tw waha agar pods create hoga tw oska name aye ga) 
(ye command bhi run karni hai vs code ky cmd mein jaha upper wali run ki waha he os ko clear/cls kr k lekin mainey ye command run nhi ki kyu ky mere pass pod create nhi hua tha tw delete kasey karta es liye mainey nechy wala kam kar ky pod create kia hai) 

###############################################

Lets Create your First Pod:

kubectl run my-first-pod --image=python --command -- sleep 3600  (Jaha docker wala kam kia tha  vs code mein waha terminal/cmd mein
                                                                  ye command run krni hai)

my-first-pod   (pod ka name)   
--image=python (python,ngnix,redis,node)
--command	   (Custom command run karo)
--	           (Yahan se container ka command shuru)
sleep 3600	   (Container ko 1 hour tak alive rakho OR yani 3600 seconds mtlb 1 hours tk pod chly ga phir band ho jaye ga) 

(kubernetes ka jo page browser py open hai waha side bar mein Pods py click kia tw my-first-pod create ho gaya ab Name ky nechy my-first-pod py click kia tw hum Metadata py a gaye Metadata means kisi chez sy related basic information name/description etc.)

