from flask import abort
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound


router = Blueprint('index_route', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/index/static')


@router.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
