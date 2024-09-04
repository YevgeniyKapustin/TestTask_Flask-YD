from flask import Blueprint, render_template, request

from src.yandex_disc.services import fetch_files_info, download_file

blueprint = Blueprint('yandex_disc', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    files = None
    public_key = None
    if request.method == 'POST':
        public_key = request.form['public_key']
        files = fetch_files_info(public_key)
    return render_template(
        'yandex_disc/index.html',
        files=files,
        download_file=download_file,
        folder_public_key=public_key if files and len(files) > 1 else None
    )
