import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_number='410038200852'
tx_reference_id='acf1d3706d6f4b708b744c47d6c14476'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_APPROVE_MODIFY
class Test_SP_DPT_APPROVE_MODIFY(object):

    def test_sp_dpt_approve_modify_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APPROVE_MODIFY(
            account_number=account_number,
            tx_reference_id=tx_reference_id
        )
        rs = sp_helper.DPT_APPROVE_MODIFY(fields_data)
        step_code = 'DPT_APPROVE_MODIFY'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"