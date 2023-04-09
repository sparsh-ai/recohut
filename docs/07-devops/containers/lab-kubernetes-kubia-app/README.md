# Deploying a NodeJS app in Kubernetes

## NodeJS App

It starts up an HTTP server on port 8080. The server responds with an HTTP response status code 200 OK and the text `You've hit <hostname>` to every request. The request handler also logs the client’s IP address to the standard output, which you’ll need later. The returned hostname is the server’s actual hostname, not the one the client sends in the HTTP request’s Host header.

```js
const http = require('http');
const os = require('os');

console.log("Kubia server starting...");

var handler = function(request, response) {
  console.log("Received request from " + request.connection.remoteAddress);
  response.writeHead(200);
  response.end("You've hit " + os.hostname() + "\n");
};

var www = http.createServer(handler);
www.listen(8080);
```

## Creating a Dockerfile for the image

To package your app into an image, you first need to create a file called Dockerfile, which will contain a list of instructions that Docker will perform when building the image. The Dockerfile needs to be in the same directory as the app.js file.

## Building the container image

Now that you have your Dockerfile and the app.js file, you have everything you need to build your image.

You’re telling Docker to build an image called kubia based on the contents of the current directory. Docker will look for the Dockerfile in the directory and build the image based on the instructions in the file.

![build](https://user-images.githubusercontent.com/62965911/211507784-57bd3cc2-e83e-4c96-a8cb-b913a4aa5a67.png)

The build process isn’t performed by the Docker client. Instead, the contents of the whole directory are uploaded to the Docker daemon and the image is built there. The client and daemon don’t need to be on the same machine at all. If you’re using Docker on a non-Linux OS, the client is on your host OS, but the daemon runs inside a VM. Because all the files in the build directory are uploaded to the daemon, if it contains many large files and the daemon isn’t running locally, the upload may take longer.

> Tip: You can see the list of locally-stored docker images by running ```$ docker images``` command.

> Note: Container images are composed of layers that can be shared among different images.

![docker-layers](https://user-images.githubusercontent.com/62965911/211507811-203b78ee-ac64-4193-a3e8-b2d9dda775b3.png)

## Running the container image

You can now run your image with the following command:

```
docker run --name kubia-container -p 8080:8080 -d kubia
```

This tells Docker to run a new container called kubia-container from the kubia image. The container will be detached from the console (-d flag), which means it will run in the background. Port 8080 on the local machine will be mapped to port 8080 inside the container (-p 8080:8080 option), so you can access the app through http://localhost:8080.

## Push the image to Dockerhub

```
docker tag kubia:latest sparshai/kubia:latest
docker push sparshai/kubia
```

## Docker commands

Here are some handy commands:

- ```$ curl localhost:8080``` for accessing your app.
- ```$ docker ps``` for listing all the running containers.
- ```$ docker inspect kubia-container``` for more detailed information
- ```$ docker exec -it kubia-container bash``` for starting docker shell
- ```$ ps aux``` for listing running processes inside docker
- ```$ docker stop kubia-container``` for stopping the container
- ```$ docker rm kubia-container``` for deleting the container
- ```$ docker push <your-id>/kubia``` for pushing image to DockerHub.

## Running the image on a different machine

After the push to Docker Hub is complete, the image will be available to everyone. You can now run the image on any machine running Docker by executing the following command: ```$ docker run -p 8080:8080 -d luksa/kubia```.

It doesn’t get much simpler than that. And the best thing about this is that your application will have the exact same environment every time and everywhere it’s run. If it ran fine on your machine, it should run as well on every other Linux machine. No need to worry about whether the host machine has Node.js installed or not. In fact, even if it does, your app won’t use it, because it will use the one installed inside the image.

## Kubernetes commands

Here are some handy commands:

- ```$ kubectl get nodes``` for listing cluster nodes
- ```$ kubectl describe node xxx-kubia-85f6-node-0rrx``` for retrieving additional details of an object
- ```$ alias k=kubectl``` to create alias for kubectl command
- ```$ kubectl get pods``` for listing pods
- ```$ kubectl get services``` for listing services

## Start the cluster

First step is to initialize the cluster in the first terminal:

```
kubeadm init --apiserver-advertise-address $(hostname -i)
```

That means you’re almost ready to go. Last you just have to initialize your cluster networking in the first terminal:


```
kubectl apply -n kube-system -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 |tr -d '\n')"
```


To join other nodes as workers to the master node, run command like the following that you will receive from the master terminal after starting the cluster.

```
kubeadm join 192.168.0.33:6443 --token 20l5u8.pekij3hq5xzux7h9 \
    --discovery-token-ca-cert-hash sha256:572d36c75cd7456302c44886f4ae99514956c99cef3db7a50be7ed78080f5a77
```

## Deploying your Node.js app

The simplest way to deploy your app is to use the kubectl run command, which will create all the necessary components without having to deal with JSON or YAML. This way, we don’t need to dive into the structure of each object yet. Try to run the image you created and pushed to Docker Hub earlier. Here’s how to run it in Kubernetes:


```
kubectl create deployment kubia-app --image=sparshai/kubia --port=8080
```

> Tip: Check the status by running ```$ k get pods``` or ```$ k describe pods``` for more detailed info.

## Behind the scenes

![deploy-process](https://user-images.githubusercontent.com/62965911/211507804-1c3d09cd-130e-49e4-90de-f3f91c312da4.png)

## Accessing your web application

With your pod running, how do you access it? We mentioned that each pod gets its own IP address, but this address is internal to the cluster and isn’t accessible from outside of it. To make the pod accessible from the outside, you’ll expose it through a Service object. You’ll create a special service of type LoadBalancer, because if you create a regular service (a ClusterIP service), like the pod, it would also only be accessible from inside the cluster. By creating a LoadBalancer-type service, an external load balancer will be created and you can connect to the pod through the load balancer’s public IP.

To create the service, you’ll tell Kubernetes to expose the ReplicationController you created earlier:

```
kubectl expose deployment kubia-app --type LoadBalancer --port 80 --target-port 8080
```

> Tip: ```k get services``` to get list of running services.