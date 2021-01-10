# Flask app demo project ![Awesome](https://camo.githubusercontent.com/abb97269de2982c379cbc128bba93ba724d8822bfbe082737772bd4feb59cb54/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667)

This is a demo project to show how to deploy a two tier application using a kubernetes cluster (minikube). Helm charts are used to deploy the application.

## Pre-requisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed and running.
- Virtualization enabled in the host.
- [Docker](https://docs.docker.com/engine/install/) installed.
- [Helm](https://helm.sh/docs/intro/install/) installed.
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) CLI installed.

## Custer Architecture
![Cluster Architecture image](https://github.com/vgeorgework/Flaskdemo/blob/master/.readme_images/minikube%20cluster.jpg)

##  Summary
The flaskapp image that we created using Dockerfile is pushed to dockerhub public repository(*[flaskapp](https://hub.docker.com/r/vgeorgework/flaskapp)*). The cluster creates a flaskapp service to redirect traffic to front end pods which is replicated by replicaset. the Mysql service is deployed by statefulset. The pod mysql uses a persistant volume claim to claim the persistant volume. The cluster also creates Configmaps and Secrets to setup environment variables. Helm chart is used to deploy the entire kuberneties cluster.


## To run this project execute below commands using minikube.<br />

```
# minikube start
# eval $(minikube docker-env)
# cd Flask_/resources/ 
```
Execute both deployment files inside mysql and flaskapp folders respectively using k8s. <br />
Example :`# kubectl create -f mysql-svc-deploy.yaml ` this will deploy all the configuration for k8s cluster. <br />
`# minikube service flask-web-svc`     # will deploy the service outside cluster uses host browser for access. <br/>

## To execute the project using helm chart:

 1. clone the github repo using `#git clone https://github.com/vgeorgework/Flaskdemo.git` 
 2. change directory `#cd Flaskdemo` 
 3. execute setup.sh file #sh setup.sh   //will create flask app and MySQL services in your PC and opens up your default browser. 

> For your ease of use, I created a "setup.sh" script to execute all the
> steps automatically. 
