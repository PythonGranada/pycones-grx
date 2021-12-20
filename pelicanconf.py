#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from pelicanconf_common import *
from pelicanconf_event import *
from pelicanconf_flags import *


SITEURL = os.getenv('SITEURL', '')
GOOGLE_ANALYTICS_CODE = os.getenv('GOOGLE_ANALYTICS_CODE', '0000')
