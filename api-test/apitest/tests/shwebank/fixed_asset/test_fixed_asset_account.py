import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.fixed_asset.fixed_asset_account_helpers import FixedAssetAccountHelper
from apitest.src.payloads.fixed_asset.fixed_asset_account_payload import FixedAssetAccountPayload

fixed_asset_account_payload = FixedAssetAccountPayload()

# data simple
# INSERT INTO `FixedAssetAccount` (`Id`, `AccountNumberDef`, `AccountNumber`, `Branchid`, `CurrencyCode`, `FixedAssetAccountName`, `Owner`, `CustomerId`, `CustomerType`, `CatalogId`, `ReferenceNumber`, `FixedAssetType`, `FixedAssetClassification`, `DepreciationMethod`, `FixedAssetGroup`, `FixedAssetLifeTime`, `FixedAssetLifeTimeUnit`, `DepreciationRate`, `Buydt`, `Dprdt`, `ProviderName`, `BookingCurrencyCode`, `Wrfrdt`, `Wrtodt`, `Wrsrn`, `OriginalPrice`, `BookingAmount`, `NetBookingValue`, `AccummulateAmount`, `ExpenseAmount`, `InsurranceValue`, `InsurranceFee`, `SalvageAmount`, `IncomeAmount`, `WeekDebit`, `WeekCredit`, `MonthDebit`, `MonthCredit`, `QuaterDebit`, `QuaterCredit`, `SemiannualDebit`, `SemiannualCredit`, `YearDebit`, `YearCredit`, `UserId`, `ApproveUser`, `StaffId`, `Remark`, `OldIdOfCustomer`, `Udfield1`, `FixedAssetStatus`, `CrossRate`, `ExpireDate`, `AccummulateNotPosted`) 
# VALUES (8, '00999USDFAC00000002', '0999201020000028', '2', 'USD', 'Window 10 Professional test', 'B', '1', 'C', '1', NULL, 'L', 'I', 'B', NULL, '5', 'Y', '0.000', '2019-12-02', '2019-12-02', 'Computer Trading', 'USD', '2019-12-02', '2019-12-02', 'UN', '3500.000', '0.000', '3500.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '1', '2', '3', NULL, NULL, NULL, 'W', '1.000000000', '2029-01-01', '-150.00000000')

id=8

account_number_def="00999USDFAC00000002"
account_number="0999201020000028"
fixed_asset_account_name="Fixed asset name 032 test update"
reference_number="refup"
fixed_asset_classification="W"
depreciation_method="S"
fixed_asset_life_time=1
fixed_asset_life_time_unit="Y"
provider_name="provider"
owner="O"

# check type number
number_checklist = {
    "id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "catalog_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "branchid": {
        "data_type": int,
        "number_of_digits": 0
    },
    "fixed_asset_life_time": {
        "data_type": int,
        "number_of_digits": 0
    },
    "depreciation_rate": {
        "data_type": float,
        "number_of_digits": 2
    },
    "original_price": {
        "data_type": float,
        "number_of_digits": 2
    },
    "booking_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "net_booking_value": {
        "data_type": float,
        "number_of_digits": 2
    },
    "accummulate_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "expense_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "insurrance_value": {
        "data_type": float,
        "number_of_digits": 2
    },
    "insurrance_fee": {
        "data_type": float,
        "number_of_digits": 2
    },
    "salvage_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "income_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "week_debit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "week_credit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "month_debit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "month_credit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "quater_debit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "quater_credit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "semiannual_debit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "semiannual_credit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "year_debit": {
        "data_type": float,
        "number_of_digits": 2
    },
    "year_credit": {
        "data_type": float,
        "number_of_digits": 2
    },
}

