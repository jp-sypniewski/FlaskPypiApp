import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service
import pypi_org.services.user_service as user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    print(str(flask.url_for('static', filename='css/site.css')))
    return {
        'packages': test_packages,
        'package_count': package_service.get_package_count(),
        'release_count': package_service.get_release_count(),
        'user_count': user_service.get_user_count()
    }