from django.urls import path, include
from home.views import all_probs
from loginstartup.views import logout_user
urlpatterns = [
    path("", all_probs, name = "all_probs"),
    path("logout", logout_user, name="logout-user"),
]