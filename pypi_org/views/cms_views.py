import flask

from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')

