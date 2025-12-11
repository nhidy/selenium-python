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
from apitest.src.helpers.credit.credit_fo_helpers import CreditFOHelper
from apitest.src.payloads.credit.credit_fo_payload import CreditFOPayload
credit_fo_payload = CreditFOPayload()
from apitest.src.helpers.deposit.deposit_fo_helpers import DepositFOHelper
from apitest.src.payloads.deposit.deposit_fo_payload import DepositFOPayload
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
categories='C2'
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
branch_code='0848'
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

# data open product limit
product_limit_name='PL Non-shared (F) auto '
customer_type='C'
reference_number=''
limit_type='F'
limit_amount=1000000000.45
accounting_group=125
secure_type='N'
secure_rate=0
description_crd_plo='Open product limit'
exchange_rate=1.0
amount=1000000000.45

# data approve product limit
credit_limit=1000000000.45
product_status='p'
description_crd_pla='Approve product limit'

# data open sub product limit
sub_product_limit_name='SPL Non-shared (F) auto '
credit_facility='TL'
description_crd_splo='Open sub-product limit'

# data approve sub product limit
product_limit_status='P'
description_crd_spla='Approve sub product limit'

# data open credit account
catalog_code_fixed='TLUSDNLT01'
catalog_name_fixed='TERM LOAN_NON-REVOLVING_LONG TERM (USD)'
sub_product='R'
credit_classification='10'
account_name_fixed='Credit FIXED auto '
maximum_limit=1000000000.45
margin=1.05
from_date='2022-12-09'
to_date='2027-12-09'
principal_first_date='2023-01-09'
int_first_date='2023-01-09'
product_tenor_type='L'
business_purpose_code='A011120'
description_crd_opn='5500: Open new credit account'

# data approve credit account
description_crd_apr='5550: Approve credit account'

