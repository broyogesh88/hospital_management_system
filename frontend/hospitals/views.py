import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

API_BASE = "http://backend_service:8001/"   # FastAPI backend


# ----------------------------------------------------
# FRONTEND UI VIEWS
# ----------------------------------------------------

def dashboard(request):
    return render(request, "hospitals/dashboard.html")


# ---------------------------------------------
# LIST ALL HOSPITALS (GET /hospitals)
# ---------------------------------------------
def hospitals_list(request):
    try:
        r = requests.get(f"{API_BASE}/hospitals")
        hospitals = r.json()
    except Exception:
        hospitals = []

    return render(request, "hospitals/list.html", {"hospitals": hospitals})


# ---------------------------------------------
# CREATE HOSPITAL (POST /hospitals)
# ---------------------------------------------
def create_hospital_ui(request):
    result = None

    if request.method == "POST":
        payload = {
            "name": request.POST.get("name"),
            "address": request.POST.get("address"),
            "phone": request.POST.get("phone"),
        }

        r = requests.post(f"{API_BASE}/hospitals", json=payload)
        result = r.json()

    return render(request, "hospitals/create.html", {"result": result})


# ---------------------------------------------
# UPLOAD CSV → FastAPI bulk upload
# ---------------------------------------------
def upload_csv_ui(request):
    result = None

    if request.method == "POST":
        file = request.FILES["file"]

        r = requests.post(
            f"{API_BASE}/hospitals/bulk/upload",
            files={"file": (file.name, file.read(), "text/csv")}
        )
        result = r.json()

    return render(request, "hospitals/upload.html", {"result": result})


# ---------------------------------------------
# LIST ALL BATCHES
# ---------------------------------------------
def batches_list(request):
    try:
        r = requests.get(f"{API_BASE}/hospitals/batches")
        data = r.json()
        batches = data.get("batches", [])
    except Exception:
        batches = []

    return render(request, "hospitals/batch_list.html", {"batches": batches})


# ---------------------------------------------
# BATCH DETAILS (list hospitals inside a batch)
# ---------------------------------------------
def batch_details_ui(request, batch_id):
    try:
        r = requests.get(f"{API_BASE}/hospitals/batch/{batch_id}")
        hospitals = r.json()
    except Exception:
        hospitals = []

    return render(request, "hospitals/batch.html", {
        "batch_id": batch_id,
        "hospitals": hospitals
    })


# ---------------------------------------------
# BATCH ACTIVATE
# ---------------------------------------------
def batch_activate_ui(request, batch_id):
    requests.patch(f"{API_BASE}/hospitals/batch/{batch_id}/activate")
    return redirect(f"/hospitals/batch/{batch_id}/")


# ---------------------------------------------
# BATCH DELETE
# ---------------------------------------------
def batch_delete_ui(request, batch_id):
    requests.delete(f"{API_BASE}/hospitals/batch/{batch_id}")
    return redirect("/hospitals/batches/")

# ---------------------------------------------
# HOSPITAL DELETE
# ---------------------------------------------
def hospital_delete_ui(request, hospital_id):
    requests.delete(f"{API_BASE}/hospitals/{hospital_id}")
    return redirect("/hospitals/")

def batch_deactivate_ui(request, batch_id):
    requests.patch(f"{API_BASE}/hospitals/batch/{batch_id}/deactivate")
    return redirect("/hospitals/batches/")
