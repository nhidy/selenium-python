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
working_date='2023-04-02'
currency_code_mmk='MMK'
customer_code='11056818'

# data open current deposit
catalog_code_current_deposit='CAMMK0000'
catalog_name_current_deposit='Current account in MMK'
deposit_type_current_deposit='Current'
deposit_sub_type_current_deposit='C1'
deposit_purpose_current_deposit='P'
account_type_current_deposit='1'
account_name_current_deposit='test batch account linkage for FD -  FD Block ' + str(random_num)
rollover_current_deposit='N'
auto_transfer_option_current_deposit='N'
# data open fixed deposit
deposit_sub_type_fixed_3m_deposit='T2'
deposit_purpose_fixed_3m_deposit='S'
account_type_fixed_3m_deposit='1'
deposit_type_fixed_3m_deposit='Fixed Deposit'
# data open fixed deposit (no rollover)
catalog_code_fixed_3m_deposit_nr='FD03NRMMK'
catalog_name_fixed_3m_deposit_nr='Fixed deposit 3 months (No rollover) in MMK'
account_name_fixed_3m_deposit_nr='test rollover FD (NR) -  FD Block ' + str(random_num)
rollover_fixed_3m_deposit_nr='N'
auto_transfer_option_fixed_3m_deposit_nr='A'
# data open fixed deposit (principal only)
catalog_code_fixed_3m_deposit_po='FD03POMMK'
catalog_name_fixed_3m_deposit_po='Fixed deposit 3 months (Principal rollover only) in MMK'
account_name_fixed_3m_deposit_po='test rollover FD (PO) -  FD Block ' + str(random_num)
rollover_fixed_3m_deposit_po='P'
auto_transfer_option_fixed_3m_deposit_po='I'
# data open fixed deposit (principal + interest)
catalog_code_fixed_3m_deposit_pi='FD03PIMMK'
catalog_name_fixed_3m_deposit_pi='Fixed deposit 1 months (Principal plus interest rollover) in MMKS'
account_name_fixed_3m_deposit_pi='test rollover FD (PI) -  FD Block ' + str(random_num)
rollover_fixed_3m_deposit_pi='A'
auto_transfer_option_fixed_3m_deposit_pi='N'


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
amount_deposit_fixed=3500000
exchange_rate=1
deposit_type_cash_fixed='T'
description_dpt_cdp='1110: Cash deposit'

# data block
block_reason='R2'
description_dpt_blk='11840: Block account'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user4']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_deposit_account_for_batch
class TestOpenDepositAccountForBatch(object):

    @pytest.mark.open_deposit_account
    def test_007_open_deposit_account_fd_007(self, user):
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

        # open fixed deposit account (no rollover)
        global account_number_new_fixed_3m_deposit_nr
        account_number_new_fixed_3m_deposit_nr = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit_nr,
            catalog_name=catalog_name_fixed_3m_deposit_nr,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit_nr,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit_nr,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit_nr,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_nr = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account (no rollover)
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_nr,
            account_holder_name=account_name_fixed_3m_deposit_nr,
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
            account_number=account_number_new_fixed_3m_deposit_nr,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit_nr,
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

        # open fixed deposit account (principal only)
        global account_number_new_fixed_3m_deposit_po
        account_number_new_fixed_3m_deposit_po = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit_po,
            catalog_name=catalog_name_fixed_3m_deposit_po,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit_po,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit_po,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit_po,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_po = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account (principal only)
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_po,
            account_holder_name=account_name_fixed_3m_deposit_po,
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
            account_number=account_number_new_fixed_3m_deposit_po,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit_po,
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

        # open fixed deposit account (prinicpal + interest)
        global account_number_new_fixed_3m_deposit_pi
        account_number_new_fixed_3m_deposit_pi = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_fixed_3m_deposit_pi,
            catalog_name=catalog_name_fixed_3m_deposit_pi,
            deposit_type=deposit_type_fixed_3m_deposit,
            deposit_sub_type=deposit_sub_type_fixed_3m_deposit,
            deposit_purpose=deposit_purpose_fixed_3m_deposit,
            account_type=account_type_fixed_3m_deposit,
            account_name=account_name_fixed_3m_deposit_pi,
            business_purpose_code=business_purpose_code,
            rollover=rollover_fixed_3m_deposit_pi,
            auto_transfer_option=auto_transfer_option_fixed_3m_deposit_pi,
            to_account_number=account_number_new_current_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            step_code = 'DPT_OPN'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            account_number_new_fixed_3m_deposit_pi = data_actual['data']['account_number']
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # account_number_new_fixed_3m_deposit = rs['account_number']
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account (prinicpal + interest)
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_fixed_3m_deposit_pi,
            account_holder_name=account_name_fixed_3m_deposit_pi,
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
            account_number=account_number_new_fixed_3m_deposit_pi,
            amount_deposit=amount_deposit_fixed,
            amount=amount_deposit_fixed,
            currency_deposit=currency_code_mmk,
            values_date=working_date,
            customer_code=customer_code,
            cash_amount_bcy=amount_deposit_fixed,
            cash_exchange_rate=exchange_rate,
            cash_amount=amount_deposit_fixed,
            cash_currency=currency_code_mmk,
            account_name=account_name_fixed_3m_deposit_pi,
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

        # block FD account (no rollover)
        fields_data = deposit_fo_payload.dpt_blk(
            account_number=account_number_new_fixed_3m_deposit_nr,
            depositor_name=account_name_fixed_3m_deposit_nr,
            depositor_id=customer_code,
            depositor_balance=amount_deposit_fixed,
            depositor_currency=currency_code_mmk,
            block_reason=block_reason,
            value_date=working_date,
            description=description_dpt_blk
        )
        try:
            rs = helper_fo_dpt.DPT_BLK(fields_data)
            step_code = 'DPT_BLK'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_BLK: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # block FD account (principal only)
        fields_data = deposit_fo_payload.dpt_blk(
            account_number=account_number_new_fixed_3m_deposit_po,
            depositor_name=account_name_fixed_3m_deposit_po,
            depositor_id=customer_code,
            depositor_balance=amount_deposit_fixed,
            depositor_currency=currency_code_mmk,
            block_reason=block_reason,
            value_date=working_date,
            description=description_dpt_blk
        )
        try:
            rs = helper_fo_dpt.DPT_BLK(fields_data)
            step_code = 'DPT_BLK'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_BLK: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # block FD account (principal + interest)
        fields_data = deposit_fo_payload.dpt_blk(
            account_number=account_number_new_fixed_3m_deposit_pi,
            depositor_name=account_name_fixed_3m_deposit_pi,
            depositor_id=customer_code,
            depositor_balance=amount_deposit_fixed,
            depositor_currency=currency_code_mmk,
            block_reason=block_reason,
            value_date=working_date,
            description=description_dpt_blk
        )
        try:
            rs = helper_fo_dpt.DPT_BLK(fields_data)
            step_code = 'DPT_BLK'
            data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
            print(json.dumps(data_actual, indent=4, sort_keys=False))
            transaction_number = data_actual['data']['transaction_number']

            # assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_BLK: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'