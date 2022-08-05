#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random

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
            {
                "name": "Euro Python",
                "photo": "/theme/images/sponsors/europython.png",
                "url": "https://www.europython-society.org/",
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
            {
                "name": "Brite Payment Group",
                "photo": "/theme/images/sponsors/brite.png",
                "url": "https://www.britepaymentgroup.com/",
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
        "url": "https://e-frontiers.ie/jobs/7799/",
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
    {
        "company_avatar": "/theme/images/jobs/travelperk.png",
        "company_name": "TravelPerk",
        "position": "Software Engineer",
        "description": "We are looking for product-oriented software engineers with 3+ years experience in any web programming language. Come and join us to work in one of the fastest growing scale-ups in the world revolutionizing the business travel industry.",
        "location": "Barcelona / Berlin / London / Birmingham hybrid",
        "skills": [
            "python",
            "django",
            "tornado",
            "react",
            "aws",
            "docker",
            "inglés alto",
        ],
        "salary": "50.000€ – 65.000€",
        "url": "https://www.travelperk.com/job-application/?gh_jid=3242844",
    },
    {
        "company_avatar": "/theme/images/jobs/travelperk.png",
        "company_name": "TravelPerk",
        "position": "Senior Software Engineer",
        "description": "We are looking for product-oriented software engineers with 3+ years experience in any web programming language. Come and join us to work in one of the fastest growing scale-ups in the world revolutionizing the business travel industry.",
        "location": "Barcelona / Berlin / London / Birmingham hybrid",
        "skills": [
            "python",
            "django",
            "tornado",
            "react",
            "aws",
            "docker",
            "inglés alto",
        ],
        "salary": "65.000€ – 90.000€",
        "url": "https://www.travelperk.com/job-application/?gh_jid=3242303",
    },
    {
        "company_avatar": "/theme/images/jobs/travelperk.png",
        "company_name": "TravelPerk",
        "position": "Engineering Manager",
        "description": "We are looking for people-oriented Engineering Managers with 3+ years experience in directly managing engineers to join us at a hyper-growth period. We’ve recently raised $115 million, making us a unicorn! Come and join us in revolutionizing the global business travel industry.",
        "location": "Barcelona / Berlin / London / Birmingham hybrid",
        "skills": ["management", "career path", "leadership",],
        "salary": "75.000€ – 95.000€",
        "url": "https://www.travelperk.com/job-application/?gh_jid=3958248",
    },
    {
        "company_avatar": "/theme/images/jobs/celtiberian.png",
        "company_name": "Celtiberian",
        "position": "Junior Full-Stack developer (Javascript/Python)",
        "description": "¿Alguna vez has deseado trabajar con startups de la mismísima California? En Celtiberian buscamos ingenieros con alguna experiencia en el desarrollo de software interesados en dominar el entorno de Javascript y Python, además de apasionados del conocimiento tecnológico.",
        "location": "Granada / Remoto",
        "skills": [
            "JavaScript",
            "Python",
            "Django",
            "React",
            "Node.js",
            "React Native",
            "Inglés alto",
        ],
        "salary": "24.000€ - 36.000€",
        "url": "https://es.linkedin.com/company/celtiberian",
        "email": "lorena@celtiberian.es",
    },
    {
        "company_avatar": "/theme/images/jobs/celtiberian.png",
        "company_name": "Celtiberian",
        "position": "Senior Full-Stack developer (Javascript/Python)",
        "description": "Si además de ser un desarrollador Full-Stack experimentado con los ecosistemas de Javascript y Python, estabas buscando una oportunidad para trabajar con startups en entornos internacionales y dinámicos, tenemos una propuesta interesante para tí.",
        "location": "Granada / Remoto",
        "skills": [
            "JavaScript",
            "Python",
            "Django",
            "React",
            "Node.js",
            "React Native",
            "Inglés alto",
        ],
        "salary": "32.000€ - 45.000€",
        "url": "https://es.linkedin.com/company/celtiberian",
        "email": "lorena@celtiberian.es",
    },
    {
        "company_avatar": "/theme/images/jobs/celtiberian.png",
        "company_name": "Celtiberian",
        "position": "DevOps Engineer",
        "description": "¿Te apasiona el DevOps y te llama la atención trabajar para startups internacionales? En Celtiberian podrás cubrir ambas demandas. Somos una consultora de software comprometida con los servicios de calidad y la formación constante en las tecnologías más punteras.",
        "location": "Granada / Remoto",
        "skills": [
            "Kubernetes",
            "Docker",
            "Python",
            "JavaScript",
            "AWS",
            "Inglés alto",
        ],
        "salary": "35.000€ - 45.000€",
        "url": "https://es.linkedin.com/company/celtiberian",
        "email": "lorena@celtiberian.es",
    },
    {
        "company_avatar": "/theme/images/jobs/intelygenz.png",
        "company_name": "Intelygenz",
        "position": "Data Scientist - ML",
        "description": "We’re looking for a Machine Learning Engineer to bring their expertise to some great projects, learn in a friendly, collaborative environment, and innovate with us. You will design and implement end-to-end data pipelines, being part of an agile team of amazing developers.",
        "location": "Madrid / Remoto",
        "skills": ["ML", "Python", "Golang", "Docker", "SQL", "Protobuf",],
        "salary": "36.000€ - 45.000€",
        "url": "https://intelygenz.com/job/731838/",
    },
    {
        "company_avatar": "/theme/images/jobs/intelygenz.png",
        "company_name": "Intelygenz",
        "position": "Data Scientist",
        "description": "As a Data Scientist your goals will be organized in two areas. Industry: process automation. Laboratory: research and testing state-of-the-art techniques and solutions to keep improving our skills and sharing with the community our knowledge and proof of concepts.",
        "location": "Madrid / Remoto",
        "skills": [
            "Numpy",
            "Pandas",
            "Scikit-learn",
            "PyTorch/Tensorflow",
            "Deep Reinforcement Learning",
            "NLP",
        ],
        "salary": "36.000€ - 45.000€",
        "url": "https://intelygenz.com/job/440392/",
    },
    {
        "company_avatar": "/theme/images/jobs/intelygenz.png",
        "company_name": "Intelygenz",
        "position": "Tech Lead Automation",
        "description": "Our next Technical Lead is very skilled in Python and/or Golang and has 5 years of experience deploying and evolving software in production environments. Also, Scalable Architectures are part of your day and Good development practices are a must for you.",
        "location": "Madrid / Remoto",
        "skills": ["Python", "Golang", "Databases", "DevOps", "Docker",],
        "salary": "50.000€ - 60.000€",
        "url": "https://intelygenz.com/job/814833/",
    },
    {
        "company_avatar": "/theme/images/jobs/intelygenz.png",
        "company_name": "Intelygenz",
        "position": "Python Developer",
        "description": "The Python Developer we are looking for has at least 3 years of experience, good developement practices and enjoy working in an agile and collaborative environment. Also, knows Docker and/or Kubernetes, ATDD and is able to communicate in English.",
        "location": "Madrid / Remoto",
        "skills": ["Python", "Docker", "TDD", "JavaScript",],
        "salary": "32.000€ - 40.000€",
        "url": "https://intelygenz.com/job/649170/",
    },
    {
        "company_avatar": "/theme/images/jobs/holaluz.png",
        "company_name": "Holaluz",
        "position": "Data Architect",
        "description": "🍼 Nursery inhouse<br/>🚀 Desarrollo profesional sin límites en una empresa apasionante y un equipo con desafíos constantes<br/>🏡 Horario flexible y posibilidad de trabajo a distancia de forma habitual.<br/>🌊 Ubicaciones de las oficinas a primera linea de mar<br/>💪 Yoga y Crossfit inhouse",
        "location": "Híbrida (Barcelona)",
        "skills": ["AWS", "Snowflake o Redshift", "Python", "SQL", "Airflow",],
        "salary": "60.000 € - 85.000 €",
        "url": "https://apply.workable.com/holaluz/j/478A031C7A/",
        "email": "ariadna.garriga@holaluz.com",
    },
    {
        "company_avatar": "/theme/images/jobs/holaluz.png",
        "company_name": "Holaluz",
        "position": "Senior Data Engineer",
        "description": "En Holaluz estamos buscando a un/a Senior Data Engineer para ser responsable de la integración, arquitectura y mantenimiento de los Datos con las tecnologías de la casa AWS, Pentaho Kettle, Python, Java, Scala, MySQL, SQL, MongoDB y Airflow. ¿Te interesa? ¡Sigue leyendo! 🙂",
        "location": "Híbrida (Barcelona)",
        "skills": [
            "AWS",
            "Pentaho Kettle",
            "Python",
            "Java",
            "Scala",
            "MySQL",
            "SQL",
            "MongoDB",
            "Airflow",
        ],
        "salary": "40.000 € - 50.000 €",
        "url": "https://holaluz.workable.com/backend/jobs/2565347/",
        "email": "ariadna.garriga@holaluz.com",
    },
    {
        "company_avatar": "/theme/images/jobs/trustyou.jpeg",
        "company_name": "TrustYou",
        "position": "Professional Python Developer",
        "description": "Imagine a workplace that allows you to own your own product and where your ideas will be heard and implemented. Imagine an environment where your performance makes a difference, not just within the company itself but for billions of travelers worldwide! That place is TrustYou.",
        "location": "Madrid / Munich / Cluj-Napoca / Remote",
        "skills": [
            "Python 3",
            "asynchronous programming",
            "PostgreSQL",
            "unit-testing",
            "Web APIs",
        ],
        "salary": "40.000€ - 60.000€",
        "url": "https://jobs.lever.co/trustyou/5732c644-7245-4f41-8ec1-50d819cf438a",
    },
    {
        "company_avatar": "/theme/images/jobs/trustyou.jpeg",
        "company_name": "TrustYou",
        "position": "Professional Engineer - Backend",
        "description": "Imagine a workplace that allows you to own your own product and where your ideas will be heard and implemented. Imagine an environment where your performance makes a difference, not just within the company itself but for billions of travelers worldwide! That place is TrustYou.",
        "location": "Spain / Germany / Romania / European Union (Remote)",
        "skills": ["Ruby on Rails", "Javascript", "PostgreSQL", "TDD",],
        "salary": "40.000€ - 70.000€",
        "url": "https://jobs.lever.co/trustyou/2ca76451-8c8a-43e6-ae54-93fdee798398",
    },
    {
        "company_avatar": "/theme/images/jobs/trustyou.jpeg",
        "company_name": "TrustYou",
        "position": "Senior Frontend Engineer",
        "description": "Imagine a workplace that allows you to own your own product and where your ideas will be heard and implemented. Imagine an environment where your performance makes a difference, not just within the company itself but for billions of travelers worldwide! That place is TrustYou.",
        "location": "Spain / Germany / Romania / European Union (Remote)",
        "skills": [
            "frontend",
            "React",
            "reusable UIs",
            "Redux/MobX",
            "NodeJS",
            "any backend language",
        ],
        "salary": "50.000€ - 70.000€",
        "url": "https://jobs.lever.co/trustyou/8f27c517-587f-4832-9d79-dbf48a5a5134",
    },
    {
        "company_avatar": "/theme/images/jobs/nucleoo.jpeg",
        "company_name": "Nucleoo",
        "position": "Software Engineer",
        "description": "Here you will be part of one of the agile development teams working on large data projects using technologies such as Python, Angular, and MongoDB. You will work together with the Lead Developer and communicate with clients in English every day.",
        "location": "Híbrido/100% remoto",
        "skills": [
            "Python",
            "Angular",
            "React",
            "Vue.js",
            "SQL or No-SQL",
            "Jasmine/cypress/Jest",
            "Git",
            "Flask",
            "C#/.NET",
            "Gitlab",
            "Docker" "Terraform",
            "AWS/Azure",
        ],
        "salary": "20.000€ - 45.000€",
        "url": "https://nucleoo.com/careers/software-engineer-python/",
        "email": "hr@nucleoo.com",
    },
    {
        "company_avatar": "/theme/images/jobs/nucleoo.jpeg",
        "company_name": "Nucleoo",
        "position": "FullStack Engineer",
        "description": "We are looking for an experienced and talented fullstack engineer  with +3 years experience for developing enterprise scale software.",
        "location": "Hibrido/100% remoto",
        "skills": [
            "English",
            "React",
            "JavaScript",
            "Typescript",
            "HTML",
            "CSS",
            "LESS",
            "computer systems",
            "algorithms",
            "flows",
            ".net",
            "c#",
            "powershell",
            "XML",
        ],
        "salary": "25.000€ - 45.000€",
        "url": "https://nucleoo.com/careers/fullstack-engineer/",
        "email": "hr@nucleoo.com",
    },
    {
        "company_avatar": "/theme/images/jobs/nucleoo.jpeg",
        "company_name": "Nucleoo",
        "position": "Quality Assurance Engineer",
        "description": "Nucleoo is looking for an experienced and talented Test Engineer who’s proficient in testing of enterprise scale software and automation of tests. ",
        "location": "Híbrido/100% remoto",
        "skills": [
            "Testrail",
            "Ttest automation code",
            "C#",
            "PowerShell",
            "Issues/bugs (Jira)",
            "Confluence",
            "Load tests",
            "Testing",
            "Development",
        ],
        "salary": "20.000€ - 45.000€",
        "url": "https://nucleoo.com/careers/quality-assurance-engineer/",
        "email": "hr@nucleoo.com",
    },
    {
        "company_avatar": "/theme/images/jobs/nucleoo.jpeg",
        "company_name": "Nucleoo",
        "position": ".Net developer",
        "description": "Nucleoo is looking for an experienced and talented Microsoft .NET Developer who’s proficient in developing enterprise scale software. ",
        "location": "Híbrida/100% remoto",
        "skills": [
            ".NET",
            "C#",
            "algorithms",
            "flows",
            "PowerShell",
            "XSLT",
            "DTD",
            "XSD",
            "XML Editors",
            "oXygen",
            "JustSystems XMetaL",
        ],
        "salary": "20.000€ - 45.000€",
        "url": "https://nucleoo.com/careers/net-developer/",
        "email": "hr@nucleoo.com",
    },
    {
        "company_avatar": "/theme/images/jobs/nucleoo.jpeg",
        "company_name": "Nucleoo",
        "position": "Javascript Engineer",
        "description": "Nucleoo is looking for a self- motivated, multi-tasker and team player engineer to join us in Granada. This is a fantastic opportunity to join a growing and innovative team.",
        "location": "Híbrida/100% remoto",
        "skills": [
            "Typescript",
            "ReactJS",
            "HTML",
            "CSS",
            "Angular",
            "Vue",
            "Cypress",
            "Node",
            "PostgreSQL",
            "AWS",
            "MongoDB",
            "Python",
        ],
        "salary": "20.000€ - 45.000€",
        "url": "https://nucleoo.com/careers/javascript-engineer/",
    },
    {
        "company_avatar": "/theme/images/jobs/ebury.jpeg",
        "company_name": "Ebury Partners UK, Ltd",
        "position": "Senior Mobile Developer - Full Remote",
        "description": "You'll take responsibility for the Mobile Apps development as part of  Channels ecosystem in Ebury. We need experience with building native iOS apps that delight users (Swift Code), writing applications in Flutter or react-Native, and good knowledge of Python.",
        "location": "Full Remote",
        "skills": ["Mobile", "IOS", "Flutter", "React-Native", "NodeJS", "Python",],
        "salary": "55.000€ - 80.000€",
        "url": "https://careers.ebury.com/jobs/1946971-senior-mobile-developer-full-remote",
        "email": "emma.casanova@ebury.com",
    },
    {
        "company_avatar": "/theme/images/jobs/ebury.jpeg",
        "company_name": "Ebury Partners UK Ltd.",
        "position": "Senior Python Developer",
        "description": "We have big experience developing complex sw systems; mainly work with Python/Django; our developers that can “build and run” services, are comfortable with dockerising the code, define standard REST endpoints, adding monitoring and alerting your services. SQL knowledge is a +",
        "location": "Full Remote",
        "skills": [
            "python",
            "django",
            "sql",
            "jenkins",
            "terraform",
            "sentry",
            "prometheus",
            "ELK",
            "Docker",
            "ECS",
            "Kubernetes",
            "kafka",
        ],
        "salary": "40.000€ - 80.000€",
        "url": "https://careers.ebury.com/jobs/1946971-senior-mobile-developer-full-remote",
        "email": "emma.casanova@ebury.com",
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
