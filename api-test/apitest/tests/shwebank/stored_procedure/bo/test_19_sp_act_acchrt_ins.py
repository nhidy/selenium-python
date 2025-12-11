import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_level=9
currency_code='MMK'
account_number='003101010777777701'
account_name='GL Test (MMK)'
short_account_name='GL Test (MMK)'
branch_code='003'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ACT_ACCHRT_INS
class Test_SP_ACT_ACCHRT_INS(object):

    def test_sp_act_acchrt_ins_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.ACT_ACCHRT_INS(
            account_level=account_level,
            currency_code=currency_code,
            account_number=account_number,
            account_name=account_name,
            short_account_name=short_account_name,
            branch_code=branch_code
        )
        rs = sp_helper.ACT_ACCHRT_INS(fields_data)
        step_code = 'SQL_INSERT_ACCHRT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"