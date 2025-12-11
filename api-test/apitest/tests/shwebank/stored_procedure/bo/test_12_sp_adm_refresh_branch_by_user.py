import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
page_size=5
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ADM_REFRESH_BRANCH_BY_USER
class Test_SP_ADM_REFRESH_BRANCH_BY_USER(object):

    def test_sp_adm_refresh_branch_by_user_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.ADM_REFRESH_BRANCH_BY_USER(
            page_size=page_size
        )
        rs = sp_helper.ADM_REFRESH_BRANCH_BY_USER(fields_data)
        step_code = 'SQL_REFRESH_BRANCH'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"