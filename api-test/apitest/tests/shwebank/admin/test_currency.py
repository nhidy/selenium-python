import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.currency_helpers import CurrencyHelper
from apitest.src.payloads.admin.currency_payload import CurrencyPayload

currency_payload = CurrencyPayload()

currency_id="AAA"
short_currency_id="88"
currency_name1="currency name 1"
currency_name2="currency name 2"
currency_name3="currency name 3"
currency_number=0
master_name1="master name 1"
master_name2="master name 2"
master_name3="master name 3"
decimal_name1="decimal name 1"
decimal_name2="decimal name 2"
decimal_name3="decimal name 3"
decimal_digits=2
rounding_digits=2
status_of_currency="N"
order=0


currency_id_update="BBB" # currency_id không được sửa
short_currency_id_update="98"
currency_name1_update="currency name 1 up"
currency_name2_update="currency name 2 up"
currency_name3_update="currency name 3 up"
currency_number_update=2
master_name1_update="master name 1 up"
master_name2_update="master name 2 up"
master_name3_update="master name 3 up"
decimal_name1_update="decimal name 1 up"
decimal_name2_update="decimal name 2 up"
decimal_name3_update="decimal name 3 up"
decimal_digits_update=3
rounding_digits_update=5
status_of_currency_update="B"
order_update=2

