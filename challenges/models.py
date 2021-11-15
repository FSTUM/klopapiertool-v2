from typing import List

from django.db import models
from django.urls import reverse

from common.utils.typing import AuthWSGIRequest


class Challenge(models.Model):
    key = models.CharField(max_length=50, unique=True)
    prompt = models.CharField(max_length=200)
    description = models.TextField()
    redirect_action = models.CharField(max_length=100)

    def submission_is_valid(self, value: str) -> bool:
        return value in self.secrets

    @property
    def secrets(self) -> List[str]:
        return [chs.secret for chs in self.challengesecret_set.all()]

    @property
    def url(self) -> str:
        return reverse("challenges:challenges", self.key)

    @property
    def short_urls(self) -> List[str]:
        results = []
        for url in self.challengeshortlink_set.all():
            results.append(reverse("challenges:challenge_short_link", url.short_link))
        return results

    def __str__(self):
        return f"{self.key}->{self.redirect_action}: [{', '.join(self.secrets)}]"


class ChallengeSecret(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    secret = models.CharField(max_length=200)

    def __str__(self):
        return self.secret


class ChallengeShortLink(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    short_link = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.short_link
