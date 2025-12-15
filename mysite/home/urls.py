from django.urls import path
from . import views

urlpatterns = [
    path("newborns/", views.newborn_list, name="newborn_list"),
]
