import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_number='460022772776'
cerfiticate_serial='FR700001'
stock_prefix='FR'
description='11803: Fixed deposit receipt issued'
branch_name='002 - Yangon Head Office Branch'
account_number_for_fee='110034784963'
currency_code='MMK'
method='DPT'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_CER
class Test_SP_DPT_CER(object):

    def test_sp_dpt_cer_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fee_data = [
            {
                "share_fee": 0.0,
                "ifc_name": "Deposit (MMK) For Same Region  (By Cash/Tr)",
                "ifc_code": 340,
                "payrate": 100,
                "ifc_value": 150.0,
                "ifc_amount": 150.0,
                "currency_account_code": "MMK",
                "floor_value": 0.0,
                "ceiling_value": 0.0,
                "share_rate": 0.0,
                "share_amount": 0.0,
                "value_type": "F",
                "round_rate": 0.0,
                "round_amount": 0.0,
                "currency_fee_code": "MMK",
                "pay_source": "DPT"
            }
        ]
        fields_data = sp_payload.DPT_CER(
            account_number=account_number,
            cerfiticate_serial=cerfiticate_serial,
            stock_prefix=stock_prefix,
            description=description,
            fee_data=fee_data,
            branch_name=branch_name,
            account_number_for_fee=account_number_for_fee,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_CER(fields_data)
        step_code = 'DPT_CER'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"