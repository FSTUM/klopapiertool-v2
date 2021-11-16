from django.urls import include, path
from django.views.generic import RedirectView

from . import views

app_name = "challenges"

urlpatterns = [
    path("challenge/<str:key>/", views.submit_challenge, name="submit_challenge"),
    path(
        "management/",
        include(
            [
                path("", RedirectView.as_view(pattern_name="challenges:list_challenges"), name="management"),
                path(
                    "challenge/",
                    include(
                        [
                            path("list/", views.list_challenges, name="list_challenges"),
                            path("edit/<int:challenge_pk>/", views.edit_challenge, name="edit_challenge"),
                            path("del/<int:challenge_pk>/", views.del_challenge, name="del_challenge"),
                            path("add/", views.add_challenge, name="add_challenge"),
                        ],
                    ),
                ),
            ],
        ),
    ),
]
