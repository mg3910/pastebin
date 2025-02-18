from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paste/<int:paste_id>", views.paste, name="paste"),
    path("upload/", views.upload, name="upload")
]