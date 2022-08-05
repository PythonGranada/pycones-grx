# -*- coding: utf-8 -*-
import random

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
