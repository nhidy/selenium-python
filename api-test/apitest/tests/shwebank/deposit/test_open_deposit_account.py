import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.deposit.deposit_fo_helpers import DepositFOHelper
from apitest.src.payloads.deposit.deposit_fo_payload import DepositFOPayload

deposit_fo_payload = DepositFOPayload()

from apitest.src.helpers.deposit.deposit_account_helpers import DepositAccountHelper
from apitest.src.payloads.deposit.deposit_account_payload import DepositAccountPayload

deposit_account_payload = DepositAccountPayload()

#  data open deposit
account_number=""
customer_type="C"
customer_code="11000013"
catalog_code="CAKHR000"
catalog_name="Current account in KHR"
deposit_type="C"
master_fd_account=""
deposit_purpose="C"
account_type="14"
seq_number=None
account_name="DPT ACC 080822 AUTO "
business_purpose_code="A011130"
rollover="A"
auto_transfer_option="N"
to_account_number=""
description="1100: Open new deposit account"

# data modify deposit
account_name_update="DPT 080822 AUTO update "
business_purpose_code_update="P"
minimum_deposit_amount_update=20
initial_deposit_amount_update=30
interest_tenor_update=2
interest_tenor_unit_update="M"
minimum_tenor_update=0
minimum_tenor_unit_update="Y"
multiple_deposit_allow_update="Y"
multiple_withdrawal_allow_update="Y"
early_withdrawal_update="N"
minimum_tenor_allow_early_withdrawal_update=0
minimum_tenor_allow_early_withdrawal_unit_update="Y"
credit_interest_update="Y"
credit_interest_tenor_update=2
credit_interest_tenor_unit_update="Y"
crediting_interest_update=1
dormant_period_update=900
dormant_period_unit_update="Y"
rollover_update="Y"
interest_due_on_holiday_update=10
principal_due_on_holiday_update=10
statement_tenor_update=10
statement_tenor_unit_update="D"
statement_format_update="E"
module_code_update="DPT"
list_ifc_balance_update=[
    {
        "module_code": "DPT",
        "ifc_code": 10,
        "value_base": "I",
        "ifc_value": 10.67,
        "margin_value": 6.54,
        "amount": 30.54,
        "paid": 20.34,
        "ifc_status": "B",
        "last_datetime": "2022-04-13",
        "amtpbl": 50.34
    }
]

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user3']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_deposit_account
class TestOpenDepositAccount(object):

    @pytest.mark.open_deposit_account
    def test_001_open_deposit_account(self, user):
        helper_fo = DepositFOHelper(user)
        helper_bo = DepositAccountHelper(user)
        i = 3024
        while i < 5015:
            global id_new, account_number_new, account_number_def_new
            id_new = 0
            account_number_new = ''
            account_number_def_new = ''
            # open deposit account 
            fields_data = deposit_fo_payload.dpt_opn(
                account_number=account_number,
                customer_type=customer_type,
                customer_code=customer_code,
                catalog_code=catalog_code,
                catalog_name=catalog_name,
                deposit_type=deposit_type,
                master_fd_account=master_fd_account,
                deposit_purpose=deposit_purpose,
                account_type=account_type,
                seq_number=seq_number,
                account_name=account_name + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover,
                auto_transfer_option=auto_transfer_option,
                to_account_number=to_account_number,
                description=description
            )
            try:
                rs = helper_fo.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new = rs['account_number']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # simple search by account_number
            fields_data = deposit_account_payload.simple_search(
                search_text=account_number_new
            )
            try:
                rs = helper_bo.DPT_SEARCH_DEPOSIT(fields_data)
                assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                if len(rs['items']) > 0:
                    assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                    id_new = rs['items'][0]['id']
                    print('id_new ' + str(i) + ': ', id_new)
                    assert 'account_number_def' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                    account_number_def_new = rs['items'][0]['account_number_def']
                    print('account_number_def_new ' + str(i) + ': ', account_number_def_new)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # modify deposit account
            fields_data = deposit_account_payload.update(
                id=id_new,
                account_name=account_name_update + str(i),
                business_purpose_code=business_purpose_code_update,
                minimum_deposit_amount=minimum_deposit_amount_update,
                initial_deposit_amount=initial_deposit_amount_update,
                interest_tenor=interest_tenor_update,
                interest_tenor_unit=interest_tenor_unit_update,
                minimum_tenor=minimum_tenor_update,
                minimum_tenor_unit=minimum_tenor_unit_update,
                multiple_deposit_allow=multiple_deposit_allow_update,
                multiple_withdrawal_allow=multiple_withdrawal_allow_update,
                early_withdrawal=early_withdrawal_update,
                minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_update,
                minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_update,
                credit_interest=credit_interest_update,
                credit_interest_tenor=credit_interest_tenor_update,
                credit_interest_tenor_unit=credit_interest_tenor_unit_update,
                crediting_interest=crediting_interest_update,
                dormant_period=dormant_period_update,
                dormant_period_unit=dormant_period_unit_update,
                rollover=rollover_update,
                interest_due_on_holiday=interest_due_on_holiday_update,
                principal_due_on_holiday=principal_due_on_holiday_update,
                statement_tenor=statement_tenor_update,
                statement_tenor_unit=statement_tenor_unit_update,
                statement_format=statement_format_update,
                account_number_def=account_number_def_new,
                module_code=module_code_update,
                list_ifc_balance=list_ifc_balance_update
            )
            try:
                # print('fields_data update: ', fields_data)
                rs = helper_bo.DPT_UPDATE_DEPOSIT(fields_data)
                # print('Response Json:', rs)
                assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            i += 1