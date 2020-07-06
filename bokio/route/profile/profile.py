from flask import abort
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound

from flask_login import login_required, current_user


router = Blueprint('profile_route', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/profile/static')


@router.route('/profile')
@login_required
def index():
    try:
        return render_template('profile.html', name=current_user.name)
    except TemplateNotFound:
        abort(404)
