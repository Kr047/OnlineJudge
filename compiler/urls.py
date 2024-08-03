from django.urls import path
from compiler.views import submit

urlpatterns = [
    path("2-Sum/",submit, name = "submit"),
]