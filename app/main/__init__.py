# -*- coding: utf-8 -*-
# Created by richie at 2018/10/15

from flask import Blueprint

main = Blueprint("main", __name__)

from . import errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
