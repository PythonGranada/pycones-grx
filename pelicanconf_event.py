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
EMAIL_LINK = "mailto:contacto@2022.es.pycon.org"
TELEGRAM_LINK = None # "https://t.me/pycones2022" # TODO

TICKETS_LINK="#"
CALL_FOR_PAPERS_LINK = "#"
SPONSORS_DOSSIER_ES = "/theme/files/dosier_patrocinio_2022_es.pdf"
SPONSORS_DOSSIER_EN = "/theme/files/dosier_patrocinio_2022_en.pdf"

# https://google-map-generator.com/
MAP_IFRAME_LINK = "https://maps.google.com/maps?q=Granada%20Paraningo%20Salud&t=&z=17&ie=UTF8&iwloc=&output=embed"

# https://cookie-bar.eu/
COOKIES_SCRIPT = "https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=es&theme=altblack&tracking=1&thirdparty=1&always=1&refreshPage=1&showNoConsent=1"


MAILJET_IFRAME_URL = "https://app.mailjet.com/widget/iframe/5JG8/Lxz"
MAILJET_TOKEN = "e61aa81ed6e82c8d70abd453dfe74bde"

ORGANIZERS = [
        {
            "name": "Python España",
            "logo": "/theme/images/organizers/python_espagna.png",
            "url": "https://es.python.org/"
        },
        {
            "name": "Universidad de Granada",
            "logo": "/theme/images/organizers/ugr.png",
            "url": "https://www.ugr.es/"
        },
        {
            "name": "Oficina software libre - Granada",
            "logo": "/theme/images/organizers/osl.png",
            "url": "https://osl.ugr.es/"
        },
        {
            "name": "Python Granada",
            "logo": "/theme/images/organizers/python_granada.png",
            "url": "http://python-granada.es/"
        },
        {
            "name": "Yes We Tech",
            "logo": "/theme/images/organizers/yes_we_tech.png",
            "url": "https://yeswetech.org/"
        },
]

EVENT_TEAM = [
    {
        "name": "Israel Saeta Pérez",
        "avatar": "https://avatars.githubusercontent.com/u/22172794",
        "tags": [{"name": "Python España", "color": "is-danger"}, {"name": "sponsors squad", "color": "is-primary"}],
        "position": "Ingeniero de Software",
        "github": "https://github.com/dukebody/",
        "twitter": "https://twitter.com/dukebody",
        "linkedin": "https://www.linkedin.com/in/israel-saeta-p%C3%A9rez-29268562/",
    },
    {
        "name": "Javier Alonso Silva",
        "avatar": "https://avatars.githubusercontent.com/u/25952165",
        "tags": [{"name": "PyLadies", "color": "is-danger"}, {"name": "support squad", "color": "is-primary"}],
        "position": "Ingeniero I+D en Teldat",
        "github": "https://github.com/Javinator9889",
        "twitter": "https://twitter.com/javinator9889",
        "linkedin": "https://linkedin.com/in/javinator9889",
    },
    {
        "name": "José Miguel López",
        "avatar": "https://avatars.githubusercontent.com/u/1655898",
        "tags": [{"name": "Python Granada", "color": "is-danger"}, {"name": "web squad", "color": "is-primary"}],
        "position": "Ingeniero de Software",
        "github": "https://github.com/josemlp91",
        "twitter": "https://twitter.com/josemlp91"
    },
    {
        "name": "Manuel Martín",
        "avatar": "https://media-exp1.licdn.com/dms/image/C4E03AQHUQEu3Vvzwgg/profile-displayphoto-shrink_200_200/0/1626865474708?e=1649894400&v=beta&t=87m2u-bcXthWZ-Q-QWiwnDQ3h6Uq67CCuTGLVjaiOlM",
        "tags": [{"name": "Python Granada", "color": "is-danger"}, {"name": "publication squad", "color": "is-primary"}],
        "position": "Doctor en Machine Learning",
        "github": "https://github.com/draxus",
        "twitter": "https://twitter.com/draxus",
        "linkedin": "https://www.linkedin.com/in/draxus/"
    },
    {
        "name": "Pablo Benavides",
        "avatar": "https://avatars.githubusercontent.com/u/49152268",
        "tags": [{"name": "Python Granada", "color": "is-danger"}, {"name": "keynoters squad", "color": "is-primary"}],
        "position": "Modelador de transportes",
        "github": "https://github.com/PybloBenavides",
    },
    {
        "name": "Pablo García Sánchez",
        "avatar": "https://avatars.githubusercontent.com/u/3056690",
        "tags": [{"name": "Oficina Software Libre Granada", "color": "is-danger"}, {"name": "infraestructure squad", "color": "is-primary"}],
        "position": "Profesor",
        "github": "https://github.com/fergunet",
        "twitter": "https://twitter.com/fergunet"
    },
    {
        "name": "Paloma de las Cuevas Delgado",
        "avatar": "https://avatars.githubusercontent.com/u/3061254",
        "tags": [{"name": "Yes We Tech", "color": "is-danger"}, {"name": "publicity squad", "color": "is-primary"}],
        "position": "Ingeniera de Software",
        "github": "https://github.com/unintendedbear",
        "twitter": "https://twitter.com/unintendedbear",
        "linkedin": "https://www.linkedin.com/in/palomacuevasd/"
    },
    {
        "name": "Juan Antonio",
        "avatar": "https://avatars.githubusercontent.com/u/5589299",
        "tags": [{"name": "Python Granada", "color": "is-danger"}, {"name": "sponsors squad", "color": "is-primary"}],
        "position": "Ingeniero de Software",
        "github": "https://github.com/juanAFernandez",
        "twitter": "https://twitter.com/_juanAFernandez",
        "linkedin": "https://www.linkedin.com/in/juanafernandez/"
    },
    {
        "name": "Israel Blancas",
        "avatar": "https://avatars.githubusercontent.com/u/4806311",
        "tags": [{"name": "Google Developer Group", "color": "is-danger"}, {"name": "sponsors squad", "color": "is-primary"}],
        "position": "Software Quality Engineer",
        "github": "https://github.com/iblancasa",
        "twitter": "https://twitter.com/iblancasa",
        "linkedin": "https://www.linkedin.com/in/iblancasa/",
    },
]



