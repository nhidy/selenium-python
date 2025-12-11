import pytest 
import json

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.neptune_helpers import NeptuneHelper

expected_status = 'Completed'
@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.test_request_neptune
class TestRequest(object):
    @pytest.mark.test_request_neptune
    def test_request_neptune(self, user):
        helper = NeptuneHelper(user)
        workflow_id = 'SQL_SEARCH_CTM'
        fields_data = {
            "search_text": "",
            "page_size": 0,
            "page_index": 0
        }
        rs = helper.get_execution_info_res_body(workflow_id, fields_data)
        print('RESPONSE' + '\n' + '\t', json.dumps(rs, indent=4, sort_keys=True))
        actual_status = rs['execution_steps'][0]['p2_status']
        assert actual_status == expected_status, f'Expected \'{expected_status}\', Actual status: \'{actual_status}\'. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'