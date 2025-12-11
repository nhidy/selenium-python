import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.mortgage.mortgage_fo_helpers import MortgageFOHelper
from apitest.src.payloads.mortgage.mortgage_fo_payload import MortgageFOPayload

mortgage_fo_payload = MortgageFOPayload()

account_number=""
account_name="MTG ACC 080822 AUTO "
customer_type="C"
customer_code="11000013"
catalog_name="Mortgage-Land & Building-KHR"
catalog_code="00000003"
collateral_asset_type="B"
collateral_asset_class="B1"
security_paper_type="A"
currency_code="USD"
collateral_rate=100
risk_allocation_rate=1
collateral_asset_value=300000.65
market_value=0
book_value=300000.65
cc_contract=""
cc_amount=0
seq_number=None
reference_number="ref num"
location="N"
legal_local_address=""
legal_address=""
expiry_date="2024-12-08"
policy_amount=0
company_issues_policy=""
policy_number="plc no"
evaluate_by="eval by"
evaluate_method="MA"
evaluate_date="2022-07-21"
new_evaluate_date="2022-07-21"
insurance="Insurance"
description="4400: Open new collateral account"
book_currency_code="ABC"
value_date="2022-12-09"

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user3']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_mortgage_account
class TestOpenMortgageAccount(object):


    @pytest.mark.open_mortgage_account
    def test_001_open_mortgage_account(self, user):
        helper = MortgageFOHelper(user)
        i = 549
        while i < 5001:
            fields_data = mortgage_fo_payload.mtg_opn(
                account_number=account_number,
                account_name=account_name + str(i),
                customer_type=customer_type,
                customer_code=customer_code,
                catalog_name=catalog_name,
                catalog_code=catalog_code,
                collateral_asset_type=collateral_asset_type,
                collateral_asset_class=collateral_asset_class,
                security_paper_type=security_paper_type,
                currency_code=currency_code,
                collateral_rate=collateral_rate,
                risk_allocation_rate=risk_allocation_rate,
                collateral_asset_value=collateral_asset_value,
                market_value=market_value,
                book_value=book_value,
                cc_contract=cc_contract,
                cc_amount=cc_amount,
                seq_number=seq_number,
                reference_number=reference_number,
                location=location,
                legal_local_address=legal_local_address,
                legal_address=legal_address,
                expiry_date=expiry_date,
                policy_amount=policy_amount,
                company_issues_policy=company_issues_policy,
                policy_number=policy_number,
                evaluate_by=evaluate_by,
                evaluate_method=evaluate_method,
                evaluate_date=evaluate_date,
                new_evaluate_date=new_evaluate_date,
                insurance=insurance,
                description=description,
                book_currency_code=book_currency_code,
                value_date=value_date
            )
            rs = helper.MTG_OPN(fields_data)
            try:
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            i += 1