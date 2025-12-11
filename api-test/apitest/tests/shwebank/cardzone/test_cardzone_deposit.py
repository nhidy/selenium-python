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

@pytest.mark.cardzonedeposit
class TestCardzoneDeposit(object):

    @pytest.mark.DPT_MDP_ATM_DPT_CZ
    def test_001_DPT_MDP_ATM_DPT_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_ATM_DPT_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_ATM_DPT_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MDP_ATM_IBFT2_BNB_CZ
    def test_002_DPT_MDP_ATM_IBFT2_BNB_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_ATM_IBFT2_BNB_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_ATM_IBFT2_BNB_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MDP_POS_VOID_ONUS_CZ
    def test_003_DPT_MDP_POS_VOID_ONUS_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_POS_VOID_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_POS_VOID_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MDP_POS_VOID_OFF_CZ
    def test_004_DPT_MDP_POS_VOID_OFF_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_POS_VOID_OFF_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_POS_VOID_OFF_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MDP_MINI_WDR_OFF_CZ
    def test_005_DPT_MDP_MINI_WDR_OFF_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_MINI_WDR_OFF_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_MINI_WDR_OFF_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MDP_MINI_CLS_WDR_CZ
    def test_006_DPT_MDP_MINI_CLS_WDR_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MDP_MINI_CLS_WDR_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MDP_MINI_CLS_WDR_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_ECOM_VOID_ONUS_CZ
    def test_007_DPT_MWR_ECOM_VOID_ONUS_CZ(self, user):
        # data test
        account_number='210029217168'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ECOM_VOID_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ECOM_VOID_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'