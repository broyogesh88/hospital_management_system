---

# 🏥 Hospital Bulk Processing Platform

Django Frontend (8000) + FastAPI Backend (8001) + Render API Integration

---

## 📌 Overview

This project provides:

### **Frontend (Port 8000)**

A **Django-based UI** that allows users to:

* Upload CSV files containing hospital data
* Manually create hospitals
* View all hospitals
* View all batches
* Activate / Deactivate batches
* Delete batches

### **Backend (Port 8001)**

A **FastAPI microservice** that:

* Parses and validates CSV files
* Creates hospitals in bulk via Render Hospital API
* Manages batches (activate, deactivate, delete)
* Provides listing APIs for hospitals and batches

### **Persistent Storage:**

All hospital data is stored in the **Render API**, not locally.

---

# 📁 Project Structure

```
project-root/
│
├── backend/             # FastAPI service
│   ├── app/
│   │   ├── main.py
│   │   ├── processor.py
│   │   ├── storage.py
│   │   ├── config.py
│   │   └── ...
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/            # Django UI
│   ├── hospital_app/
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

# 🚀 Running the Application

You can run the project in two ways:

---

# 🐳 Option 1 — Run with Docker (Recommended)

### 1️⃣ Build & start containers

```bash
docker-compose up --build
```

### 2️⃣ Access the apps

| Service             | URL                                                                                |
| ------------------- | ---------------------------------------------------------------------------------- |
| **Django Frontend** | [http://localhost:8000](http://localhost:8000)                                     |
| **FastAPI Backend** | [http://localhost:8001](http://localhost:8001)                                     |
| **Render API**      | [https://hospital-directory.onrender.com](https://hospital-directory.onrender.com) |

---

# 🛠 Option 2 — Run Locally (Without Docker)

### 1️⃣ Start backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

### 2️⃣ Start frontend (Django)

```bash
cd frontend
pip install -r requirements.txt
python3 manage.py runserver
```

Frontend runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Backend runs at: **[http://127.0.0.1:8001](http://127.0.0.1:8001)**

---

# ⚙️ Environment Configuration

Django uses the following environment variable:

```
API_BASE=http://backend:8001
```

When not set, it defaults to:

```
http://127.0.0.1:8001
```

---

# 📦 Docker Files

### **Frontend Dockerfile**

Runs:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

### **Backend Dockerfile**

Runs:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

### **docker-compose.yml**

Brings up both services and links networking.

---

# 📄 Available Features

## ✔ CSV Bulk Upload

Frontend → FastAPI → Render API
Batch ID generated automatically.

## ✔ View All Batches

Includes:

* Batch ID
* Number of hospitals
* Active / Inactive status

## ✔ Activate Batch

PATCH call:

```
/hospitals/batch/{batch_id}/activate
```

## ✔ Deactivate Batch

PATCH call with payload:

```
{"active": false}
```

## ✔ Delete Batch

Deletes all hospitals in the batch and removes from local mapping.

---

# 🔗 API Endpoints (FastAPI)

### **Bulk Upload**

```
POST /hospitals/bulk/upload
```

### **List Hospitals**

```
GET /hospitals
```

### **List Batches**

```
GET /hospitals/batches
```

### **Batch Details**

```
GET /hospitals/batch/{batch_id}
```

### **Activate Batch**

```
PATCH /hospitals/batch/{batch_id}/activate
```

### **Deactivate Batch**

```
PATCH /hospitals/batch/{batch_id}/deactivate
```

### **Delete Batch**

```
DELETE /hospitals/batch/{batch_id}
```

---

# 🧪 Testing

You can test FastAPI endpoints using:

```bash
http://localhost:8001/docs
```

You can test Django UI directly at:

```bash
http://localhost:8000
```

---

# ❗ Troubleshooting

### 🟠 Django cannot reach backend inside Docker

Make sure Django uses:

```
API_BASE=http://backend:8001
```

### 🟠 FastAPI “connection refused”

Ensure container is running:

```bash
docker ps
```

### 🟠 Batch not deleting

Ensure backend logs show DELETE calls to Render.

---

# 📌 Future Enhancements

* Persistent batch storage (DB)
* Background jobs for large CSV files
* Authentication (JWT/OAuth)
* Monitoring dashboard (Prometheus/Grafana)
* Retry + Dead-letter queue for Render failures
* Production Nginx gateway

---
