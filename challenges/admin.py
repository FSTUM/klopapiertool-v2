from django.contrib import admin
from .models import Challenge,ChallengeShortLink,ChallengeSecret
# Register your models here.

admin.register(Challenge)
admin.register(ChallengeShortLink)
admin.register(ChallengeSecret)
