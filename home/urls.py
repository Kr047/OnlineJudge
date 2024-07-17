from django.urls import path, include
from home.views import home_scr
urlpatterns = [
    path("homescreen/", home_scr, name = "home_scr"),
]