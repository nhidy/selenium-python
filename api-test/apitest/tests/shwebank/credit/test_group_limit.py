from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.group_limit_helpers import GroupLimitHelper
from apitest.src.payloads.credit.group_limit_payload import GroupLimitPayload

group_limit_payload = GroupLimitPayload()

group_limit_name="group limit name test"
currency_code="KHR"
credit_limit=10000.56


group_limit_code_update="0999000004"
group_limit_name_update="group limit name test update"
currency_code_update="USD"
credit_limit_update=1000000.36


# check type number
number_checklist = {
    "credit_limit": {
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

@pytest.mark.group_limit
class TestGroupLimit(object):


    @pytest.mark.simple_search_group_limit_before_add
    def test_001_simple_search_group_limit_before_add(self, user):
        global total_count
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.simple_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
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


    @pytest.mark.advanced_search_group_limit_before_add
    def test_002_advanced_search_group_limit_before_add(self, user):
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.advanced_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_ADV_CRDGRPLM(fields_data)
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


    @pytest.mark.add_group_limit
    def test_003_add_group_limit(self, user):
        global id_new, group_limit_code_new
        id_new = 0
        group_limit_code_new = ''
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.add(
            group_limit_name=group_limit_name,
            currency_code=currency_code,
            credit_limit=credit_limit
        )
        rs = helper.CRD_INSERT_CRDGRPLM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'group_limit_code' in rs, f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            group_limit_code_new = rs['group_limit_code']
            # check result
            assert group_limit_name == rs['group_limit_name'], f'Expected \'{group_limit_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_limit == rs['credit_limit'], f'Expected \'{credit_limit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = group_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_group_limit_after_add
    def test_004_simple_search_group_limit_after_add(self, user):
        search_rs = False
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = group_limit_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
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


    @pytest.mark.advanced_search_group_limit_after_add
    def test_005_advanced_search_group_limit_after_add(self, user):
        search_rs = False
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.advanced_search(
            page_size=50,
            group_limit_name=search_text
        )
        rs = helper.CRD_SEARCH_ADV_CRDGRPLM(fields_data)
        try:
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = group_limit_payload.advanced_search(
                    page_size=total_count_adv,
                    group_limit_name=search_text
                )
                rs = helper.CRD_SEARCH_ADV_CRDGRPLM(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['group_limit_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_group_limit
    def test_006_update_group_limit(self, user):
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.update(
            id=id_new,
            group_limit_code=group_limit_code_update,
            group_limit_name=group_limit_name_update,
            currency_code=currency_code_update,
            credit_limit=credit_limit_update
        )
        rs = helper.CRD_UPDATE_CRDGRPLM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_name_update == rs['group_limit_name'], f'Expected \'{group_limit_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_limit_update == rs['credit_limit'], f'Expected \'{credit_limit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert group_limit_code_new == rs['group_limit_code'], f'Expected \'{group_limit_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_group_limit
    def test_007_delete_group_limit(self, user):
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.delete(
            id=id_new
        )
        rs = helper.CRD_DELETE_CRDGRPLM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = group_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_group_limit
    def test_008_view_group_limit(self, user):
        helper = GroupLimitHelper(user)
        fields_data = group_limit_payload.add(
            group_limit_name=group_limit_name,
            currency_code=currency_code,
            credit_limit=credit_limit
        )
        rs = helper.CRD_INSERT_CRDGRPLM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'group_limit_code' in rs, f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            group_limit_code_new = rs['group_limit_code']
            
            fields_data = group_limit_payload.view(
                id=id_new
            )
            rs = helper.CRD_VIEW_CRDGRPLM(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_code_new == rs['group_limit_code'], f'Expected \'{group_limit_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_name == rs['group_limit_name'], f'Expected \'{group_limit_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_limit == rs['credit_limit'], f'Expected \'{credit_limit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = group_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = group_limit_payload.delete(
                id=id_new
            )
            rs = helper.CRD_DELETE_CRDGRPLM(fields_data)
            # check total_count search all after delete
            fields_data = group_limit_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDGRPLM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'