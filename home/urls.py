from django.urls import path, include
from home.views import all_probs
urlpatterns = [
    path("homescreen/", all_probs, name = "all_probs"),
]