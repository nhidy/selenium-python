from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.user_account_helpers import UserAccountHelper
from apitest.src.payloads.admin.user_account_payload import UserAccountPayload

user_account_payload = UserAccountPayload()

old_user_id=""
user_name="user name test"
login_name="loginnametest"
branch_id=999
department_id=1
cashier=0
officer=0
operation_staff=0
dealer=0
inter_branch_user=0
branch_manager=0
main_language="en"
home="home"
office="office"
cell="cell"
facsimile="facsimile"
telex="telex"
user_phone=""
remark=""
user_account_status="N"
time_zone=7
thousand_separate_character=","
decimal_separate_character="."
date_format="D1"
long_date_format="D1"
time_format="T1"
policy_id=0
expire_date=datetime.fromisoformat("2022-03-01").strftime('%Y-%m-%dT%H:%M:%S')

user_code_update="00928"
old_user_id_update=""
user_name_update="user name test update"
login_name_update="logintestup"
branch_id_update=848
department_id_update=1
cashier_update=1
officer_update=1
operation_staff_update=1
dealer_update=1
inter_branch_user_update=1
branch_manager_update=1
main_language_update="en"
home_update="h up"
office_update="o up"
cell_update="c up"
facsimile_update="f up"
telex_update="t up"
user_phone_update="up"
remark_update="up"
user_account_status_update="N"
time_zone_update=7
thousand_separate_character_update=","
decimal_separate_character_update="."
date_format_update="D1"
long_date_format_update="D1"
time_format_update="T1"
policy_id_update=0
expire_date_update=datetime.fromisoformat("2022-04-21").strftime('%Y-%m-%dT%H:%M:%S')

