from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.mortgage.mortgage_account_helpers import MortgageAccountHelper
from apitest.src.payloads.mortgage.mortgage_account_payload import MortgageAccountPayload

mortgage_account_payload = MortgageAccountPayload()

# data simple
# INSERT INTO `MortgageAccount` (`Id`, `AccountNumberDef`, `AccountNumber`, `BranchId`, `CurrencyCode`, `BookCurrencyCode`, `AccountName`, `CustomerId`, `CustomerType`, `CatalogId`, `BookScope`, `CollateralAssetType`, `CollateralRate`, `CollateralAssetClassification`, `RiskAllocationRate`, `CollateralAccountStatus`, `SecurityPaperType`, `SecurityPaperNumber`, `OtherPaperData`, `CollateralAssetValue`, `MarketValue`, `BookValue`, `MortgageAmount`, `ReleasedCollateralAmount`, `KeepingAmount`, `KeepingReleaseAmount`, `OtherCounterPartyCollateralAmount`, `OtherCounterPartyCollateralReleased`, `SumInsuranceAmount`, `PremiumAmount`, `WasRegisterAtCollateralCenter`, `DepreciationOption`, `OriginalAmount`, `AccumulateOfDepreciationAmount`, `NetBookValueAfterDepreciation`, `WeekDebit`, `WeekCredit`, `MonthDebit`, `MonthCredit`, `QuarterDebit`, `QuarterCredit`, `SemiAnnualDebit`, `SemiAnnualCredit`, `YearDebit`, `YearCredit`, `CreatedBy`, `ApprovedBy`, `AccountManagerStaffId`, `OpenDate`, `CloseDate`, `LastTransactionDate`, `Remark`, `ReferenceNumber`, `CCContract`, `CCAmount`, `OtherAddress`, `Location`, `Owner`, `UserDefine1`, `UserDefine2`, `UserDefine3`, `UserDefine4`, `UserDefine5`, `CompanyIssuesPolicy`, `ExpiryDate`, `PolicyAmount`, `PolicyNumber`, `LegalLocalAddress`, `LocalAddress`, `EvaluateBy`, `EvaluateMethod`, `EvaluateDate`, `NewEvaluateDate`, `Insurance`) VALUES
# (3, '00999USDMTG00000121', '0999102020001213', 2, 'USD', 'USD', 'House test', 102, 'C', 1, '0', 'B', '100.000', 'B1', '100.000', 'P', 'A', '123', NULL, '11111.000', '0.000', '11111.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', NULL, 'N', '0.000', '0.000', NULL, '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', 1, 2, 3, '2021-08-09 00:00:00', NULL, '2022-12-09 00:00:00', NULL, NULL, NULL, '0.000', '{\"P\":\"f\",\"A\":\"g\",\"B\":\"h\",\"S\":\"j\",\"T\":\"h\",\"D\":\"h\",\"W\":\"g\",\"H\":\"f\",\"L\":\"b\",\"N\":\"a\"}', 'Y', NULL, NULL, NULL, NULL, NULL, NULL, '0', '2021-08-09 00:00:00', '0.000', '123', '{\"R\":\"12\",\"C\":\"01\",\"T\":\"01030201\",\"D\":\"010302\",\"W\":\"0103\",\"H\":\"123\",\"Z\":\"123\"}', '{\"R\":\"\",\"C\":\"\",\"T\":\"\",\"D\":\"\",\"W\":\"\",\"H\":\"\",\"Z\":\"\"}', '123', NULL, '2021-08-09 00:00:00', '2022-08-09 00:00:00', '3132');

# INSERT INTO `MortgageBalance` (`Id`, `DefAccountNumber`, `MortgageReference`, `ModuleCode`, `Amount`, `ClearAmount`, `SetDate`, `ClearDate`, `ModuleAmount`, `ModuleClearAmount`) VALUES
# (NULL, '00999USDMTG00000121', '1', '1', '200.0000', '100.0000', '2022-04-15 09:23:58', '2022-04-15 09:23:58', '400.0000', '300.0000'),

id_new=13
account_number='0999102020001213'

