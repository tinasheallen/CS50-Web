from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entries, name="entries"),
    path("search/", views.search, name="searching"),
    path("new/", views.createPage, name="createPage" ),
    path("edit/", views.edit, name="edit"),
    path("editPage/", views.editPage, name="editPage"),
    path("randomPage", views.randomPage, name="randomPage")
]
