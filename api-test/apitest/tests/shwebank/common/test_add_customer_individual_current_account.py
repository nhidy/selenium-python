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
working_date='2022-12-09' 
hocifcd=''
# customer_private_enterprise='E'
customer_private_individual='I'
title='01'
title_of_organization=''
suffix=''
firstname='FIRST'
lastname='LAST'
midname=''
# fullname_enterprise='TEST AUTO Enterprise '
fullname_individual='TEST AUTO Individual '
firstname_local=''
lastname_local=''
midname_local=''
shortname=''
gender='01'
date_of_birth=datetime.fromisoformat('1992-02-25').strftime('%Y-%m-%dT%H:%M:%S')
place_of_birth='Place of birth (pob)'
nation='KH'
country='VN'
paper_type='I'
# paper_number_enterprise='0412'+ str(random_num)
paper_number_individual='I0313'+ str(random_num)
issue_date_of_paper=datetime.fromisoformat('2022-03-21').strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_paper='id place sd'
expire_date_of_paper=datetime.fromisoformat('2023-03-22').strftime('%Y-%m-%dT%H:%M:%S')
paper_type_sub=''
paper_number_sub=''
issue_date_of_sub_paper=datetime.fromisoformat('2024-03-25').strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_sub_paper=''
customer_group_type=''
customer_sub_group_type=''
categories='C1'
sector='AX'
subsector='AXA'
resident='R'
line1='04'
line2='04040401'
line3='040404'
line4='0404'
line5='27'
phone_home=''
phone_mobile=''
email=''
education=''
marital_status=''
profession=''
business_type=''
financial=''
isic_code=''
managing_branch_code='848'
customer_status='P'
classify='N'
polists='N'
repolists='N'
country_of_income='MM'
fatca_status='N'
government_id=''
international_id=''
oversea_juristic_id=''
gfmis_code='98'
branch_code='848'
group_code=''
customer_credit_line=40000000005.96
currency_code_mmk='MMK'
customer_sub_type='I'
father_name='FAR'
description_ctm_apr='Approve customer'


# data open current deposit MMK
catalog_code_current_deposit='CAMMK0000'
catalog_name_current_deposit='Current account in MMK'
deposit_type_current_deposit='Current'
deposit_purpose_current_deposit='P'
account_type_current_deposit='1'
account_name_current_deposit_mmk_01='DPT 1 current AUTO MMK '
account_name_current_deposit_mmk_02='DPT 2 current AUTO MMK '
rollover_current_deposit='N'
auto_transfer_option_current_deposit='N'
business_purpose_code=''
customer_type='C'
description_dpt_opn='1100: Open new deposit account'