account_name_update="MTG account test update"
collateral_rate_update=40
risk_allocation_rate_update=10
was_register_at_collateral_center_update="Y"
security_paper_type_update="A"
security_paper_number_update="876334222"
paper_type_update="B"
paper_number_update="7323"
market_value_update=29000.67
other_counter_party_collateral_amount_update=4550.74
other_counter_party_collateral_released_update=5650.33
sum_insurance_amount_update=52234.43
premium_amount_update=78434.24
original_amount_update=2436.23
remark_update="remart test up"
reference_number_update="7534235"
cc_contract_update="co up"
cc_amount_update=76432.66
name_of_title_update="n up"
house_no_update="h up"
plot_no_update="p up"
holding_no_update="l up"
ward_no_update="w up"
block_no_update="b up"
area_update="a up"
street_update="s up"
town_ship_update="t up"
division_city_update="d up"
location_update="l up"
owner_update="o up"
user_define1_update="u1"
user_define2_update="u2"
user_define3_update="u3"
user_define4_update="u4"
user_define5_update="u5"
company_issues_policy_update="com up"
expiry_date_update=datetime.fromisoformat("2022-03-28").strftime('%Y-%m-%dT%H:%M:%S')
policy_amount_update=2450.23
policy_number_update="po up"
province_legal_update="p up"
district_legal_update="d up"
sub_district_legal_update="s up"
village_legal_update="v up"
address_in_combodia_legal_update="a up"
address_legal_update="add up"
zip_code_legal_update="z up"
province_local_update="p up"
district_local_update="d up"
sub_district_local_update="s up"
village_local_update="v up"
address_in_combodia_local_update="a up"
address_local_update="add up"
zip_code_local_update="z up"
evaluate_by_update="Q"
evaluate_method_update="V"
evaluate_date_update=datetime.fromisoformat("2022-03-27").strftime('%Y-%m-%dT%H:%M:%S')
new_evaluate_date_update=datetime.fromisoformat("2022-03-29").strftime('%Y-%m-%dT%H:%M:%S')
insurance_update="test"


