import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
customer_code='11001699'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_PRINT_CUSTOMER_INFO
class Test_SP_PRINT_CUSTOMER_INFO(object):

    def test_sp_print_customer_info_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.PRINT_CUSTOMER_INFO(
            customer_code=customer_code
        )
        rs = sp_helper.PRINT_CUSTOMER_INFO(fields_data)
        step_code = 'VOUCHER'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"