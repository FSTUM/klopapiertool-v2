from typing import Callable

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render

from common.utils.typing import AuthWSGIRequest

klopapier_staff_member_required: Callable = staff_member_required(login_url="login")


def leaderboard(request: AuthWSGIRequest) -> HttpResponse:
    ideas = []

    context = {"ideas": ideas}
    return render(request, "common/leaderboard/leaderboard.html", context)
