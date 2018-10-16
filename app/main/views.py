# -*- coding: utf-8 -*-
# Created by richie at 2018/10/15

from flask import render_template

def index():
    return render_template("index.html")
