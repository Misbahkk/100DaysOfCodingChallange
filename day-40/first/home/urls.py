from . import views
from django.urls import path

urlpatterns = [
    path("",views.Home ,name="Home"),
    path("about/",views.About , name="about")
]
