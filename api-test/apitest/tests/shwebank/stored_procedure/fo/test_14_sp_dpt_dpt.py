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
account_name_credit='TEST AUTO ADD PERSONAL'
debit_account_number='110030974696'
debit_currency_code='MMK'
credit_currency_code='MMK'
debit_rate=1.0
cross_rate=1.0
original_cross_rate=1.0
reverse_rate=1.0
credit_rate=1.0
debit_amount=200000.0
credit_amount=200000.0
base_amount=200000.0
credit_account_number='110029931105'
fee_amount=500.0
receive_amount=199500.0
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_DPT
class Test_SP_DPT_DPT(object):

    def test_sp_dpt_dpt_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fee_data = [
            {
                "share_fee": 0.0,
                "ifc_name": "Communication Fee for Different Region (MMK)",
                "value_type": "F",
                "ifc_code": 307,
                "payrate": 100,
                "ifc_value": 500.0,
                "ifc_amount": 500.0,
                "currency_account_code": "MMK",
                "floor_value": 0.0,
                "ceiling_value": 0.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "MMK",
                "pay_source": "DPT"
            }
        ]
        fields_data = sp_payload.DPT_DPT(
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
        rs = sp_helper.DPT_DPT(fields_data)
        step_code = 'DPT_DPT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"