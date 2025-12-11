import json
import pytest
import time

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.credit_fo_helpers import CreditFOHelper
from apitest.src.payloads.credit.credit_fo_payload import CreditFOPayload

credit_fo_payload = CreditFOPayload()

from apitest.src.helpers.credit.credit_account_helpers import CreditAccountHelper
from apitest.src.payloads.credit.credit_account_payload import CreditAccountPayload

credit_account_payload = CreditAccountPayload()

# data open product limit
product_limit_name="PL 080822 (F) auto "
customer_type="C"
customer_code="11000013"
reference_number=""
limit_type="F"
currency_code="USD"
limit_amount=100.45
accounting_group=121
secure_type="N"
secure_rate=0
description_crd_plo="Open product limit"
exchange_rate=1.0
amount=100.45

# data approve product limit
credit_limit=100.45
product_status="p"
description_crd_pla="Approve product limit"
customer_name=""

# data open sub product limit
product_limit_code_new="1100001312522"
sub_product_limit_name="SPL 080822 (F) auto "
credit_facility="TL"
description_crd_splo="Open sub-product limit"

# data approve sub product limit
product_limit_status="P"
description_crd_spla="Approve sub product limit"

# data open credit account
sub_product_limit_code_new="1100001312522131"
catalog_code="TLUSDNLT01"
catalog_name="TERM LOAN_NON-REVOLVING_LONG TERM (USD)"
sub_product="N"
credit_classification="02"
account_holder_name="Credit acc 080822 auto "
maximum_limit=200.45
margin=0.04
from_date="2022-10-05"
to_date="2023-10-05"
principal_first_date="2022-11-05"
int_first_date="2022-11-05"
branch_code="0848"
product_tenor_type="F"
business_purpose_code="A011120"
description_crd_opn="5500: Open new credit account"

# data approve credit account
description_crd_apr="5550: Approve credit account"
fee_data=[]

# data modify credit account
account_name_update="CRD 080822 AUTO update "
secure_type_update="N"
secure_rate_update=0
principal_tenor_update=2
principal_tenor_unit_update="M"
interest_tenor_update=2
interest_tenor_unit_update="M"
credit_purpose_update=""
disbursement_mode_update="R"
is_provision_update="Y"
restruct_update="A"
limit_from_third_party_update=0
operative_limit_from_third_party_update=0
interest_first_date_update="2022-04-02"
from_date_update="2022-03-02"
to_date_update="2023-03-02"
ranking_status_update="A"
staff_id_update=3
remark_update="abv"
reference_number_update="345231231"
is_restructured_update="Y"
principal_provision_rate_0_update=0
principal_provision_rate_1_update=0
principal_provision_rate_2_update=0
principal_provision_rate_3_update=0
principal_provision_rate_4_update=0
interest_provision_rate_0_update=0
interest_provision_rate_1_update=0
interest_provision_rate_2_update=0
interest_provision_rate_3_update=0
interest_provision_rate_4_update=0
business_purpose_code_update="D"
fine_tenor_update=0
fine_tenor_unit_update="D"
principal_grace_period_update=0
holiday_principal_due_on_update=0
interest_grace_period_update=0
holiday_interest_tenor_update=0
fine_grace_period_update=0
holiday_fine_tenor_update=0
discount_rate_update=0
re_discount_rate_update=0
module_code_update="CRD"
list_ifc_balance_update=[
    {
        "module_code": "CRD",
        "ifc_code": 5,
        "value_base": "I",
        "ifc_value": 0,
        "margin_value": 15.54,
        "amount": 20.67,
        "paid": 10.43,
        "ifc_status": "B",
        "last_datetime": "2022-04-13",
        "amtpbl": 10.22
    }
]
payment_list_update=[]
principal_list_update=[
	{
		"id": 1,
		"due_number": 1,
		"due_date": "2021-11-01",
		"amount": 408.160, 
		"paid_amount": 0.000
	},
	{
		"id": 3,
		"due_number": 2,
		"due_date": "2021-12-01",
		"amount": 407.160,
		"paid_amount": 0.000
	},
	{
		"id": 6,
		"due_number": 3,
		"due_date": "2021-12-31",
		"amount": 409.160,
		"paid_amount": 0.000
	},
	{
		"id": 7,
		"due_number": 4,
		"due_date": "2022-02-01",
		"amount": 308.160,
		"paid_amount": 0.000
	},
	{
		"id": 9,
		"due_number": 5,
		"due_date": "2022-03-01",
		"amount": 508.160,
		"paid_amount": 0.000
	},
	{
		"id": 12,
		"due_number": 6,
		"due_date": "2022-04-01",
		"amount": 408.160,
		"paid_amount": 0.000
	}
]


