# 📘 Kubernetes Quick Reference Guide

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

| Command / Path                      | Purpose                                           |
| ----------------------------------- | ------------------------------------------------- | ------------------------------------------ |
| `kubectl describe pod PODNAME`      | Shows events and details of the pod.              |
| `kubectl logs PODNAME`              | Displays logs from the pod.                       |
| `crictl ps                          | grep PODNAME`                                     | Shows running containers matching the pod. |
| `/var/log/container`, `cni`, `pods` | System-level logs related to pods and networking. |

---

## Common Errors

| Error Type               | Description                             |
| ------------------------ | --------------------------------------- |
| High CPU or Volume usage | Check with `kubectl describe pod`.      |
| `CrashLoopBackOff`       | The pod failed to start multiple times. |

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
