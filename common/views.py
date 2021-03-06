from typing import Callable

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from common.forms import SelectIdeaForm
from common.models import Idea
from common.utils.typing import AuthWSGIRequest

klopapier_staff_member_required: Callable = staff_member_required(login_url="login")


def leaderboard(request: AuthWSGIRequest) -> HttpResponse:
    ideas: list[Idea] = list(Idea.objects.all())

    form = SelectIdeaForm(request.POST or None)

    voted_ideas: list[int] = request.session.get("voted_ideas", [])
    if form.is_valid():
        idea_id = form.cleaned_data["id"]
        # voted_ideas: list[int] = json.loads(voted_ideas_json)
        if idea_id not in voted_ideas:
            idea: Idea = get_object_or_404(Idea, id=idea_id)
            idea.votes += 1
            idea.save()
            voted_ideas.append(idea_id)
            # request.session["voted_ideas"]=json.dumps(voted_ideas)
            request.session["voted_ideas"] = voted_ideas
            messages.success(request, _("saved your vote for the idea '{}'").format(idea.content))

    context = {"ideas": ideas, "form": form, "voted_ideas": voted_ideas}
    return render(request, "common/leaderboard/leaderboard.html", context)


def login_failed(request: WSGIRequest) -> HttpResponse:
    messages.error(request, _("You are not allowed to login to the application."))
    return redirect("main-view")
