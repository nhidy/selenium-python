import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_name_credit='GL test paygate of digital'
credit_account_number='001101010666666602'
debit_currency_code='MMK'
credit_currency_code='USD'
debit_rate=1.0
cross_rate=4.274E-05
original_cross_rate=4.2735E-05
reverse_rate=23397.28591483
credit_rate=23400.0
debit_amount=4000000.0
credit_amount=170.94
base_amount=4000000.0
fee_amount=1.71
receive_amount=169.23
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CSH_ACT
class Test_SP_CSH_ACT(object):

    def test_sp_csh_act_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fee_data = [
            {
                "share_fee": 0.0,
                "ifc_name": "Commission Fees-Bank Charges",
                "value_type": "P",
                "ifc_code": 354,
                "payrate": 100,
                "ifc_value": 1.0,
                "ifc_amount": 1.71,
                "currency_account_code": "USD",
                "floor_value": 0.0,
                "ceiling_value": 0.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "USD",
                "pay_source": "ACT"
            }
        ]
        fields_data = sp_payload.CSH_ACT(
            account_name_credit=account_name_credit,
            credit_account_number=credit_account_number,
            debit_currency_code=debit_currency_code,
            credit_currency_code=credit_currency_code,
            debit_rate=debit_rate,
            cross_rate=cross_rate,
            original_cross_rate=original_cross_rate,
            reverse_rate=reverse_rate,
            credit_rate=credit_rate,
            debit_amount=debit_amount,
            credit_amount=credit_amount,
            base_amount=base_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            fee_data=fee_data
        )
        rs = sp_helper.CSH_ACT(fields_data)
        step_code = 'CSH_ACT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"