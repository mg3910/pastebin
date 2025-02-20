from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paste/<uuid:paste_uid>", views.paste, name="paste"),
    path("upload/", views.upload, name="upload"),
    path("recent/", views.PasteListView.as_view(), name="recent")
]