# check type number
number_checklist = {
    "branch_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "department_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "cashier": {
        "data_type": int,
        "number_of_digits": 0
    },
    "officer": {
        "data_type": int,
        "number_of_digits": 0
    },
    "operation_staff": {
        "data_type": int,
        "number_of_digits": 0
    },
    "dealer": {
        "data_type": int,
        "number_of_digits": 0
    },
    "inter_branch_user": {
        "data_type": int,
        "number_of_digits": 0
    },
    "branch_manager": {
        "data_type": int,
        "number_of_digits": 0
    },
    "time_zone": {
        "data_type": int,
        "number_of_digits": 0
    },
    "policy_id": {
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

@pytest.mark.user_account
class TestUserAccount(object):


    @pytest.mark.simple_search_user_account_before_add
    def test_001_simple_search_user_account_before_add(self, user):
        global total_count
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'user_code' in rs['items'][0], f'Key \"user_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'user_name' in rs['items'][0], f'Key \"user_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'login_name' in rs['items'][0], f'Key \"login_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_name' in rs['items'][0], f'Key \"department_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'status' in rs['items'][0], f'Key \"status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'is_online' in rs['items'][0], f'Key \"is_online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                # assert 'email' in rs['items'][0], f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_user_account_before_add
    def test_002_advanced_search_user_account_before_add(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'user_code' in rs['items'][0], f'Key \"user_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'user_name' in rs['items'][0], f'Key \"user_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'login_name' in rs['items'][0], f'Key \"login_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'department_name' in rs['items'][0], f'Key \"department_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'status' in rs['items'][0], f'Key \"status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'is_online' in rs['items'][0], f'Key \"is_online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                # assert 'email' in rs['items'][0], f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_user_account
    def test_003_add_user_account(self, user):
        global id_new, user_code_new
        id_new = 0
        user_code_new = ''
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.add(
            old_user_id=old_user_id,
            user_name=user_name,
            login_name=login_name,
            branch_id=branch_id,
            department_id=department_id,
            cashier=cashier,
            officer=officer,
            operation_staff=operation_staff,
            dealer=dealer,
            inter_branch_user=inter_branch_user,
            branch_manager=branch_manager,
            main_language=main_language,
            home=home,
            office=office,
            cell=cell,
            facsimile=facsimile,
            telex=telex,
            user_phone=user_phone,
            remark=remark,
            user_account_status=user_account_status,
            time_zone=time_zone,
            thousand_separate_character=thousand_separate_character,
            decimal_separate_character=decimal_separate_character,
            date_format=date_format,
            long_date_format=long_date_format,
            time_format=time_format,
            policy_id=policy_id,
            expire_date=expire_date
        )
        rs = helper.ADM_INSERT_USER_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'user_code' in rs, f'Key \"user_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            user_code_new = rs['user_code']
            # check result
            assert old_user_id == rs['old_user_id'], f'Expected \'{old_user_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name == rs['user_name'], f'Expected \'{user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert login_name == rs['login_name'], f'Expected \'{login_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_id == rs['branch_id'], f'Expected \'{branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_id == rs['department_id'], f'Expected \'{department_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cashier == rs['cashier'], f'Expected \'{cashier}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert officer == rs['officer'], f'Expected \'{officer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert operation_staff == rs['operation_staff'], f'Expected \'{operation_staff}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert dealer == rs['dealer'], f'Expected \'{dealer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert inter_branch_user == rs['inter_branch_user'], f'Expected \'{inter_branch_user}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_manager == rs['branch_manager'], f'Expected \'{branch_manager}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home == rs['home'], f'Expected \'{home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office == rs['office'], f'Expected \'{office}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell == rs['cell'], f'Expected \'{cell}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile == rs['facsimile'], f'Expected \'{facsimile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex == rs['telex'], f'Expected \'{telex}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_phone == rs['user_phone'], f'Expected \'{user_phone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark == rs['remark'], f'Expected \'{remark}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_account_status == rs['user_account_status'], f'Expected \'{user_account_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone == rs['time_zone'], f'Expected \'{time_zone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format == rs['date_format'], f'Expected \'{date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format == rs['long_date_format'], f'Expected \'{long_date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format == rs['time_format'], f'Expected \'{time_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_id == rs['policy_id'], f'Expected \'{policy_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date == rs['expire_date'], f'Expected \'{expire_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = user_account_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_user_account_after_add
    def test_004_simple_search_user_account_after_add(self, user):
        search_rs = False
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = user_account_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
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


    @pytest.mark.advanced_search_user_account_after_add
    def test_005_advanced_search_user_account_after_add(self, user):
        search_rs = False
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.advanced_search(
            page_size=50,
            user_name=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_ACCOUNT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = user_account_payload.advanced_search(
                    page_size=total_count_adv,
                    user_name=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_USER_ACCOUNT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['user_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_user_account
    def test_006_update_user_account(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.update(
            id=id_new,
            user_code=user_code_update,
            old_user_id=old_user_id_update,
            user_name=user_name_update,
            login_name=login_name_update,
            branch_id=branch_id_update,
            department_id=department_id_update,
            cashier=cashier_update,
            officer=officer_update,
            operation_staff=operation_staff_update,
            dealer=dealer_update,
            inter_branch_user=inter_branch_user_update,
            branch_manager=branch_manager_update,
            main_language=main_language_update,
            home=home_update,
            office=office_update,
            cell=cell_update,
            facsimile=facsimile_update,
            telex=telex_update,
            user_phone=user_phone_update,
            remark=remark_update,
            user_account_status=user_account_status_update,
            time_zone=time_zone_update,
            thousand_separate_character=thousand_separate_character_update,
            decimal_separate_character=decimal_separate_character_update,
            date_format=date_format_update,
            long_date_format=long_date_format_update,
            time_format=time_format_update,
            policy_id=policy_id_update,
            expire_date=expire_date_update,
        )
        rs = helper.ADM_UPDATE_USER_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert old_user_id_update == rs['old_user_id'], f'Expected \'{old_user_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name_update == rs['user_name'], f'Expected \'{user_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert login_name_update == rs['login_name'], f'Expected \'{login_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_id_update == rs['branch_id'], f'Expected \'{branch_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_id_update == rs['department_id'], f'Expected \'{department_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cashier_update == rs['cashier'], f'Expected \'{cashier_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert officer_update == rs['officer'], f'Expected \'{officer_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert operation_staff_update == rs['operation_staff'], f'Expected \'{operation_staff_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert dealer_update == rs['dealer'], f'Expected \'{dealer_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert inter_branch_user_update == rs['inter_branch_user'], f'Expected \'{inter_branch_user_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_manager_update == rs['branch_manager'], f'Expected \'{branch_manager_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language_update == rs['main_language'], f'Expected \'{main_language_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home_update == rs['home'], f'Expected \'{home_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office_update == rs['office'], f'Expected \'{office_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell_update == rs['cell'], f'Expected \'{cell_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile_update == rs['facsimile'], f'Expected \'{facsimile_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex_update == rs['telex'], f'Expected \'{telex_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_phone_update == rs['user_phone'], f'Expected \'{user_phone_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_account_status_update == rs['user_account_status'], f'Expected \'{user_account_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone_update == rs['time_zone'], f'Expected \'{time_zone_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character_update == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character_update == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format_update == rs['date_format'], f'Expected \'{date_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format_update == rs['long_date_format'], f'Expected \'{long_date_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format_update == rs['time_format'], f'Expected \'{time_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_id_update == rs['policy_id'], f'Expected \'{policy_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date_update == rs['expire_date'], f'Expected \'{expire_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)

            assert user_code_new == rs['user_code'], f'Expected \'{user_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_user_account
    def test_007_delete_user_account(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_USER_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = user_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_user_account
    def test_008_view_user_account(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.add(
            old_user_id=old_user_id,
            user_name=user_name,
            login_name=login_name,
            branch_id=branch_id,
            department_id=department_id,
            cashier=cashier,
            officer=officer,
            operation_staff=operation_staff,
            dealer=dealer,
            inter_branch_user=inter_branch_user,
            branch_manager=branch_manager,
            main_language=main_language,
            home=home,
            office=office,
            cell=cell,
            facsimile=facsimile,
            telex=telex,
            user_phone=user_phone,
            remark=remark,
            user_account_status=user_account_status,
            time_zone=time_zone,
            thousand_separate_character=thousand_separate_character,
            decimal_separate_character=decimal_separate_character,
            date_format=date_format,
            long_date_format=long_date_format,
            time_format=time_format,
            policy_id=policy_id,
            expire_date=expire_date
        )
        rs = helper.ADM_INSERT_USER_ACCOUNT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'user_code' in rs, f'Key \"user_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            user_code_new = rs['user_code']
            fields_data = user_account_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_USER_ACCOUNT(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_code_new == rs['user_code'], f'Expected \'{user_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check result
            assert old_user_id == rs['old_user_id'], f'Expected \'{old_user_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name == rs['user_name'], f'Expected \'{user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert login_name == rs['login_name'], f'Expected \'{login_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_id == rs['branch_id'], f'Expected \'{branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert department_id == rs['department_id'], f'Expected \'{department_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cashier == rs['cashier'], f'Expected \'{cashier}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert officer == rs['officer'], f'Expected \'{officer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert operation_staff == rs['operation_staff'], f'Expected \'{operation_staff}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert dealer == rs['dealer'], f'Expected \'{dealer}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert inter_branch_user == rs['inter_branch_user'], f'Expected \'{inter_branch_user}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_manager == rs['branch_manager'], f'Expected \'{branch_manager}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home == rs['home'], f'Expected \'{home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office == rs['office'], f'Expected \'{office}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell == rs['cell'], f'Expected \'{cell}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile == rs['facsimile'], f'Expected \'{facsimile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex == rs['telex'], f'Expected \'{telex}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_phone == rs['user_phone'], f'Expected \'{user_phone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert remark == rs['remark'], f'Expected \'{remark}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_account_status == rs['user_account_status'], f'Expected \'{user_account_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone == rs['time_zone'], f'Expected \'{time_zone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format == rs['date_format'], f'Expected \'{date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format == rs['long_date_format'], f'Expected \'{long_date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format == rs['time_format'], f'Expected \'{time_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert policy_id == rs['policy_id'], f'Expected \'{policy_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date == rs['expire_date'], f'Expected \'{expire_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = user_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = user_account_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_USER_ACCOUNT(fields_data)
            # check total_count search all after delete
            fields_data = user_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_user_account_check_page
    def test_009_simple_search_user_account_check_page(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_user_account_check_page
    def test_010_advanced_search_user_account_check_page(self, user):
        helper = UserAccountHelper(user)
        fields_data = user_account_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_ACCOUNT(fields_data)
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