@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user4']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_credit_account
class TestOpenCreditAccount(object):

    @pytest.mark.open_credit_account
    def test_001_open_credit_account(self, user):
        helper_fo = CreditFOHelper(user)
        helper_bo = CreditAccountHelper(user)
        i = 3954
        while i < 5005:
            # open product limit
            # time.sleep(6)
            # global product_limit_code_new
            # product_limit_code_new = ''
            # fields_data = credit_fo_payload.crd_plo(
            #     product_limit_name=product_limit_name + str(i),
            #     customer_type=customer_type,
            #     customer_code=customer_code,
            #     reference_number=reference_number,
            #     limit_type=limit_type,
            #     currency_code=currency_code,
            #     limit_amount=limit_amount,
            #     accounting_group=accounting_group,
            #     secure_type=secure_type,
            #     secure_rate=secure_rate,
            #     description=description_crd_plo,
            #     exchange_rate=exchange_rate,
            #     amount=amount
            # )
            # try:
            #     rs = helper_fo.CRD_PLO(fields_data)
            #     assert 'product_limit_code' in rs, f'Key \"product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     product_limit_code_new = rs['product_limit_code']
            # except:
            #     assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # approve product limit
            # time.sleep(6)
            # fields_data = credit_fo_payload.crd_pla(
            #     product_limit_code=product_limit_code_new,
            #     product_limit_name=product_limit_name + str(i),
            #     customer_type=customer_type,
            #     customer_code=customer_code,
            #     reference_number=reference_number,
            #     currency_code=currency_code,
            #     credit_limit=credit_limit,
            #     limit_type=limit_type,
            #     product_status=product_status,
            #     description=description_crd_pla,
            #     customer_name=customer_name,
            #     amount=amount,
            #     exchange_rate=exchange_rate
            # )
            # try:
            #     rs = helper_fo.CRD_PLA(fields_data)
            #     assert 'product_limit_code' in rs, f'Key \"product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # except:
            #     assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # # open sub product limit
            # time.sleep(6)
            # global sub_product_limit_code_new
            # sub_product_limit_code_new = ''
            # fields_data = credit_fo_payload.crd_splo(
            #     product_limit_code=product_limit_code_new,
            #     sub_product_limit_name=sub_product_limit_name + str(i),
            #     customer_type=customer_type,
            #     currency_code=currency_code,
            #     reference_number=reference_number,
            #     customer_code=customer_code,
            #     limit_amount=limit_amount,
            #     credit_facility=credit_facility,
            #     description=description_crd_splo,
            #     exchange_rate=exchange_rate,
            #     amount=amount
            # )
            # try:
            #     rs = helper_fo.CRD_SPLO(fields_data)
            #     assert 'sub_product_limit_code' in rs, f'Key \"sub_product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     # sub_product_limit_code_new = rs['sub_product_limit_code']
            # except:
            #     assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # # aprove sub product limit
            # time.sleep(6)
            # fields_data = credit_fo_payload.crd_spla(
            #     sub_product_limit_code=sub_product_limit_code_new,
            #     sub_product_limit_name=sub_product_limit_name + str(i),
            #     customer_type=customer_type,
            #     reference_number=reference_number,
            #     customer_code=customer_code,
            #     product_limit_code=product_limit_code_new,
            #     currency_code=currency_code,
            #     credit_limit=credit_limit,
            #     product_limit_status=product_limit_status,
            #     description=description_crd_spla,
            #     amount=amount,
            #     exchange_rate=exchange_rate
            # )
            # try:
            #     rs = helper_fo.CRD_SPLA(fields_data)
            #     assert 'sub_product_limit_code' in rs, f'Key \"sub_product_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # except:
            #     assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # # open credit account
            # time.sleep(6)
            global id_new, account_number_new, account_number_def_new
            id_new = 0
            account_number_new = ''
            account_number_def_new = ''
            fields_data = credit_fo_payload.crd_opn(
                customer_type=customer_type,
                customer_code=customer_code,
                sub_product_limit_code=sub_product_limit_code_new,
                catalog_code=catalog_code,
                catalog_name=catalog_name,
                credit_facility=credit_facility,
                sub_product=sub_product,
                credit_classification=credit_classification,
                currency_code=currency_code,
                account_holder_name=account_holder_name + str(i),
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
                rs = helper_fo.CRD_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new = rs['account_number']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            #  approve credit account
            # time.sleep(6)
            # fields_data = credit_fo_payload.crd_apr(
            #     account_number=account_number_new,
            #     customer_type=customer_type,
            #     account_holder_name=account_holder_name,
            #     catalog_code=catalog_code,
            #     catalog_name=catalog_name,
            #     currency_code=currency_code,
            #     credit_limit=credit_limit,
            #     amount=amount,
            #     exchange_rate=exchange_rate,
            #     sub_product_limit_code=sub_product_limit_code_new,
            #     description=description_crd_apr,
            #     fee_data=fee_data
            # )
            # try:
            #     rs = helper_fo.CRD_APR(fields_data)
            #     assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     account_number_new = rs['account_number']
            # except:
            #     assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # simple search by account_number
            # time.sleep(6)
            fields_data = credit_account_payload.simple_search(
                search_text=account_number_new
            )
            try:
                rs = helper_bo.CRD_SEARCH_SP_CREDIT(fields_data)
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

            # modify credit account
            # time.sleep(6)
            fields_data = credit_account_payload.update(
            id=id_new,
            account_name=account_name_update + str(i),
            secure_type=secure_type_update,
            secure_rate=secure_rate_update,
            principal_tenor=principal_tenor_update,
            principal_tenor_unit=principal_tenor_unit_update,
            interest_tenor=interest_tenor_update,
            interest_tenor_unit=interest_tenor_unit_update,
            credit_purpose=credit_purpose_update,
            disbursement_mode=disbursement_mode_update,
            is_provision=is_provision_update,
            restruct=restruct_update,
            limit_from_third_party=limit_from_third_party_update,
            operative_limit_from_third_party=operative_limit_from_third_party_update,
            interest_first_date=interest_first_date_update,
            from_date=from_date_update,
            to_date=to_date_update,
            ranking_status=ranking_status_update,
            staff_id=staff_id_update,
            remark=remark_update,
            reference_number=reference_number_update,
            is_restructured=is_restructured_update,
            principal_provision_rate_0=principal_provision_rate_0_update,
            principal_provision_rate_1=principal_provision_rate_1_update,
            principal_provision_rate_2=principal_provision_rate_2_update,
            principal_provision_rate_3=principal_provision_rate_3_update,
            principal_provision_rate_4=principal_provision_rate_4_update,
            interest_provision_rate_0=interest_provision_rate_0_update,
            interest_provision_rate_1=interest_provision_rate_1_update,
            interest_provision_rate_2=interest_provision_rate_2_update,
            interest_provision_rate_3=interest_provision_rate_3_update,
            interest_provision_rate_4=interest_provision_rate_4_update,
            business_purpose_code=business_purpose_code_update,
            fine_tenor=fine_tenor_update,
            fine_tenor_unit=fine_tenor_unit_update,
            principal_grace_period=principal_grace_period_update,
            holiday_principal_due_on=holiday_principal_due_on_update,
            interest_grace_period=interest_grace_period_update,
            holiday_interest_tenor=holiday_interest_tenor_update,
            fine_grace_period=fine_grace_period_update,
            holiday_fine_tenor=holiday_fine_tenor_update,
            discount_rate=discount_rate_update,
            re_discount_rate=re_discount_rate_update,
            module_code=module_code_update,
            list_ifc_balance=list_ifc_balance_update,
            payment_list=payment_list_update,
            principal_list=principal_list_update
            )
            try:
                # print('fields_data update: ', fields_data)
                rs = helper_bo.CRD_UPDATE_CREDIT(fields_data)
                # print('Response Json:', rs)
                assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            i += 1