# check type number
number_checklist = {
    "currency_number": {
        "data_type": int,
        "number_of_digits": 0
    },
    "decimal_digits": {
        "data_type": int,
        "number_of_digits": 0
    },
    "order": {
        "data_type": int,
        "number_of_digits": 0
    },
    "rounding_digits": {
        "data_type": int,
        "number_of_digits": 0
    },
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text='AAA'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.currency
class TestCurrency(object):


    @pytest.mark.simple_search_currency_before_add
    def test_001_simple_search_currency_before_add(self, user):
        global total_count
        helper = CurrencyHelper(user)
        fields_data = currency_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_id' in rs['items'][0], f'Key \"currency_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'short_currency_id' in rs['items'][0], f'Key \"short_currency_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_number' in rs['items'][0], f'Key \"currency_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'status_of_currency' in rs['items'][0], f'Key \"status_of_currency\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'order' in rs['items'][0], f'Key \"order\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_currency_before_add
    def test_002_advanced_search_currency_before_add(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_CURRENCY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_id' in rs['items'][0], f'Key \"currency_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'short_currency_id' in rs['items'][0], f'Key \"short_currency_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_number' in rs['items'][0], f'Key \"currency_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'status_of_currency' in rs['items'][0], f'Key \"status_of_currency\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'order' in rs['items'][0], f'Key \"order\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_currency
    def test_003_add_currency(self, user):
        global id_new
        id_new = 0
        helper = CurrencyHelper(user)
        fields_data = currency_payload.add(
            currency_id=currency_id,
            short_currency_id=short_currency_id,
            currency_name1=currency_name1,
            currency_name2=currency_name2,
            currency_name3=currency_name3,
            currency_number=currency_number,
            master_name1=master_name1,
            master_name2=master_name2,
            master_name3=master_name3,
            decimal_name1=decimal_name1,
            decimal_name2=decimal_name2,
            decimal_name3=decimal_name3,
            decimal_digits=decimal_digits,
            rounding_digits=rounding_digits,
            status_of_currency=status_of_currency,
            order=order
        )
        rs = helper.ADM_INSERT_CURRENCY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert currency_id == rs['currency_id'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_currency_id == rs['short_currency_id'], f'Expected \'{short_currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name1 == rs['currency_name1'], f'Expected \'{currency_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name2 == rs['currency_name2'], f'Expected \'{currency_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name3 == rs['currency_name3'], f'Expected \'{currency_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_number == rs['currency_number'], f'Expected \'{currency_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name1 == rs['master_name1'], f'Expected \'{master_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name2 == rs['master_name2'], f'Expected \'{master_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name3 == rs['master_name3'], f'Expected \'{master_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name1 == rs['decimal_name1'], f'Expected \'{decimal_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name2 == rs['decimal_name2'], f'Expected \'{decimal_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name3 == rs['decimal_name3'], f'Expected \'{decimal_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_digits == rs['decimal_digits'], f'Expected \'{decimal_digits}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rounding_digits == rs['rounding_digits'], f'Expected \'{rounding_digits}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_currency == rs['status_of_currency'], f'Expected \'{status_of_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = currency_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_currency_after_add
    def test_004_simple_search_currency_after_add(self, user):
        search_rs = False
        helper = CurrencyHelper(user)
        fields_data = currency_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = currency_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
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


    @pytest.mark.advanced_search_currency_after_add
    def test_005_advanced_search_currency_after_add(self, user):
        search_rs = False
        helper = CurrencyHelper(user)
        fields_data = currency_payload.advanced_search(
            page_size=50,
            currency_id=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_CURRENCY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = currency_payload.advanced_search(
                    page_size=total_count_adv,
                    currency_id=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_CURRENCY(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['currency_id']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_currency
    def test_006_update_currency(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.update(
            id=id_new,
            currency_id=currency_id_update,
            short_currency_id=short_currency_id_update,
            currency_name1=currency_name1_update,
            currency_name2=currency_name2_update,
            currency_name3=currency_name3_update,
            currency_number=currency_number_update,
            master_name1=master_name1_update,
            master_name2=master_name2_update,
            master_name3=master_name3_update,
            decimal_name1=decimal_name1_update,
            decimal_name2=decimal_name2_update,
            decimal_name3=decimal_name3_update,
            decimal_digits=decimal_digits_update,
            rounding_digits=rounding_digits_update,
            status_of_currency=status_of_currency_update,
            order=order_update
        )
        rs = helper.ADM_UPDATE_CURRENCY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # currency_id khong duoc sua
            assert currency_id == rs['currency_id'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_currency_id_update == rs['short_currency_id'], f'Expected \'{short_currency_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name1_update == rs['currency_name1'], f'Expected \'{currency_name1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name2_update == rs['currency_name2'], f'Expected \'{currency_name2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name3_update == rs['currency_name3'], f'Expected \'{currency_name3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_number_update == rs['currency_number'], f'Expected \'{currency_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name1_update == rs['master_name1'], f'Expected \'{master_name1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name2_update == rs['master_name2'], f'Expected \'{master_name2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name3_update == rs['master_name3'], f'Expected \'{master_name3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name1_update == rs['decimal_name1'], f'Expected \'{decimal_name1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name2_update == rs['decimal_name2'], f'Expected \'{decimal_name2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name3_update == rs['decimal_name3'], f'Expected \'{decimal_name3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_digits_update == rs['decimal_digits'], f'Expected \'{decimal_digits_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rounding_digits_update == rs['rounding_digits'], f'Expected \'{rounding_digits_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_currency_update == rs['status_of_currency'], f'Expected \'{status_of_currency_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order_update == rs['order'], f'Expected \'{order_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_currency
    def test_007_delete_currency(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_CURRENCY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = currency_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_currency
    def test_008_view_currency(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.add(
            currency_id=currency_id,
            short_currency_id=short_currency_id,
            currency_name1=currency_name1,
            currency_name2=currency_name2,
            currency_name3=currency_name3,
            currency_number=currency_number,
            master_name1=master_name1,
            master_name2=master_name2,
            master_name3=master_name3,
            decimal_name1=decimal_name1,
            decimal_name2=decimal_name2,
            decimal_name3=decimal_name3,
            decimal_digits=decimal_digits,
            rounding_digits=rounding_digits,
            status_of_currency=status_of_currency,
            order=order
        )
        rs = helper.ADM_INSERT_CURRENCY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = currency_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_CURRENCY(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_id == rs['currency_id'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_currency_id == rs['short_currency_id'], f'Expected \'{short_currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name1 == rs['currency_name1'], f'Expected \'{currency_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name2 == rs['currency_name2'], f'Expected \'{currency_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_name3 == rs['currency_name3'], f'Expected \'{currency_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_number == rs['currency_number'], f'Expected \'{currency_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name1 == rs['master_name1'], f'Expected \'{master_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name2 == rs['master_name2'], f'Expected \'{master_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_name3 == rs['master_name3'], f'Expected \'{master_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name1 == rs['decimal_name1'], f'Expected \'{decimal_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name2 == rs['decimal_name2'], f'Expected \'{decimal_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_name3 == rs['decimal_name3'], f'Expected \'{decimal_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_digits == rs['decimal_digits'], f'Expected \'{decimal_digits}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rounding_digits == rs['rounding_digits'], f'Expected \'{rounding_digits}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_currency == rs['status_of_currency'], f'Expected \'{status_of_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = currency_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = currency_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_CURRENCY(fields_data)
            # check total_count search all after delete
            fields_data = currency_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_currency_check_page
    def test_009_simple_search_currency_check_page(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_currency_check_page
    def test_010_advanced_search_currency_check_page(self, user):
        helper = CurrencyHelper(user)
        fields_data = currency_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_CURRENCY(fields_data)
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