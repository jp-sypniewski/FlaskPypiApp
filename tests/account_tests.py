from flask import Response

from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app, client
import unittest.mock


def test_viewmodel_register_validation_when_valid():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a' * 6
    }

    # creating fake request context so it thinks it's within flask
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # act
    # using mock's patch to 'fake' the behavior and creates the return value
    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    # assert
    assert vm.error is None


def test_viewmodel_register_validation_for_existing_user():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a' * 6
    }

    # creating fake request context so it thinks it's within flask
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # act
    # using mock's patch to 'fake' the behavior and creates the return value
    target = 'pypi_org.services.user_service.find_user_by_email'
    test_user = User(email=form_data.get('email'))
    with unittest.mock.patch(target, return_value=test_user):
        vm.validate()

    # assert
    assert vm.error is not None
    assert 'already exists' in vm.error


def test_view_register_view_new_user():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    from pypi_org.views.account_views import register_post
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a' * 6
    }

    target = 'pypi_org.services.user_service.find_user_by_email'
    find_user = unittest.mock.patch(target, return_value=None)
    target = 'pypi_org.services.user_service.create_user'
    create_user = unittest.mock.patch(target, return_value=User())
    request = flask_app.test_request_context(path='/account/register', data=form_data)

    with find_user, create_user, request:
        # act
        resp: Response = register_post()

    # assert
    assert resp.location == '/account'


def test_integration_account_home_no_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get('/account')

    assert resp.status_code == 302
    assert resp.location == 'http://localhost/account/login'


def test_integration_account_home_with_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    test_user = User(name='First', email='anemail@address.com')
    with unittest.mock.patch(target, return_value=test_user):
        resp: Response = client.get('/account')

    assert resp.status_code == 200
    assert b'First' in resp.data
