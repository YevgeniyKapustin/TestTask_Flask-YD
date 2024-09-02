from flask import Flask

from settings import settings
from src.yandex_disc.blueprint import blueprint as yandex_disc_bp

app = Flask(settings.APP_NAME)

app.register_blueprint(yandex_disc_bp, url_prefix='/v1/yandex_disc')

if __name__ == '__main__':
    app.run(debug=True)
