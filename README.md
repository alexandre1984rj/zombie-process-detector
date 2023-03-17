# zombie-process-detector

Zombie processes are not active processes, but rather remnants of dead processes that have not been properly cleaned up by their parent process. When a process dies on a Linux system, its process descriptor stays in memory with a status of EXIT_ZOMBIE. The parent process is notified of the death of its child process with the SIGCHLD signal and is expected to use the wait() system call to read the exit status and other information from the dead process. This allows the parent process to retrieve information from the dead process before the zombie process is completely removed from memory.

Normally, the wait() system call is executed quickly, so zombie processes do not accumulate on the system. However, if a parent process is not programmed properly and never calls wait(), its zombie children will remain in memory until they are cleaned up. To kill zombie processes without rebooting the system, certain steps can be followed.

This app was written in Python with Docker for logging zombie processes info from k8s EKS node.

  <p align="center">
      <img width="150" src="./public/assets/zombie.png" alt="zombie" />
  </p>

# Installation

### Via helm chart
```
$ git clone https://github.com/alexandre1984rj/zombie-process-detector.git
$ cd charts
$ helm install zombie-process-detector .
```

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/alexandre1984rj/zombie-process-detector.git
$ docker build -t zombie-process-detector .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/alexandre84rj/zombie-process-detector/).
```
docker pull alexandre84rj/zombie-process-detector
```

### Run the container into k8s node
Create a container from the image.
```
$ docker run --name my-container -d alexandre84rj/zombie-process-detector
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
$ docker inspect -f '{{ .Config.Hostname }}' my-container
```

