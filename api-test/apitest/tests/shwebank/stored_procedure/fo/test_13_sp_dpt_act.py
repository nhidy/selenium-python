import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_name_debit='TEST AUTO ADD PERSONAL'
account_name_credit='GL test paygate of digital'
debit_account_number='110030974696'
debit_currency_code='MMK'
credit_currency_code='USD'
debit_rate=1.0
cross_rate=4.274E-05
original_cross_rate=4.2735E-05
reverse_rate=23397.28591483
credit_rate=23400.0
debit_amount=5000000.0
credit_amount=213.68
base_amount=5000000.0
credit_account_number='001101010666666602'
fee_amount=52.14
receive_amount=161.54
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_ACT
class Test_SP_DPT_ACT(object):

    def test_sp_dpt_act_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fee_data = [
            {
                "share_fee": 0.0,
                "ifc_name": "Commission Fees-Bank Charges",
                "value_type": "P",
                "ifc_code": 354,
                "payrate": 100,
                "ifc_value": 1.0,
                "ifc_amount": 2.14,
                "currency_account_code": "USD",
                "floor_value": 0.0,
                "ceiling_value": 0.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "USD",
                "pay_source": "ACT"
            },
            {
                "share_fee": 0.0,
                "ifc_name": "Commission on Letter of Credit Issued (3 months)",
                "value_type": "P",
                "ifc_code": 355,
                "payrate": 100,
                "ifc_value": 0.25,
                "ifc_amount": 50.0,
                "currency_account_code": "USD",
                "floor_value": 50.0,
                "ceiling_value": 1500.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "USD",
                "pay_source": "ACT"
            }
        ]
        fields_data = sp_payload.DPT_ACT(
            account_name_debit=account_name_debit,
            account_name_credit=account_name_credit,
            debit_account_number=debit_account_number,
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
            credit_account_number=credit_account_number,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_ACT(fields_data)
        step_code = 'DPT_ACT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"