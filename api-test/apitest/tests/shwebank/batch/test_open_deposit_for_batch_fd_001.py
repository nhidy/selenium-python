from datetime import datetime
import json
import random
import pytest
import time

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility

from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
from apitest.src.helpers.customer.customer_fo_helpers import CustomerFOHelper
from apitest.src.payloads.customer.customer_fo_payload import CustomerFOPayload
customer_single_payload = CustomerSinglePayload()
customer_fo_payload = CustomerFOPayload()
from apitest.src.helpers.deposit.deposit_fo_helpers import DepositFOHelper
from apitest.src.payloads.deposit.deposit_fo_payload import DepositFOPayload
from apitest.src.helpers.deposit.deposit_account_helpers import DepositAccountHelper
from apitest.src.payloads.deposit.deposit_account_payload import DepositAccountPayload
deposit_account_payload = DepositAccountPayload()
deposit_fo_payload = DepositFOPayload()

# customer
random_num=random.randrange(100, 100000)
working_date='2023-10-05'
currency_code_mmk='MMK'
customer_code='11000001'

# data open current deposit
catalog_code_current_deposit='CAMMK0000'
catalog_name_current_deposit='Current account in MMK'
deposit_type_current_deposit='Current'
deposit_sub_type_current_deposit='C1'
deposit_purpose_current_deposit='P'
account_type_current_deposit='1'
account_name_current_deposit='test 09/01/2025 batch account linkage for FD no rollover ' + str(random_num)
rollover_current_deposit='N'
auto_transfer_option_current_deposit='N'
# data open fixed deposit
catalog_code_fixed_3m_deposit='FD03NRMMK'
catalog_name_fixed_3m_deposit='Fixed deposit 3 months (No rollover) in MMK'
deposit_type_fixed_3m_deposit='Fixed Deposit'
deposit_sub_type_fixed_3m_deposit='T2'
deposit_purpose_fixed_3m_deposit='S'
account_type_fixed_3m_deposit='1'
account_name_fixed_3m_deposit='test 09/01/2025 batch FD 3M ' + str(random_num)
rollover_fixed_3m_deposit='N'
auto_transfer_option_fixed_3m_deposit='A'

business_purpose_code=''
customer_type='C'
description_dpt_opn='1100: Open new deposit account'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data cash deposit current
amount_deposit_current=100000
exchange_rate=1
deposit_type_cash_current='C'
description_dpt_cdp='1110: Cash deposit'

# data cash deposit fixed
amount_deposit_fixed=15000000
exchange_rate=1
deposit_type_cash_fixed='T'
description_dpt_cdp='1110: Cash deposit'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user5']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_deposit_account_for_batch
class TestOpenDepositAccountForBatch(object):

    @pytest.mark.open_deposit_account
    def test_001_open_deposit_account_fd_001(self, user):
        helper_fo_dpt = DepositFOHelper(user)
        # open current deposit account 
        global account_number_new_current_deposit
        account_number_new_current_deposit = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_current_deposit,
            catalog_name=catalog_name_current_deposit,
            deposit_type=deposit_type_current_deposit,
            deposit_sub_type=deposit_sub_type_current_deposit,
            deposit_purpose=deposit_purpose_current_deposit,
            account_type=account_type_current_deposit,
            account_name=account_name_current_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_current_deposit,
            auto_transfer_option=auto_transfer_option_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_current_deposit = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_current_deposit = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve current deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_current_deposit,
            account_holder_name=account_name_current_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_current_deposit,
            amount_deposit=amount_deposit_current,
            amount=amount_deposit_current,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_current,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_current,
            cash_currency=currency_code_mmk,
            account_name=account_name_current_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_current,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # open fixed deposit account 1
        global account_number_new_fixed_3m_deposit_001
        account_number_new_fixed_3m_deposit_001 = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit,
            catalog_name=catalog_name_fixed_3m_deposit,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_001 = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit_001 = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_001,
            account_holder_name=account_name_fixed_3m_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_fixed_3m_deposit_001,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_fixed,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # open fixed deposit account 2
        global account_number_new_fixed_3m_deposit_002
        account_number_new_fixed_3m_deposit_002 = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit,
            catalog_name=catalog_name_fixed_3m_deposit,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_002 = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit_002 = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_002,
            account_holder_name=account_name_fixed_3m_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_fixed_3m_deposit_002,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_fixed,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # open fixed deposit account 3
        global account_number_new_fixed_3m_deposit_003
        account_number_new_fixed_3m_deposit_003 = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit,
            catalog_name=catalog_name_fixed_3m_deposit,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_003 = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit_003 = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_003,
            account_holder_name=account_name_fixed_3m_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_fixed_3m_deposit_003,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_fixed,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # open fixed deposit account 4
        global account_number_new_fixed_3m_deposit_004
        account_number_new_fixed_3m_deposit_004 = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit,
            catalog_name=catalog_name_fixed_3m_deposit,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_004 = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit_004 = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_004,
            account_holder_name=account_name_fixed_3m_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_fixed_3m_deposit_004,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_fixed,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # open fixed deposit account 5
        global account_number_new_fixed_3m_deposit_005
        account_number_new_fixed_3m_deposit_005 = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit,
            catalog_name=catalog_name_fixed_3m_deposit,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_005 = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit_005 = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_005,
            account_holder_name=account_name_fixed_3m_deposit,
            description=description_dpt_apr
        )
        try:
            rs = helper_fo_dpt.DPT_APR(fields_data)
            step_code = 'DPT_APR'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_APR: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # cash deposit
        fields_data = deposit_fo_payload.dpt_cdp(
            account_number=account_number_new_fixed_3m_deposit_005,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit,
            exchange_rate=exchange_rate,
            cross_rate=exchange_rate,
            deposit_type=deposit_type_cash_fixed,
            id_issue_date=working_date,
            description=description_dpt_cdp
        )
        try:
            rs = helper_fo_dpt.DPT_CDP(fields_data)
            step_code = 'DPT_CDP'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']
            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_CDP: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'