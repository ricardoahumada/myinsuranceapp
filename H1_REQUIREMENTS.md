# Allianz Hackathon
1. [ Requirements. ](#Requirements)
2. [ Solution delivery. ](#Solution_delivery)

<a name="Requirements"></a>
## Requirements

### 1. Github repo
Next characteristics are expected for the repo:
- Name: **myinsuranceapp-[YOURFIRSTNAME]**
  - e.g. myinsuranceapp-unax
- Branches: develop and deploy
  - **develop**: must contain all elements including...
    - Dockerfile
    - Jenkinsfile-develop
  - **deploy**: must contain all elements including...
    - k8 yaml manifests
    - terraform files
    - Jenkinsfile-deploy
  - It is expected that a push in "develop branch" will trigger the jenkins "develop-pipelin" build.
  - In the same way, it is expected that a push in "develop branch" will trigger the jenkins "deploy-pipelin" pipeline.
  - When develop phase fnish, a merge into deploy must be done and after a push for triggering the deploy pipeline.

### 2. Jenkins pipelines
Must exists two pipelines:
- **develop-pipeline** must include:
  - checkout
  - build/preparation
  - unit testings
  - acceptance testing (simulated/flask)
  - image build
  - image push
  - clean up
- **deploy-pipeline** must include:
  - checkout
  - build/preparation
  - unit tests
  - acceptance tests (simulated/flask)
  - image build
  - image push
  - k8 deploy
  - acceptance tests (real/request)
  - clean up

### 3. Docker image names
- The app image must be called: **myinsuranceapp[YOURFIRSTNAME]:v8**
  - e.g. myinsuranceappunax:v8

### 4. ACR
You can publish the image in dockerhub or acr. For ACR case, this comfig must be used.
- Login server: hackathonimages.azurecr.io
- Username: hackathonimages
- password: ctV/uI5D=8/lLq88YwXsy3XvGFJMEwgQ
- password2: RTJY/KJMsIgSLCpQfZepgicay3t5PoYG

### 5. Kubernetes workloads
You can deploy in mminikube or AKS. In any case, the kubernetes workloads must be called like this:
- deployment:
- service:
You must port forward the service to this port:
- 5050

### 6. AKS cluster
The cluster definition must have next characteristics:
- name: akshackathon[YOURFIRSTNAME]
- nodes: 2
- location: eastasia
Must not contain sensitive information

<a name="Solution_delivery"></a>
## Solution delivery
- You must upload your solution to the campus (https://campus2.netmind.es/mod/assign/view.php?id=12632).
- The delivery must iclude:
  - The github repo url (please add me to the collaborators)
  - The jenkins server url ([IP]:8080)
  - The AKS name and url/Fqdn