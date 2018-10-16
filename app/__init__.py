# -*- coding: utf-8 -*-
# Created by richie at 2018/10/15

from flask import Flask
from flask_via import Via
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babelex import Babel
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_moment import Moment
from flask_marshmallow import Marshmallow
from settings import config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
via = Via()
babel = Babel()
mail = Mail()
pagedown = PageDown()
moment = Moment()
ma = Marshmallow()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    init_plugin(app)

    return app


def init_plugin(app):
    via.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    moment.init_app(app)
    ma.init_app(app)


