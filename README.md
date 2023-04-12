[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## IDS 721 individual project 2

Project name: Kubernetes based Continuous Delivery

Created a customized Docker container deploys a python script that reverse a string.\
Pushed the image to DockerHub\
Project is deployed automatically to Kubernetes cluster whenever you push changes to the main branch of GitHub repository. \
The GitHub Actions workflow will automatically build, test, and deploy application to the Kubernetes cluster.\

# Steps to deploy with Kubernetes FastAPI app:
Push container to DockerHub (Optional): i.e. docker build -t <hub-user>/<repo-name>[:<tag>] and docker push <hub-user>/<repo-name>:<tag> Example of a pushed FastAPI container here: https://hub.docker.com/repository/docker/noahgift/fastapi-kube\
minikube start\
minikube dashboard --url\
Hover over link and "follow link"\
Create a deployment: kubectl create deployment hello-fastapi --image=registry.hub.docker.com/noahgift/fastapi-kube\
View deployment: kubectl get deployments\
Create service and expose it: kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080\
View services: kubectl get service hello-fastapi\
minikube service hello-fastapi --url\
Curl web service: i.e. curl http://192.168.49.2:31224 \
Cleanup:\
kubectl delete service hello-fastapi\
kubectl delete deployment hello-fastapi\
minikube stop
