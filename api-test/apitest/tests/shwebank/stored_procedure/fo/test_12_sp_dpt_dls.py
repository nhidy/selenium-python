import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
account_number='410038200852'
balance=486800.32
interest_accrual=0.0
interest_payable_receivable=0.0
interest_due=0.0
gross_interest_paid_out=0.0
interest_pre_calculate=0.0
penalty_fee=0.0
total_amount=0.0
another_deposit_account='110034784963'
depositor_name='TEST AUTO ADD PERSONAL'
depositor_id='11001572'
depositor_address='Home, Street, Ward, Township'
description='1190: Close deposit account by deposit'
currency_code='MMK'
ifc_code=0
sum_amount=486800.32
receive_currency='MMK'
accrual_interest_amount=0.0
balance_received=486800.32
branch_name='003 - Bayint Naung Branch'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_DLS
class Test_SP_DPT_DLS(object):

    def test_sp_dpt_dls_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_DLS(
            account_number=account_number,
            balance=balance,
            interest_accrual=interest_accrual,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            gross_interest_paid_out=gross_interest_paid_out,
            interest_pre_calculate=interest_pre_calculate,
            penalty_fee=penalty_fee,
            total_amount=total_amount,
            another_deposit_account=another_deposit_account,
            depositor_name=depositor_name,
            depositor_id=depositor_id,
            depositor_address=depositor_address,
            description=description,
            currency_code=currency_code,
            ifc_code=ifc_code,
            sum_amount=sum_amount,
            receive_currency=receive_currency,
            accrual_interest_amount=accrual_interest_amount,
            balance_received=balance_received,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_DLS(fields_data)
        step_code = 'DPT_DLS'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        
        assert '', f"Expected: ..., Actual: response Json:"