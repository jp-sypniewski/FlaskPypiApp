import datetime
import unittest.mock

from flask import Response

from tests.test_client import flask_app


def test_package_details_success():
    # arrange
    from pypi_org.data.package import Package
    from pypi_org.data.releases import Release
    from pypi_org.views.package_views import package_details

    test_package = Package()
    test_package.id = 'sqlalchemy'
    test_package.description = "TBD"
    test_package.releases = [
        Release(created_date=datetime.datetime.now(), major_ver=1, minor_ver=2, build_ver=345),
        Release(created_date=datetime.datetime.now() - datetime.timedelta(days=7))
    ]

    #act
    patch_value = unittest.mock.patch('pypi_org.services.package_service.get_package_by_id', return_value=test_package)
    request_context = flask_app.test_request_context(path='/project/' + test_package.id)
    with patch_value, request_context:
        resp: Response = package_details(test_package.id)

    # assert
    assert b'sqlalchemy 1.2.345' in resp.data

def test_package_details_404(client):
    # arrange
    bad_package = 'sqlalchemeee_missing'

    # act
    patch_value = unittest.mock.patch('pypi_org.services.package_service.get_package_by_id', return_value=None)
    with patch_value:
        resp: Response = client.get(bad_package)

    # assert
    assert resp.status_code == 404