# data open current deposit
catalog_code_current_deposit='CAUSD000'
catalog_name_current_deposit='Current account in USD'
deposit_type_current_deposit='Current'
deposit_purpose_current_deposit='P'
account_type_current_deposit='1'
account_name_current_deposit='DPT current individual AUTO '
rollover_current_deposit='N'
auto_transfer_option_current_deposit='N'
business_purpose_code='A011130'
customer_type='C'
description_dpt_opn='1100: Open new deposit account'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data disbursement credit
disbursement_amount_deposit=1000000000.45
cross_rate=1.0
deposit_amount=1000000000.45
# exchange_rate=1.0
disbursement_amount_equivalent_in_bcy=1000000000.45
receiver_address='Chab Kab, Anlong Run, Thma Koul, Battambang'
amount=1000000000.45
exchange_rate_debit=1.0
repidtype='I'
description_crd_tdr='5523: Disbursement by transfer'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user6']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_credit_0848_fixed_usd
class TestOpenCredit0848FixedUsd(object):

    @pytest.mark.open_credit_0848_fixed_usd
    def test_001_open_credit_0848_fixed_usd(self, user):
        helper_bo_ctm = CustomerSingleHelper(user)
        helper_fo_ctm = CustomerFOHelper(user)
        helper_fo_crd = CreditFOHelper(user)
        helper_fo_dpt = DepositFOHelper(user)
        i = 1
        while i < 2:
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
                managing_branch_code=branch_code,
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

            time.sleep(60)
            # open product limit
            global product_limit_code_new
            product_limit_code_new = ''
            fields_data = credit_fo_payload.crd_plo(
                product_limit_name=product_limit_name + str(i),
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                reference_number=reference_number,
                limit_type=limit_type,
                currency_code=currency_code_usd,
                limit_amount=limit_amount,
                accounting_group=accounting_group,
                secure_type=secure_type,
                secure_rate=secure_rate,
                description=description_crd_plo,
                exchange_rate=exchange_rate,
                amount=amount
            )
            try:
                rs = helper_fo_crd.CRD_PLO(fields_data)
                assert 'product_limit_code' in rs, f'Key \"product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                product_limit_code_new = rs['product_limit_code']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # approve product limit
            fields_data = credit_fo_payload.crd_pla(
                product_limit_code=product_limit_code_new,
                product_limit_name=product_limit_name + str(i),
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                reference_number=reference_number,
                currency_code=currency_code_usd,
                credit_limit=credit_limit,
                limit_type=limit_type,
                product_status=product_status,
                description=description_crd_pla,
                customer_name=fullname_individual + str(i),
                amount=amount,
                exchange_rate=exchange_rate
            )
            try:
                rs = helper_fo_crd.CRD_PLA(fields_data)
                assert 'product_limit_code' in rs, f'Key \"product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # open sub product limit
            global sub_product_limit_code_new
            sub_product_limit_code_new = ''
            fields_data = credit_fo_payload.crd_splo(
                product_limit_code=product_limit_code_new,
                sub_product_limit_name=sub_product_limit_name + str(i),
                customer_type=customer_type,
                currency_code=currency_code_usd,
                reference_number=reference_number,
                customer_code=customer_code_individual_new,
                limit_amount=limit_amount,
                credit_facility=credit_facility,
                description=description_crd_splo,
                exchange_rate=exchange_rate,
                amount=amount
            )
            try:
                rs = helper_fo_crd.CRD_SPLO(fields_data)
                assert 'sub_product_limit_code' in rs, f'Key \"sub_product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                sub_product_limit_code_new = rs['sub_product_limit_code']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # aprove sub product limit
            fields_data = credit_fo_payload.crd_spla(
                sub_product_limit_code=sub_product_limit_code_new,
                sub_product_limit_name=sub_product_limit_name + str(i),
                customer_type=customer_type,
                reference_number=reference_number,
                customer_code=customer_code_individual_new,
                product_limit_code=product_limit_code_new,
                currency_code=currency_code_usd,
                credit_limit=credit_limit,
                product_limit_status=product_limit_status,
                description=description_crd_spla,
                amount=amount,
                exchange_rate=exchange_rate
            )
            try:
                rs = helper_fo_crd.CRD_SPLA(fields_data)
                assert 'sub_product_limit_code' in rs, f'Key \"sub_product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # open credit account
            global account_number_new_credit
            account_number_new_credit = ''
            fields_data = credit_fo_payload.crd_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                sub_product_limit_code=sub_product_limit_code_new,
                catalog_code=catalog_code_fixed,
                catalog_name=catalog_name_fixed,
                credit_facility=credit_facility,
                sub_product=sub_product,
                credit_classification=credit_classification,
                currency_code=currency_code_usd,
                account_holder_name=account_name_fixed + str(i),
                maximum_limit=maximum_limit,
                credit_limit=credit_limit,
                margin=margin,
                from_date=from_date,
                to_date=to_date,
                principal_first_date=principal_first_date,
                int_first_date=int_first_date,
                amount=amount,
                exchange_rate=exchange_rate,
                branch_code=branch_code,
                product_tenor_type=product_tenor_type,
                business_purpose_code=business_purpose_code,
                description=description_crd_opn
            )
            try:
                rs = helper_fo_crd.CRD_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_credit = rs['account_number']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve credit account
            fields_data = credit_fo_payload.crd_apr(
                account_number=account_number_new_credit,
                customer_type=customer_type,
                account_holder_name=account_name_fixed,
                catalog_code=catalog_code_fixed,
                catalog_name=catalog_name_fixed,
                currency_code=currency_code_usd,
                credit_limit=credit_limit,
                amount=amount,
                exchange_rate=exchange_rate,
                sub_product_limit_code=sub_product_limit_code_new,
                description=description_crd_apr
            )
            try:
                rs = helper_fo_crd.CRD_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # open current deposit account
            global account_number_new_current_deposit
            account_number_new_current_deposit = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code=customer_code_individual_new,
                catalog_code=catalog_code_current_deposit,
                catalog_name=catalog_name_current_deposit,
                deposit_type=deposit_type_current_deposit,
                deposit_purpose=deposit_purpose_current_deposit,
                account_type=account_type_current_deposit,
                account_name=account_name_current_deposit + str(i),
                business_purpose_code=business_purpose_code,
                rollover=rollover_current_deposit,
                auto_transfer_option=auto_transfer_option_current_deposit,
                description=description_dpt_opn
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_current_deposit = rs['account_number']
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
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            time.sleep(60)
            # disburement credit account by transfer
            fields_data = credit_fo_payload.crd_tdr(
                credit_account=account_number_new_credit,
                disbursement_amount_deposit=disbursement_amount_deposit,
                deposit_account=account_number_new_current_deposit,
                deposit_account_name=account_name_current_deposit + str(i),
                currency_code=currency_code_usd,
                cross_rate=cross_rate,
                deposit_amount=deposit_amount,
                exchange_rate=exchange_rate,
                disbursement_amount_equivalent_in_bcy=disbursement_amount_equivalent_in_bcy,
                receiver_name=fullname_individual + str(i),
                receiver_code=customer_code_individual_new,
                receiver_address=receiver_address,
                values_date=working_date,
                currency_of_credit_account=currency_code_usd,
                amount=amount,
                exchange_rate_debit=exchange_rate_debit,
                repidtype=repidtype,
                description=description_crd_tdr
            )
            try:
                rs = helper_fo_crd.CRD_TDR(fields_data)
                assert 'credit_account' in rs, f'Key \"credit_account\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            i += 1