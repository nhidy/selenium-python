import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.user_role_helpers import UserRoleHelper
from apitest.src.payloads.admin.user_role_payload import UserRolePayload

user_role_payload = UserRolePayload()

rolename="Role test"
userrolestatus="Y"
roletemplatedid=1

# check type number
number_checklist = {
    "roletemplatedid": {
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

@pytest.mark.user_role
class TestUserRole(object):


    @pytest.mark.add_user_role
    def test_001_add_user_role(self, user):
        global id_new
        id_new = 0
        helper = UserRoleHelper(user)
        fields_data = user_role_payload.add(
            rolename=rolename,
            userrolestatus=userrolestatus,
            roletemplatedid=roletemplatedid
        )
        rs = helper.ADM_INSERT_USER_ROLE(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert rolename == rs['rolename'], f'Expected \'{rolename}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert userrolestatus == rs['userrolestatus'], f'Expected \'{userrolestatus}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert roletemplatedid == rs['roletemplatedid'], f'Expected \'{roletemplatedid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_user_role
    def test_002_view_user_role(self, user):
        helper = UserRoleHelper(user)
        fields_data = user_role_payload.view(
            id=id_new
        )
        rs = helper.ADM_VIEW_USER_ROLE(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rolename == rs['rolename'], f'Expected \'{rolename}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert userrolestatus == rs['userrolestatus'], f'Expected \'{userrolestatus}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert roletemplatedid == rs['roletemplatedid'], f'Expected \'{roletemplatedid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_user_role
    def test_003_delete_user_role(self, user):
        helper = UserRoleHelper(user)
        fields_data = user_role_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_USER_ROLE(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'