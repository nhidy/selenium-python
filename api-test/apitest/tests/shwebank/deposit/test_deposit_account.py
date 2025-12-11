import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.deposit.deposit_account_helpers import DepositAccountHelper
from apitest.src.payloads.deposit.deposit_account_payload import DepositAccountPayload

deposit_account_payload = DepositAccountPayload()

account_number_def_update="00999USDDPT00000081"
account_number_update="099999020000224"
account_name_update="DPT account test update"
business_purpose_code_update="P"
minimum_deposit_amount_update=100
initial_deposit_amount_update=10
interest_tenor_update=1
interest_tenor_unit_update="M"
minimum_tenor_update=0
minimum_tenor_unit_update="Y"
multiple_deposit_allow_update="Y"
multiple_withdrawal_allow_update="Y"
early_withdrawal_update="N"
minimum_tenor_allow_early_withdrawal_update=0
minimum_tenor_allow_early_withdrawal_unit_update="Y"
credit_interest_update="Y"
credit_interest_tenor_update=1
credit_interest_tenor_unit_update="M"
crediting_interest_update=0
dormant_period_update=100
dormant_period_unit_update="Y"
rollover_update="N"
branch_id_update=999

# check type number
number_checklist = {
    "branch_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "customer_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "catalog_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "deposit_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
     "tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tenor_2": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_tenor_allow_early_withdrawal": {
        "data_type": int,
        "number_of_digits": 0
    },
    "credit_interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "crediting_interest": {
        "data_type": int,
        "number_of_digits": 0
    },
    "intacrrt": {
        "data_type": int,
        "number_of_digits": 0
    },
    "dormant_period": {
        "data_type": int,
        "number_of_digits": 0
    },
    "rollover_to_catalog": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_due_on_holiday": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_due_on_holiday": {
        "data_type": int,
        "number_of_digits": 0
    },
    "statement_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tariff_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_created": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_approved": {
        "data_type": int,
        "number_of_digits": 0
    },
    "account_manager_staff_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "periodic": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_accrual": {
        "data_type": float,
        "number_of_digits": 3
    },
    "periodic_deposit_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "minimum_deposit_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "deposit_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "withdraw_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "current_balance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "icbal": {
        "data_type": float,
        "number_of_digits": 3
    },
    "month_average_balance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "quarter_average_balance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "semi_annual_average_balance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "year_average_balance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "interest_paid": {
        "data_type": float,
        "number_of_digits": 3
    },
    "intpre": {
        "data_type": float,
        "number_of_digits": 3
    },
    "intpbl": {
        "data_type": float,
        "number_of_digits": 3
    },
    "initial_deposit_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "interest_due": {
        "data_type": float,
        "number_of_digits": 3
    },
    "intovd": {
        "data_type": float,
        "number_of_digits": 3
    },
    "intspamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "interest_not_paid": {
        "data_type": float,
        "number_of_digits": 3
    },
    "inamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "examt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvbalance": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvmavgamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvqavgamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvhavgamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvyavgamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rintpaid": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rintpre": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintpbl": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintdue": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintovd": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintspamt": {
        "data_type": float,
        "number_of_digits": 3
    },
    "rvintnypd": {
        "data_type": float,
        "number_of_digits": 3
    },
    "earmark_book_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "week_debit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "week_credit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "month_debit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "month_credit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "quarter_debit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "quarter_credit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "semi_annual_debit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "semi_annual_credit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "year_debit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "year_credit": {
        "data_type": float,
        "number_of_digits": 3
    },
    "minimum_dormant_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text='test'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.deposit_account
