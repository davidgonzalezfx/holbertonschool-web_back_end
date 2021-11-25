#!/usr/bin/env python3
""" Flask application """


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ l18n Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object("1-app.Config")
babel = Babel(app)


@app.route("/")
def hello_world():
    """ Handle default route """
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """ Gets the best matching language for user """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    if hasattr(g, "user"):
        if g.user.get('locale') in Config.LANGUAGES:
            return g.user.get('locale')
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.before_request
def before_request():
    """ Gets user and set it as a global """
    user = get_user()
    if user:
        g.user = user


def get_user():
    """ Returns user from request """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None
