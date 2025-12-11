import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
master_account_number='110025729834'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_DELETE_ACCOUNTLINKAGE
class Test_SP_DPT_DELETE_ACCOUNTLINKAGE(object):

    def test_sp_dpt_delete_accountlinkage_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_DELETE_ACCOUNTLINKAGE(
            master_account_number=master_account_number
        )
        rs = sp_helper.DPT_DELETE_ACCOUNTLINKAGE(fields_data)
        step_code = 'DPT_DELETE_ACCOUNTLINKAGE'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"