# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from pelican import signals, utils
from collections import namedtuple, defaultdict
import icalendar
import logging
import os.path
import pytz
import json
import pytz

log = logging.getLogger(__name__)


def parse_tstamp(datetime_string):
    """Parse a timestamp string in format "YYYY-MM-DD HH:MM"

    :returns: datetime
    """
    return datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S')



def generate_ical_file(pelican_object):
    """Generate an iCalendar file
    """

    ics_fname = pelican_object.settings['EVENTS_ICS_FNAME']
    curr_events = json.loads(pelican_object.settings['EVENT_TALKS'])

    if not ics_fname:
        return

    ics_fname = os.path.join(pelican_object.settings['OUTPUT_PATH'], ics_fname)

    ical = icalendar.Calendar()
    ical.add('prodid', '-//My calendar product//mxm.dk//')
    ical.add('version', '2.0')

    events_titles = []
    for e in curr_events:
        title = e.get("title")
        if title not in events_titles:
            event = icalendar.Event()
            event.add('SUMMARY', e.get("title"))
            event.add('DTSTART', parse_tstamp(e.get("start")))
            event.add('DTEND', parse_tstamp(e.get("end")))
            ical.add_component(event)
            events_titles.append(title)

    with open(ics_fname, 'wb') as f:
        f.write(ical.to_ical())


def register():
    signals.finalized.connect(generate_ical_file)