# check type number
number_checklist = {
    "collateral_rate": {
        "data_type": float,
        "number_of_digits": 3
    },
    "risk_allocation_rate": {
        "data_type": float,
        "number_of_digits": 3
    },
    "collateral_asset_value": {
        "data_type": float,
        "number_of_digits": 3
    },
    "market_value": {
        "data_type": float,
        "number_of_digits": 3
    },
    "book_value": {
        "data_type": float,
        "number_of_digits": 3
    },
    "current_secure_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "cc_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "released_collateral_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "keeping_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "keeping_release_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "other_counter_party_collateral_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "other_counter_party_collateral_released": {
        "data_type": float,
        "number_of_digits": 3
    },
    "sum_insurance_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "premium_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "original_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "accumulate_of_depreciation_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "net_book_value_after_depreciation": {
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
    "policy_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "customer_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "branch_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "created_by": {
        "data_type": int,
        "number_of_digits": 0
    },
    "approved_by": {
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

@pytest.mark.mortgage_account
class TestMortgageAccount(object):


    @pytest.mark.simple_search_mortgage_account
    def test_001_simple_search_mortgage_account(self, user):
        global total_count
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.simple_search(
            page_size=50
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_mortgage_account
    def test_002_advanced_search_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.advanced_search(
            page_size=50
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_mortgage_account
    def test_003_update_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.update(
            id=id_new,
            account_name=account_name_update,
            cc_contract=cc_contract_update,
            collateral_rate=collateral_rate_update,
            risk_allocation_rate=risk_allocation_rate_update,
            was_register_at_collateral_center=was_register_at_collateral_center_update,
            security_paper_type=security_paper_type_update,
            security_paper_number=security_paper_number_update,
            name_of_title=name_of_title_update,
            house_no=house_no_update,
            plot_no=plot_no_update,
            holding_no=holding_no_update,
            ward_no=ward_no_update,
            block_no=block_no_update,
            area=area_update,
            street=street_update,
            town_ship=town_ship_update,
            division_city=division_city_update,
            location=location_update,
            province_legal=province_legal_update,
            district_legal=district_legal_update,
            sub_district_legal=sub_district_legal_update,
            village_legal=village_legal_update,
            address_in_combodia_legal=address_in_combodia_legal_update,
            address_legal=address_legal_update,
            zip_code_legal=zip_code_legal_update,
            province_local=province_local_update,
            district_local=district_local_update,
            sub_district_local=sub_district_local_update,
            village_local=village_local_update,
            address_in_combodia_local=address_in_combodia_local_update,
            address_local=address_local_update,
            zip_code_local=zip_code_local_update,
            evaluate_by=evaluate_by_update,
            evaluate_method=evaluate_method_update,
            evaluate_date=evaluate_date_update,
            new_evaluate_date=new_evaluate_date_update,
            insurance=insurance_update,
            paper_type=paper_type_update,
            paper_number=paper_number_update,
            market_value=market_value_update,
            cc_amount=cc_amount_update,
            other_counter_party_collateral_amount=other_counter_party_collateral_amount_update,
            other_counter_party_collateral_released=other_counter_party_collateral_released_update,
            sum_insurance_amount=sum_insurance_amount_update,
            premium_amount=premium_amount_update,
            original_amount=original_amount_update,
            remark=remark_update,
            reference_number=reference_number_update,
            owner=owner_update,
            user_define1=user_define1_update,
            user_define2=user_define2_update,
            user_define3=user_define3_update,
            user_define4=user_define4_update,
            user_define5=user_define5_update,
            policy_number=policy_number_update,
            expiry_date=expiry_date_update,
            policy_amount=policy_amount_update,
            company_issues_policy=company_issues_policy_update
        )
        rs = helper.MTG_UPDATE_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_name' in rs, f'Key \"account_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'cc_contract' in rs, f'Key \"cc_contract\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_rate' in rs, f'Key \"collateral_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'risk_allocation_rate' in rs, f'Key \"risk_allocation_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'was_register_at_collateral_center' in rs, f'Key \"was_register_at_collateral_center\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'security_paper_type' in rs, f'Key \"security_paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'security_paper_number' in rs, f'Key \"security_paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_address' in rs, f'Key \"other_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'name_of_title' in rs['other_address'], f'Key \"name_of_title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'house_no' in rs['other_address'], f'Key \"house_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'plot_no' in rs['other_address'], f'Key \"plot_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'holding_no' in rs['other_address'], f'Key \"holding_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'ward_no' in rs['other_address'], f'Key \"ward_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'block_no' in rs['other_address'], f'Key \"block_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'area' in rs['other_address'], f'Key \"area\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'street' in rs['other_address'], f'Key \"street\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'town_ship' in rs['other_address'], f'Key \"town_ship\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'division_city' in rs['other_address'], f'Key \"division_city\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'location' in rs, f'Key \"location\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_in_combodia' in rs['legal_local_address'], f'Key \"address_in_combodia\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zip_code' in rs['legal_local_address'], f'Key \"zip_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'local_address' in rs, f'Key \"local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_in_combodia' in rs['local_address'], f'Key \"address_in_combodia\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zip_code' in rs['local_address'], f'Key \"zip_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_by' in rs, f'Key \"evaluate_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_method' in rs, f'Key \"evaluate_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_date' in rs, f'Key \"evaluate_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'new_evaluate_date' in rs, f'Key \"new_evaluate_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'insurance' in rs, f'Key \"insurance\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_paper_data' in rs, f'Key \"other_paper_data\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs['other_paper_data'], f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs['other_paper_data'], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'market_value' in rs, f'Key \"market_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'cc_amount' in rs, f'Key \"cc_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_counter_party_collateral_amount' in rs, f'Key \"other_counter_party_collateral_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_counter_party_collateral_released' in rs, f'Key \"other_counter_party_collateral_released\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sum_insurance_amount' in rs, f'Key \"sum_insurance_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'premium_amount' in rs, f'Key \"premium_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'original_amount' in rs, f'Key \"original_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'remark' in rs, f'Key \"remark\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'reference_number' in rs, f'Key \"reference_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'owner' in rs, f'Key \"owner\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define1' in rs, f'Key \"user_define1\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define2' in rs, f'Key \"user_define2\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define3' in rs, f'Key \"user_define3\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define4' in rs, f'Key \"user_define4\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define5' in rs, f'Key \"user_define5\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'policy_number' in rs, f'Key \"policy_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expiry_date' in rs, f'Key \"expiry_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'policy_amount' in rs, f'Key \"policy_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'company_issues_policy' in rs, f'Key \"company_issues_policy\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cc_contract_update == rs['cc_contract'], f'Expected \'{cc_contract_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_rate_update == rs['collateral_rate'], f'Expected \'{collateral_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert risk_allocation_rate_update == rs['risk_allocation_rate'], f'Expected \'{risk_allocation_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert was_register_at_collateral_center_update == rs['was_register_at_collateral_center'], f'Expected \'{was_register_at_collateral_center_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_type_update == rs['security_paper_type'], f'Expected \'{security_paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_number_update == rs['security_paper_number'], f'Expected \'{security_paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert name_of_title_update == rs['other_address']['name_of_title'], f'Expected \'{name_of_title_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert house_no_update == rs['other_address']['house_no'], f'Expected \'{house_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert plot_no_update == rs['other_address']['plot_no'], f'Expected \'{plot_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_no_update == rs['other_address']['holding_no'], f'Expected \'{holding_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ward_no_update == rs['other_address']['ward_no'], f'Expected \'{ward_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert block_no_update == rs['other_address']['block_no'], f'Expected \'{block_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert area_update == rs['other_address']['area'], f'Expected \'{area_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert street_update == rs['other_address']['street'], f'Expected \'{street_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert town_ship_update == rs['other_address']['town_ship'], f'Expected \'{town_ship_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert division_city_update == rs['other_address']['division_city'], f'Expected \'{division_city_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert location_update == rs['location'], f'Expected \'{location_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert province_legal_update == rs['legal_local_address']['province'], f'Expected \'{province_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal_update == rs['legal_local_address']['district'], f'Expected \'{district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal_update == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal_update == rs['legal_local_address']['village'], f'Expected \'{village_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_legal_update == rs['legal_local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal_update == rs['legal_local_address']['address'], f'Expected \'{address_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_legal_update == rs['legal_local_address']['zip_code'], f'Expected \'{zip_code_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert province_local_update == rs['local_address']['province'], f'Expected \'{province_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_local_update == rs['local_address']['district'], f'Expected \'{district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_local_update == rs['local_address']['sub_district'], f'Expected \'{sub_district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_local_update == rs['local_address']['village'], f'Expected \'{village_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_local_update == rs['local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_update == rs['local_address']['address'], f'Expected \'{address_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_local_update == rs['local_address']['zip_code'], f'Expected \'{zip_code_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert evaluate_by_update == rs['evaluate_by'], f'Expected \'{evaluate_by_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_method_update == rs['evaluate_method'], f'Expected \'{evaluate_method_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_date_update == rs['evaluate_date'], f'Expected \'{evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert new_evaluate_date_update == rs['new_evaluate_date'], f'Expected \'{new_evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert insurance_update == rs['insurance'], f'Expected \'{insurance_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_update == rs['other_paper_data']['paper_type'], f'Expected \'{paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_update == rs['other_paper_data']['paper_number'], f'Expected \'{paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert market_value_update == rs['market_value'], f'Expected \'{market_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cc_amount_update == rs['cc_amount'], f'Expected \'{cc_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert other_counter_party_collateral_amount_update == rs['other_counter_party_collateral_amount'], f'Expected \'{other_counter_party_collateral_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert other_counter_party_collateral_released_update == rs['other_counter_party_collateral_released'], f'Expected \'{other_counter_party_collateral_released_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sum_insurance_amount_update == rs['sum_insurance_amount'], f'Expected \'{sum_insurance_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert premium_amount_update == rs['premium_amount'], f'Expected \'{premium_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert original_amount_update == rs['original_amount'], f'Expected \'{original_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number_update == rs['reference_number'], f'Expected \'{reference_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner_update == rs['owner'], f'Expected \'{owner_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define1_update == rs['user_define1'], f'Expected \'{user_define1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define2_update == rs['user_define2'], f'Expected \'{user_define2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define3_update == rs['user_define3'], f'Expected \'{user_define3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define4_update == rs['user_define4'], f'Expected \'{user_define4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define5_update == rs['user_define5'], f'Expected \'{user_define5_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_number_update == rs['policy_number'], f'Expected \'{policy_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expiry_date_update == rs['expiry_date'], f'Expected \'{expiry_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_amount_update == rs['policy_amount'], f'Expected \'{policy_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_issues_policy_update == rs['company_issues_policy'], f'Expected \'{company_issues_policy_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_mortgage_account_after_update
    def test_004_simple_search_mortgage_account_after_update(self, user):
        search_rs = False
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = mortgage_account_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item): 
                        list_item = rs['items'][i].items()
                        for key, value in list_item:
                            if search_text in str(value):
                                search_rs = True
                                break
                    assert search_rs, f'Search with simple search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_mortgage_account_after_update
    def test_005_advanced_search_mortgage_account_after_update(self, user):
        search_rs = False
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.advanced_search(
            page_size=50,
            account_name=search_text
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = mortgage_account_payload.advanced_search(
                    page_size=total_count_adv,
                    account_name=search_text
                )
                rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['account_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_mortgage_account
    def test_006_view_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.view(
            id=id_new
        )
        rs = helper.MTG_VIEW_MORTGAGE_ACCOUNT(fields_data)
        try:
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_number_def' in rs, f'Key \"account_number_def\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_name' in rs, f'Key \"account_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'cc_contract' in rs, f'Key \"cc_contract\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'book_currency_code' in rs, f'Key \"book_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_type' in rs, f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_id' in rs, f'Key \"customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_id' in rs, f'Key \"branch_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_account_status' in rs, f'Key \"collateral_account_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_asset_type' in rs, f'Key \"collateral_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_asset_classification' in rs, f'Key \"collateral_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_rate' in rs, f'Key \"collateral_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'risk_allocation_rate' in rs, f'Key \"risk_allocation_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'book_scope' in rs, f'Key \"book_scope\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_option' in rs, f'Key \"depreciation_option\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'was_register_at_collateral_center' in rs, f'Key \"was_register_at_collateral_center\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'security_paper_type' in rs, f'Key \"security_paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'security_paper_number' in rs, f'Key \"security_paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_address' in rs, f'Key \"other_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'name_of_title' in rs['other_address'], f'Key \"name_of_title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'house_no' in rs['other_address'], f'Key \"house_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'plot_no' in rs['other_address'], f'Key \"plot_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'holding_no' in rs['other_address'], f'Key \"holding_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'ward_no' in rs['other_address'], f'Key \"ward_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'block_no' in rs['other_address'], f'Key \"block_no\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'area' in rs['other_address'], f'Key \"area\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'street' in rs['other_address'], f'Key \"street\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'town_ship' in rs['other_address'], f'Key \"town_ship\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'division_city' in rs['other_address'], f'Key \"division_city\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'location' in rs, f'Key \"location\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_in_combodia' in rs['legal_local_address'], f'Key \"address_in_combodia\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zip_code' in rs['legal_local_address'], f'Key \"zip_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'local_address' in rs, f'Key \"local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_in_combodia' in rs['local_address'], f'Key \"address_in_combodia\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zip_code' in rs['local_address'], f'Key \"zip_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_by' in rs, f'Key \"evaluate_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_method' in rs, f'Key \"evaluate_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'evaluate_date' in rs, f'Key \"evaluate_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'new_evaluate_date' in rs, f'Key \"new_evaluate_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'insurance' in rs, f'Key \"insurance\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'open_date' in rs, f'Key \"open_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'close_date' in rs, f'Key \"close_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'last_transaction_date' in rs, f'Key \"last_transaction_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by' in rs, f'Key \"created_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by' in rs, f'Key \"approved_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_manager_staff_id' in rs, f'Key \"account_manager_staff_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_paper_data' in rs, f'Key \"other_paper_data\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs['other_paper_data'], f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs['other_paper_data'], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_asset_value' in rs, f'Key \"collateral_asset_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'market_value' in rs, f'Key \"market_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'book_value' in rs, f'Key \"book_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'current_secure_amount' in rs, f'Key \"current_secure_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'cc_amount' in rs, f'Key \"cc_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'released_collateral_amount' in rs, f'Key \"released_collateral_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'keeping_amount' in rs, f'Key \"keeping_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'keeping_release_amount' in rs, f'Key \"keeping_release_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_counter_party_collateral_amount' in rs, f'Key \"other_counter_party_collateral_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'other_counter_party_collateral_released' in rs, f'Key \"other_counter_party_collateral_released\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sum_insurance_amount' in rs, f'Key \"sum_insurance_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'premium_amount' in rs, f'Key \"premium_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'original_amount' in rs, f'Key \"original_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'accumulate_of_depreciation_amount' in rs, f'Key \"accumulate_of_depreciation_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'net_book_value_after_depreciation' in rs, f'Key \"net_book_value_after_depreciation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'week_debit' in rs, f'Key \"week_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'week_credit' in rs, f'Key \"week_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'month_debit' in rs, f'Key \"month_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'month_credit' in rs, f'Key \"month_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'quarter_debit' in rs, f'Key \"quarter_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'quarter_credit' in rs, f'Key \"quarter_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'semi_annual_debit' in rs, f'Key \"semi_annual_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'semi_annual_credit' in rs, f'Key \"semi_annual_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'year_debit' in rs, f'Key \"year_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'year_credit' in rs, f'Key \"year_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'remark' in rs, f'Key \"remark\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'reference_number' in rs, f'Key \"reference_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'owner' in rs, f'Key \"owner\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define1' in rs, f'Key \"user_define1\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define2' in rs, f'Key \"user_define2\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define3' in rs, f'Key \"user_define3\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define4' in rs, f'Key \"user_define4\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_define5' in rs, f'Key \"user_define5\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'policy_number' in rs, f'Key \"policy_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expiry_date' in rs, f'Key \"expiry_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'policy_amount' in rs, f'Key \"policy_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'company_issues_policy' in rs, f'Key \"company_issues_policy\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_name' in rs, f'Key \"customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by_code' in rs, f'Key \"created_by_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by_name' in rs, f'Key \"created_by_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by_code' in rs, f'Key \"approved_by_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by_name' in rs, f'Key \"approved_by_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_manager_staff_code' in rs, f'Key \"account_manager_staff_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_manager_staff_name' in rs, f'Key \"account_manager_staff_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cc_contract_update == rs['cc_contract'], f'Expected \'{cc_contract_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_rate_update == rs['collateral_rate'], f'Expected \'{collateral_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert risk_allocation_rate_update == rs['risk_allocation_rate'], f'Expected \'{risk_allocation_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert was_register_at_collateral_center_update == rs['was_register_at_collateral_center'], f'Expected \'{was_register_at_collateral_center_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_type_update == rs['security_paper_type'], f'Expected \'{security_paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_number_update == rs['security_paper_number'], f'Expected \'{security_paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert name_of_title_update == rs['other_address']['name_of_title'], f'Expected \'{name_of_title_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert house_no_update == rs['other_address']['house_no'], f'Expected \'{house_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert plot_no_update == rs['other_address']['plot_no'], f'Expected \'{plot_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_no_update == rs['other_address']['holding_no'], f'Expected \'{holding_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ward_no_update == rs['other_address']['ward_no'], f'Expected \'{ward_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert block_no_update == rs['other_address']['block_no'], f'Expected \'{block_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert area_update == rs['other_address']['area'], f'Expected \'{area_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert street_update == rs['other_address']['street'], f'Expected \'{street_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert town_ship_update == rs['other_address']['town_ship'], f'Expected \'{town_ship_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert division_city_update == rs['other_address']['division_city'], f'Expected \'{division_city_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert location_update == rs['location'], f'Expected \'{location_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_legal_update == rs['legal_local_address']['province'], f'Expected \'{province_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal_update == rs['legal_local_address']['district'], f'Expected \'{district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal_update == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal_update == rs['legal_local_address']['village'], f'Expected \'{village_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_legal_update == rs['legal_local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal_update == rs['legal_local_address']['address'], f'Expected \'{address_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_legal_update == rs['legal_local_address']['zip_code'], f'Expected \'{zip_code_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_local_update == rs['local_address']['province'], f'Expected \'{province_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_local_update == rs['local_address']['district'], f'Expected \'{district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_local_update == rs['local_address']['sub_district'], f'Expected \'{sub_district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_local_update == rs['local_address']['village'], f'Expected \'{village_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_local_update == rs['local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_update == rs['local_address']['address'], f'Expected \'{address_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_local_update == rs['local_address']['zip_code'], f'Expected \'{zip_code_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_by_update == rs['evaluate_by'], f'Expected \'{evaluate_by_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_method_update == rs['evaluate_method'], f'Expected \'{evaluate_method_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_date_update == rs['evaluate_date'], f'Expected \'{evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert new_evaluate_date_update == rs['new_evaluate_date'], f'Expected \'{new_evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert insurance_update == rs['insurance'], f'Expected \'{insurance_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_update == rs['other_paper_data']['paper_type'], f'Expected \'{paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_update == rs['other_paper_data']['paper_number'], f'Expected \'{paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert market_value_update == rs['market_value'], f'Expected \'{market_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cc_amount_update == rs['cc_amount'], f'Expected \'{cc_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert other_counter_party_collateral_amount_update == rs['other_counter_party_collateral_amount'], f'Expected \'{other_counter_party_collateral_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert other_counter_party_collateral_released_update == rs['other_counter_party_collateral_released'], f'Expected \'{other_counter_party_collateral_released_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sum_insurance_amount_update == rs['sum_insurance_amount'], f'Expected \'{sum_insurance_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert premium_amount_update == rs['premium_amount'], f'Expected \'{premium_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert original_amount_update == rs['original_amount'], f'Expected \'{original_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number_update == rs['reference_number'], f'Expected \'{reference_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner_update == rs['owner'], f'Expected \'{owner_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define1_update == rs['user_define1'], f'Expected \'{user_define1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define2_update == rs['user_define2'], f'Expected \'{user_define2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define3_update == rs['user_define3'], f'Expected \'{user_define3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define4_update == rs['user_define4'], f'Expected \'{user_define4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define5_update == rs['user_define5'], f'Expected \'{user_define5_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_number_update == rs['policy_number'], f'Expected \'{policy_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expiry_date_update == rs['expiry_date'], f'Expected \'{expiry_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_amount_update == rs['policy_amount'], f'Expected \'{policy_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_issues_policy_update == rs['company_issues_policy'], f'Expected \'{company_issues_policy_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = mortgage_account_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.mortgage_account_check_number_null
    def test_007_mortgage_account_check_number_null(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.update(
            id=id_new,
            account_name=account_name_update,
            cc_contract=cc_contract_update,
            was_register_at_collateral_center=was_register_at_collateral_center_update,
            security_paper_type=security_paper_type_update,
            security_paper_number=security_paper_number_update,
            name_of_title=name_of_title_update,
            house_no=house_no_update,
            plot_no=plot_no_update,
            holding_no=holding_no_update,
            ward_no=ward_no_update,
            block_no=block_no_update,
            area=area_update,
            street=street_update,
            town_ship=town_ship_update,
            division_city=division_city_update,
            location=location_update,
            province_legal=province_legal_update,
            district_legal=district_legal_update,
            sub_district_legal=sub_district_legal_update,
            village_legal=village_legal_update,
            address_in_combodia_legal=address_in_combodia_legal_update,
            address_legal=address_legal_update,
            zip_code_legal=zip_code_legal_update,
            province_local=province_local_update,
            district_local=district_local_update,
            sub_district_local=sub_district_local_update,
            village_local=village_local_update,
            address_in_combodia_local=address_in_combodia_local_update,
            address_local=address_local_update,
            zip_code_local=zip_code_local_update,
            evaluate_by=evaluate_by_update,
            evaluate_method=evaluate_method_update,
            evaluate_date=evaluate_date_update,
            new_evaluate_date=new_evaluate_date_update,
            insurance=insurance_update,
            paper_type=paper_type_update,
            paper_number=paper_number_update,
            remark=remark_update,
            reference_number=reference_number_update,
            owner=owner_update,
            user_define1=user_define1_update,
            user_define2=user_define2_update,
            user_define3=user_define3_update,
            user_define4=user_define4_update,
            user_define5=user_define5_update,
            policy_number=policy_number_update,
            expiry_date=expiry_date_update,
            company_issues_policy=company_issues_policy_update
        )
        rs = helper.MTG_UPDATE_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cc_contract_update == rs['cc_contract'], f'Expected \'{cc_contract_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['collateral_rate'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['risk_allocation_rate'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert was_register_at_collateral_center_update == rs['was_register_at_collateral_center'], f'Expected \'{was_register_at_collateral_center_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_type_update == rs['security_paper_type'], f'Expected \'{security_paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert security_paper_number_update == rs['security_paper_number'], f'Expected \'{security_paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert name_of_title_update == rs['other_address']['name_of_title'], f'Expected \'{name_of_title_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert house_no_update == rs['other_address']['house_no'], f'Expected \'{house_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert plot_no_update == rs['other_address']['plot_no'], f'Expected \'{plot_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_no_update == rs['other_address']['holding_no'], f'Expected \'{holding_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ward_no_update == rs['other_address']['ward_no'], f'Expected \'{ward_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert block_no_update == rs['other_address']['block_no'], f'Expected \'{block_no_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert area_update == rs['other_address']['area'], f'Expected \'{area_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert street_update == rs['other_address']['street'], f'Expected \'{street_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert town_ship_update == rs['other_address']['town_ship'], f'Expected \'{town_ship_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert division_city_update == rs['other_address']['division_city'], f'Expected \'{division_city_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert location_update == rs['location'], f'Expected \'{location_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert province_legal_update == rs['legal_local_address']['province'], f'Expected \'{province_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal_update == rs['legal_local_address']['district'], f'Expected \'{district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal_update == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal_update == rs['legal_local_address']['village'], f'Expected \'{village_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_legal_update == rs['legal_local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal_update == rs['legal_local_address']['address'], f'Expected \'{address_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_legal_update == rs['legal_local_address']['zip_code'], f'Expected \'{zip_code_legal_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert province_local_update == rs['local_address']['province'], f'Expected \'{province_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_local_update == rs['local_address']['district'], f'Expected \'{district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_local_update == rs['local_address']['sub_district'], f'Expected \'{sub_district_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_local_update == rs['local_address']['village'], f'Expected \'{village_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_in_combodia_local_update == rs['local_address']['address_in_combodia'], f'Expected \'{address_in_combodia_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_update == rs['local_address']['address'], f'Expected \'{address_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zip_code_local_update == rs['local_address']['zip_code'], f'Expected \'{zip_code_local_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert evaluate_by_update == rs['evaluate_by'], f'Expected \'{evaluate_by_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_method_update == rs['evaluate_method'], f'Expected \'{evaluate_method_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert evaluate_date_update == rs['evaluate_date'], f'Expected \'{evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert new_evaluate_date_update == rs['new_evaluate_date'], f'Expected \'{new_evaluate_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert insurance_update == rs['insurance'], f'Expected \'{insurance_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_update == rs['other_paper_data']['paper_type'], f'Expected \'{paper_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_update == rs['other_paper_data']['paper_number'], f'Expected \'{paper_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['market_value'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['cc_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['other_counter_party_collateral_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['other_counter_party_collateral_released'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['sum_insurance_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['premium_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['original_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number_update == rs['reference_number'], f'Expected \'{reference_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner_update == rs['owner'], f'Expected \'{owner_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define1_update == rs['user_define1'], f'Expected \'{user_define1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define2_update == rs['user_define2'], f'Expected \'{user_define2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define3_update == rs['user_define3'], f'Expected \'{user_define3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define4_update == rs['user_define4'], f'Expected \'{user_define4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_define5_update == rs['user_define5'], f'Expected \'{user_define5_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_number_update == rs['policy_number'], f'Expected \'{policy_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expiry_date_update == rs['expiry_date'], f'Expected \'{expiry_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['policy_amount'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_issues_policy_update == rs['company_issues_policy'], f'Expected \'{company_issues_policy_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_mortgage_account
    def test_008_delete_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.delete(
            id=id_new
        )
        rs = helper.MTG_DELETE_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = mortgage_account_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count - 1) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_mortgage_account_check_page
    def test_009_simple_search_mortgage_account_check_page(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_mortgage_account_check_page
    def test_010_advanced_search_mortgage_account_check_page(self, user):
        helper = MortgageAccountHelper(user)
        fields_data = mortgage_account_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'