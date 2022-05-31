#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random

EVENT_TITLE = "PyConES 2022"
EVENT_SUBTITLE = "Granada"
EVENT_DESCRIPTION_MINI = (
    "PyConES, la conferencia nacional sobre Python más importante de España"
)
EVENT_DESCRIPTION = """
Os damos la bienvenida a la PyConES, la conferencia nacional sobre Python más importante de España.<br><br>
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

ORGANIZERS = [
    {
        "name": "Python España",
        "logo": "/theme/images/organizers/python_espagna.png",
        "url": "https://es.python.org/",
    },
    {
        "name": "Universidad de Granada",
        "logo": "/theme/images/organizers/ugr.png",
        "url": "https://www.ugr.es/",
    },
    {
        "name": "Oficina de Software libre de la Universidad de Granada",
        "logo": "/theme/images/organizers/osl.png",
        "url": "https://osl.ugr.es/",
    },
    {
        "name": "Python Granada",
        "logo": "/theme/images/organizers/python_granada.png",
        "url": "http://python-granada.es/",
    },
    {
        "name": "Yes We Tech",
        "logo": "/theme/images/organizers/yes_we_tech.png",
        "url": "https://yeswetech.org/",
    },
]

TEAM = [
    {
        "name": "Maribel García Arenas",
        "avatar": "/theme/images/organizers/maribel.jpeg",
        "tags": [
            {
                "name": "Oficina de Software Libre de la Universidad de Granada",
                "color": "is-danger",
            },
            {"name": "infraestructure squad", "color": "is-info"},
        ],
        "position": "Profesora",
        "github": "https://github.com/mgarenas",
        "twitter": "https://twitter.com/misgarenas",
    },
    {
        "name": "Pablo García Sánchez",
        "avatar": "/theme/images/organizers/pablo-osl.png",
        "tags": [
            {
                "name": "Oficina de Software Libre de la Universidad de Granada",
                "color": "is-danger",
            },
            {"name": "infraestructure squad", "color": "is-info"},
        ],
        "position": "Profesor",
        "github": "https://github.com/fergunet",
        "twitter": "https://twitter.com/fergunet",
        "linkedin": "https://www.linkedin.com/in/pgarciasanchez/",
    },
    {
        "name": "Israel Saeta Pérez",
        "avatar": "/theme/images/organizers/isra.jpeg",
        "tags": [
            {"name": "Python España", "color": "is-danger"},
            {"name": "sponsors squad", "color": "is-info"},
        ],
        "position": "Ingeniero de Software",
        "github": "https://github.com/dukebody/",
        "twitter": "https://twitter.com/dukebody",
        "linkedin": "https://www.linkedin.com/in/israel-saeta-p%C3%A9rez-29268562/",
    },
    {
        "name": "Javier Alonso Silva",
        "avatar": "/theme/images/organizers/javi.jpeg",
        "tags": [
            {"name": "PyLadies", "color": "is-danger"},
            {"name": "support squad", "color": "is-info"},
        ],
        "position": "Ingeniero I+D en Teldat",
        "github": "https://github.com/Javinator9889",
        "twitter": "https://twitter.com/javinator9889",
        "linkedin": "https://linkedin.com/in/javinator9889",
    },
    {
        "name": "José Miguel López",
        "avatar": "/theme/images/organizers/josemi.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "web squad", "color": "is-info"},
        ],
        "position": "Ingeniero de Software",
        "github": "https://github.com/josemlp91",
        "twitter": "https://twitter.com/josemlp91",
        "linkedin": "https://www.linkedin.com/in/josmilope/",
    },
    {
        "name": "Manuel Martín",
        "avatar": "/theme/images/organizers/draxus.jpg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "publication squad", "color": "is-info"},
        ],
        "position": "Doctor en Machine Learning",
        "github": "https://github.com/draxus",
        "twitter": "https://twitter.com/draxus",
        "linkedin": "https://www.linkedin.com/in/draxus/",
    },
    {
        "name": "Pablo Benavides",
        "avatar": "/theme/images/organizers/pablo.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "keynoters squad", "color": "is-info"},
        ],
        "position": "Modelador de transportes",
        "github": "https://github.com/PybloBenavides",
    },
    {
        "name": "Paloma de las Cuevas Delgado",
        "avatar": "/theme/images/organizers/paloma.jpeg",
        "tags": [
            {"name": "Yes We Tech", "color": "is-danger"},
            {"name": "publicity squad", "color": "is-info"},
        ],
        "position": "Ingeniera de Software",
        "github": "https://github.com/unintendedbear",
        "twitter": "https://twitter.com/unintendedbear",
        "linkedin": "https://www.linkedin.com/in/palomacuevasd/",
    },
    {
        "name": "Juan Antonio",
        "avatar": "/theme/images/organizers/juanantonio.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "sponsors squad", "color": "is-info"},
        ],
        "position": "Ingeniero de Software",
        "github": "https://github.com/juanAFernandez",
        "twitter": "https://twitter.com/_juanAFernandez",
        "linkedin": "https://www.linkedin.com/in/juanafernandez/",
    },
    {
        "name": "Israel Blancas",
        "avatar": "/theme/images/organizers/israel.jpeg",
        "tags": [
            {"name": "Google Developer Group", "color": "is-danger"},
            {"name": "sponsors squad", "color": "is-info"},
        ],
        "position": "Software Quality Engineer",
        "github": "https://github.com/iblancasa",
        "twitter": "https://twitter.com/iblancasa",
        "linkedin": "https://www.linkedin.com/in/iblancasa/",
    },
    {
        "name": "Pedro Mayorgas Parejo",
        "avatar": "/theme/images/organizers/pedro.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "web squad", "color": "is-info"},
        ],
        "position": "Ingeniero Informático y Técnico en Administración de Sistemas",
        "github": "https://github.com/lovelace9981",
    },
    {
        "name": "Cristina Diaz",
        "avatar": "/theme/images/organizers/cristina.jpeg",
        "tags": [
            {"name": "Google Developer Group", "color": "is-danger"},
            {"name": "diversity squad", "color": "is-info"},
        ],
        "position": "Software Developer",
        "github": "https://github.com/LadyNightmare/",
        "twitter": "https://twitter.com/lady_devs",
        "linkedin": "https://www.linkedin.com/in/cdg-97/",
    },
    {
        "name": "José Miguel Castillo García",
        "avatar": "#",
        "tags": [
            {
                "name": "Oficina de Software Libre de la Universidad de Granada",
                "color": "is-danger",
            },
            {"name": "sponsors squad", "color": "is-info"},
        ],
        "position": "Técnico de laboratorio",
    },
    {
        "name": "Anna Peña Martínez",
        "avatar": "/theme/images/organizers/anna.jpeg",
        "tags": [{"name": "publication squad", "color": "is-info"}],
        "position": "Product Lead",
        "twitter": "https://twitter.com/annalogik",
        "linkedin": "https://www.linkedin.com/in/annalogik/",
    },
    {
        "name": "Jimena E. Bermúdez",
        "avatar": "/theme/images/organizers/jimena.jpeg",
        "tags": [
            {"name": "PyLadies", "color": "is-danger"},
            {"name": "publicity squad", "color": "is-info"},
        ],
        "position": "Ingeniera de Software",
        "twitter": "https://twitter.com/Jimena_y_yo",
        "linkedin": "https://www.linkedin.com/in/jimena-eb/",
        "github": "https://github.com/JimenaEB",
    },
    {
        "name": "Paula Guijarro",
        "avatar": "/theme/images/organizers/paula.jpeg",
        "tags": [{"name": "PyLadies", "color": "is-danger"}],
        "position": "Site Reliability Engineer",
        "linkedin": "https://www.linkedin.com/in/paula-guijarro/",
        "github": "https://github.com/paulaguijarro",
    },
    {
        "name": "Alberto Rasillo Fernández",
        "avatar": "#",
        "tags": [{"name": "Python España", "color": "is-danger"},],
        "position": "Ingeniero de software",
    },
    {
        "name": "Christian Prada Osuna",
        "avatar": "/theme/images/organizers/cristian.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "sponsors squad", "color": "is-info"},
        ],
        "position": "Technical Lead Software Developer",
        "linkedin": "https://es.linkedin.com/in/christian-prada-osuna-0741217b",
        "github": "https://github.com/cprada87",
        "twitter": "https://twitter.com/dev_morphheus",
    },
    {
        "name": "Sara Medrano Sánchez",
        "avatar": "/theme/images/organizers/sara.jpeg",
        "tags": [
            {"name": "Python Granada", "color": "is-danger"},
            {"name": "attendes squad", "color": "is-info"},
        ],
        "twitter": "https://twitter.com/SrtSanz_",
    },
    {
        "name": "Maria Moreno de Castro",
        "avatar": "/theme/images/organizers/maria.png",
        "tags": [
            {"name": "PyData", "color": "is-danger"},
            {"name": "attendees squad", "color": "is-info"},
        ],
        "position": "Data Scientist",
        "linkedin": "https://www.linkedin.com/in/maria-moreno-de-castro/",
        "github": "https://github.com/MMdeCastro",
    },
    {
        "name": "Pedro González Rodelas",
        "avatar": "/theme/images/organizers/prodelas.jpeg",
        "tags": [
            {"name": "Universidad de Granada", "color": "is-danger"},
            {"name": "infraestructure squad", "color": "is-info"},
        ],
        "position": "Profesor",
        "linkedin": "https://www.linkedin.com/in/pedro-gonzalez-rodelas",
        "github": "https://github.com/prodelas",
        "twitter": "https://twitter.com/PedroGRodelas",
    },
    {
        "name": "Cristián Maureira-Fredes",
        "avatar": "/theme/images/organizers/cristian-maureira.jpg",
        "tags": [{"name": "Python España", "color": "is-danger"},],
        "position": "R&D Manager",
        "linkedin": "https://www.linkedin.com/in/cmaureir/",
        "github": "https://github.com/cmaureir",
        "twitter": "https://twitter.com/cmaureir",
    },
]

random.shuffle(TEAM)


PAST_EDITIONS = [
    {
        "name": "PyConES 2013 - Madrid",
        "logo": "/theme/images/past_editions/2013.png",
        "url": "https://2013.es.pycon.org/",
    },
    {
        "name": "PyConES 2014 - Zaragoza",
        "logo": "/theme/images/past_editions/2014.png",
        "url": "https://2014.es.pycon.org/",
    },
    {
        "name": "PyConES 2015 - Valencia",
        "logo": "/theme/images/past_editions/2015.png",
        "url": "https://2015.es.pycon.org/",
    },
    {
        "name": "PyConES 2016 - Almería",
        "logo": "/theme/images/past_editions/2016.jpg",
        "url": "https://2016.es.pycon.org/",
    },
    {
        "name": "PyConES 2017 - Cáceres",
        "logo": "/theme/images/past_editions/2017.png",
        "url": "https://2017.es.pycon.org/",
    },
    {
        "name": "PyConES 2018 - Málaga",
        "logo": "/theme/images/past_editions/2018.png",
        "url": "https://2018.es.pycon.org/",
    },
    {
        "name": "PyConES 2019 - Alicante",
        "logo": "/theme/images/past_editions/2019.png",
        "url": "https://2019.es.pycon.org/",
    },
    {
        "name": "PyConES 2020 - Pandemic Edition",
        "logo": "/theme/images/past_editions/2020.png",
        "url": "https://2020.es.pycon.org/",
    },
    {
        "name": "PyConES 2021 - Vaccine Edition",
        "logo": "/theme/images/past_editions/2021.png",
        "url": "https://2021.es.pycon.org/",
    },
]


KEYNOTERS = [
    {
        "name": "Mai Giménez",
        "photo_big": "/theme/images/keynoters/mai.png",
        "url": "/pages/mai.html",
        "twitter": "@maidotgimenez",
        "description": "La era del diamante: sesgos y riesgos en IA. En la más pura tradición valenciana, esta charla no es una charla, es una falla.",
    },
    {
        "name": "Nieves Ábalos",
        "photo_big": "/theme/images/keynoters/nieves.jpg",
        "url": "/pages/nieves.html",
        "twitter": "@nieves_as",
        "description": "Experta en Sistemas de Diálogo o Interfaces conversacionales (chatbots y asistentes de texto y voz) desde 2009",
    },
]

SPONSORS = [
    {
        "level_name": "keystone",
        "title": "Keystone 🏆",
        "size": "270px",
        "order": 1,
        "members": [
            {
                "name": "PSF",
                "photo": "/theme/images/sponsors/psf.png",
                "url": "https://www.python.org/psf/",
            },
        ],
    },
    {
        "level_name": "diamond",
        "title": "Diamante 💎",
        "size": "250px",
        "order": 2,
        "members": [
            {
                "name": "APSL",
                "photo": "/theme/images/sponsors/apsl.png",
                "url": "https://www.apsl.net/",
            },
            {
                "name": "Cívica",
                "photo": "/theme/images/sponsors/civica.png",
                "url": "https://civica-soft.com/",
            },
            {
                "name": "Intelygenz",
                "photo": "/theme/images/sponsors/intelygenz.png",
                "url": "https://intelygenz.com/",
            },
            {
                "name": "Intelligenia",
                "photo": "/theme/images/sponsors/intelligenia.png",
                "url": "https://www.intelligenia.com/",
            },
            {
                "name": "TravelPerk",
                "photo": "/theme/images/sponsors/travelperk.png",
                "url": "https://www.travelperk.com/es/",
            },
            {
                "name": "Twilio",
                "photo": "/theme/images/sponsors/twilio.png",
                "url": "https://www.twilio.com/",
            },
            {
                "name": "Datadog",
                "photo": "/theme/images/sponsors/datadog.png",
                "url": "https://www.datadoghq.com/",
            },
            {
                "name": "BlueTab",
                "photo": "/theme/images/sponsors/bluetab.png",
                "url": "http://www.bluetab.net/en/",
            },
        ],
    },
    {
        "level_name": "platinum",
        "title": "Platino 💽",
        "size": "210px",
        "order": 3,
        "members": [
            {
                "name": "Ebury",
                "photo": "/theme/images/sponsors/ebury.png",
                "url": "https://www.ebury.es/",
            },
            {
                "name": "TrustYou",
                "photo": "/theme/images/sponsors/trustyou.png",
                "url": "https://www.trustyou.com/es/",
            },
            {
                "name": "Perkin Elmer",
                "photo": "/theme/images/sponsors/perkinelmer.png",
                "url": "https://www.perkinelmer.com/",
            },
            {
                "name": "Cathedral Software",
                "photo": "/theme/images/sponsors/cathedralsoftware.png",
                "url": "https://www.cathedralsw.com/",
            },
            {
                "name": "Octopus Energy",
                "photo": "/theme/images/sponsors/octopus.png",
                "url": "https://www.octopusenergy.es/",
            },
            {
                "name": "eFrontiers",
                "photo": "/theme/images/sponsors/efrontiers.png",
                "url": "http://www.e-frontiers.com/",
            },
            {
                "name": "Zara Tech",
                "photo": "/theme/images/sponsors/zara.png",
                "url": "https://techteams.es/",
            },
            {
                "name": "Nucleoo",
                "photo": "/theme/images/sponsors/nucleoo.png",
                "url": "https://nucleoo.com/es/home-es/",
            },
        ],
    },
    {
        "level_name": "gold",
        "title": "Oro 📀",
        "size": "180px",
        "order": 4,
        "members": [
            {
                "name": "holaluz",
                "photo": "/theme/images/sponsors/holaluz.png",
                "url": "https://holaluz.com/",
            },
            {
                "name": "Orbital Ads",
                "photo": "/theme/images/sponsors/orbitalads.png",
                "url": "https://www.orbitalads.com/",
            },
            {
                "name": "4Geeks Academy",
                "photo": "/theme/images/sponsors/4geeks.png",
                "url": "https://4geeksacademy.com/es/inicio",
            },
            {
                "name": "Financial Force",
                "photo": "/theme/images/sponsors/financialforce.png",
                "url": "https://www.financialforce.com/",
            },
            {
                "name": "Back Market",
                "photo": "/theme/images/sponsors/bm.png",
                "url": "https://www.backmarket.es/",
            },
            {
                "name": "uenergia",
                "photo": "/theme/images/sponsors/uenergia.png",
                "url": "https://www.uenergia.es/es/",
            },
            {
                "name": "celtiberian",
                "photo": "/theme/images/sponsors/celtiberian.png",
                "url": "https://www.celtiberian.es/",
            },
            {
                "name": "Kave Home ",
                "photo": "/theme/images/sponsors/kavehome.png",
                "url": "https://kavehome.com/",
            },
            {
                "name": "Alight",
                "photo": "/theme/images/sponsors/alight.png",
                "url": "https://www.alight.com/",
            },
            {
                "name": "Kairós",
                "photo": "/theme/images/sponsors/kairos.png",
                "url": "https://www.kairosds.com/es/index.html",
            },
            {
                "name": "Skydance Animation Madrid",
                "photo": "/theme/images/sponsors/skydance.png",
                "url": "https://skydance.com/",
            },
        ],
    },
    {
        "level_name": "silver",
        "title": "Plata 💿",
        "size": "150px",
        "order": 5,
        "members": [
            {
                "name": "Kaleidos",
                "photo": "/theme/images/sponsors/kaleidos.png",
                "url": "https://kaleidos.net/",
            },
            {
                "name": "CodeSyntax",
                "photo": "/theme/images/sponsors/codesyntax.png",
                "url": "https://www.codesyntax.com/",
            },
            {
                "name": "Alea Soluciones",
                "photo": "/theme/images/sponsors/aleasoluciones.png",
                "url": "https://www.alea-soluciones.com/",
            },
            {
                "name": "Nazaríes IT",
                "photo": "/theme/images/sponsors/nazaries.png",
                "url": "https://www.nazaries.com/",
            },
            {
                "name": "Badger",
                "photo": "/theme/images/sponsors/badger.png",
                "url": "https://www.badgermapping.com/",
            },
            {
                "name": "Novatec",
                "photo": "/theme/images/sponsors/novatec.png",
                "url": "https://www.novatec-gmbh.de/en/granada/",
            },
            {
                "name": "Blink",
                "photo": "/theme/images/sponsors/blink.png",
                "url": "https://blinkeye.com/",
            },
            {
                "name": "GISCE",
                "photo": "/theme/images/sponsors/gisce.png",
                "url": "https://gisce.net/es/",
            },
            {
                "name": "PhotoPills",
                "photo": "/theme/images/sponsors/photopills.png",
                "url": "https://www.photopills.com/es",
            },
            {
                "name": "Joor",
                "photo": "/theme/images/sponsors/joor.png",
                "url": "https://www.joor.com/",
            },
        ],
    },
    {
        "level_name": "friend",
        "title": "Colaboran 💡",
        "size": "150px",
        "order": 6,
        "members": [
            {
                "name": "Renfe",
                "photo": "/theme/images/sponsors/renfe.png",
                "url": "https://www.renfe.com/",
            },
            {
                "name": "Ayuntamiento Granada",
                "photo": "/theme/images/sponsors/ayuntamiento.png",
                "url": "https://www.granada.org/",
            },
            {
                "name": "Coviran",
                "photo": "/theme/images/sponsors/coviran.png",
                "url": "https://www.coviran.es/",
            },
            {
                "name": "Freewear",
                "photo": "/theme/images/sponsors/freewear.png",
                "url": "https://www.freewear.org/",
            },
        ],
    },
]

for s in SPONSORS:
    random.shuffle(s["members"])


JOBS = [
    {
        "company_avatar": "/theme/images/jobs/ef.jpeg",
        "company_name": "e-Frontiers",
        "position": "Senior Python Developer",
        "description": "Buscamos desarrolladores con experiencia en Python para trabajar remotamente desde cualquier país europeo para trabajar en una empresa tecnológica con producto propio, una potente herramienta analítica, que opera en diferentes países y que ya está siendo considerada como el nuevo unicornio tecnológico español.",
        "location": "España/ 100% remoto",
        "skills": [
            "python",
            "unittest",
            "docker",
            "kubernetes",
            "kafka",
            "spark",
            "inglés alto",
        ],
        "salary": "50.000 - 70.000 €",
        "url": "https://e-frontiers.ie/find-a-job/senior-python-developer-7348/",
        "email": "alejandro.pino@e-frontiers.ie",
    },
    {
        "company_avatar": "/theme/images/jobs/ef.jpeg",
        "company_name": "e-Frontiers",
        "position": "Senior Python Mid-Senior",
        "description": "Estás descubriendo el poder de Python, pero quieres explorar todas sus posibilidades. Tenemos vacantes abiertas en una empresa enfocada al desarrollo de múltiples aplicaciones aplicadas a las finanzas: herramientas Fintech! Si te gusta cacharrear con el código tenemos que hablar :D",
        "location": "Pozuelo de Alarcón (Madrid) / Semirremoto",
        "skills": ["python", "flask", "docker", "kubernetes", "sql"],
        "salary": "30.000€ – 42.000€",
        "url": "https://e-frontiers.ie/find-a-job/python-developer-mid-senior-7330/",
        "email": "alejandro.pino@e-frontiers.ie",
    },
    {
        "company_avatar": "/theme/images/jobs/ef.jpeg",
        "company_name": "e-Frontiers",
        "position": "Python Developer EUROPE – 100% REMOTE",
        "description": "Te gusta trabajar con Python, desde casa, desde cualquier lugar de Europa… ¡Tenemos que hablar! Tenemos diversas oportunidades abiertas para desarrolladores Python en empresas de producto propio, con sede principalmente en España e Irlanda, esperándote.",
        "location": "Europa / Remoto 100%",
        "skills": [
            "python",
            "django",
            "flask",
            "sql",
            "docker",
            "aws/azure",
            "inglés alto",
        ],
        "salary": "40.000€ – 60.000€",
        "url": "https://e-frontiers.ie/find-a-job/python-developer-europe-100-remote-7799/",
        "email": "alejandro.pino@e-frontiers.ie",
    },
    {
        "company_avatar": "/theme/images/jobs/ef.jpeg",
        "company_name": "e-Frontiers",
        "position": "Python Developer IRELAND",
        "description": "We are looking for a Python Developer to join an Investment Management Firm in Dublin. You will be working within their Infrastructure Reliability Engineering team. Their goal is to ensure platform reliability and operational agility by developing visualizations, dashboards, and tools that reveal insights in data.",
        "location": "Irlanda / Ambas opciones 100% Remoto y Presencial",
        "skills": [
            "python",
            "django",
            "flask",
            "sql",
            "docker",
            "aws/azure",
            "inglés alto",
        ],
        "salary": "40.000€ – 60.000€",
        "url": "https://e-frontiers.ie/find-a-job/python-developer-7708/",
        "email": "lisa.cappelli@e-frontiers.ie",
    },
    {
        "company_avatar": "/theme/images/jobs/alea.jpeg",
        "company_name": "Alea",
        "position": "Senior Developer",
        "description": "Buscamos a alguien de backend. Pero que no le tenga miedo a sistemas, redes, negocio... Con experiencia en desarrollo de aplicaciones con buenas prácticas (XP, arquitecturas limpias o hexagonales), testing (TDD) y que le guste mucho trabajar en equipo puesto que hacemos pairing",
        "location": "Madrid / Remoto",
        "skills": [
            "python",
            "testing",
            "clean code",
            "arquitecturas limpias",
            "colaboración",
            "trabajo en equipo",
            "empatía",
            "proactividad",
        ],
        "salary": "40.000€ – 50.000€",
        "url": "https://aleasoluciones.notion.site/Forma-parte-del-equipo-p-blica-968223e26cc84d94bb9d0efc8038535e",
        "email": "desarrollo@alea-soluciones.com",
    },
]

random.shuffle(JOBS)


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