class TestDepositAccount(object):


    @pytest.mark.simple_search_deposit_account
    def test_001_simple_search_deposit_account(self, user):
        global total_count
        helper = DepositAccountHelper(user)
        fields_data = deposit_account_payload.simple_search(
            page_size=5
        )
        rs = helper.DPT_SEARCH_DEPOSIT(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_deposit_account
    def test_002_advanced_search_deposit_account(self, user):
        helper = DepositAccountHelper(user)
        fields_data = deposit_account_payload.advanced_search(
            page_size=5
        )
        rs = helper.DPT_ADSEARCH_DEPOSIT(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    # @pytest.mark.update_deposit_account
    # def test_003_update_deposit_account(self, user):
    #     helper = DepositAccountHelper(user)
    #     id_new=1
    #     fields_data = deposit_account_payload.update(
    #         id=id_new,
    #         # account_number_def=account_number_def_update,
    #         account_number=account_number_update,
    #         account_name=account_name_update,
    #         business_purpose_code=business_purpose_code_update,
    #         minimum_deposit_amount=minimum_deposit_amount_update,
    #         initial_deposit_amount=initial_deposit_amount_update,
    #         interest_tenor=interest_tenor_update,
    #         interest_tenor_unit=interest_tenor_unit_update,
    #         minimum_tenor=minimum_tenor_update,
    #         minimum_tenor_unit=minimum_tenor_unit_update,
    #         multiple_deposit_allow=multiple_deposit_allow_update,
    #         multiple_withdrawal_allow=multiple_withdrawal_allow_update,
    #         early_withdrawal=early_withdrawal_update,
    #         minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_update,
    #         minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_update,
    #         credit_interest=credit_interest_update,
    #         credit_interest_tenor=credit_interest_tenor_update,
    #         credit_interest_tenor_unit=credit_interest_tenor_unit_update,
    #         crediting_interest=crediting_interest_update,
    #         dormant_period=dormant_period_update,
    #         dormant_period_unit=dormant_period_unit_update,
    #         rollover=rollover_update,
    #         branch_id=branch_id_update
    #     )
    #     rs = helper.DPT_UPDATE_DEPOSIT(fields_data)
    #     check_data_type(rs)
    #     assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     # assert account_number_def_update == rs['account_number_def'], f'Expected \'{account_number_def_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert account_number_update == rs['account_number'], f'Expected \'{account_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert business_purpose_code_update == rs['business_purpose_code'], f'Expected \'{business_purpose_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert minimum_deposit_amount_update == rs['minimum_deposit_amount'], f'Expected \'{minimum_deposit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert initial_deposit_amount_update == rs['initial_deposit_amount'], f'Expected \'{initial_deposit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert interest_tenor_update == rs['interest_tenor'], f'Expected \'{interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert interest_tenor_unit_update == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert minimum_tenor_update == rs['minimum_tenor'], f'Expected \'{minimum_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert minimum_tenor_unit_update == rs['minimum_tenor_unit'], f'Expected \'{minimum_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert multiple_deposit_allow_update == rs['multiple_deposit_allow'], f'Expected \'{multiple_deposit_allow_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert multiple_withdrawal_allow_update == rs['multiple_withdrawal_allow'], f'Expected \'{multiple_withdrawal_allow_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert early_withdrawal_update == rs['early_withdrawal'], f'Expected \'{early_withdrawal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert minimum_tenor_allow_early_withdrawal_update == rs['minimum_tenor_allow_early_withdrawal'], f'Expected \'{minimum_tenor_allow_early_withdrawal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert minimum_tenor_allow_early_withdrawal_unit_update == rs['minimum_tenor_allow_early_withdrawal_unit'], f'Expected \'{minimum_tenor_allow_early_withdrawal_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert credit_interest_update == rs['credit_interest'], f'Expected \'{credit_interest_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert credit_interest_tenor_update == rs['credit_interest_tenor'], f'Expected \'{credit_interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert credit_interest_tenor_unit_update == rs['credit_interest_tenor_unit'], f'Expected \'{credit_interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert crediting_interest_update == rs['crediting_interest'], f'Expected \'{crediting_interest_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert dormant_period_update == rs['dormant_period'], f'Expected \'{dormant_period_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert dormant_period_unit_update == rs['dormant_period_unit'], f'Expected \'{dormant_period_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert rollover_update == rs['rollover'], f'Expected \'{rollover_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert branch_id_update == rs['branch_id'], f'Expected \'{branch_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_deposit_account
    def test_004_view_deposit_account(self, user):
        helper = DepositAccountHelper(user)
        id_new = 1
        fields_data = deposit_account_payload.view_by_id(
            id=id_new
        )
        rs = helper.DPT_VIEW_DEPOSIT(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        # assert account_number_def_update == rs['account_number_def'], f'Expected \'{account_number_def_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # assert account_number_update == rs['account_number'], f'Expected \'{account_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # check total_count search all after view
        fields_data = deposit_account_payload.simple_search(
            page_size=50
        )
        rs = helper.DPT_SEARCH_DEPOSIT(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_deposit_account
    def test_005_delete_deposit_account(self, user):
        helper = DepositAccountHelper(user)
        id_new = 2
        fields_data = deposit_account_payload.delete_by_id(
            id=id_new
        )
        rs = helper.DPT_DELETE_DEPOSIT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = deposit_account_payload.simple_search(
                page_size=50
            )
            rs = helper.DPT_SEARCH_DEPOSIT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'