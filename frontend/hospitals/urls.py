from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),

    # Hospital List + Create
    path("", views.hospitals_list, name="hospitals_list"),
    path("create/", views.create_hospital_ui, name="create_hospital"),

    # CSV Upload
    path("upload/", views.upload_csv_ui, name="upload_csv"),

    # Batches
    path("batches/", views.batches_list, name="batches_list"),
    path("batch/<str:batch_id>/", views.batch_details_ui, name="batch_details"),
    path("batch/<str:batch_id>/activate/", views.batch_activate_ui, name="batch_activate"),
    path("batch/<str:batch_id>/delete/", views.batch_delete_ui, name="batch_delete"),

    # Hospital actions
    path("delete/<str:hospital_id>/", views.hospital_delete_ui, name="delete_hospital"),
    path("batch/<str:batch_id>/deactivate/", views.batch_deactivate_ui),

]
