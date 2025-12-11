import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_name='TEST AUTO ADD PERSONAL'
account_number='410038200852'
agent_hub_referral='BGO-GBG-AH'
id=6257
initial_deposit_amount=50000.0
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_UPDATE_DEPOSIT
class Test_SP_DPT_UPDATE_DEPOSIT(object):

    def test_sp_dpt_update_deposit_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        list_ifc_balance = [
            {
                "ifc_code": 114,
                "value_base": "A",
                "ifc_value": 9.0,
                "margin_value": 0.0,
                "ifc_status": "N",
                "amount": 0.0,
                "paid": 0.0,
                "amtpbl": 0.0,
                "basic_balance": 0.0,
                "prepaid_amount": 0.0,
                "module_code": "DPT",
                "last_datetime": "2023-09-11T00:00:00"
            }
        ]
        fields_data = sp_payload.DPT_UPDATE_DEPOSIT(
            account_name=account_name,
            account_number=account_number,
            agent_hub_referral=agent_hub_referral,
            id=id,
            initial_deposit_amount=initial_deposit_amount,
            list_ifc_balance=list_ifc_balance
        )
        rs = sp_helper.DPT_UPDATE_DEPOSIT(fields_data)
        step_code = 'DPT_UPDATE_DEPOSIT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"