🚀 End-to-End Application Deployment on GCP using Docker & Kubernetes (GKE)

📌 Overview

This project demonstrates how to build, containerize, test, and deploy a Python application using Docker and Kubernetes on Google Cloud Platform (GCP).

The repository showcases a complete cloud-native deployment pipeline, where a Python data processing application is packaged into a Docker container and deployed to a Google Kubernetes Engine (GKE) cluster.

The project highlights modern DevOps and cloud engineering practices, including containerization, orchestration, automated testing, and scalable infrastructure deployment.

🏗 Architecture

The application follows a cloud-native containerized architecture.

Developer
   ↓
Python Application
   ↓
Docker Container
   ↓
Container Registry
   ↓
Kubernetes Deployment
   ↓
Google Kubernetes Engine (GKE)
   ↓
Scalable Cloud Application
Deployment Flow

The Python application is developed locally.

The application is packaged into a Docker container.

The Docker image is pushed to a container registry.

Kubernetes deployment configuration is created.

The application is deployed to Google Kubernetes Engine (GKE).

Kubernetes manages scaling, load balancing, and container orchestration.

⚙️ Technology Stack
Layer	Technology
Application	Python
Containerization	Docker
Orchestration	Kubernetes
Cloud Platform	Google Cloud Platform
Kubernetes Platform	Google Kubernetes Engine (GKE)
Testing	PyTest
Infrastructure	YAML
📂 Project Structure
app/
│
├── api.py
├── fetch.py
├── transform.py
├── mask.py
├── writer.py
├── main.py
└── __init__.py

tests/
│
├── unit tests for application modules

Dockerfile
requirements.txt
README.md
Module Responsibilities

api.py
Handles API communication and service interactions.

fetch.py
Responsible for retrieving raw data from source systems.

transform.py
Processes and transforms raw data into structured formats.

mask.py
Applies masking logic to sensitive or confidential data.

writer.py
Writes processed data to target systems or outputs.

main.py
Application entry point that orchestrates the full pipeline.

🐳 Docker Containerization

The application is containerized using Docker to ensure consistent environments across development, testing, and production.

Build Docker Image
docker build -t gcp-kubernetes-pipeline .
Run Container Locally
docker run -p 8000:8000 gcp-kubernetes-pipeline
☸ Kubernetes Deployment (GKE)

The Docker container is deployed to Google Kubernetes Engine (GKE) for orchestration and scalability.

Create GKE Cluster
gcloud container clusters create pipeline-cluster
Configure kubectl
gcloud container clusters get-credentials pipeline-cluster
Deploy Application
kubectl apply -f deployment.yaml
Expose the Service
kubectl apply -f service.yaml

Kubernetes manages:

container orchestration

automatic scaling

service exposure

application availability

🧪 Automated Testing

The project includes automated tests implemented using PyTest to validate application modules and ensure reliability across deployments.

Automated tests help ensure:

pipeline logic correctness

application stability

consistent behaviour across environments

Run tests locally:

pytest
📈 Key Features

✔ End-to-end cloud-native application deployment
✔ Docker-based containerization
✔ Kubernetes orchestration with Google Kubernetes Engine (GKE)
✔ Modular Python pipeline architecture
✔ Automated testing using PyTest
✔ Scalable container deployment architecture
✔ Production-ready DevOps workflow

🌍 Real-World Use Cases

This architecture can be used for:

Data processing pipelines

AI / ML model deployment

Microservices platforms

API services

Enterprise data platforms

🚀 Getting Started
Clone Repository
git clone https://github.com/harshitboots/gcp-kubernetes-pipeline.git
cd gcp-kubernetes-pipeline
Install Dependencies
pip install -r requirements.txt
Run Application
python app/main.py
👨‍💻 Author

Harshit Tripathi

Lead Data Engineer | AI Platform Builder

🌐 Portfolio
https://www.harshittripathi.com

💼 LinkedIn
https://www.linkedin.com/in/harshittripathi