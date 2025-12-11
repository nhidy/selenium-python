import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
from_teller_code='nhidoan'
to_teller_code='nhiteller'
to_teller_name='Nhi Teller'
amount=1000.45
currency='MMK'
description='Nhi Doan move 1000.45 MMK cash to Nhi Teller'
user_approve='nhiteller'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CSH_MOV
class Test_SP_CSH_MOV(object):

    def test_sp_csh_mov_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.CSH_MOV(
            from_teller_code=from_teller_code,
            to_teller_code=to_teller_code,
            to_teller_name=to_teller_name,
            amount=amount,
            currency=currency,
            description=description,
            user_approve=user_approve
        )
        rs = sp_helper.CSH_MOV(fields_data)
        step_code = 'CSH_MOV'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"