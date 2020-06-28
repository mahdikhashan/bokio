from flask import abort
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound


router = Blueprint('editor_route', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/editor/static')


@router.route('/editor')
def index():
    try:
        return render_template('index.html', page='this is your page.')
    except TemplateNotFound:
        abort(404)
