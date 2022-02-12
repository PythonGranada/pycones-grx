# -*- coding: utf-8 -*-
import jinja2
from jinja2_simple_tags import StandaloneTag
from datetime import datetime
import pathlib

class NowExtension(StandaloneTag):
    tags = {"now"}
    template_path = pathlib.Path(__file__).parent.joinpath("templates").resolve()
    template_loader = jinja2.FileSystemLoader(searchpath=template_path)
    template_env = jinja2.Environment(loader=template_loader)


    def render(self):
        template = template_env.get_template("now.html.jinja2")
        return template.render()
