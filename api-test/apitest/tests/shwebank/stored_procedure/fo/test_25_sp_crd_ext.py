import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
credit_account='110013219295'
credit_limit=10000000.0
oustanding_balance=8333333.33
old_expire_date='2024-01-24T00:00:00Z'
new_expire_date='2024-03-24T00:00:00Z'
creditor_name='Pham Thi Bich Ngoc'
creditor_code='11001411'
creditor_address='JITS, NHC, 22, BT, HCM'
description='5598: Extend credit account'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CRD_EXT
class Test_SP_CRD_EXT(object):

    def test_sp_crd_ext_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.CRD_EXT(
            credit_account=credit_account,
            credit_limit=credit_limit,
            oustanding_balance=oustanding_balance,
            old_expire_date=old_expire_date,
            new_expire_date=new_expire_date,
            creditor_name=creditor_name,
            creditor_code=creditor_code,
            creditor_address=creditor_address,
            description=description
        )
        rs = sp_helper.CRD_EXT(fields_data)
        step_code = 'CRD_EXT'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"