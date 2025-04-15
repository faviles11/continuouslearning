# 📘 Kubernetes Quick Reference Guide

![K8s Diagram](https://platform9.com/wp-content/uploads/2019/05/kubernetes-constructs-concepts-architecture.jpg)

---

## Directory explanation:

## 📂 Kubernetes Node Directory Reference Table

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

### Example of kubectl describe pod PODNAME:

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

### Example of kubectl logs PODNAME:

```text
[INFO] Server started at http://0.0.0.0:8080
[INFO] Connected to database
[INFO] Listening for requests...
[INFO] GET /api/health - 200 OK
```

### Example of:

crictl ps | grep PODNAME

a1b2c3d4e5f6 my-app:latest About a minute ago Running PODNAME

crictl inspect a1b2c3d4e5f6

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

---

## Basic `kubectl` Usage

| Command                                                      | Description                           |
| ------------------------------------------------------------ | ------------------------------------- |
| `kubectl create`                                             | Creates a resource.                   |
| `kubectl delete`                                             | Deletes a resource.                   |
| `kubectl create deployment nginx --image=nginx --replicas=5` | Creates a deployment with 5 replicas. |

---

## Maintaining Infrastructure

| Command                                                      | Description                                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------- |
| `kubectl create deployment nginx --image=nginx --replicas=0` | Creates a deployment with no active pods (useful for testing). |

| Use Case               | Note                                        |
| ---------------------- | ------------------------------------------- |
| Database in this setup | Not recommended without persistent storage. |

---

## ReplicaSets

| Feature    | Description                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------- |
| ReplicaSet | Ensures the desired number of pod replicas are running. Automatically handles volumes for each pod. |

---

## DaemonSets

| Feature   | Description                                                   |
| --------- | ------------------------------------------------------------- |
| DaemonSet | Ensures a specific pod runs on **every node** in the cluster. |

---

## Deployments

| Feature    | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| Deployment | Describes the desired state of pods, manages ReplicaSets, rolling updates, and rollback. |

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
