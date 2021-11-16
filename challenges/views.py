from django import forms
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext as _

from challenges.forms import ChallengeForm, UserSolutionSubmissionForm
from challenges.models import Challenge, ChallengeShortLink
from common.utils.typing import AuthWSGIRequest
from common.views import klopapier_staff_member_required


def challenge_short_link(request: WSGIRequest, short_link: str) -> HttpResponse:
    challenge_obj: ChallengeShortLink = get_object_or_404(ChallengeShortLink, short_link=short_link)
    return redirect("challenges:challenges", challenge_obj.challenge)


def challenge(request: WSGIRequest, key: str) -> HttpResponse:
    challenge_obj: Challenge = get_object_or_404(Challenge, key=key)

    form = UserSolutionSubmissionForm(request.POST or None)
    if form.is_valid():
        proposed_solution = form.cleaned_data["proposed_solution"]
        if challenge_obj.submission_is_valid(proposed_solution):
            messages.success(request, _("This solution is correct"))
            return redirect(challenge_obj.redirect_action)
        messages.error(request, _("This solution is incorrect"))
    context = {
        "challenge": challenge_obj,
        "form": form,
    }
    return render(request, "challenges/challenges/main-template.html", context)


@klopapier_staff_member_required
def list_challenges(request: AuthWSGIRequest) -> HttpResponse:
    challenges: QuerySet[Challenge] = Challenge.objects.all()
    context = {"challenges": challenges}
    return render(request, "challenges/management/list_challenges.html", context)


@klopapier_staff_member_required
def edit_challenge(request: AuthWSGIRequest, challenge_pk: int) -> HttpResponse:
    challenge_obj: Challenge = get_object_or_404(Challenge, pk=challenge_pk)

    form = ChallengeForm(request.POST or None, instance=challenge_obj)
    if form.is_valid():
        form.save()
        messages.success(request, _("The Challenge was successfully updated"))
        return redirect("challenges:list_challenges")

    context = {"challenge": challenge_obj, "form": form}
    return render(request, "challenges/management/edit_challenges.html", context)


@klopapier_staff_member_required
def del_challenge(request: AuthWSGIRequest, challenge_pk: int) -> HttpResponse:
    challenge_obj: Challenge = get_object_or_404(Challenge, pk=challenge_pk)

    form = forms.Form(request.POST or None)
    if form.is_valid():
        challenge_obj.delete()
        messages.success(request, _("The Challenge was successfully updated"))
        return redirect("challenges:list_challenges")

    context = {"challenge": challenge_obj, "form": form}
    return render(request, "challenges/management/del_challenges.html", context)


@klopapier_staff_member_required
def add_challenge(request: AuthWSGIRequest) -> HttpResponse:
    form = ChallengeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, _("The Challenge was successfully added"))
        return redirect("challenges:list_challenges")

    context = {"form": form}
    return render(request, "challenges/management/add_challenges.html", context)
