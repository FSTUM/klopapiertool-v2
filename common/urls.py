from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "common"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="common:leaderboard"), name="index"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
