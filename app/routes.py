# -*- coding: utf-8 -*-
# Created by richie at 2018/10/15


from .main import main as blueprint_main
from flask_via.routers import default

routes = [
    default.Blueprint(blueprint_main),
]
