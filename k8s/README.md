# 📘 Kubernetes Quick Reference Guide

![K8s Diagram](https://platform9.com/wp-content/uploads/2019/05/kubernetes-constructs-concepts-architecture.jpg)

---

## Directory explanation:

### Kubernetes Node Directory Reference Table

| Directory Path                                   | Description / Purpose                                                               | What It's Useful For                                                        |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `/var/lib/kubelet`                               | Stores kubelet state, mounted volumes, pod specs, and other node-level runtime data | Inspecting pod state, checking mounted volumes, debugging pod lifecycle     |
| `/var/log/pods`                                  | Contains logs from running pods, organized by namespace and pod UID                 | Accessing pod logs directly from the node, especially after crashes         |
| `/var/lib/docker/containers` _(if using Docker)_ | Stores raw logs and container metadata used by the Docker runtime                   | Viewing low-level container logs, especially when `kubectl logs` fails      |
| `/etc/kubernetes`                                | Core cluster configuration, static pod definitions, kubeconfig files                | Inspecting static control plane pods, viewing admin kubeconfig              |
| `/etc/kubernetes/manifests`                      | Contains YAML files for static pods like kube-apiserver, etcd, kube-scheduler       | Managing core Kubernetes components on control plane nodes                  |
| `/etc/kubernetes/pki`                            | TLS certificates for secure communication between cluster components                | Debugging auth issues, renewing or replacing certificates                   |
| `/var/lib/etcd`                                  | Stores the etcd database files (only on etcd/control-plane nodes)                   | etcd backups/restores, checking data persistence                            |
| `/var/run/secrets/kubernetes.io/serviceaccount`  | Auto-mounted secrets inside pods containing service account tokens                  | Verifying service account authentication and access from inside a pod       |
| `/var/log/containers`                            | Symlinked logs for each container, named by pod and container                       | Easier way to correlate pod logs without needing container IDs              |
| `/var/run/docker.sock` _(if Docker is used)_     | UNIX socket used for communication with the Docker daemon                           | Accessing Docker directly with tools like `docker` or `crictl`              |
| `/run/containerd` or `/run/cri-containerd.sock`  | Containerd's socket and runtime files                                               | Used when containerd is the container runtime (common in modern Kubernetes) |
| `/var/lib/containerd`                            | Containerd's storage for images, containers, snapshots                              | Debugging container/image issues under containerd                           |

## Kubernetes Resource Types Overview

| Resource Type                        | Description                                                                                        | Common Use Cases                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `Pod`                                | The smallest deployable unit in Kubernetes. Can contain one or more containers.                    | Running application workloads                                               |
| `Deployment`                         | Manages a ReplicaSet to ensure a specified number of identical Pods are running.                   | Rolling updates, scaling applications                                       |
| `ReplicaSet`                         | Ensures a specified number of Pod replicas are running at all times.                               | Mostly used indirectly by Deployments                                       |
| `StatefulSet`                        | Like Deployments but for stateful apps. Maintains identity and order of Pods.                      | Databases, queues, or any app needing stable storage or hostnames           |
| `DaemonSet`                          | Ensures a Pod runs on **every** node (or selected nodes) in the cluster.                           | Running node-level services like log shippers or monitoring agents          |
| `Job`                                | Creates Pods to run batch jobs and ensures they finish successfully.                               | One-time batch processing                                                   |
| `CronJob`                            | Creates Jobs on a scheduled time (like a UNIX cron).                                               | Scheduled tasks (e.g., backups, reports)                                    |
| `Service`                            | Abstracts access to Pods as a stable network endpoint. Supports ClusterIP, NodePort, LoadBalancer. | Load balancing and service discovery                                        |
| `Ingress`                            | Manages external access to Services, typically via HTTP/HTTPS routing.                             | Exposing web applications using host/path-based routing                     |
| `ConfigMap`                          | Stores configuration as key-value pairs, separate from code.                                       | Injecting environment-specific configs into Pods                            |
| `Secret`                             | Stores sensitive data like passwords, tokens, and certificates (base64-encoded).                   | Secure configuration injection                                              |
| `PersistentVolume (PV)`              | A piece of storage in the cluster that has been provisioned.                                       | Used for durable storage needs                                              |
| `PersistentVolumeClaim (PVC)`        | A request for storage by a user, which binds to a PV.                                              | Allows users to consume cluster storage without worrying about provisioning |
| `Namespace`                          | Logical cluster partitioning to isolate resources.                                                 | Multi-team environments, resource separation                                |
| `Node`                               | A worker machine in Kubernetes (VM or physical).                                                   | Where Pods are scheduled and run                                            |
| `ServiceAccount`                     | Provides identity for processes inside Pods to talk to the API server.                             | RBAC and secure communications                                              |
| `Role` / `ClusterRole`               | Defines permissions within a namespace (`Role`) or across the cluster (`ClusterRole`).             | Fine-grained access control                                                 |
| `RoleBinding` / `ClusterRoleBinding` | Grants access defined in a Role to a user or ServiceAccount.                                       | Enabling RBAC policies                                                      |
| `HorizontalPodAutoscaler (HPA)`      | Automatically scales Pods based on CPU or custom metrics.                                          | Auto-scaling apps under load                                                |
| `NetworkPolicy`                      | Controls ingress and egress network traffic to/from Pods.                                          | Securing intra-cluster communication                                        |
| `ResourceQuota`                      | Limits resource usage (CPU, memory, etc.) in a namespace.                                          | Preventing resource exhaustion by enforcing limits                          |
| `LimitRange`                         | Sets default CPU/memory limits and requests for Pods/Containers.                                   | Applying sensible defaults and constraints                                  |

---

## Basic Architecture

| Component          | Role                                                |
| ------------------ | --------------------------------------------------- |
| API Server         | Central control plane component                     |
| Scheduler          | Decides where to place new pods                     |
| Controller Manager | Reconciles cluster state (e.g., Deployments, Nodes) |
| etcd               | Stores the cluster state (key-value)                |
| Kubelet            | Runs on nodes, manages containers                   |
| Container Runtime  | Actually runs the containers                        |
| kube-proxy         | Handles networking on each node                     |

---

## Configuration file example:

```text
apiVersion: v1           -> Specifies the API version to use
kind: Pod                -> The resource type
metadata:                -> Identifies: Name & Labels
  name: my-app
  labels:
    app: web
spec:                    -> Pod actual configuration
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```

---

## Kubernetes CLI Cheat Sheet

### Basic Commands

| Category            | Task                             | Command                                                  |
| ------------------- | -------------------------------- | -------------------------------------------------------- |
| Workload Management | Get all pods                     | kubectl get pods                                         |
| Workload Management | Get all deployments              | kubectl get deployments                                  |
| Networking          | Get all services                 | kubectl get svc                                          |
| Networking          | Get ingress resources            | kubectl get ingress                                      |
| Read/Inspect        | Describe a pod                   | kubectl describe pod PODNAME                             |
| Read/Inspect        | View deployment YAML             | kubectl get deployment DEPLOYMENT -o yaml                |
| Read/Inspect        | Get events                       | kubectl get events --sort-by=.metadata.creationTimestamp |
| Logs                | Get logs from a pod              | kubectl logs PODNAME                                     |
| Logs                | Follow logs in real time         | kubectl logs -f PODNAME                                  |
| Logs                | Logs from a specific container   | kubectl logs PODNAME -c CONTAINERNAME                    |
| Deployment & Config | Apply a YAML file                | kubectl apply -f filename.yaml                           |
| Deployment & Config | Create a deployment              | kubectl create deployment nginx --image=nginx            |
| Deployment & Config | Delete a pod                     | kubectl delete pod PODNAME                               |
| Deployment & Config | Execute shell inside a container | kubectl exec -it PODNAME -- /bin/sh                      |
| Port Forwarding     | Port forward a pod               | kubectl port-forward pod/PODNAME 8080:80                 |
| Port Forwarding     | Port forward a service           | kubectl port-forward svc/SVCNAME 8080:80                 |

### Advance Commands

| Category             | Task                           | Command                                                         |
| -------------------- | ------------------------------ | --------------------------------------------------------------- |
| Read/Inspect         | View all resources             | kubectl get all                                                 |
| Read/Inspect         | View resource usage (pods)     | kubectl top pod                                                 |
| Read/Inspect         | View resource usage (nodes)    | kubectl top node                                                |
| Deployment & Config  | Restart a deployment           | kubectl rollout restart deployment DEPLOYMENTNAME               |
| Deployment & Config  | Check rollout status           | kubectl rollout status deployment DEPLOYMENTNAME                |
| Deployment & Config  | Apply dry-run to preview YAML  | kubectl apply -f file.yaml --dry-run=client -o yaml             |
| Secrets & ConfigMaps | Create ConfigMap from env file | kubectl create configmap NAME --from-env-file=.env              |
| Secrets & ConfigMaps | Create Secret from literal     | kubectl create secret generic mysecret --from-literal=key=value |
| Secrets & ConfigMaps | Decode a base64 secret         | `echo <base64_string>                                           |
| Cluster Management   | Get nodes                      | kubectl get nodes                                               |
| Cluster Management   | Cordon a node                  | kubectl cordon NODE                                             |
| Cluster Management   | Uncordon a node                | kubectl uncordon NODE                                           |
| Cluster Management   | Drain a node                   | kubectl drain NODE --ignore-daemonsets                          |
| Cluster Management   | Delete all pods in a namespace | kubectl delete pods --all -n NAMESPACE                          |
| Context Switching    | Show current context           | kubectl config current-context                                  |
| Context Switching    | Switch context                 | kubectl config use-context CONTEXTNAME                          |

---

## kubectl & kubelet

| Component | Description                                                                          |
| --------- | ------------------------------------------------------------------------------------ |
| `kubectl` | CLI tool to send commands to the Kubernetes API Server.                              |
| `kubelet` | Runs on each node and translates API instructions into actions (e.g., running pods). |

---

## `kubeadm` Commands

| Command              | Function                                         |
| -------------------- | ------------------------------------------------ |
| `kubeadm init`       | Initializes the Kubernetes cluster.              |
| `kubeadm join`       | Joins a node to an existing cluster.             |
| `kubeadm reset`      | Cleans the current Kubernetes setup from a node. |
| `kubeadm token list` | Lists tokens to join new nodes to the cluster.   |

---

## `kube-system` Namespace

| Component    | Function                                              |
| ------------ | ----------------------------------------------------- |
| `etcd`       | Key-value database where all cluster state is stored. |
| `dns`        | Internal name resolution for services and pods.       |
| `calico`     | CNI plugin for networking and network policies.       |
| `kube-proxy` | Manages network rules and traffic routing.            |
| `scheduler`  | Decides on which node a pod should run.               |

---

## Container Runtime

| Runtime      | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| `containerd` | The container runtime used by Kubernetes to run containers. |

---

## Pod Troubleshooting

| Command / Path                 | Purpose                                     |
| ------------------------------ | ------------------------------------------- |
| `kubectl describe pod PODNAME` | Shows events and details of the pod.        |
| `kubectl logs PODNAME`         | Displays logs from the pod.                 |
| `crictl ps PIPE grep PODNAME`  | Shows running containers matching the pods. |
| `/var/log/PODDIR`              | Fetch pod data.                             |

### Example of:

```bash
kubectl describe pod PODNAME
```

```text
Name:         PODNAME
Namespace:    default
Node:         node-1/192.168.1.10
Start Time:   Mon, 10 Apr 2025 14:32:18 +0000
Labels:       app=my-app
Status:       Running
IP:           10.1.1.15
Containers:
  my-app-container:
    Container ID:   docker://a1b2c3d4e5
    Image:          my-app:latest
    State:          Running
    Started:        Mon, 10 Apr 2025 14:32:20 +0000
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  1m    default-scheduler  Successfully assigned default/my-app-pod-12345 to node-1
  Normal  Pulled     1m    kubelet            Container image "my-app:latest" already present on machine
  Normal  Started    1m    kubelet            Started container my-app-container
```

### Example of k:

```bash
kubectl logs PODNAME

```

```text
[INFO] Server started at http://0.0.0.0:8080
[INFO] Connected to database
[INFO] Listening for requests...
[INFO] GET /api/health - 200 OK
```

### Example of:

```bash
crictl ps | grep PODNAME

```

```text
a1b2c3d4e5f6 my-app:latest About a minute ago Running PODNAME

```

```bash
crictl inspect a1b2c3d4e5f6

```

```text
{
  "status": {
    "id": "a1b2c3d4e5f6",
    "state": "CONTAINER_RUNNING",
    "pid": 10234,
    "image": {
      "image": "my-app:latest"
    },
    "createdAt": "2025-04-10T14:32:20Z"
  },
  "info": {
    "runtimeSpec": {
      "linux": {
        "resources": {
          "cpuPeriod": 100000,
          "cpuQuota": 50000,
          "memoryLimitInBytes": 536870912
        }
      }
    }
  }
}
```

### Example of:

```bash
cd /var/log/PODNAME

```

```text
Then:
```

```bash
cat PODNAME/0.log
```

---

## Common Errors

| Error Type               | Description                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| High CPU or Volume usage | Check with `kubectl describe pod`.                                                                     |
| `CrashLoopBackOff`       | The pod failed to start multiple times. Which means that something could be happenning with the image. |

---

## Namespaces & Control Groups

| Concept                | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| Namespace              | Logical isolation of resources within a cluster. |
| Control Group (cgroup) | Restricts resource usage (CPU/RAM) of pods.      |

---

## Labels & Networking

| Item                          | Usage                                             |
| ----------------------------- | ------------------------------------------------- |
| Labels                        | Used to organize and select Kubernetes resources. |
| Network policies (via Calico) | Control traffic between pods based on labels.     |

---

## Manifests & Helm

| Tool          | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| Manifest YAML | Files that define Kubernetes resources (pods, services, etc.). |
| Helm          | Kubernetes package manager to install applications easily.     |

### Manifest are located in:

```bash
cat etc/kubernetes/manifest
```

### List helm packages

```bash
helm list
```

---

## Basic `kubectl` Usage

| Command                                                      | Description                           |
| ------------------------------------------------------------ | ------------------------------------- |
| `kubectl create`                                             | Creates a resource.                   |
| `kubectl delete`                                             | Deletes a resource.                   |
| `kubectl create deployment nginx --image=nginx --replicas=5` | Creates a deployment with 5 replicas. |

---

## Deployment types

| Command    | Description                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Deployment | Creates a deployment with no active pods (useful for testing). -> Database in this setup Not recommended without persistent storage. |
| ReplicaSet | Ensures the desired number of pod replicas are running. Automatically handles volumes for each pod.                                  |
| DaemonSet  | Ensures a specific pod runs on **every node** in the cluster.                                                                        |

---

## `/etc/kubernetes/manifests`

| File / Path                 | Description                                                                       |
| --------------------------- | --------------------------------------------------------------------------------- |
| `/etc/kubernetes/manifests` | System-critical YAMLs (etcd, controller-manager, scheduler). Auto-run by kubelet. |

---

## Persistent Storage (PV & PVC)

| Concept                       | Description                                          |
| ----------------------------- | ---------------------------------------------------- |
| PV (Persistent Volume)        | Cluster-level storage resource.                      |
| PVC (Persistent Volume Claim) | Pod's request to use a PV.                           |
| VolumeMount                   | Mounts PVC into the pod container.                   |
| StorageClass                  | Defines how storage is provisioned (e.g., AWS, GCP). |

---

## `--dry-run` Flag

| Command Pattern            | Purpose                                                            |
| -------------------------- | ------------------------------------------------------------------ |
| `--dry-run=client -o yaml` | Simulates the command without applying changes (good for preview). |

---

## Resource Limits in YAML

| Field                     | Purpose                  |
| ------------------------- | ------------------------ |
| `resources.limits.memory` | Limits pod memory usage. |
| `resources.limits.cpu`    | Limits pod CPU usage.    |

---

## Kubernetes Services

| Type           | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `ClusterIP`    | Internal communication within the cluster.                 |
| `NodePort`     | Exposes the service outside the cluster via a node’s IP.   |
| `LoadBalancer` | Uses cloud provider’s load balancer to expose the service. |

```bash
kubectl expose pod PODNAME --type=NodePort --port=80
```
