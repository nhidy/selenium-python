from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.user_policy_helpers import UserPolicyHelper
from apitest.src.payloads.admin.user_policy_payload import UserPolicyPayload

user_policy_payload = UserPolicyPayload()

descr="policy test"
effective_from=datetime.fromisoformat("2022-03-01").strftime('%Y-%m-%dT%H:%M:%S')
effective_to=datetime.fromisoformat("2022-03-01").strftime('%Y-%m-%dT%H:%M:%S')
enforce_password_history=0
maximum_password_age=0
minimum_password_length=0
password_complexity_requirements="x"
password_have_special_symbol="l"
password_have_upper_case="u"
password_have_symbol="s"
password_have_number="n"
can_login_from=""
can_login_to=""
lockout_tthrs=""

descr_update="update policy test"
effective_from_update=datetime.fromisoformat("2021-04-21").strftime('%Y-%m-%dT%H:%M:%S')
effective_to_update=datetime.fromisoformat("2021-04-21").strftime('%Y-%m-%dT%H:%M:%S')
enforce_password_history_update=9
maximum_password_age_update=4
minimum_password_length_update=8
password_complexity_requirements_update="x"
password_have_special_symbol_update="2"
password_have_upper_case_update="v"
password_have_symbol_update="a"
password_have_number_update="A"
can_login_from_update=""
can_login_to_update=""
lockout_tthrs_update=3

