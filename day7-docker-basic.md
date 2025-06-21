# Day 7 – Docker Basics

## ✅ What I Learned
Docker is a platform to create, run, and deploy containers that include app code and dependencies.

## ✅ Containers vs VMs

| Feature         | Virtual Machine                | Docker Container            |
|----------------|--------------------------------|-----------------------------|
| OS             | Full guest OS                  | Uses host OS                |
| Size           | Heavy (GBs)                    | Lightweight (MBs)           |
| Boot time      | Slow (minutes)                 | Fast (seconds)              |
| Performance    | Moderate                       | High                        |

## ✅ Commands Used

```bash
docker --version
docker run hello-world
docker build -t python-docker-app .
docker run python-docker-app

