#!/usr/bin/env python3
"""
basic Flask app
"""

from typing import Dict, Union
from flask import Flask, render_template, request
import flask
from flask_babel import Babel


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
    return request.accept_languages.best_match(match)


@app.route('/', methods=['GET'])
def home() -> str:
    """Basic welcome"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
