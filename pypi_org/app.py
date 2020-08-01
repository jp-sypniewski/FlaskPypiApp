import os
import flask

import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=False)

def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite')

    db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    # from pypi_org.views import home_views
    app.register_blueprint(home_views.blueprint)
    # app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
