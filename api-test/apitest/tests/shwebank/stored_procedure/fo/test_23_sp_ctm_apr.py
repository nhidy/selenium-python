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
customer_name='A NAME'
description='Approve customer'
customer_status='P'
created_by='ac02'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CTM_APR
class Test_SP_CTM_APR(object):

    def test_sp_ctm_apr_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.CTM_APR(
            customer_code=customer_code,
            customer_name=customer_name,
            description=description,
            customer_status=customer_status,
            created_by=created_by
        )
        rs = sp_helper.CTM_APR(fields_data)
        step_code = 'CTM_APR'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"