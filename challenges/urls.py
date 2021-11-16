from django.urls import include, path

from . import views

app_name = "challenges"

urlpatterns = [
    path("c/<str:short_link>", views.challenge_short_link, name="challenge_short_link"),
    path("challenge/<str:key>", views.challenge, name="challenges"),
    path(
        "management/",
        include(
            [
                path(
                    "challange/",
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
