# -*- coding: utf-8 -*-
# Created by richie at 2018/10/15


from . import views
from flask_via.routers.default import Functional

routes = [
    Functional('/', views.index, endpoint='index'),
    Functional('/index', views.index, endpoint='index'),
]