search_text='test'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.fixed_asset_account
class TestFixedAssetAccount(object):


    @pytest.mark.simple_search_fixed_asset_account
    def test_001_simple_search_fixed_asset_account(self, user):
        global total_count
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.simple_search(
            page_size=5
        )
        rs = helper.SQL_SEARCH_FACACT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'account_number' in rs['items'][0], f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_account_name' in rs['items'][0], f'Key \"fixed_asset_account_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'booking_currency_code' in rs['items'][0], f'Key \"booking_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_type' in rs['items'][0], f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_status' in rs['items'][0], f'Key \"fixed_asset_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_fixed_asset_account
    def test_002_advanced_search_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.advanced_search(
            page_size=5
        )
        rs = helper.SQL_ADSEARCH_FACACT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'account_number' in rs['items'][0], f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_account_name' in rs['items'][0], f'Key \"fixed_asset_account_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'booking_currency_code' in rs['items'][0], f'Key \"booking_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_type' in rs['items'][0], f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_status' in rs['items'][0], f'Key \"fixed_asset_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_fixed_asset_account
    def test_003_update_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.update(
            id=id,
            fixed_asset_account_name=fixed_asset_account_name,
            reference_number=reference_number,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            fixed_asset_life_time=fixed_asset_life_time,
            fixed_asset_life_time_unit=fixed_asset_life_time_unit,
            provider_name=provider_name,
            owner=owner
        )
        rs = helper.SQL_UPDATE_FACACT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id == rs['id'], f'Expected \'{id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number_def == rs['account_number_def'], f'Expected \'{account_number_def}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_account_name == rs['fixed_asset_account_name'], f'Expected \'{fixed_asset_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number == rs['reference_number'], f'Expected \'{reference_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method == rs['depreciation_method'], f'Expected \'{depreciation_method}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_life_time == rs['fixed_asset_life_time'], f'Expected \'{fixed_asset_life_time}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_life_time_unit == rs['fixed_asset_life_time_unit'], f'Expected \'{fixed_asset_life_time_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provider_name == rs['provider_name'], f'Expected \'{provider_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner == rs['owner'], f'Expected \'{owner}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_fixed_asset_account_after_update
    def test_004_simple_search_fixed_asset_account_after_update(self, user):
        search_rs = False
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.SQL_SEARCH_FACACT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = fixed_asset_account_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.SQL_SEARCH_FACACT(fields_data)
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


    @pytest.mark.advanced_search_fixed_asset_account_after_update
    def test_005_advanced_search_fixed_asset_account_after_update(self, user):
        search_rs = False
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.advanced_search(
            page_size=5,
            account_number=account_number
        )
        rs = helper.SQL_ADSEARCH_FACACT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{account_number}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = fixed_asset_account_payload.advanced_search(
                    page_size=total_count_adv,
                    account_number=account_number
                )
                rs = helper.SQL_ADSEARCH_FACACT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if account_number in rs['items'][i]['account_number']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {account_number}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_fixed_asset_account
    def test_006_view_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.view(
            id=id
        )
        rs = helper.SQL_VIEW_FACACT(fields_data)
        try:
            # check key
            assert 'account_number_def' in rs, f'Key \"account_number_def\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_account_name' in rs, f'Key \"fixed_asset_account_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'booking_currency_code' in rs, f'Key \"booking_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branchid' in rs, f'Key \"branchid\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'reference_number' in rs, f'Key \"reference_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_id' in rs, f'Key \"catalog_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_type' in rs, f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_classification' in rs, f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_method' in rs, f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_life_time' in rs, f'Key \"fixed_asset_life_time\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_life_time_unit' in rs, f'Key \"fixed_asset_life_time_unit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'provider_name' in rs, f'Key \"provider_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'owner' in rs, f'Key \"owner\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_status' in rs, f'Key \"fixed_asset_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_rate' in rs, f'Key \"depreciation_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'original_price' in rs, f'Key \"original_price\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'booking_amount' in rs, f'Key \"booking_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'net_booking_value' in rs, f'Key \"net_booking_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'accummulate_amount' in rs, f'Key \"accummulate_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expense_amount' in rs, f'Key \"expense_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'insurrance_value' in rs, f'Key \"insurrance_value\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'insurrance_fee' in rs, f'Key \"insurrance_fee\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'salvage_amount' in rs, f'Key \"salvage_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'income_amount' in rs, f'Key \"income_amount\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'week_debit' in rs, f'Key \"week_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'week_credit' in rs, f'Key \"week_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'month_debit' in rs, f'Key \"month_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'month_credit' in rs, f'Key \"month_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'quater_debit' in rs, f'Key \"quater_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'quater_credit' in rs, f'Key \"quater_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'semiannual_debit' in rs, f'Key \"semiannual_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'semiannual_credit' in rs, f'Key \"semiannual_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'year_debit' in rs, f'Key \"year_debit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'year_credit' in rs, f'Key \"year_credit\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_code' in rs, f'Key \"user_created_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_name' in rs, f'Key \"user_created_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_code' in rs, f'Key \"user_approved_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_name' in rs, f'Key \"user_approved_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'staff_code' in rs, f'Key \"staff_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'staff_name' in rs, f'Key \"staff_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_name' in rs, f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_name' in rs, f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id == rs['id'], f'Expected \'{id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number_def == rs['account_number_def'], f'Expected \'{account_number_def}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_account_name == rs['fixed_asset_account_name'], f'Expected \'{fixed_asset_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number == rs['reference_number'], f'Expected \'{reference_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method == rs['depreciation_method'], f'Expected \'{depreciation_method}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_life_time == rs['fixed_asset_life_time'], f'Expected \'{fixed_asset_life_time}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_life_time_unit == rs['fixed_asset_life_time_unit'], f'Expected \'{fixed_asset_life_time_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provider_name == rs['provider_name'], f'Expected \'{provider_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner == rs['owner'], f'Expected \'{owner}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = fixed_asset_account_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACACT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.fixed_asset_account_check_number_null
    def test_007_fixed_asset_account_check_number_null(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.update(
            id=id,
            fixed_asset_account_name=fixed_asset_account_name,
            reference_number=reference_number,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            provider_name=provider_name,
            owner=owner
        )
        rs = helper.SQL_UPDATE_FACACT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id == rs['id'], f'Expected \'{id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number_def == rs['account_number_def'], f'Expected \'{account_number_def}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_account_name == rs['fixed_asset_account_name'], f'Expected \'{fixed_asset_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reference_number == rs['reference_number'], f'Expected \'{reference_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method == rs['depreciation_method'], f'Expected \'{depreciation_method}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['fixed_asset_life_time'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provider_name == rs['provider_name'], f'Expected \'{provider_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert owner == rs['owner'], f'Expected \'{owner}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_fixed_asset_account
    def test_008_delete_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.delete(
            id=id
        )
        rs = helper.SQL_DELETE_FACACT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id == rs['id'], f'Expected \'{id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = fixed_asset_account_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACACT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count - 1) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_fixed_asset_account_check_page
    def test_009_simple_search_fixed_asset_account_check_page(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_SEARCH_FACACT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_fixed_asset_account_check_page
    def test_010_advanced_search_fixed_asset_account_check_page(self, user):
        helper = FixedAssetAccountHelper(user)
        fields_data = fixed_asset_account_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_ADSEARCH_FACACT(fields_data)
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