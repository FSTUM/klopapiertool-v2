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
                path(
                    "secret/",
                    include(
                        [
                            path("edit/<int:secret_pk>/", views.edit_secret, name="edit_secret"),
                            path("del/<int:secret_pk>/", views.del_secret, name="del_secret"),
                            path("add/<int:challenge_pk>/", views.add_secret, name="add_secret"),
                        ],
                    ),
                ),
                path(
                    "short_link/",
                    include(
                        [
                            path("edit/<int:short_link_pk>/", views.edit_short_link, name="edit_short_link"),
                            path("del/<int:short_link_pk>/", views.del_short_link, name="del_short_link"),
                            path("add/<int:challenge_pk>/", views.add_short_link, name="add_short_link"),
                        ],
                    ),
                ),
            ],
        ),
    ),
]
