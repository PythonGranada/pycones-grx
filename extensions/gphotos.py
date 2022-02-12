# -*- coding: utf-8 -*-
import jinja2
from jinja2_simple_tags import StandaloneTag
from datetime import datetime
import pathlib

class GPhotosExtension(StandaloneTag):
    tags = {"gphotos"}
    template_path = pathlib.Path(__file__).parent.joinpath("templates").resolve()
    template_loader = jinja2.FileSystemLoader(searchpath=template_path)
    template_env = jinja2.Environment(loader=template_loader)


    def render(self, url, title, description, background_color="#ffffff"):
        template = self.template_env.get_template("gphotos.html.jinja2")
        photos = self.get_photos(url)
        context = {"url": url, "title": title, "description": description, "photos": photos, "background_color": background_color}
        return template.render(**context)

    @staticmethod
    def get_photos(url):
        return ["https://lh3.googleusercontent.com/HjqgkoOygqNuOE7puXJVTEvQkv2bVg2iOEJLhzJdZVPGm_BQUhzW9019iKpzddittBEZyUyuh_Vdmhy1xSVjYHStrqYyxsjJcY6uibCbeVk5cRnsBiazBmzEHcWdIIlCWUS69RqZEw=w1920-h1080"]
