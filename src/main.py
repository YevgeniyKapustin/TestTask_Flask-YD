from flask import Flask

from src.settings import settings
from src.yandex_disc.blueprint import blueprint as yandex_disc_bp

app: Flask = Flask(settings.APP_NAME)
app.secret_key = settings.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.register_blueprint(yandex_disc_bp, url_prefix='api/v1/yandex_disc')
