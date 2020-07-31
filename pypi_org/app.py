import flask

app = flask.Flask(__name__)

def main():
    print('in main')
    register_blueprints()
    app.run(debug=False)


def register_blueprints():
    print('in register_blueprints')
    from pypi_org.views import home_views
    # from pypi_org.views import home_views
    app.register_blueprint(home_views.blueprint)
    # app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
