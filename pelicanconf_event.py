#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pelicanconf_event_jobs import *
from pelicanconf_event_organizers import *
from pelicanconf_event_past_editions import *
from pelicanconf_event_sponsors import *
from pelicanconf_event_keynoters import *


EVENT_TITLE = "PyConES 2022"
EVENT_SUBTITLE = "Granada"
EVENT_DESCRIPTION_MINI = "PyConES, la conferencia de Python más importante de España"
EVENT_DESCRIPTION = """
Os damos la bienvenida a la PyConES, la conferencia de Python más importante de España.<br><br>
Un evento que reunirá a cientos de entusiastas de Python, una agenda increíble y unas oportunidades de trabajo
maravillosas. <br><br>
También puedes formar parte de nuestros patrocinadores y tener tu espacio dentro del evento.
"""

TWITTER_USERNAME = "pycones"
TWITTER_LINK = f"https://twitter.com/{TWITTER_USERNAME}"
YOUTUBE_LINK = "https://www.youtube.com/PythonEspa%C3%B1aOficial"
GITHUB_LINK = "https://github.com/python-spain"
EMAIL_LINK = "mailto:contacto@2022.es.pycon.org"
TELEGRAM_LINK = "https://t.me/PyConES2022"

TICKETS_LINK = "https://pycones2022.eventbrite.es"
CALL_FOR_PAPERS_LINK = "https://charlas.2022.es.pycon.org/pycones2022/cfp"
SPONSORS_DOSSIER_ES = "/theme/files/dosier_patrocinio_2022_es.pdf"
SPONSORS_DOSSIER_EN = "/theme/files/dosier_patrocinio_2022_en.pdf"

# https://google-map-generator.com/
MAP_IFRAME_LINK = "https://maps.google.com/maps?q=Granada%20Paraningo%20Salud&t=&z=17&ie=UTF8&iwloc=&output=embed"

# https://cookie-bar.eu/
COOKIES_SCRIPT = "https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=es&theme=altblack&tracking=1&thirdparty=1&always=1&refreshPage=1&showNoConsent=1"


MAILJET_IFRAME_URL = "https://app.mailjet.com/widget/iframe/5JG8/Lxz"
MAILJET_TOKEN = "e61aa81ed6e82c8d70abd453dfe74bde"

GOOGLE_PHOTOS_URL = "https://photos.app.goo.gl/a5c7f5DmyjLExXhL7"
GOOGLE_PHOTOS_TITLE = "PyConEs GRX"
GOOGLE_PHOTOS_DESCRIPTION = "PyConEs GRX"


WALLPAPERS = [
    "/theme/images/wallpapers/alhambra_por_dentro.webp",
    "/theme/images/wallpapers/alhambra_por_fuera.webp",
    "/theme/images/wallpapers/arco_arabe.webp",
    "/theme/images/wallpapers/azulejo_rombos.webp",
    "/theme/images/wallpapers/carlos_quinto.webp",
    "/theme/images/wallpapers/catedral.webp",
    "/theme/images/wallpapers/lamparas_arabes.webp",
    "/theme/images/wallpapers/silla_arabe.webp",
    "/theme/images/wallpapers/tienda_lamparas.webp",
]

SELECTED_WALLPAPER = random.choice(WALLPAPERS)

EVENT_TRACKS = json.dumps(
    [
        {"id": "core", "title": "Track Core"},
        {"id": "data", "title": "Track Data", "eventColor": "green"},
        {"id": "web", "title": "Track Web", "eventColor": "orange"},
    ]
)

EVENT_START_DATE = "2022-09-30"
EVENT_START_DATE_STR = "Del 30 de Septiembre"
EVENT_END_DATE_STR = "Al 2 de Octubre"
EVENT_TALKS = json.dumps(
    [
        {
            "id": "1",
            "resourceId": "core",
            "start": "2022-09-30T15:00:00",
            "end": "2022-09-30T17:30:00",
            "title": "Introducción a Data Science en Python",
            "editable": False,
            "description": "Francisco Correoso, Guillem Duran, Juan Carlos González, Jordi Contestí, Antònia Tugores",
            "url": "https://stackoverflow.com/",
        }
    ]
)
