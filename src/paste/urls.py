from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paste/<uuid:paste_id>", views.paste, name="paste"),
    path("upload/", views.upload, name="upload"),
    path("recent/", views.PasteListView.as_view(), name="recent")
]