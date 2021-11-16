from typing import Callable

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from common.models import Idea
from common.utils.typing import AuthWSGIRequest

klopapier_staff_member_required: Callable = staff_member_required(login_url="login")


def leaderboard(request: AuthWSGIRequest) -> HttpResponse:
    ideas: QuerySet[Idea] = Idea.objects.all()

    context = {"ideas": ideas}
    return render(request, "common/leaderboard/leaderboard.html", context)
