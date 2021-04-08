from django.urls import path
from . import views

urlpatteerns = [
    path("", views.MujPrvniPohled.as_view(), name="index")
]