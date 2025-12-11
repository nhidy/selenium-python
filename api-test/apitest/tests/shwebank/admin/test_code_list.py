import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.helpers.admin.branch_helpers import BranchHelper
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.code_list_helpers import CodeListHelper
from apitest.src.payloads.admin.code_list_payload import CodeListPayload

code_list_payload = CodeListPayload()

code_id="CODE01"
code_name="code name"
caption="caption test"
english="english"
vietnamese="vietnamese"
laothian="laothian"
khmer="khmer"
myanmar="myanmar"
code_group="ACT"
code_index=1
code_value="val"
ftag="fta"
visible=1


code_id_update="CODE02"
code_name_update="code name test"
caption_update="update test caption"
english_update="english up"
vietnamese_update="vietnamese up"
laothian_update="laothian up"
khmer_update="khmer up"
myanmar_update="myanmar up"
code_group_update="DPT"
code_index_update=2
code_value_update="val up"
ftag_update="ftup"
visible_update=0

# check type number
number_checklist = {
    "code_index": {
        "data_type": int,
        "number_of_digits": 0
    },
    "visible": {
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

@pytest.mark.code_list
class TestCodeList(object):


    @pytest.mark.simple_search_code_list_before_add
    def test_001_simple_search_code_list_before_add(self, user):
        global total_count
        helper = CodeListHelper(user)
        fields_data = code_list_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_id' in rs['items'][0], f'Key \"code_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_name' in rs['items'][0], f'Key \"code_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'caption' in rs['items'][0], f'Key \"caption\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_group' in rs['items'][0], f'Key \"code_group\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_index' in rs['items'][0], f'Key \"code_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'ftag' in rs['items'][0], f'Key \"ftag\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'visible' in rs['items'][0], f'Key \"visible\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_code_list_before_add
    def test_002_advanced_search_code_list_before_add(self, user):
        helper = CodeListHelper(user)
        fields_data = code_list_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_CODE_LIST(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_id' in rs['items'][0], f'Key \"code_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_name' in rs['items'][0], f'Key \"code_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'caption' in rs['items'][0], f'Key \"caption\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_group' in rs['items'][0], f'Key \"code_group\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'code_index' in rs['items'][0], f'Key \"code_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'ftag' in rs['items'][0], f'Key \"ftag\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'visible' in rs['items'][0], f'Key \"visible\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_code_list
    def test_003_add_code_list(self, user):
        global id_new
        id_new = 0
        helper = CodeListHelper(user)
        fields_data = code_list_payload.add(
            code_id=code_id,
            code_name=code_name,
            caption=caption,
            english=english,
            vietnamese=vietnamese,
            laothian=laothian,
            khmer=khmer,
            myanmar=myanmar,
            code_group=code_group,
            code_index=code_index,
            code_value=code_value,
            ftag=ftag,
            visible=visible
        )
        rs = helper.ADM_INSERT_CODE_LIST(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert code_id == rs['code_id'], f'Expected \'{code_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_name == rs['code_name'], f'Expected \'{code_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert caption == rs['caption'], f'Expected \'{caption}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert english == rs['english'], f'Expected \'{english}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese == rs['vietnamese'], f'Expected \'{vietnamese}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laothian == rs['laothian'], f'Expected \'{laothian}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer == rs['khmer'], f'Expected \'{khmer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert myanmar == rs['myanmar'], f'Expected \'{myanmar}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_group == rs['code_group'], f'Expected \'{code_group}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_index == rs['code_index'], f'Expected \'{code_index}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_value == rs['code_value'], f'Expected \'{code_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ftag == rs['ftag'], f'Expected \'{ftag}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert visible == rs['visible'], f'Expected \'{visible}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = code_list_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_code_list_after_add
    def test_004_simple_search_code_list_after_add(self, user):
        search_rs = False
        helper = CodeListHelper(user)
        fields_data = code_list_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = code_list_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
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


    @pytest.mark.advanced_search_code_list_after_add
    def test_005_advanced_search_code_list_after_add(self, user):
        search_rs = False
        helper = CodeListHelper(user)
        fields_data = code_list_payload.advanced_search(
            page_size=50,
            caption=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_CODE_LIST(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = code_list_payload.advanced_search(
                    page_size=total_count_adv,
                    caption=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_CODE_LIST(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['caption']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_code_list
    def test_006_update_code_list(self, user):
        helper = CodeListHelper(user)
        fields_data = code_list_payload.update(
            id=id_new,
            code_id=code_id_update,
            code_name=code_name_update,
            caption=caption_update,
            english=english_update,
            vietnamese=vietnamese_update,
            laothian=laothian_update,
            khmer=khmer_update,
            myanmar=myanmar_update,
            code_group=code_group_update,
            code_index=code_index_update,
            code_value=code_value_update,
            ftag=ftag_update,
            visible=visible_update
        )
        rs = helper.ADM_UPDATE_CODE_LIST(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_id == rs['code_id'], f'Expected \'{code_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_name == rs['code_name'], f'Expected \'{code_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            assert caption_update == rs['caption'], f'Expected \'{caption_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert english_update == rs['english'], f'Expected \'{english_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese_update == rs['vietnamese'], f'Expected \'{vietnamese_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laothian_update == rs['laothian'], f'Expected \'{laothian_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer_update == rs['khmer'], f'Expected \'{khmer_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert myanmar_update == rs['myanmar'], f'Expected \'{myanmar_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_group_update == rs['code_group'], f'Expected \'{code_group_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_index_update == rs['code_index'], f'Expected \'{code_index_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_value_update == rs['code_value'], f'Expected \'{code_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ftag_update == rs['ftag'], f'Expected \'{ftag_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert visible_update == rs['visible'], f'Expected \'{visible_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_code_list
    def test_007_delete_code_list(self, user):
        helper = CodeListHelper(user)
        fields_data = code_list_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_CODE_LIST(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = code_list_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_code_list
    def test_008_view_code_list(self, user):
        helper = CodeListHelper(user)
        fields_data = code_list_payload.add(
            code_id=code_id,
            code_name=code_name,
            caption=caption,
            english=english,
            vietnamese=vietnamese,
            laothian=laothian,
            khmer=khmer,
            myanmar=myanmar,
            code_group=code_group,
            code_index=code_index,
            code_value=code_value,
            ftag=ftag,
            visible=visible
        )
        rs = helper.ADM_INSERT_CODE_LIST(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = code_list_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_CODE_LIST(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_id == rs['code_id'], f'Expected \'{code_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_name == rs['code_name'], f'Expected \'{code_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert caption == rs['caption'], f'Expected \'{caption}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert english == rs['english'], f'Expected \'{english}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese == rs['vietnamese'], f'Expected \'{vietnamese}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laothian == rs['laothian'], f'Expected \'{laothian}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer == rs['khmer'], f'Expected \'{khmer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert myanmar == rs['myanmar'], f'Expected \'{myanmar}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_group == rs['code_group'], f'Expected \'{code_group}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_index == rs['code_index'], f'Expected \'{code_index}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert code_value == rs['code_value'], f'Expected \'{code_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ftag == rs['ftag'], f'Expected \'{ftag}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert visible == rs['visible'], f'Expected \'{visible}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = code_list_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = code_list_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_CODE_LIST(fields_data)
            # check total_count search all after delete
            fields_data = code_list_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_code_list_check_page
    def test_009_simple_search_code_list_check_page(self, user):
        helper = BranchHelper(user)
        fields_data = code_list_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_code_list_check_page
    def test_010_advanced_search_code_list_check_page(self, user):
        helper = BranchHelper(user)
        fields_data = code_list_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_BRANCH(fields_data)
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