from django.contrib import admin

from .models import Challenge, ChallengeSecret, ChallengeShortLink

# Register your models here.

admin.register(Challenge)
admin.register(ChallengeShortLink)
admin.register(ChallengeSecret)
