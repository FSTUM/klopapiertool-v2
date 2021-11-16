from typing import TypeVar

from django.core.cache import cache
from django.db import models

SingletonType = TypeVar("SingletonType", bound="SingletonModel")


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1  # pylint: disable=invalid-name
        super().save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls) -> SingletonType:
        obj: SingletonType
        obj, _success = cls.objects.get_or_create(pk=1)
        return obj


class LoggedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Settings(SingletonModel, LoggedModel):
    # flag register

    def __str__(self):
        return f"Settings {self.pk}"


class Idea(models.Model):
    class Meta:
        ordering = ["-votes"]

    votes = models.PositiveIntegerField()
    content = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return f"{self.votes}: {self.content}"
