from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from common.utils.typing import AuthWSGIRequest


def leaderboard(request: AuthWSGIRequest) -> HttpResponse:
    ideas = []

    context = {"ideas": ideas}
    return render(request, "common/leaderboard/leaderboard.html", context)
