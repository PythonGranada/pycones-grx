#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random

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
TELEGRAM_LINK = "https://t.me/PyConES2022"

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
            "name": "Oficina de Software libre de la Universidad de Granada",
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

TEAM = [
    {
        "name": "Maribel García Arenas",
        "avatar": "https://avatars.githubusercontent.com/u/3056362",
        "tags": [{"name": "Oficina de Software Libre de la Universidad de Granada", "color": "is-danger"}, {"name": "infraestructure squad", "color": "is-primary"}],
        "position": "Profesora",
        "github": "https://github.com/mgarenas",
        "twitter": "https://twitter.com/misgarenas",
    },
    {
        "name": "Pablo García Sánchez",
        "avatar": "https://avatars.githubusercontent.com/u/3056690",
        "tags": [{"name": "Oficina de Software Libre de la Universidad de Granada", "color": "is-danger"}, {"name": "infraestructure squad", "color": "is-primary"}],
        "position": "Profesor",
        "github": "https://github.com/fergunet",
        "twitter": "https://twitter.com/fergunet",
        "linkedin": "https://www.linkedin.com/in/pgarciasanchez/"
    },
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
    {
        "name": "Pedro Mayorgas Parejo",
        "avatar": "https://avatars.githubusercontent.com/u/64685260",
        "tags": [{"name": "Python Granada", "color": "is-danger"}, {"name": "web squad", "color": "is-primary"}],
        "position": "Ingeniero Informático y Técnico en Administración de Sistemas",
        "github": "https://github.com/lovelace9981",
    },
    {
        "name": "Cristina Diaz",
        "avatar": "https://pbs.twimg.com/profile_images/1466381833168424966/WI_yR4bo_400x400.jpg",
        "tags": [{"name": "Google Developer Group", "color": "is-danger"}, {"name": "diversity squad", "color": "is-primary"}],
        "position": "Software Developer",
        "github": "https://github.com/LadyNightmare/",
        "twitter": "https://twitter.com/lady_devs",
        "linkedin": "https://www.linkedin.com/in/cdg-97/",
    },
]

random.shuffle(TEAM)



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


KEYNOTERS = [
    {
        "name": 'Antonio Garcia',
        "photo_big": 'https://picsum.photos/800/600',
        "photo": 'https://bulma.io/images/placeholders/96x96.png',
        "url": "#",
        "twitter": "@john",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris."
    }
]

SPONSORS = [
    {
        "level_name": "keystone",
        "title": "Keystone 🏆",
        "size": "270px",
        "order": 1,
        "members": []
    },
    {
        "level_name": "diamond",
        "title": "Diamante 💎",
        "size": "250px",
        "order": 2,
        "members": [
            {
                "name": 'APSL',
                "photo": '/theme/images/sponsors/apsl.png',
                "url": "https://www.apsl.net/"
            },
            {
                "name": 'Cívica',
                "photo": '/theme/images/sponsors/civica.png',
                "url": "https://civica-soft.com/"
            },
            {
                "name": 'Intelygenz',
                "photo": '/theme/images/sponsors/intelygenz.png',
                "url": "https://intelygenz.com/"
            }
        ]
    },
    {
        "level_name": "platinum",
        "title": "Platino 💽",
        "size": "200px",
        "order": 3,
        "members": []
    },
    {
        "level_name": "gold",
        "title": "Oro 📀",
        "size": "180px",
        "order": 4,
        "members": []
    },
    {
        "level_name": "silver",
        "title": "Plata 💿",
        "size": "150px",
        "order": 5,
        "members": [
            {
                "name": 'Kaleidos',
                "photo": '/theme/images/sponsors/kaleidos.png',
                "url": "https://kaleidos.net/"
            },
            {
                "name": 'CodeSyntax',
                "photo": '/theme/images/sponsors/codesyntax.png',
                "url": "https://www.codesyntax.com/"
            },
            {
                "name": 'Alea Soluciones',
                "photo": '/theme/images/sponsors/aleasoluciones.png',
                "url": "https://www.alea-soluciones.com/"
            },
            {
                "name": 'Nazaríes IT',
                "photo": '/theme/images/sponsors/nazaries.png',
                "url": "https://www.nazaries.com/"
            }
        ]
    }
]

for s in SPONSORS:
    random.shuffle(s["members"])


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
        }
    ]
)
