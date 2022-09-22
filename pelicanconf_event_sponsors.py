# -*- coding: utf-8 -*-
import random

SPONSORS = [
    {
        "level_name": "keystone",
        "title": "Keystone 🏆",
        "size": "270px",
        "size_schedule": "500px",
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
        "size_schedule": "400px",
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
        "size_schedule": "200px",
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
        "size_schedule": "200px",
        "order": 4,
        "members": [
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
                "name": "holaluz",
                "photo": "/theme/images/sponsors/holaluz.png",
                "url": "https://holaluz.com/",
            },
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
            {
                "name": "Singular",
                "photo": "/theme/images/sponsors/singular.png",
                "url": "https://www.sngular.com/es/",
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
                "name": "Facultad de Medicina, UGR",
                "photo": "/theme/images/sponsors/facultad_medicina_ugr.png",
                "url": "https://medicina.ugr.es",
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
