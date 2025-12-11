from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.sub_product_limit_helpers import SubProductLimitHelper
from apitest.src.payloads.credit.sub_product_limit_payload import SubProductLimitPayload

sub_product_limit_payload = SubProductLimitPayload()

id_new=1

sub_product_limit_code="110000131000601"
sub_product_limit_name_update="sub product name update"
currency_code_update="USD"
limit_amount_update=150000.36
credit_facility_update="LA"


# check type number
number_checklist = {
    "limit_amount_update": {
        "data_type": float,
        "number_of_digits": 3
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

@pytest.mark.sub_product_limit
class TestSubProductLimit(object):


    @pytest.mark.simple_search_sub_product_limit
    def test_001_simple_search_sub_product_limit(self, user):
        global total_count
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.simple_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_SP_CRDSPL(fields_data)
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


    @pytest.mark.advanced_search_sub_product_limit
    def test_002_advanced_search_sub_product_limit(self, user):
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.advanced_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_ADV_CRDSPL(fields_data)
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


    @pytest.mark.update_sub_product_limit
    def test_003_update_sub_product_limit(self, user):
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.update(
            id=id_new,
            sub_product_limit_code="sub_product_limit_code",
            sub_product_limit_name=sub_product_limit_name_update,
            currency_code=currency_code_update,
            limit_amount=limit_amount_update,
            credit_facility=credit_facility_update
        )
        rs = helper.CRD_UPDATE_CRDSPL(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_product_limit_code == rs['sub_product_limit_code'], f'Expected \'{sub_product_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_product_limit_name_update == rs['sub_product_limit_name'], f'Expected \'{sub_product_limit_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_amount_update == rs['limit_amount'], f'Expected \'{limit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_facility_update == rs['credit_facility'], f'Expected \'{credit_facility_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_sub_product_limit_after_update
    def test_004_simple_search_sub_product_limit_after_update(self, user):
        search_rs = False
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.CRD_SEARCH_SP_CRDSPL(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if total_count == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = sub_product_limit_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.CRD_SEARCH_SP_CRDSPL(fields_data)
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


    @pytest.mark.advanced_search_sub_product_limit_after_update
    def test_005_advanced_search_sub_product_limit_after_update(self, user):
        search_rs = False
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.advanced_search(
            page_size=50,
            sub_product_limit_name=search_text
        )
        rs = helper.CRD_SEARCH_ADV_CRDSPL(fields_data)
        try:
            if total_count == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = sub_product_limit_payload.advanced_search(
                    page_size=total_count_adv,
                    sub_product_limit_name=search_text
                )
                rs = helper.CRD_SEARCH_ADV_CRDSPL(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['sub_product_limit_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_sub_product_limit
    def test_006_view_sub_product_limit(self, user):
        helper = SubProductLimitHelper(user)
        fields_data = sub_product_limit_payload.view(
            id=id_new
        )
        rs = helper.CRD_VIEW_CRDSPL(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_product_limit_code == rs['sub_product_limit_code'], f'Expected \'{sub_product_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_product_limit_name_update == rs['sub_product_limit_name'], f'Expected \'{sub_product_limit_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert limit_amount_update == rs['limit_amount'], f'Expected \'{limit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_facility_update == rs['credit_facility'], f'Expected \'{credit_facility_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = sub_product_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDSPL(fields_data)
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