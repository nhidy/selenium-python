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

@pytest.mark.cardzonewithdrawal
class TestCardzoneWithdrawal(object):

    @pytest.mark.DPT_MWR_ATM_WDR_ONUS_CZ
    def test_001_DPT_MWR_ATM_WDR_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ATM_WDR_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ATM_WDR_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_ATM_WDR_OFF_ISS_CZ
    def test_002_DPT_MWR_ATM_WDR_OFF_ISS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ATM_WDR_OFF_ISS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ATM_WDR_OFF_ISS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_ATM_IBFT2_ISS_CZ
    def test_003_DPT_MWR_ATM_IBFT2_ISS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ATM_IBFT2_ISS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ATM_IBFT2_ISS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_ATM_TOPUP_CZ
    def test_004_DPT_MWR_ATM_TOPUP_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ATM_TOPUP_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ATM_TOPUP_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_POS_SALE_ONUS_CZ
    def test_005_DPT_MWR_POS_SALE_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_POS_SALE_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_POS_SALE_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_POS_SALE_OFF_CZ
    def test_006_DPT_MWR_POS_SALE_OFF_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_POS_SALE_OFF_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_POS_SALE_OFF_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_POS_CAV_ONUS_CZ
    def test_007_DPT_MWR_POS_CAV_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_POS_CAV_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_POS_CAV_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_ECOM_SALE_ONUS_CZ
    def test_008_DPT_MWR_ECOM_SALE_ONUS_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_ECOM_SALE_ONUS_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_ECOM_SALE_ONUS_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'

    @pytest.mark.DPT_MWR_MINI_CLS_RES_CZ
    def test_009_DPT_MWR_MINI_CLS_RES_CZ(self, user):
        # data test
        account_number='210030387638'
        amount=10000.45
        helper = CardzoneHelper(user)
        fields_data = cardzone_payload.DPT_MWR_MINI_CLS_RES_CZ(
            account_number=account_number,
            amount=amount
        )
        rs = helper.DPT_MWR_MINI_CLS_RES_CZ(fields_data)
        rs_transaction_number = rs['transaction_number']
        print('transaction_number: ', rs_transaction_number)
        assert rs_transaction_number is not None, f'Expected transaction_number is NOT NULL, Actual response Json: {json.dumps(rs, indent=4, sort_keys=False)}'