#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

EVENT_TITLE = "PyConES 2022"
EVENT_SUBTITLE = "Granada"
EVENT_DESCRIPTION_MINI = "PyConES, la conferencia nacional sobre Python más importante de España"
EVENT_DESCRIPTION = """
Bienvenidos a la PyConES, la conferencia nacional sobre Python más importante de España.<br><br>
Un evento que reunirá a los ponentes más interesantes, una agenda increíble y unas oportunidades de trabajo
maravillosas en el mundo IT. <br><br>
Tambien puedes formar parte de nuestros patrocinadores y tener tu espacio dentro del evento.
"""

TWITTER_USERNAME = "pycones"
TWITTER_LINK = f"https://twitter.com/{TWITTER_USERNAME}"
YOUTUBE_LINK = "https://www.youtube.com/PythonEspa%C3%B1aOficial"
GITHUB_LINK = "https://github.com/python-spain"
EMAIL_LINK = "mailto:contact2022@es.pycon.org" # TODO
TELEGRAM_LINK = "https://t.me/pycones2022" # TODO

TICKETS_LINK="#"
CALL_FOR_PAPERS_LINK = "#"
SPONSORS_DOSSIER = "#"

# https://google-map-generator.com/
MAP_IFRAME_LINK = "https://maps.google.com/maps?q=Granada%20Paraningo%20Salud&t=&z=17&ie=UTF8&iwloc=&output=embed"

# https://cookie-bar.eu/
COOKIES_SCRIPT = "https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=es&theme=altblack&tracking=1&thirdparty=1&always=1&refreshPage=1&showNoConsent=1"


MAILJET_IFRAME_URL = "https://app.mailjet.com/widget/iframe/5JG8/Lxz"
MAILJET_TOKEN = "e61aa81ed6e82c8d70abd453dfe74bde"

PAST_EDITIONS = [
    {
        "name": "PyConES 2013 - Madrid",
        "logo": "/theme/images/past_editions/2013.png",
        "url": "https://2013.es.pycon.org/"
    },
    {
        "name": "PyConES 2014 - Zaragoza",
        "logo": "/theme/images/past_editions/2014.svg",
        "url": "https://2014.es.pycon.org/"
    },
    {
        "name": "PyConES 2015 - Valencia",
        "logo": "/theme/images/past_editions/2015.png",
        "url": "https://2015.es.pycon.org/"
    },
    {
        "name": "PyConES 2016 - Almeria",
        "logo": "/theme/images/past_editions/2016.jpg",
        "url": "https://2016.es.pycon.org/"
    },
    {
        "name": "PyConES 2017 - Cáceres",
        "logo": "/theme/images/past_editions/2017.png",
        "url": "https://2016.es.pycon.org/"
    },
    {
        "name": "PyConES 2018 - Málaga",
        "logo": "/theme/images/past_editions/2018.svg",
        "url": "https://2018.es.pycon.org/"
    },
    {
        "name": "PyConES 2019 - Alicante",
        "logo": "/theme/images/past_editions/2019.png",
        "url": "https://2019.es.pycon.org/"
    },
    {
        "name": "PyConES 2020 - Pandemic Edition",
        "logo": "/theme/images/past_editions/2020.png",
        "url": "https://2020.es.pycon.org/"
    },
    {
        "name": "PyConES 2021 - Vaccine Edition",
        "logo": "/theme/images/past_editions/2021.svg",
        "url": "https://2021.es.pycon.org/"
    },

]


EVENT_KEYNOTERS = [
    {
        "name": 'Antonio Garcia',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'Paco Perez',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'John Pepe',
        "photo_big": 'https://bulma.io/images/placeholders/1280x960.png',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    }
]

SPONSORS = {
    "keystone": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        }
    ],
    "diamond": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
    "platinum": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
    "gold": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
    "silver": [
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
        {
            "name": 'Sponsor',
            "photo": 'https://bulma.io/images/placeholders/1280x960.png',
            "url": "#"
        },
    ],
}

EVENT_TRACKS = json.dumps([
     { "id": 'core', "title": 'Track Core' },
     { "id": 'data', "title": 'Track Data', "eventColor": 'green' },
     { "id": 'web', "title": 'Track Web', "eventColor": 'orange' },
])

EVENT_START_DATE = "2022-09-30"
EVENT_START_DATE_STR = "01 de Octubre 2022"
EVENT_TALKS = json.dumps(
    [
        {
            "id":"1",
            "resourceId":"core",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"Introducción a Data Science en Python",
            "editable":False,
            "description":"Francisco Correoso, Guillem Duran, Juan Carlos González, Jordi Contestí, Antònia Tugores",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"2",
            "resourceId":"web",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"TDD de cero a cien (o casi)",
            "editable":False,
            "description":"TDD de cero a cien (o casi)",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"3",
            "resourceId":"data",
            "start":"2022-09-30T15:00:00",
            "end":"2022-09-30T17:30:00",
            "title":"Representación de datos geográficos",
            "editable":False,
            "description":"Representación de datos geográficos",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"4",
            "resourceId": "data",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Café",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"5",
            "resourceId": "web",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Café",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"6",
            "resourceId": "core",
            "start":"2022-09-30T17:30:00",
            "end":"2022-09-30T18:00:00",
            "title":"Charla con un título bastante largo",
            "editable":False,
            "description":"Café",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"7",
            "resourceId": "data",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"¡Eureka! - Python y ciencia",
            "editable":False,
            "description":"¡Eureka! - Python y ciencia",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"8",
            "resourceId": "web",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"Las herramientas de un detective",
            "editable":False,
            "description":"Las herramientas de un detective",
            "url":"https://stackoverflow.com/"
        },
        {
            "id":"9",
            "resourceId": "core",
            "start":"2022-09-30T18:00:00",
            "end":"2022-09-30T20:30:00",
            "title":"Pyomo – Optimización en Python",
            "editable":False,
            "description":"Pyomo – Optimización en Python",
            "url":"https://stackoverflow.com/"
        },

    ]
)
