import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.accounting.account_group_detail_helpers import AccountGroupDetailHelper
from apitest.src.payloads.accounting.account_group_detail_payload import AccountGroupDetailPayload

account_group_detail_payload = AccountGroupDetailPayload()

module="DPT"
system_account_name="SYSTEM_ACCOUNT_TEST"
bank_define_account_name="account name test"

bank_define_account_name_update="account name test update"

# check type number
number_checklist = {
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text = 'test'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.account_group_detail
class TestAccountGroupDetail(object):


    @pytest.mark.simple_search_account_group_detail_before_add
    def test_001_simple_search_account_group_detail_before_add(self, user):
        global total_count
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.simple_search(
            page_size=5
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_account_group_detail_before_add
    def test_002_advanced_search_account_group_detail_before_add(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.advanced_search(
            page_size=5
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_ADVANCE(fields_data)
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


    @pytest.mark.add_account_group_detail
    def test_003_add_account_group_detail(self, user):
        global id_new
        id_new = 0
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.add(
            module=module,
            system_account_name=system_account_name,
            bank_define_account_name=bank_define_account_name
        )
        rs = helper.ACT_ACGRPDEFDTL_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert module == rs['module'], f'Expected \'{module}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert system_account_name == rs['system_account_name'], f'Expected \'{system_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_define_account_name == rs['bank_define_account_name'], f'Expected \'{bank_define_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = account_group_detail_payload.simple_search(
                page_size=5
            )
            rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_group_detail_after_add
    def test_004_simple_search_account_group_detail_after_add(self, user):
        search_rs = False
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = account_group_detail_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_account_group_detail_after_add
    def test_005_advanced_search_account_group_detail_after_add(self, user):
        search_rs = False
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.advanced_search(
            page_size=5,
            system_account_name=system_account_name
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_ADVANCE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{system_account_name}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = account_group_detail_payload.advanced_search(
                    page_size=total_count_adv,
                    system_account_name=system_account_name
                )
                rs = helper.ACT_ACGRPDEFDTL_SER_ADVANCE(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if system_account_name in rs['items'][i]['system_account_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {system_account_name}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_account_group_detail
    def test_006_update_account_group_detail(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.update(
            id=id_new,
            bank_define_account_name=bank_define_account_name_update
        )
        rs = helper.ACT_ACGRPDEFDTL_UPD(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert module == rs['module'], f'Expected \'{module}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert system_account_name == rs['system_account_name'], f'Expected \'{system_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_define_account_name_update == rs['bank_define_account_name'], f'Expected \'{bank_define_account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_account_group_detail
    def test_007_delete_account_group_detail(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.delete(
            id=id_new
        )
        rs = helper.ACT_ACGRPDEFDTL_DEL(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = account_group_detail_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_account_group_detail
    def test_008_view_account_group_detail(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.add(
            module=module,
            system_account_name=system_account_name,
            bank_define_account_name=bank_define_account_name
        )
        rs = helper.ACT_ACGRPDEFDTL_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = account_group_detail_payload.view(
                id=id_new
            )
            rs = helper.ACT_ACGRPDEFDTL_VIEW(fields_data)
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert module == rs['module'], f'Expected \'{module}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert system_account_name == rs['system_account_name'], f'Expected \'{system_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_define_account_name == rs['bank_define_account_name'], f'Expected \'{bank_define_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = account_group_detail_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = account_group_detail_payload.delete(
                id=id_new
            )
            rs = helper.ACT_ACGRPDEFDTL_DEL(fields_data)
            # check total_count search all after delete
            fields_data = account_group_detail_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_group_detail_check_page
    def test_009_simple_search_account_group_detail_check_page(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_account_group_detail_check_page
    def test_010_advanced_search_account_group_detail_check_page(self, user):
        helper = AccountGroupDetailHelper(user)
        fields_data = account_group_detail_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_ADVANCE(fields_data)
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