PAST_EDITIONS = [
    {
        "name": "PyConES 2013 - Madrid",
        "logo": "/theme/images/past_editions/2013.png",
        "url": "https://2013.es.pycon.org/"
    },
    {
        "name": "PyConES 2014 - Zaragoza",
        "logo": "/theme/images/past_editions/2014.png",
        "url": "https://2014.es.pycon.org/"
    },
    {
        "name": "PyConES 2015 - Valencia",
        "logo": "/theme/images/past_editions/2015.png",
        "url": "https://2015.es.pycon.org/"
    },
    {
        "name": "PyConES 2016 - Almería",
        "logo": "/theme/images/past_editions/2016.jpg",
        "url": "https://2016.es.pycon.org/"
    },
    {
        "name": "PyConES 2017 - Cáceres",
        "logo": "/theme/images/past_editions/2017.png",
        "url": "https://2017.es.pycon.org/"
    },
    {
        "name": "PyConES 2018 - Málaga",
        "logo": "/theme/images/past_editions/2018.png",
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
        "logo": "/theme/images/past_editions/2021.png",
        "url": "https://2021.es.pycon.org/"
    },

]


EVENT_KEYNOTERS = [
    {
        "name": 'Antonio Garcia',
        "photo_big": 'https://picsum.photos/800/600',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'Paco Perez',
        "photo_big": 'https://picsum.photos/800/600',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    },
    {
        "name": 'John Pepe',
        "photo_big": 'https://picsum.photos/800/600',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    }
]

SPONSORS = {
    "keystone": [
        {
            "name": 'Snoobs Sugar-Gold',
            "photo": 'https://picsum.photos/800/600?random=1',
            "url": "#"
        },
        {
            "name": 'Oil-Can Clovenhoof',
            "photo": 'https://picsum.photos/800/600?random=2',
            "url": "#"
        },
        {
            "name": 'Bill Beenie-Weenie Rosenthal',
            "photo": 'https://picsum.photos/800/600?random=3',
            "url": "#"
        }
    ],
    "diamond": [
        {
            "name": 'Big Burps Johnson',
            "photo": 'https://picsum.photos/800/600?random=4',
            "url": "#"
        },
        {
            "name": 'Johnny Clutterbuck',
            "photo": 'https://picsum.photos/800/600?random=5',
            "url": "#"
        },
        {
            "name": 'Buttermilk Overturf',
            "photo": 'https://picsum.photos/800/600?random=6',
            "url": "#"
        },
        {
            "name": 'Squids Johnson',
            "photo": 'https://picsum.photos/800/600?random=7',
            "url": "#"
        },
    ],
    "platinum": [
        {
            "name": 'Jimbo Rosenthal',
            "photo": 'https://picsum.photos/800/600?random=8',
            "url": "#"
        },
        {
            "name": 'Dennis Clawhammer Endicott',
            "photo": 'https://picsum.photos/800/600?random=9',
            "url": "#"
        },
        {
            "name": 'Slaps Putney',
            "photo": 'https://picsum.photos/800/600?random=10',
            "url": "#"
        },
    ],
    "gold": [
        {
            "name": 'Potato Bug Clovenhoof',
            "photo": 'https://picsum.photos/800/600?random=11',
            "url": "#"
        },
        {
            "name": 'Snorki Fewhairs',
            "photo": 'https://picsum.photos/800/600?random=12',
            "url": "#"
        },
        {
            "name": 'Lil Debil Winterkorn',
            "photo": 'https://picsum.photos/800/600?random=13',
            "url": "#"
        },
        {
            "name": 'Sweet Tea MBembo',
            "photo": 'https://picsum.photos/800/600?random=14',
            "url": "#"
        },
        {
            "name": 'Chad Porkins',
            "photo": 'https://picsum.photos/800/600?random=15',
            "url": "#"
        },

    ],
    "silver": [
        {
            "name": 'Chigger Guster',
            "photo": 'https://picsum.photos/800/600?random=16',
            "url": "#"
        },
        {
            "name": 'Scut Listenbee',
            "photo": 'https://picsum.photos/800/600?random=17',
            "url": "#"
        },
        {
            "name": 'Johnny Nettles',
            "photo": 'https://picsum.photos/800/600?random=18',
            "url": "#"
        },
        {
            "name": 'Scut Clovenhoof',
            "photo": 'https://picsum.photos/800/600?random=19',
            "url": "#"
        },
        {
            "name": 'Worms Nettles',
            "photo": 'https://picsum.photos/800/600?random=20',
            "url": "#"
        },

    ],
}

EVENT_TRACKS = json.dumps([
     { "id": 'core', "title": 'Track Core' },
     { "id": 'data', "title": 'Track Data', "eventColor": 'green' },
     { "id": 'web', "title": 'Track Web', "eventColor": 'orange' },
])

EVENT_START_DATE = "2022-09-31"
EVENT_START_DATE_STR = "Del 30 de Septiembre"
EVENT_END_DATE_STR = "Al 2 de Octubre"
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
