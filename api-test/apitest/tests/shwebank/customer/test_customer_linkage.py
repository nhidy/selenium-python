from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.customer.customer_linkage_helpers import CustomerLinkageHelper
from apitest.src.payloads.customer.customer_linkage_payload import CustomerLinkagePayload
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload

customer_linkage_payload = CustomerLinkagePayload()
customer_single_payload = CustomerSinglePayload()

master_customer_id=2
linkage_description="desc test"
detail_customer_id=1
linkage_type="AN"
linkage_status="N"
group_limit_code="GRPLMCD001"
linkage_credit_line=200.56
currency_code="USD"

linkage_description_update="update test desc"
detail_customer_id_update=3
linkage_type_update="OR"
linkage_status_update="B"
group_limit_code_update="GRPLMCD002"
linkage_credit_line_update=200.21
currency_code_update="KHR"

# check type number
number_checklist = {
    "linkage_credit_line": {
        "data_type": float,
        "number_of_digits": 2
    },
    "master_customer_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "detail_customer_id": {
        "data_type": int,
        "number_of_digits": 0
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

@pytest.mark.customer_linkage
class TestCustomerLinkage(object):


    @pytest.mark.simple_search_customer_linkage_before_add
    def test_001_simple_search_customer_linkage_before_add(self, user):
        global total_count
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.simple_search(
            page_size=5
        )
        rs = helper.SQL_SEARCH_CTMLKG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_code' in rs['items'][0], f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'master_customer_code' in rs['items'][0], f'Key \"master_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'master_customer_name' in rs['items'][0], f'Key \"master_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_description' in rs['items'][0], f'Key \"linkage_description\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_credit_line' in rs['items'][0], f'Key \"linkage_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_limit_code' in rs['items'][0], f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_linkage_before_add
    def test_002_advanced_search_customer_linkage_before_add(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.advanced_search(
            page_size=5
        )
        rs = helper.SQL_ADSEARCH_CTMLKG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_code' in rs['items'][0], f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'master_customer_code' in rs['items'][0], f'Key \"master_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'master_customer_name' in rs['items'][0], f'Key \"master_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_description' in rs['items'][0], f'Key \"linkage_description\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'linkage_credit_line' in rs['items'][0], f'Key \"linkage_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_limit_code' in rs['items'][0], f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_customer_linkage
    def test_003_add_customer_linkage(self, user):
        global id_new, linkage_code_new
        id_new = 0
        linkage_code_new = ''
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.add(
            master_customer_id=master_customer_id,
            linkage_description=linkage_description,
            detail_customer_id=detail_customer_id,
            linkage_type=linkage_type,
            linkage_status=linkage_status,
            group_limit_code=group_limit_code,
            linkage_credit_line=linkage_credit_line,
            currency_code=currency_code
        )
        rs = helper.SQL_INSERT_CTMLKG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'linkage_code' in rs, f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            linkage_code_new = rs['linkage_code']
            # check key
            assert 'master_customer_id' in rs, f'Key \"master_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_code' in rs, f'Key \"master_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_name' in rs, f'Key \"master_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_description' in rs, f'Key \"linkage_description\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_id' in rs, f'Key \"detail_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_code' in rs, f'Key \"detail_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_name' in rs, f'Key \"detail_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_type' in rs, f'Key \"linkage_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_status' in rs, f'Key \"linkage_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_limit_code' in rs, f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_credit_line' in rs, f'Key \"linkage_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check result
            assert master_customer_id == rs['master_customer_id'], f'Expected \'{master_customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_description == rs['linkage_description'], f'Expected \'{linkage_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert detail_customer_id == rs['detail_customer_id'], f'Expected \'{detail_customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_type == rs['linkage_type'], f'Expected \'{linkage_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_status == rs['linkage_status'], f'Expected \'{linkage_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_code == rs['group_limit_code'], f'Expected \'{group_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_credit_line == rs['linkage_credit_line'], f'Expected \'{linkage_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = customer_linkage_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_CTMLKG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_linkage_after_add
    def test_004_simple_search_customer_linkage_after_add(self, user):
        search_rs = False
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.SQL_SEARCH_CTMLKG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
            #     assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # else:
            #     total_count_sp = rs['total_count']
            #     # show all items
            #     fields_data = customer_linkage_payload.simple_search(
            #         page_size=total_count_sp,
            #         search_text=search_text
            #     )
            #     rs = helper.SQL_SEARCH_CTMLKG(fields_data)
            #     # check value
            #     total_item = len(rs['items'])
            #     if total_item > 0:
            #         for i in range(total_item): 
            #             list_item = rs['items'][i].items()
            #             for key, value in list_item:
            #                 if search_text in str(value):
            #                     search_rs = True
            #                     break
            #         assert search_rs, f'Search with simple search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     else:
            #         assert total_item != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_linkage_after_add
    def test_005_advanced_search_customer_linkage_after_add(self, user):
        search_rs = False
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.advanced_search(
            page_size=50,
            linkage_description=search_text
        )
        rs = helper.SQL_ADSEARCH_CTMLKG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
            #     assert search_rs, f'Search with advanced search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # else:
            #     total_count_adv = rs['total_count']
            #     # show all items
            #     fields_data = customer_linkage_payload.advanced_search(
            #         page_size=total_count_adv,
            #         linkage_description=search_text
            #     )
            #     rs = helper.SQL_ADSEARCH_CTMLKG(fields_data)
            #     # check value
            #     total_item = len(rs['items'])
            #     if total_item > 0:
            #         for i in range(total_item):
            #             if search_text in rs['items'][i]['linkage_description']:
            #                 search_rs = True
            #                 break
            #         assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     else:
            #         assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_customer_linkage
    def test_006_update_customer_linkage(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.update(
            id=id_new,
            linkage_description=linkage_description_update,
            detail_customer_id=detail_customer_id_update,
            linkage_type=linkage_type_update,
            linkage_status=linkage_status_update,
            group_limit_code=group_limit_code_update,
            linkage_credit_line=linkage_credit_line_update,
            currency_code=currency_code_update
        )
        rs = helper.SQL_UPDATE_CTMLKG(fields_data)
        try:
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_code' in rs, f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_id' in rs, f'Key \"master_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_code' in rs, f'Key \"master_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_name' in rs, f'Key \"master_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_description' in rs, f'Key \"linkage_description\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_id' in rs, f'Key \"detail_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_code' in rs, f'Key \"detail_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_name' in rs, f'Key \"detail_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_type' in rs, f'Key \"linkage_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_status' in rs, f'Key \"linkage_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_limit_code' in rs, f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_credit_line' in rs, f'Key \"linkage_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_code_new == rs['linkage_code'], f'Expected \'{linkage_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_description_update == rs['linkage_description'], f'Expected \'{linkage_description_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert detail_customer_id_update == rs['detail_customer_id'], f'Expected \'{detail_customer_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_type_update == rs['linkage_type'], f'Expected \'{linkage_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_status_update == rs['linkage_status'], f'Expected \'{linkage_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_code_update == rs['group_limit_code'], f'Expected \'{group_limit_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_credit_line_update == rs['linkage_credit_line'], f'Expected \'{linkage_credit_line_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_customer_linkage
    def test_007_delete_customer_linkage(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.delete(
            id=id_new
        )
        rs = helper.SQL_DELETE_CTMLKG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = customer_linkage_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTMLKG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_customer_linkage
    def test_008_view_customer_linkage(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.add(
            master_customer_id=master_customer_id,
            linkage_description=linkage_description,
            detail_customer_id=detail_customer_id,
            linkage_type=linkage_type,
            linkage_status=linkage_status,
            group_limit_code=group_limit_code,
            linkage_credit_line=linkage_credit_line,
            currency_code=currency_code
        )
        rs = helper.SQL_INSERT_CTMLKG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'linkage_code' in rs, f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            linkage_code_new = rs['linkage_code']
            fields_data = customer_linkage_payload.view(
                id=id_new
            )
            rs = helper.SQL_VIEW_CTMLKG(fields_data)
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_code' in rs, f'Key \"linkage_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_id' in rs, f'Key \"master_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_code' in rs, f'Key \"master_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'master_customer_name' in rs, f'Key \"master_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_description' in rs, f'Key \"linkage_description\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_id' in rs, f'Key \"detail_customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_code' in rs, f'Key \"detail_customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'detail_customer_name' in rs, f'Key \"detail_customer_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_type' in rs, f'Key \"linkage_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_status' in rs, f'Key \"linkage_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_limit_code' in rs, f'Key \"group_limit_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'linkage_credit_line' in rs, f'Key \"linkage_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check result
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_code_new == rs['linkage_code'], f'Expected \'{linkage_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert master_customer_id == rs['master_customer_id'], f'Expected \'{master_customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_description == rs['linkage_description'], f'Expected \'{linkage_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert detail_customer_id == rs['detail_customer_id'], f'Expected \'{detail_customer_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_type == rs['linkage_type'], f'Expected \'{linkage_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_status == rs['linkage_status'], f'Expected \'{linkage_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_limit_code == rs['group_limit_code'], f'Expected \'{group_limit_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert linkage_credit_line == rs['linkage_credit_line'], f'Expected \'{linkage_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = customer_linkage_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTMLKG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = customer_linkage_payload.delete(
                id=id_new
            )
            rs = helper.SQL_DELETE_CTMLKG(fields_data)
            # check total_count search all after delete
            fields_data = customer_linkage_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTMLKG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_linkage_check_page
    def test_009_simple_search_customer_linkage_check_page(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_SEARCH_CTMLKG(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_linkage_check_page
    def test_010_advanced_search_customer_linkage_check_page(self, user):
        helper = CustomerLinkageHelper(user)
        fields_data = customer_linkage_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_ADSEARCH_CTMLKG(fields_data)
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