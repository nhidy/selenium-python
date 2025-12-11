import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_name_debit='GL test paygate of digital'
account_name_credit='GL test trust account of digital'
debit_account_number='001101010666666602'
credit_account_number='004101010444444401'
debit_currency_code='USD'
credit_currency_code='MMK'
debit_rate=23400.0
cross_rate=23400.0
reverse_rate=4.274E-05
original_cross_rate=23400.0
credit_rate=1.0
debit_amount=5000.0
credit_amount=117000000.0
base_amount=117000000.0
fee_amount=700.0
receive_amount=116999300.0
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ACT_ACT
class Test_SP_ACT_ACT(object):

    def test_sp_act_act_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fee_data = [
            {
                "share_fee": 0.0,
                "ifc_name": "Communication Fee for Different Region (MMK)",
                "value_type": "F",
                "ifc_code": 307,
                "payrate": 100,
                "ifc_value": 700.0,
                "ifc_amount": 700.0,
                "currency_account_code": "MMK",
                "floor_value": 0.0,
                "ceiling_value": 0.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "MMK",
                "pay_source": "ACT"
            }
        ]
        fields_data = sp_payload.ACT_ACT(
            account_name_debit=account_name_debit,
            account_name_credit=account_name_credit,
            debit_account_number=debit_account_number,
            credit_account_number=credit_account_number,
            debit_currency_code=debit_currency_code,
            credit_currency_code=credit_currency_code,
            debit_rate=debit_rate,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            original_cross_rate=original_cross_rate,
            credit_rate=credit_rate,
            debit_amount=debit_amount,
            credit_amount=credit_amount,
            base_amount=base_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            fee_data=fee_data
        )
        rs = sp_helper.ACT_ACT(fields_data)
        step_code = 'ACT_ACT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"