# check type number
number_checklist = {
    "enforce_password_history": {
        "data_type": int,
        "number_of_digits": 0
    },
    "maximum_password_age": {
        "data_type": int,
        "number_of_digits": 0
    },
    "pwdagemin": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_password_length": {
        "data_type": int,
        "number_of_digits": 0
    },
    "lockout_tthrs": {
        "data_type": int,
        "number_of_digits": 0
    },
    "lkoutthrs": {
        "data_type": int,
        "number_of_digits": 0
    },
    "resetlkout": {
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

@pytest.mark.user_policy
class TestUserPolicy(object):


    @pytest.mark.simple_search_user_policy_before_add
    def test_001_simple_search_user_policy_before_add(self, user):
        global total_count
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.simple_search(
            page_size=50
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
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


    @pytest.mark.advanced_search_user_policy_before_add
    def test_002_advanced_search_user_policy_before_add(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.advanced_search(
            page_size=50
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_POLICY(fields_data)
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


    @pytest.mark.add_user_policy
    def test_003_add_user_policy(self, user):
        global id_new
        id_new = 0
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.add(
            descr=descr,
            effective_from=effective_from,
            effective_to=effective_to,
            enforce_password_history=enforce_password_history,
            maximum_password_age=maximum_password_age,
            minimum_password_length=minimum_password_length,
            password_complexity_requirements=password_complexity_requirements,
            password_have_special_symbol=password_have_special_symbol,
            password_have_upper_case=password_have_upper_case,
            password_have_symbol=password_have_symbol,
            password_have_number=password_have_number,
            can_login_from=can_login_from,
            can_login_to=can_login_to,
            lockout_tthrs=lockout_tthrs
        )
        rs = helper.ADM_INSERT_USER_POLICY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert descr == rs['descr'], f'Expected \'{descr}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_from == rs['effective_from'], f'Expected \'{effective_from}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_to == rs['effective_to'], f'Expected \'{effective_to}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert enforce_password_history == rs['enforce_password_history'], f'Expected \'{enforce_password_history}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert maximum_password_age == rs['maximum_password_age'], f'Expected \'{maximum_password_age}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert minimum_password_length == rs['minimum_password_length'], f'Expected \'{minimum_password_length}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_complexity_requirements == rs['password_complexity_requirements'], f'Expected \'{password_complexity_requirements}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_special_symbol == rs['password_have_special_symbol'], f'Expected \'{password_have_special_symbol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_upper_case == rs['password_have_upper_case'], f'Expected \'{password_have_upper_case}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_symbol == rs['password_have_symbol'], f'Expected \'{password_have_symbol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_number == rs['password_have_number'], f'Expected \'{password_have_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_from == rs['can_login_from'], f'Expected \'{can_login_from}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_to == rs['can_login_to'], f'Expected \'{can_login_to}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lockout_tthrs == rs['lockout_tthrs'], f'Expected \'{lockout_tthrs}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = user_policy_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_user_policy_after_add
    def test_004_simple_search_user_policy_after_add(self, user):
        search_rs = False
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = user_policy_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
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


    @pytest.mark.advanced_search_user_policy_after_add
    def test_005_advanced_search_user_policy_after_add(self, user):
        search_rs = False
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.advanced_search(
            page_size=50,
            descr=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_POLICY(fields_data)
        try:
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = user_policy_payload.advanced_search(
                    page_size=total_count_adv,
                    descr=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_USER_POLICY(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['descr']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_user_policy
    def test_006_update_user_policy(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.update(
            id=id_new,
            descr=descr_update,
            effective_from=effective_from_update,
            effective_to=effective_to_update,
            enforce_password_history=enforce_password_history_update,
            maximum_password_age=maximum_password_age_update,
            minimum_password_length=minimum_password_length_update,
            password_complexity_requirements=password_complexity_requirements_update,
            password_have_special_symbol=password_have_special_symbol_update,
            password_have_upper_case=password_have_upper_case_update,
            password_have_symbol=password_have_symbol_update,
            password_have_number=password_have_number_update,
            can_login_from=can_login_from_update,
            can_login_to=can_login_to_update,
            lockout_tthrs=lockout_tthrs_update,
        )
        rs = helper.ADM_UPDATE_USER_POLICY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert descr_update == rs['descr'], f'Expected \'{descr_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_from_update == rs['effective_from'], f'Expected \'{effective_from_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_to_update == rs['effective_to'], f'Expected \'{effective_to_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert enforce_password_history_update == rs['enforce_password_history'], f'Expected \'{enforce_password_history_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert maximum_password_age_update == rs['maximum_password_age'], f'Expected \'{maximum_password_age_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert minimum_password_length_update == rs['minimum_password_length'], f'Expected \'{minimum_password_length_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_complexity_requirements_update == rs['password_complexity_requirements'], f'Expected \'{password_complexity_requirements_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_special_symbol_update == rs['password_have_special_symbol'], f'Expected \'{password_have_special_symbol_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_upper_case_update == rs['password_have_upper_case'], f'Expected \'{password_have_upper_case_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_symbol_update == rs['password_have_symbol'], f'Expected \'{password_have_symbol_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_number_update == rs['password_have_number'], f'Expected \'{password_have_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_from_update == rs['can_login_from'], f'Expected \'{can_login_from_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_to_update == rs['can_login_to'], f'Expected \'{can_login_to_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lockout_tthrs_update == rs['lockout_tthrs'], f'Expected \'{lockout_tthrs_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_user_policy
    def test_007_delete_user_policy(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_USER_POLICY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = user_policy_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_user_policy
    def test_008_view_user_policy(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.add(
            descr=descr,
            effective_from=effective_from,
            effective_to=effective_to,
            enforce_password_history=enforce_password_history,
            maximum_password_age=maximum_password_age,
            minimum_password_length=minimum_password_length,
            password_complexity_requirements=password_complexity_requirements,
            password_have_special_symbol=password_have_special_symbol,
            password_have_upper_case=password_have_upper_case,
            password_have_symbol=password_have_symbol,
            password_have_number=password_have_number,
            can_login_from=can_login_from,
            can_login_to=can_login_to,
            lockout_tthrs=lockout_tthrs,
        )
        rs = helper.ADM_INSERT_USER_POLICY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = user_policy_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_USER_POLICY(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert descr == rs['descr'], f'Expected \'{descr}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_from == rs['effective_from'], f'Expected \'{effective_from}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert effective_to == rs['effective_to'], f'Expected \'{effective_to}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert enforce_password_history == rs['enforce_password_history'], f'Expected \'{enforce_password_history}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert maximum_password_age == rs['maximum_password_age'], f'Expected \'{maximum_password_age}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert minimum_password_length == rs['minimum_password_length'], f'Expected \'{minimum_password_length}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_complexity_requirements == rs['password_complexity_requirements'], f'Expected \'{password_complexity_requirements}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_special_symbol == rs['password_have_special_symbol'], f'Expected \'{password_have_special_symbol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_upper_case == rs['password_have_upper_case'], f'Expected \'{password_have_upper_case}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_symbol == rs['password_have_symbol'], f'Expected \'{password_have_symbol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_have_number == rs['password_have_number'], f'Expected \'{password_have_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_from == rs['can_login_from'], f'Expected \'{can_login_from}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert can_login_to == rs['can_login_to'], f'Expected \'{can_login_to}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lockout_tthrs == rs['lockout_tthrs'], f'Expected \'{lockout_tthrs}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = user_policy_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = user_policy_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_USER_POLICY(fields_data)
            # check total_count search all after delete
            fields_data = user_policy_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_user_policy_check_page
    def test_009_simple_search_user_policy_check_page(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_user_policy_check_page
    def test_010_advanced_search_user_policy_check_page(self, user):
        helper = UserPolicyHelper(user)
        fields_data = user_policy_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_POLICY(fields_data)
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