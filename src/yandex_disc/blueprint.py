from flask import Blueprint, render_template, request

from src.yandex_disc.services import fetch_files_info, get_download_link

blueprint = Blueprint('yandex_disc', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
async def index():
    files = None
    if request.method == 'POST':
        public_key = request.form['public_key']
        files = await fetch_files_info(public_key)
    return render_template(
        'yandex_disc/index.html',
        files=files,
        get_download_link=get_download_link
    )
