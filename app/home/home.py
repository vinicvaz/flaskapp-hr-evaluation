from flask import Blueprint
from flask import current_app as app
from app.home.views import home


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/home/static'
)

home_bp.add_url_rule('/', view_func=home, methods=['GET'])