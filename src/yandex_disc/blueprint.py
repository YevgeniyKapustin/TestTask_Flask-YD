from flask import Blueprint, render_template, request, session

from src.yandex_disc.services import fetch_files_info, download_file

blueprint = Blueprint('yandex_disc', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Отображает основную страницу для работы с яндекс диском."""
    files: list[dict] | None = None
    filtered_files: list[dict] | None = None
    public_key: str | None = None
    selected_type: str | None = None

    if request.method == 'POST':
        session['form_data'] = request.form
        public_key: str | None = request.form.get('public_key') or session.get('public_key')
        selected_type: str | None = request.form.get('selected_type') or session.get('selected_type')
        if public_key:
            files: list[dict] | None = fetch_files_info(public_key)
        if selected_type and selected_type != 'all':
            filtered_files: list[dict] | None = [file for file in files if file.get('mime_type') == selected_type]

    return render_template(
        'yandex_disc/index.html',
        files=filtered_files if filtered_files else files,
        download_file=download_file,
        folder_public_key=public_key if files and len(files) > 1 else None,
        types={file.get('mime_type') for file in files if file} if files else [],
        public_key=public_key if public_key else '',
        selected_type=selected_type
    )
