#!/bin/sh
#To execute this script the host machine needs to installed minikube, helm, git and kubectl
# git clone https://github.com/vgeorgework/Flaskdemo.git
# cd Flaskdemo
minikube start
eval $(minikube docker-env)
helm install --set db.username=testuser,db.password=user@123 flaskapp helmcharts/
kubectl get all
echo "sleeper executed for around 2 mins for cluster creation............................................................."
sleep 1m
kubectl get po
sleep 20
kubectl get all
sleep 1m
echo "checking with kubectl get all ...................................................... "
sleep 5
kubectl get all
echo "executing service command in minikube" 
sleep 5
minikube service flask-web-svc
