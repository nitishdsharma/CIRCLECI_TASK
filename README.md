## Assignment Info 
Deploy Kubernetes Pod using CircleCI.

## Jobs performed
1. Creating a Docker image
2. Pushing it to the Docker Hub (Registry).
3. Running a Kubernetes deployment script which calls the Docker image.

## Requirements and Dependencies
1. CircleCI 2.1
2. Kuberentes cluster with 1.13+ version.
3. Dockerfile for the webservice.
4. DockerHub registry - To push and store the docker images.
5. Workstation
6. Github account

## Deployment steps
1. Create  Kuberentes single node cluster by removing taints. Initializa with Public IP of the node.

	1) kubeadm init --pod-network-cidr=192.168.0.0/16 --apiserver-cert-extra-sans=<Public IP>
	2) Ref doc: https://medium.com/htc-research-engineering-blog/install-a-kubernetes-cluster-with-kubeadm-on-ubuntu-step-by-stepff-c118514bc5e0
2. Remove taints to deploy the pods on master node itself. Use the below command.

	1) kubectl taint nodes --all node-role.kubernetes.io/master- 

3. Apply Calico CNI for setting up K8S communication and policy.

4. Creat a service account, role, Token and role binding to access services, objects of a particular namespace in K8S environment.

5. Create application Dockerfile, deployment script and config.yaml for circleci. Pushed them in a Git Repository.

6. Link the CircleCI account with Github Repository.

7. Add the Github Repository as a Project in CircleCI, start following it. Add the required environment variables such as KUBERNETES_SERVER, KUBERNETES_TOKEN, DOCKER_USERNAME etc in the project.

8. Commit all the script files in Github Repository.

## Output

1. Commit should trigger the CircleCI Project job and it should be successful.

2. Webservice pod and its service should be up and running.

## Testing the accessiblity of Pod

1. Identify the service NodePort.

2. curl Public IP:NodePort

3. Query response should contain Name and Joke by Chuck Norris.
