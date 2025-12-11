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
gender=''
date_of_birth=datetime.fromisoformat('1992-02-25').strftime('%Y-%m-%dT%H:%M:%S')
place_of_birth='Place of birth (pob)'
nation='KH'
country='VN'
paper_type='I'
# paper_number_enterprise='0412'+ str(random_num)
paper_number_individual='0313'+ str(random_num)
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
address_local_legal='a lo'
province_legal=''
village_legal=''
sub_district_legal=''
district_legal=''
address_legal=''
zipcode_legal=''
address_local_contact=''
province_contact='04'
village_contact='04040401'
sub_district_contact='040404'
district_contact='0404'
address_contact='27'
zipcode_contact='z34'
address_local_normal=''
province_normal=''
village_normal=''
sub_district_normal=''
district_normal=''
address_normal=''
zipcode_normal=''
phone_home=''
phone_mobile=''
email=''
education=''
marital_status=''
profession='010101'
business_type='01010'
financial=''
isic_code=''
managing_branch_code='0848'
customer_status='P'
classify='N'
polists='N'
repolists='N'
country_of_income='AD'
fatca_status='N'
government_id=''
international_id=''
oversea_juristic_id=''
gfmis_code='98'
branchid=1
group_id=''
customer_credit_line=40000000005.96
currency_code_usd='USD'
description_ctm_apr='Approve customer'

# data open saving deposit
catalog_code_saving_deposit='SAKHR000'
catalog_name_saving_deposit='Saving account in KHR'
deposit_type_saving_deposit='Saving'
master_fd_account_saving_deposit=''
deposit_purpose_saving_deposit='P'
account_type_saving_deposit='1'
account_name_saving_deposit='DPT saving individual AUTO '
rollover_saving_deposit='N'
auto_transfer_option_saving_deposit='N'
to_account_number_saving_deposit=''
# data open fixed deposit
catalog_code_fixed_deposit='FD03MKHR'
catalog_name_fixed_deposit='Fixed deposit 3 months in KHR'
deposit_type_fixed_deposit='Fixed Deposit'
master_fd_account_fixed_deposit=''
deposit_purpose_fixed_deposit='S'
account_type_fixed_deposit='1'
account_name_fixed_deposit='DPT 3M individual AUTO '
rollover_fixed_deposit='P'
auto_transfer_option_fixed_deposit='I'
# to_account_number_fixed_deposit=''
# data open deposit
business_purpose_code='A011130'
customer_type='C'
seq_number=None
description_dpt_opn='1100: Open new deposit account'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data cash deposit
amount_deposit=1000000000.05
exchange_rate=1
deposit_type_cash='T'
currency_code_khr='KHR'
description_dpt_cdp='1110: Cash deposit'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user4']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_individual_deposit_account
class TestOpenIndividualDepositAccount(object):

    @pytest.mark.open_deposit_account
    def test_001_open_deposit_account(self, user):
        helper_bo_ctm = CustomerSingleHelper(user)
        helper_fo_ctm = CustomerFOHelper(user)
        helper_fo_dpt = DepositFOHelper(user)
        i = 108
        while i < 140:
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
                address_local_legal=address_local_legal,
                province_legal=province_legal,
                village_legal=village_legal,
                sub_district_legal=sub_district_legal,
                district_legal=district_legal,
                address_legal=address_legal,
                zipcode_legal=zipcode_legal,
                address_local_contact=address_local_contact,
                province_contact=province_contact,
                village_contact=village_contact,
                sub_district_contact=sub_district_contact,
                district_contact=district_contact,
                address_contact=address_contact,
                zipcode_contact=zipcode_contact,
                address_local_normal=address_local_normal,
                province_normal=province_normal,
                village_normal=village_normal,
                sub_district_normal=sub_district_normal,
                district_normal=district_normal,
                address_normal=address_normal,
                zipcode_normal=zipcode_normal,
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
                branchid=branchid,
                group_id=group_id,
                customer_credit_line=customer_credit_line,
                currency_code=currency_code_usd
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

            # open saving deposit account 
            global account_number_new_saving_deposit
            account_number_new_saving_deposit = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_saving_deposit,
                catalog_name=catalog_name_saving_deposit,
                deposit_type=deposit_type_saving_deposit,
                master_fd_account=master_fd_account_saving_deposit,
                deposit_purpose=deposit_purpose_saving_deposit,
                account_type=account_type_saving_deposit,
                seq_number=seq_number,
                account_name=account_name_saving_deposit + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_saving_deposit,
                auto_transfer_option=auto_transfer_option_saving_deposit,
                to_account_number=to_account_number_saving_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_saving_deposit = rs['account_number']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve saving deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_saving_deposit,
                account_holder_name=account_name_saving_deposit,
                description=description_ctm_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            time.sleep(60)
            # open fixed deposit account 
            global account_number_new_fixed_deposit
            account_number_new_fixed_deposit = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_fixed_deposit,
                catalog_name=catalog_name_fixed_deposit,
                deposit_type=deposit_type_fixed_deposit,
                master_fd_account=master_fd_account_fixed_deposit,
                deposit_purpose=deposit_purpose_fixed_deposit,
                account_type=account_type_fixed_deposit,
                seq_number=seq_number,
                account_name=account_name_fixed_deposit + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_fixed_deposit,
                auto_transfer_option=auto_transfer_option_fixed_deposit,
                to_account_number=account_number_new_saving_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_fixed_deposit = rs['account_number']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve fixed deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_fixed_deposit,
                account_holder_name=account_name_fixed_deposit,
                description=description_ctm_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_fixed_deposit,
                amount_deposit=amount_deposit,
                amount=amount_deposit,
                currency_deposit=currency_code_khr,
                values_date=working_date,
                customer_code=customer_code_individual_new,
                cash_amount_bcy=amount_deposit,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit,
                cash_currency=currency_code_khr,
                account_name=account_name_fixed_deposit,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            i += 1