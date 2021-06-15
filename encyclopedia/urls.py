from django.urls import path

from . import views
app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("edit", views.edit, name="edit"),
    path("randompage", views.randompage, name="randompage"),
    path("new", views.new, name="new"),
    path("wiki/<str:title>", views.article, name="article"),    
]
