import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
id=3
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_TRS_VIEW_ACCOUNT
class Test_SP_TRS_VIEW_ACCOUNT(object):

    def test_sp_trs_view_account_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.TRS_VIEW_ACCOUNT(
            id=id
        )
        rs = sp_helper.TRS_VIEW_ACCOUNT(fields_data)
        step_code = 'TRS_VIEW_ACCOUNT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"