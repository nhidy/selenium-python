import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.neptune_helpers import NeptuneHelper

expected_status = 'Completed'
@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    return req

@pytest.mark.auth_service
class TestAuthorizeService(object):
    @pytest.mark.login_service
    def test_login_service(self, user):
        user.login_service()

    @pytest.mark.login_service_helper
    def test_login_service_helper(self, user):
        helper = NeptuneHelper(user)
        workflow_id = 'UMG_LOGIN'
        fields_data = {
            "username": "admin",
            "password": "123456"
        }
        rs = helper.get_execution_info_res_body(workflow_id, fields_data)
        actual_status = rs['execution_steps'][0]['p2_status']
        assert actual_status == expected_status, f'Expected \'{expected_status}\', Actual status: \'{actual_status}\''
        assert rs['execution_steps'][0]['p2_content']['Response']['OUTPUT']['login']['Token'], f'Empty Token'