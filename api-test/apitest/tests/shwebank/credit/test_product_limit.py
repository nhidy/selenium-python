from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.product_limit_helpers import ProductLimitHelper
from apitest.src.payloads.credit.product_limit_payload import ProductLimitPayload

product_limit_payload = ProductLimitPayload()

product_limit_code="1100000310001"
customer_type="C"
customer_id=3
id_new=1

product_limit_name_update="product name test update"
limit_type_update="A"
currency_code_update="USD"
limit_amount_update=100000.48
product_status_update="B"
accounting_group_update=102
exchange_rate_update=0
secure_type_update=""
secure_rate_update=0

# check type number
number_checklist = {
    "limit_amount": {
        "data_type": float,
        "number_of_digits": 3
    },
    "accounting_group": {
        "data_type": int,
        "number_of_digits": 0
    },
    "customer_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "exchange_rate": {
        "data_type": float,
        "number_of_digits": 8
    },
    "secure_rate": {
        "data_type": float,
        "number_of_digits": 8
    },
    "id": {
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

@pytest.mark.product_limit
class TestProductLimit(object):


    @pytest.mark.simple_search_product_limit
    def test_001_simple_search_product_limit(self, user):
        global total_count
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.simple_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_SP_CRDPL(fields_data)
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


    @pytest.mark.advanced_search_product_limit_before_add
    def test_002_advanced_search_product_limit_before_add(self, user):
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.advanced_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_ADV_CRDPL(fields_data)
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


    @pytest.mark.update_product_limit
    def test_003_update_product_limit(self, user):
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.update(
            id=id_new,
            product_limit_code="product_limit_code_update",
            product_limit_name=product_limit_name_update,
            customer_type="B",
            customer_id=5,
            limit_type=limit_type_update,
            currency_code=currency_code_update,
            limit_amount=limit_amount_update,
            product_status=product_status_update,
            accounting_group=accounting_group_update,
            exchange_rate=exchange_rate_update,
            secure_type=secure_type_update,
            secure_rate=secure_rate_update
        )
        rs = helper.CRD_UPDATE_CRDPL(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert product_limit_code == rs['product_limit_code'], f'Expected \'{product_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_id == rs['customer_id'], f'Expected \'{customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            assert product_limit_name_update == rs['product_limit_name'], f'Expected \'{product_limit_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_type_update == rs['limit_type'], f'Expected \'{limit_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_amount_update == rs['limit_amount'], f'Expected \'{limit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert product_status_update == rs['product_status'], f'Expected \'{product_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_update == rs['accounting_group'], f'Expected \'{accounting_group_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert exchange_rate_update == rs['exchange_rate'], f'Expected \'{exchange_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_type_update == rs['secure_type'], f'Expected \'{secure_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_rate_update == rs['secure_rate'], f'Expected \'{secure_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_product_limit_after_update
    def test_004_simple_search_product_limit_after_update(self, user):
        search_rs = False
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.CRD_SEARCH_SP_CRDPL(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if total_count == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = product_limit_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.CRD_SEARCH_SP_CRDPL(fields_data)
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


    @pytest.mark.advanced_search_product_limit_after_update
    def test_005_advanced_search_product_limit_after_update(self, user):
        search_rs = False
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.advanced_search(
            page_size=50,
            product_limit_name=search_text
        )
        rs = helper.CRD_SEARCH_ADV_CRDPL(fields_data)
        try:
            if total_count == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = product_limit_payload.advanced_search(
                    page_size=total_count_adv,
                    product_limit_name=search_text
                )
                rs = helper.CRD_SEARCH_ADV_CRDPL(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['product_limit_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_product_limit
    def test_006_view_product_limit(self, user):
        helper = ProductLimitHelper(user)
        fields_data = product_limit_payload.view(
            id=id_new
        )
        rs = helper.CRD_VIEW_CRDPL(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert product_limit_code == rs['product_limit_code'], f'Expected \'{product_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_id == rs['customer_id'], f'Expected \'{customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            assert product_limit_name_update == rs['product_limit_name'], f'Expected \'{product_limit_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_type_update == rs['limit_type'], f'Expected \'{limit_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_amount_update == rs['limit_amount'], f'Expected \'{limit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert product_status_update == rs['product_status'], f'Expected \'{product_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_update == rs['accounting_group'], f'Expected \'{accounting_group_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert exchange_rate_update == rs['exchange_rate'], f'Expected \'{exchange_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_type_update == rs['secure_type'], f'Expected \'{secure_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_rate_update == rs['secure_rate'], f'Expected \'{secure_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = product_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDPL(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'