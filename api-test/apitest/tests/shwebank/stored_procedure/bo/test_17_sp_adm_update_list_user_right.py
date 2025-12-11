import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid

# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ADM_UPDATE_LIST_USER_RIGHT
class Test_SP_ADM_UPDATE_LIST_USER_RIGHT(object):

    def test_sp_adm_update_list_user_right_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        list_user_right = [
            {
                "role_id": 2,
                "command_id": "0120050020010",
                "command_id_detail": "A",
                "invoke": 0,
                "approve": 1
            },
            {
                "role_id": 2,
                "command_id": "ACT_MAN",
                "command_id_detail": "I",
                "invoke": 1,
                "approve": 1
            }
        ]
        fields_data = sp_payload.ADM_UPDATE_LIST_USER_RIGHT(
            list_user_right=list_user_right
        )
        rs = sp_helper.ADM_UPDATE_LIST_USER_RIGHT(fields_data)
        step_code = 'SQL_MULTI_UPDATE_USER_RIGHT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"