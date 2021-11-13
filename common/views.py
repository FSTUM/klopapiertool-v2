from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from common.utils.typing import AuthWSGIRequest


@login_required(login_url="login")
def dashboard(request: AuthWSGIRequest) -> HttpResponse:
    return render(request, "common/common_dashboard.html")
