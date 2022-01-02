from django import forms
from django.utils.translation import gettext as _

from challenges.models import Challenge, ChallengeSecret, ChallengeShortLink


class UserSolutionSubmissionForm(forms.Form):
    proposed_solution = forms.CharField(max_length=200, strip=True, label=_("Solution you want to propose"))


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude: list[str] = ["prompt", "description"]


class ChallangeBasedForm(forms.ModelForm):
    class Meta:
        exclude: list[str] = ["challenge"]

    def __init__(self, *args, **kwargs):
        self.challenge: Challenge = kwargs.pop("challenge")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.challenge = self.challenge
        if commit:
            obj.save()
        return obj


class ChallengeSecretForm(ChallangeBasedForm):
    class Meta(ChallangeBasedForm.Meta):
        model = ChallengeSecret


class ChallengeShortLinkForm(ChallangeBasedForm):
    class Meta(ChallangeBasedForm.Meta):
        model = ChallengeShortLink
