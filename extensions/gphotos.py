# -*- coding: utf-8 -*-
import jinja2
from jinja2_simple_tags import StandaloneTag
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree
import pathlib
import requests
import random
import re


class GPhotosExtension(StandaloneTag):
    tags = {"gphotos"}
    template_path = pathlib.Path(__file__).parent.joinpath("templates").resolve()
    template_loader = jinja2.FileSystemLoader(searchpath=template_path)
    template_env = jinja2.Environment(loader=template_loader)


    def render(self, url, title, description, background_color="#ffffff"):
        template = self.template_env.get_template("gphotos.html.jinja2")
        photos = self.get_photos(url)
        context = {
            "url": url,
            "title": title,
            "description": description,
            "photos": photos,
            "background_color": background_color
        }

        return template.render(**context)

    @staticmethod
    def get_photos(url):
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        dom = etree.HTML(str(soup))

        scripts = dom.xpath("//script")
        pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        photos_urls = []

        for x in scripts:
            if 'initDataCallback' in str(x.text):
                urls = re.findall(pattern, str(x.text))
                for u in urls:
                    if len(u) > 150 and "video" not in u:
                        full_url = f"{u}=w1920-h1080"
                        photos_urls.append(full_url)

        random.shuffle(photos_urls)
        photos_urls = list(set(photos_urls))
        return photos_urls
