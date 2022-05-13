#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import sys
import os
import pytz

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pelicanconf_flags import *

AUTHOR = "Python España Org"
SITENAME = "PyConES 2022 GRX"
PATH = "content"
THEME = "theme"
PLUGIN_PATHS = ["plugins"]

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"
DEFAULT_DATE_FORMAT = "%d/%M/%Y"

MARKUP = ("md",)

PLUGINS = ["i18n_subsites", "assets", "events"]
STATIC_PATHS = ["images", "extra/manifest.json"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n", "extensions.gphotos.GPhotosExtension"],
}

EVENTS_ICS_FNAME = "calendar.ics"

DIRECT_TEMPLATES = [
    "index",
    "blog",
    "keynoters",
    "sponsorship",
    "schedule",
    "gallery",
    "past_editions",
    "organizers",
    "jobs",
]
MENUITEMS_NAVBAR = [
    ("La ciudad", "/pages/granada.html"),
    ("Organización", "/organizers.html"),
]

if ENABLED_SPEAKERS:
    MENUITEMS_NAVBAR.append(tuple(("Ponentes", "/keynoters.html")))

if ENABLED_SPONSORSHIPS:
    MENUITEMS_NAVBAR.append(tuple(("Patrocinios", "/sponsorship.html")))

if ENABLED_FINANCIAL_AID:
    MENUITEMS_NAVBAR.append(tuple(("Becas", "/becas.html")))

if ENABLED_SCHEDULE:
    MENUITEMS_NAVBAR.append(tuple(("Horario", "/schedule.html")))

if ENABLED_GALLERY:
    MENUITEMS_NAVBAR.append(tuple(("Galería", "/gallery.html")))

if ENABLED_PAST_EDITIONS:
    MENUITEMS_NAVBAR.append(tuple(("Ediciones pasadas", "/past_editions.html")))

if ENABLED_JOBS:
    MENUITEMS_NAVBAR.append(tuple(("Ofertas de trabajo", "/jobs.html")))

if ENABLED_BLOG:
    MENUITEMS_NAVBAR.append(tuple(("Blog", "/blog.html")))


NAVBAR_STYLE = "is-primary"
THEME_LOGO = "/theme/images/piconesGR_mini.svg"
MAIN_LOGO = "/theme/images/piconesGR_horizontal.svg"
MAIN_LOGO_PNG = "/theme/images/piconesGR_horizontal.png"
FOOTER = "Copyright © Python España & PyConES 2022 Org"
THEME_COLOR = "#0E749CFF"
LAST_UPDATE = datetime.now(pytz.timezone(TIMEZONE)).strftime("%B %d, %Y %A, %H:%M:%S")
