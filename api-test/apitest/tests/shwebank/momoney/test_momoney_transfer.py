import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.momoney.momoney_helpers import MomoneyHelper
from apitest.src.payloads.momoney.momoney_payload import MomoneyPayload

momoney_payload = MomoneyPayload()

@pytest.fixture(scope='session')
def user():
    user_momoney = USER_LOGIN['user11']
    req = RequestUtility(user_momoney)
    req.openapi_login_mo()
    return req

@pytest.mark.momoneytransfer
class TestMomoneyTransfer(object):

    @pytest.mark.DPT_TRF_MOMONEY
    def test_001_DPT_TRF_MOMONEY(self, user):
        # data test
        debit_account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        helper = MomoneyHelper(user)
        fields_data = momoney_payload.DPT_TRF_MOMONEY(
            debit_account_number=debit_account_number,
            credit_account_number=credit_account_number,
            amount=amount
        )
        rs = helper.DPT_TRF_MOMONEY(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_TRF_FEE_MOMONEY
    def test_002_DPT_TRF_FEE_MOMONEY(self, user):
        # data test
        debit_account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        fee1=100
        fee2=300
        helper = MomoneyHelper(user)
        fields_data = momoney_payload.DPT_TRF_FEE_MOMONEY(
            debit_account_number=debit_account_number,
            credit_account_number=credit_account_number,
            amount=amount,
            fee1=fee1,
            fee2=fee2
        )
        rs = helper.DPT_TRF_FEE_MOMONEY(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'