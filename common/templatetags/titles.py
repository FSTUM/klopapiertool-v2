import random

from django import template

register = template.Library()


@register.simple_tag
def random_title():
    titles = [
        "Das geht kloa",
        "Ob du be-klo-ppt bist, hab ich jefragt",
        "Star Wars II: Angriff der Klo(n)krieger",
        "Da kann i net klogen",
        "Ich hab nen Klo-ß im Hals",
        "Achtung ein Zy-klo-n!!",
        "Vekloziraptor",
        "Wie nennt man einen Einäugigen auf dem Klo? Zyklop",
        "Klo-pf dir auf die Schulter für diese coole neue Klopapier",
        "Tobi Grasberger",
        "Wie nennt man ein dixiklo an der Straßenecke mit Essensversorgung? Ec-klo-kal",
        "Klockdown: Schließung der Klos ab 22 Uhr",
    ]
    return random.choice(titles)  # nosec: fully defined