# data open current deposit USD
catalog_code_current_deposit_usd='CAUSD0000'
catalog_name_current_deposit_usd='Current account in USD'
deposit_type_current_deposit='Current'
deposit_purpose_current_deposit='P'
account_type_current_deposit='1'
account_name_current_deposit_usd_01='DPT 1 current AUTO USD '
rollover_current_deposit='N'
auto_transfer_option_current_deposit='N'
business_purpose_code=''
customer_type='C'
description_dpt_opn='1100: Open new deposit account'
currency_code_usd='USD'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data cash deposit
amount_deposit=10000000.05
exchange_rate=1
deposit_type_cash='T'
description_dpt_cdp='1110: Cash deposit'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user5']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.add_customer_individual_current_account
class TestAddCustomerIndividualCurrentAccount(object):

    @pytest.mark.open_deposit_account
    def test_001_open_deposit_account(self, user):
        helper_bo_ctm = CustomerSingleHelper(user)
        helper_fo_ctm = CustomerFOHelper(user)
        helper_fo_dpt = DepositFOHelper(user)
        i = 21
        while i < 26:
            # add individual customer
            global id_individual_new, customer_code_individual_new
            id_individual_new = 0
            customer_code_individual_new = ''
            fields_data_individual = customer_single_payload.add(
                hocifcd=hocifcd,
                customer_private=customer_private_individual,
                title=title,
                title_of_organization=title_of_organization,
                suffix=suffix,
                firstname=firstname,
                lastname=lastname,
                midname=midname,
                fullname=fullname_individual + str(i),
                firstname_local=firstname_local,
                lastname_local=lastname_local,
                midname_local=midname_local,
                shortname=shortname,
                gender=gender,
                date_of_birth=date_of_birth,
                place_of_birth=place_of_birth,
                nation=nation,
                country=country,
                paper_type=paper_type,
                paper_number=paper_number_individual + str(i),
                issue_date_of_paper=issue_date_of_paper,
                issue_place_of_paper=issue_place_of_paper,
                expire_date_of_paper=expire_date_of_paper,
                paper_type_sub=paper_type_sub,
                paper_number_sub=paper_number_sub,
                issue_date_of_sub_paper=issue_date_of_sub_paper,
                issue_place_of_sub_paper=issue_place_of_sub_paper,
                customer_group_type=customer_group_type,
                customer_sub_group_type=customer_sub_group_type,
                categories=categories,
                sector=sector,
                subsector=subsector,
                resident=resident,
                line1=line1,
                line2=line2,
                line3=line3,
                line4=line4,
                line5=line5,
                phone_home=phone_home,
                phone_mobile=phone_mobile,
                email=email,
                education=education,
                marital_status=marital_status,
                profession=profession,
                business_type=business_type,
                financial=financial,
                isic_code=isic_code,
                managing_branch_code=managing_branch_code,
                customer_status=customer_status,
                classify=classify,
                polists=polists,
                repolists=repolists,
                country_of_income=country_of_income,
                fatca_status=fatca_status,
                government_id=government_id,
                international_id=international_id,
                oversea_juristic_id=oversea_juristic_id,
                gfmis_code=gfmis_code,
                branch_code=branch_code,
                group_code=group_code,
                customer_credit_line=customer_credit_line,
                currency_code=currency_code_mmk,
                customer_sub_type=customer_sub_type,
                father_name=father_name
            )
            rs = helper_bo_ctm.SQL_INSERT_CTM(fields_data_individual)
            try:
                assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                id_individual_new = rs['id']
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                customer_code_individual_new = rs['customer_code']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # approve individual customer
            fields_data_approve_individual = customer_fo_payload.ctm_apr(
                customer_code=customer_code_individual_new,
                customer_name=fullname_individual + str(i),
                customer_status=customer_status,
                description=description_ctm_apr
            )
            try:
                rs = helper_fo_ctm.CTM_APR(fields_data_approve_individual)
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
            time.sleep(65)
            # open current deposit account 01 MMK
            global account_number_new_current_deposit_01
            account_number_new_current_deposit_01 = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_current_deposit,
                catalog_name=catalog_name_current_deposit,
                deposit_type=deposit_type_current_deposit,
                deposit_purpose=deposit_purpose_current_deposit,
                account_type=account_type_current_deposit,
                account_name=account_name_current_deposit_mmk_01 + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_current_deposit,
                auto_transfer_option=auto_transfer_option_current_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_current_deposit_01 = rs['account_number']
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_OPN: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve current deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_current_deposit_01,
                account_holder_name=account_name_current_deposit_mmk_01,
                description=description_dpt_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_APR: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            time.sleep(65)
            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_current_deposit_01,
                amount_deposit=amount_deposit,
                amount=amount_deposit,
                currency_deposit=currency_code_mmk,
                values_date=working_date,
                customer_code=customer_code_individual_new,
                cash_amount_bcy=amount_deposit,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit,
                cash_currency=currency_code_mmk,
                account_name=account_name_current_deposit_mmk_01,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_CDP: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # open current deposit account MMK 02
            global account_number_new_current_deposit_02
            account_number_new_current_deposit_02 = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_current_deposit,
                catalog_name=catalog_name_current_deposit,
                deposit_type=deposit_type_current_deposit,
                deposit_purpose=deposit_purpose_current_deposit,
                account_type=account_type_current_deposit,
                account_name=account_name_current_deposit_mmk_02 + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_current_deposit,
                auto_transfer_option=auto_transfer_option_current_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_current_deposit_02 = rs['account_number']
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_OPN: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve current deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_current_deposit_02,
                account_holder_name=account_name_current_deposit_mmk_02,
                description=description_dpt_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_APR: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            time.sleep(65)
            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_current_deposit_02,
                amount_deposit=amount_deposit,
                amount=amount_deposit,
                currency_deposit=currency_code_mmk,
                values_date=working_date,
                customer_code=customer_code_individual_new,
                cash_amount_bcy=amount_deposit,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit,
                cash_currency=currency_code_mmk,
                account_name=account_name_current_deposit_mmk_02,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_CDP: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            

            # open current deposit account 01 USD
            global account_number_new_current_deposit_usd_01
            account_number_new_current_deposit_usd_01 = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_current_deposit_usd,
                catalog_name=catalog_name_current_deposit_usd,
                deposit_type=deposit_type_current_deposit,
                deposit_purpose=deposit_purpose_current_deposit,
                account_type=account_type_current_deposit,
                account_name=account_name_current_deposit_usd_01 + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_current_deposit,
                auto_transfer_option=auto_transfer_option_current_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_current_deposit_usd_01 = rs['account_number']
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_OPN: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve current deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_current_deposit_usd_01,
                account_holder_name=account_name_current_deposit_usd_01,
                description=description_dpt_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_APR: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            time.sleep(65)
            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_current_deposit_usd_01,
                amount_deposit=amount_deposit,
                amount=amount_deposit,
                currency_deposit=currency_code_usd,
                values_date=working_date,
                customer_code=customer_code_individual_new,
                cash_amount_bcy=amount_deposit,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit,
                cash_currency=currency_code_usd,
                account_name=account_name_current_deposit_usd_01,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_CDP: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            i += 1