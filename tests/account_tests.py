from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app
import unittest.mock

def test_register_validation_when_valid():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a'*6
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

def test_register_validation_for_existing_user():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a'*6
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
    assert 'exist' in vm.error
