from typing import List

from django import forms
from django.utils.translation import ugettext_lazy as _

from challenges.models import Challenge


class UserSolutionSubmissionForm(forms.Form):
    proposed_solution = forms.CharField(max_length=200, strip=True, label=_("Solution you want to propose"))


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude: List[str] = []
