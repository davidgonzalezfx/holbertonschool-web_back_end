#!/usr/bin/env python3
"""
basic Flask app
"""

from typing import Dict, Union
from flask import Flask, render_template, request
import flask
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


class Config(object):
    """Config class for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int) -> Union[dict, None]:
    """ function that returns a user dictionary or None if the ID
    cannot be found"""
    return users.get(int(login_as)) if login_as else None


@app.before_request
def before_request():
    """Method executed before all other functions."""
    login_as = request.args.get('login_as')
    user = get_user(login_as)
    if user:
        flask.g.user = user


@babel.localeselector
def get_locale() -> str:
    """Get locale parameters"""
    locale = request.args.get('locale')
    match = app.config['LANGUAGES']
    if locale and locale in match:
        return locale
    try:
        user = flask.g.user
    except:
        user = None
    if user:
        locale = user.get('locale', '')
        if locale and locale in match:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in match:
        return locale
    return request.accept_languages.best_match(match)


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone parameters"""
    try:
        timezone = request.args.get('timezone')
        if timezone:
            tz = pytz.timezone(timezone)
            return timezone
        timezone = flask.g.user.get('timezone')
        if timezone:
            tz = pytz.timezone(timezone)
            return timezone
        timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
        if timezone:
            tz = pytz.timezone(timezone)
            return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return 'UTC'


@app.route('/', methods=['GET'])
def home() -> str:
    """Basic welcome"""
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time)
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
