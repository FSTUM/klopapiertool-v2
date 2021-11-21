import json
from typing import Callable, List, Set

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from common.forms import SelectIdeaForm
from common.models import Idea
from common.utils.typing import AuthWSGIRequest

klopapier_staff_member_required: Callable = staff_member_required(login_url="login")


def leaderboard(request: AuthWSGIRequest) -> HttpResponse:
    ideas: List[Idea] = list(Idea.objects.all())

    form = SelectIdeaForm(request.POST or None)

    voted_ideas: List[int] = request.session.get("voted_ideas", [])
    if not isinstance(voted_ideas, list):
        voted_ideas = list()
    if form.is_valid():
        idea_id = form.cleaned_data["id"]
        # voted_ideas: List[int] = json.loads(voted_ideas_json)
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
