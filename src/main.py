from flask import Flask

from settings import settings

app = Flask(settings.APP_NAME)


@app.route("/")
def hello_world():
    return f'<p>{settings.APP_NAME}</p>'


if __name__ == '__main__':
    app.run(debug=True)
