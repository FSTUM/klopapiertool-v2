import random
import string
from subprocess import run  # nosec: used for flushing the db

import django.utils.timezone

# noinspection PyPackageRequirements
import lorem
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.datetime_safe import datetime

import challenges.models as m_challenges
import common.models as m_common


def showroom_fixture_state():
    confirmation = input("Do you really want to load the showroom fixture? (This will flush the database) [y/n]")
    if confirmation.lower() != "y":
        return
    showroom_fixture_state_no_confirmation()


def showroom_fixture_state_no_confirmation():
    run(["python3", "manage.py", "flush", "--noinput"], check=True)

    # user
    _generate_superusers()

    # app common
    _generate_ideas()

    # app challenges
    _generate_challenges()


def _generate_ideas():
    for _ in range(random.randint(15, 30)):
        content = random.choice(
            [
                f"{rand_company_name()} for president",
                f"Could you kindly feature {rand_company_name()} on your next issue? "
                f"Kindly, {rand_firstname()} {rand_last_name()}",
                f"{rand_firstname()} enjoyed this",
                "https://fsmpi.de/aushaenge",
                "https://fsmpi.de/faq",
            ]
            + [f"https://xkcd.com/{random.randint(1, 2542)}/"] * 3,
        )
        if not m_common.Idea.objects.filter(content=content).exists():
            m_common.Idea.objects.create(
                votes=random.choice((random.randint(1, 150), 69, random.randint(1, 10), 0, 0)),
                content=content,
            )


def _generate_challenges():
    challenges = []
    for _ in range(random.randint(5, 15)):
        url = random.choice(("https://fsmpi.de", "https://fsmpi.de/aushaenge", "https://fsmpi.de/units"))
        key = rand_firstname() + "_" + rand_company_name()
        challenges.append(
            m_challenges.Challenge.objects.create(
                key=key,
                prompt=lorem.sentence(),
                description=lorem.paragraph(),
                redirect_action=url,
            ),
        )
    for challenge in challenges:
        shortlinks = random.choice([0] * 2 + [1] * 3 + [3] * 4 + [6])
        for _ in range(shortlinks):
            short_link = "".join([random.choice(string.ascii_lowercase)] * random.randint(5, 10))

            if not m_challenges.ChallengeShortLink.objects.filter(short_link=short_link).exists():
                m_challenges.ChallengeShortLink.objects.create(
                    challenge=challenge,
                    short_link=short_link,
                )
    for challenge in challenges:
        secrets = random.choice([0] + [1] * 3 + [3] * 4 + [6])
        for _ in range(secrets):
            secret=rand_company_name().lower()
            if not m_challenges.ChallengeSecret.objects.filter(challenge=challenge,secret=secret).exists():
                m_challenges.ChallengeSecret.objects.create(
                    challenge=challenge,
                    secret=secret,
                )


def _generate_superusers():
    users = [
        ("frank", "130120", "Frank", "Elsinga", "elsinga@example.com"),
        ("password", "username", "Nelson 'Big Head'", "Bighetti", "bighetti@example.com"),
    ]
    for username, password, first_name, last_name, email in users:
        get_user_model().objects.create(
            username=username,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            email=email,
            date_joined=django.utils.timezone.make_aware(datetime.today()),
        )


def rand_company_name():
    cool_names = ["Caliburst", "Ironhide", "Stylor", "Spectro", "Camshaft", "Haywire", "Snarl", "Starscream"]
    violent_names = ["Warpath", "Recoil", "Broadside", "Scattershot", "Thundercracker"]
    lame_names = ["Scrapper", "Streetwise", "Arcana", "Grax", "Drag Strip", "Chromedome", "Slag"]
    return random.choice(cool_names + violent_names + lame_names)


def rand_firstname():
    male_names = ["Wolfgang", "Walter", "Loke", "Waldemar", "Adam", "Gunda", "Hartmut", "Jochen", "Severin", "Elmar"]
    female_names = ["Agnes", "Sylvia", "Karla", "Erika", "Felicitas", "Emma", "Simone", "Linda", "Erika", "Miriam"]
    return random.choice(male_names + female_names)


def rand_last_name():
    ger_last_names = ["Fenstermacher", "Achterberg", "Bergmann", "Reich", "Werner", "Hochberg", "Bruhn", "Schlosser"]
    common_last_names = ["Peters", "Hofer"]
    last_names = ["Essert", "Simons", "Gross", "Mangold", "Sander", "Lorentz", "Hoffmann", "Hennig", "Beyer"]
    return random.choice(ger_last_names + common_last_names + last_names)
