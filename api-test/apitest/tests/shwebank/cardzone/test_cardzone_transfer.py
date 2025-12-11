import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.cardzone.cardzone_helpers import CardzoneHelper
from apitest.src.payloads.cardzone.cardzone_payload import CardzonePayload

cardzone_payload = CardzonePayload()

@pytest.fixture(scope='session')
def user():
    user_cardzone = USER_LOGIN['user10']
    req = RequestUtility(user_cardzone)
    req.openapi_login_cz()
    return req

@pytest.mark.cardzonetransfer
class TestCardzoneTransfer(object):

    @pytest.mark.DPT_TRF_MINI_WDR_ONUS_CZ
    def test_001_DPT_TRF_MINI_WDR_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_TRF_MINI_WDR_ONUS_CZ(
            account_number=account_number,
            credit_account_number=credit_account_number,
            amount=amount
        )
        rs = helper.DPT_TRF_MINI_WDR_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_TRF_ATM_IBFT_ONUS_CZ
    def test_002_DPT_TRF_ATM_IBFT_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_TRF_ATM_IBFT_ONUS_CZ(
            account_number=account_number,
            credit_account_number=credit_account_number,
            amount=amount
        )
        rs = helper.DPT_TRF_ATM_IBFT_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_TRF_ATM_IBFT1_CZ
    def test_003_DPT_TRF_ATM_IBFT1_CZ(self, user):
        # data test
        account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_TRF_ATM_IBFT1_CZ(
            account_number=account_number,
            credit_account_number=credit_account_number,
            amount=amount
        )
        rs = helper.DPT_TRF_ATM_IBFT1_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_TRF_MINI_DPT_CZ
    def test_004_DPT_TRF_MINI_DPT_CZ(self, user):
        # data test
        account_number='210030387638'
        credit_account_number='350047767896'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_TRF_MINI_DPT_CZ(
            account_number=account_number,
            credit_account_number=credit_account_number,
            amount=amount
        )
        rs = helper.DPT_TRF_MINI_DPT_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'
