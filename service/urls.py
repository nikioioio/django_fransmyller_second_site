from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name = "page-service"),
    path("upload/", views.simple_upload, name = "upload_file"),
    path('upl/', views.read_file)
]