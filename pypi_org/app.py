import os
import flask

import pypi_org.data.db_session as db_session
from pypi_org.data.users import User
from pypi_org.nosql import mongo_setup

app = flask.Flask(__name__)


def main():
    configure()


def configure():
    register_blueprints()
    setup_db()
    app.run(debug=False)


def setup_db():
    mongo_setup.global_init()




def register_blueprints():
    from pypi_org.views import home_views
    app.register_blueprint(home_views.blueprint)
    from pypi_org.views import package_views
    app.register_blueprint(package_views.blueprint)
    from pypi_org.views import account_views
    app.register_blueprint(account_views.blueprint)
    from pypi_org.views import seo_views
    app.register_blueprint(seo_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()
