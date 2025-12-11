import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
customer_code='12000020'
current_status='N'
new_status='S'
description='Change customer status'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CTM_CAS
class Test_SP_CTM_CAS(object):

    def test_sp_ctm_cas_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.CTM_CAS(
            customer_code=customer_code,
            current_status=current_status,
            new_status=new_status,
            description=description
        )
        rs = sp_helper.CTM_CAS(fields_data)
        step_code = 'CTM_CAS'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"