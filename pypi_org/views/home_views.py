import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    print(str(flask.url_for('static', filename='css/site.css')))
    return {'packages': test_packages}