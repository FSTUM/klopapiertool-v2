from modeltranslation.translator import TranslationOptions, translator

from challenges.models import Challenge


class ChallengeTranslationOptions(TranslationOptions):
    fields = ("prompt", "description")
    required_languages = ("en", "de")


translator.register(Challenge, ChallengeTranslationOptions)
