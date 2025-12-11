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
branch_code='003'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ADM_CLOSE_BRANCH
class Test_SP_ADM_CLOSE_BRANCH(object):

    def test_sp_adm_close_branch_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.ADM_CLOSE_BRANCH(
            id=id,
            branch_code=branch_code
        )
        rs = sp_helper.ADM_CLOSE_BRANCH(fields_data)
        step_code_01 = 'IMPORT_CHECK_PENDING_TRANSACTION'
        data_actual_01 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_01)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        step_code_02 = 'SQL_CLOSE_BRANCH'
        data_actual_02 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_02)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"