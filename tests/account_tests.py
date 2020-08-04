from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app

def test_register_validation_when_valid():
    # 3 a's of testing: arrange, act, then assert

    # arrange
    form_data = {
        'name': 'first',
        'email': 'anemail@address.com',
        'password': 'a'*6
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # act
    vm.validate()

    # assert
    assert vm.error is None