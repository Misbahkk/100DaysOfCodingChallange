from project_2 import views
from django.urls import path


urlpatterns = [
    path("Home/",views.Home1 , name='Home'),
    path("About1/",views.About1,name='About1'),
]