import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_number='110030974696'
from_date='2023-09-11T00:00:00Z'
to_date='2023-09-11T00:00:00Z'
description='1160: Transaction history inquiry'
branch_name='003 - Bayint Naung Branch'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_HIS
class Test_SP_DPT_HIS(object):

    def test_sp_dpt_his_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_HIS(
            account_number=account_number,
            from_date=from_date,
            to_date=to_date,
            description=description,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_HIS(fields_data)
        step_code = 'DPT_HIS'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"