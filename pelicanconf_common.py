#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pelicanconf_flags import *

AUTHOR = 'Python España Org'
SITENAME = 'PyConES 2022 GRX'
PATH = 'content'
THEME = "theme"
PLUGIN_PATHS = ["plugins"]

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
MARKUP = ("md",)

PLUGINS = ["i18n_subsites", "assets", "events"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

EVENTS_ICS_FNAME =  'calendar.ics'
DIRECT_TEMPLATES = ['index', 'blog', 'keynoters', 'sponsorship', 'schedule']
MENUITEMS_NAVBAR = [
    ("La ciudad", "/pages/granada.html"),
    ("Código de conducta", "/pages/code-of-conduct.html"),
    ("Organizadores", "/pages/organizers.html")
]

if ENABLED_SPEAKERS:
    MENUITEMS_NAVBAR.append(tuple(("Ponentes", "/keynoters.html")))

if ENABLED_SPONSORSHIPS:
    MENUITEMS_NAVBAR.append(tuple(("Patrocinadores", "/sponsorship.html")))

if ENABLED_SCHEDULE:
    MENUITEMS_NAVBAR.append(tuple(("Horario", "/schedule.html")))

if ENABLED_BLOG:
    MENUITEMS_NAVBAR.append(tuple(("Blog", "/blog.html")))

NAVBAR_STYLE = "is-primary"
THEME_LOGO = "/theme/images/piconesGR_mini.svg"
FOOTER= "Copyright © Python España & PyConES 2022 Org"
