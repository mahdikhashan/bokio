from flask import abort
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound


router = Blueprint('home_route', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/home/static')


@router.route('/home')
def home():
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)


@router.route('/home/<string>')
def home_item(string: str):
    try:
        return render_template('item.html', string=string)
    except TemplateNotFound:
        abort(404)


@router.route('/home/create')
def create_item():
    try:
        return render_template('create.html')
    except TemplateNotFound:
        abort(404)
