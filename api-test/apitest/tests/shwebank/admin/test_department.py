import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.department_helpers import DepartmentHelper
from apitest.src.payloads.admin.department_payload import DepartmentPayload

department_payload = DepartmentPayload()

branch_id=999
department_name="department name test"

department_code_update="00003" #Khong duoc sua
branch_id_update=2
department_name_update="update department name test"

# check type number
number_checklist = {
    "branch_id": {
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

@pytest.mark.department
class TestDepartment(object):


    @pytest.mark.simple_search_department_before_add
    def test_001_simple_search_department_before_add(self, user):
        global total_count
        helper = DepartmentHelper(user)
        fields_data = department_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_code' in rs['items'][0], f'Key \"department_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_name' in rs['items'][0], f'Key \"department_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_department_before_add
    def test_002_advanced_search_department_before_add(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_DEPARTMENT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_code' in rs['items'][0], f'Key \"department_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_name' in rs['items'][0], f'Key \"department_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_department
    def test_003_add_department(self, user):
        global id_new, department_code
        id_new = 0
        department_code = ''
        helper = DepartmentHelper(user)
        fields_data = department_payload.add(
            branch_id=branch_id,
            department_name=department_name
        )
        rs = helper.ADM_INSERT_DEPARTMENT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'department_code' in rs, f'Key \"department_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            department_code = rs['department_code']
            
            # check result
            assert branch_id == rs['branch_id'], f'Expected \'{branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_name == rs['department_name'], f'Expected \'{department_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = department_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_department_after_add
    def test_004_simple_search_department_after_add(self, user):
        search_rs = False
        helper = DepartmentHelper(user)
        fields_data = department_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = department_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
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


    @pytest.mark.advanced_search_department_after_add
    def test_005_advanced_search_department_after_add(self, user):
        search_rs = False
        helper = DepartmentHelper(user)
        fields_data = department_payload.advanced_search(
            page_size=50,
            department_name=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_DEPARTMENT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = department_payload.advanced_search(
                    page_size=total_count_adv,
                    department_name=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_DEPARTMENT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['department_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_department
    def test_006_update_department(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.update(
            id=id_new,
            department_code=department_code_update,
            branch_id=branch_id_update,
            department_name=department_name_update
        )
        rs = helper.ADM_UPDATE_DEPARTMENT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_code == rs['department_code'], f'Expected \'{department_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_id_update == rs['branch_id'], f'Expected \'{branch_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_name_update == rs['department_name'], f'Expected \'{department_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_department
    def test_007_delete_department(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_DEPARTMENT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = department_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_department
    def test_008_view_department(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.add(
            branch_id=branch_id,
            department_name=department_name
        )
        rs = helper.ADM_INSERT_DEPARTMENT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'department_code' in rs, f'Key \"department_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            department_code = rs['department_code']
            fields_data = department_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_DEPARTMENT(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_code == rs['department_code'], f'Expected \'{department_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_id == rs['branch_id'], f'Expected \'{branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_name == rs['department_name'], f'Expected \'{department_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = department_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = department_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_DEPARTMENT(fields_data)
            # check total_count search all after delete
            fields_data = department_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_department_check_page
    def test_009_simple_search_department_check_page(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_department_check_page
    def test_010_advanced_search_department_check_page(self, user):
        helper = DepartmentHelper(user)
        fields_data = department_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_DEPARTMENT(fields_data)
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