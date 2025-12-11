import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.branch_helpers import BranchHelper
from apitest.src.payloads.admin.branch_payload import BranchPayload

branch_payload = BranchPayload()

old_branch_id=""
branch_name="branch name test"
branch_address="27 Nguyen Huu Tho"
branch_phone=""
home="home"
office="office"
cell="cell"
facsimile="facsimile"
telex="telex"
tax_code=""
base_currency_code="USD"
base_currency_name="USD"
local_currency_code="USD"
local_currency_name="USD"
bic="bic"
domestic_bank_code="domestic code"
internal_code="internal code"
country="KH"
main_language="en"
time_zone_of_branch=7
thousand_separate_character=","
decimal_separate_character="."
date_format_for_short="yyDDmm"
long_date_format=""
time_format="HH"
online="Y"
ud_field1="ud field1"
long_branch_name="long branch name"

old_branch_id_update=""
branch_name_update="update branch name test"
branch_address_update="27 Nguyen Huu Tho"
branch_phone_update=""
home_update="home up"
office_update="office up"
cell_update="cell up"
facsimile_update="facsimile up"
telex_update="telex up"
tax_code_update=""
base_currency_code_update="USD"
base_currency_name_update="USD"
local_currency_code_update="USD"
local_currency_name_update="USD"
bic_update="bic up"
domestic_bank_code_update="domestic code up"
internal_code_update="internal code up"
country_update="KH"
main_language_update="en"
time_zone_of_branch_update=7
thousand_separate_character_update=","
decimal_separate_character_update="."
date_format_for_short_update="yyDDmm"
long_date_format_update=""
time_format_update="HH"
online_update="Y"
ud_field1_update="ud field1 up"
long_branch_name_update="long branch name up"

# check type number
number_checklist = {
    "time_zone_of_branch": {
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

@pytest.mark.branch
class TestBranch(object):


    @pytest.mark.simple_search_branch_before_add
    def test_001_simple_search_branch_before_add(self, user):
        global total_count
        helper = BranchHelper(user)
        fields_data = branch_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_code' in rs['items'][0], f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_address' in rs['items'][0], f'Key \"branch_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'base_currency_code' in rs['items'][0], f'Key \"base_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'online' in rs['items'][0], f'Key \"online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_branch_before_add
    def test_002_advanced_search_branch_before_add(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_code' in rs['items'][0], f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_address' in rs['items'][0], f'Key \"branch_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'base_currency_code' in rs['items'][0], f'Key \"base_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'online' in rs['items'][0], f'Key \"online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_branch
    def test_003_add_branch(self, user):
        global id_new, branch_code_new
        id_new = 0
        branch_code_new = ''
        helper = BranchHelper(user)
        fields_data = branch_payload.add(
            old_branch_id=old_branch_id,
            branch_name=branch_name,
            branch_address=branch_address,
            branch_phone=branch_phone,
            home=home,
            office=office,
            cell=cell,
            facsimile=facsimile,
            telex=telex,
            tax_code=tax_code,
            base_currency_code=base_currency_code,
            base_currency_name=base_currency_name,
            local_currency_code=local_currency_code,
            local_currency_name=local_currency_name,
            bic=bic,
            domestic_bank_code=domestic_bank_code,
            internal_code=internal_code,
            country=country,
            main_language=main_language,
            time_zone_of_branch=time_zone_of_branch,
            thousand_separate_character=thousand_separate_character,
            decimal_separate_character=decimal_separate_character,
            date_format_for_short=date_format_for_short,
            long_date_format=long_date_format,
            time_format=time_format,
            online=online,
            ud_field1=ud_field1,
            long_branch_name=long_branch_name
        )
        rs = helper.ADM_INSERT_BRANCH(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            branch_code_new = rs['branch_code']
            # check result
            assert old_branch_id == rs['old_branch_id'], f'Expected \'{old_branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_name == rs['branch_name'], f'Expected \'{branch_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_address == rs['branch_address'], f'Expected \'{branch_address}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_phone == rs['branch_phone'], f'Expected \'{branch_phone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home == rs['home'], f'Expected \'{home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office == rs['office'], f'Expected \'{office}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell == rs['cell'], f'Expected \'{cell}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile == rs['facsimile'], f'Expected \'{facsimile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex == rs['telex'], f'Expected \'{telex}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tax_code == rs['tax_code'], f'Expected \'{tax_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_code == rs['base_currency_code'], f'Expected \'{base_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_name == rs['base_currency_name'], f'Expected \'{base_currency_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_code == rs['local_currency_code'], f'Expected \'{local_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_name == rs['local_currency_name'], f'Expected \'{local_currency_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bic == rs['bic'], f'Expected \'{bic}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert domestic_bank_code == rs['domestic_bank_code'], f'Expected \'{domestic_bank_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert internal_code == rs['internal_code'], f'Expected \'{internal_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone_of_branch == rs['time_zone_of_branch'], f'Expected \'{time_zone_of_branch}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format_for_short == rs['date_format_for_short'], f'Expected \'{date_format_for_short}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format == rs['long_date_format'], f'Expected \'{long_date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format == rs['time_format'], f'Expected \'{time_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert online == rs['online'], f'Expected \'{online}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ud_field1 == rs['ud_field1'], f'Expected \'{ud_field1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_branch_name == rs['long_branch_name'], f'Expected \'{long_branch_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = branch_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_branch_after_add
    def test_004_simple_search_branch_after_add(self, user):
        search_rs = False
        helper = BranchHelper(user)
        fields_data = branch_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = branch_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
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


    @pytest.mark.advanced_search_branch_after_add
    def test_005_advanced_search_branch_after_add(self, user):
        search_rs = False
        helper = BranchHelper(user)
        fields_data = branch_payload.advanced_search(
            page_size=50,
            branch_name=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = branch_payload.advanced_search(
                    page_size=total_count_adv,
                    branch_name=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_BRANCH(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['branch_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_branch
    def test_006_update_branch(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.update(
            id=id_new,
            old_branch_id=old_branch_id_update,
            branch_name=branch_name_update,
            branch_address=branch_address_update,
            branch_phone=branch_phone_update,
            home=home_update,
            office=office_update,
            cell=cell_update,
            facsimile=facsimile_update,
            telex=telex_update,
            tax_code=tax_code_update,
            base_currency_code=base_currency_code_update,
            base_currency_name=base_currency_name_update,
            local_currency_code=local_currency_code_update,
            local_currency_name=local_currency_name_update,
            bic=bic_update,
            domestic_bank_code=domestic_bank_code_update,
            internal_code=internal_code_update,
            country=country_update,
            main_language=main_language_update,
            time_zone_of_branch=time_zone_of_branch_update,
            thousand_separate_character=thousand_separate_character_update,
            decimal_separate_character=decimal_separate_character_update,
            date_format_for_short=date_format_for_short_update,
            long_date_format=long_date_format_update,
            time_format=time_format_update,
            online=online_update,
            ud_field1=ud_field1_update,
            long_branch_name=long_branch_name_update
        )
        rs = helper.ADM_UPDATE_BRANCH(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code_new == rs['branch_code'], f'Expected \'{branch_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            assert old_branch_id_update == rs['old_branch_id'], f'Expected \'{old_branch_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_name_update == rs['branch_name'], f'Expected \'{branch_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_address_update == rs['branch_address'], f'Expected \'{branch_address_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_phone_update == rs['branch_phone'], f'Expected \'{branch_phone_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home_update == rs['home'], f'Expected \'{home_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office_update == rs['office'], f'Expected \'{office_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell_update == rs['cell'], f'Expected \'{cell_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile_update == rs['facsimile'], f'Expected \'{facsimile_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex_update == rs['telex'], f'Expected \'{telex_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tax_code_update == rs['tax_code'], f'Expected \'{tax_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_code_update == rs['base_currency_code'], f'Expected \'{base_currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_name_update == rs['base_currency_name'], f'Expected \'{base_currency_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_code_update == rs['local_currency_code'], f'Expected \'{local_currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_name_update == rs['local_currency_name'], f'Expected \'{local_currency_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bic_update == rs['bic'], f'Expected \'{bic_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert domestic_bank_code_update == rs['domestic_bank_code'], f'Expected \'{domestic_bank_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert internal_code_update == rs['internal_code'], f'Expected \'{internal_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_update == rs['country'], f'Expected \'{country_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language_update == rs['main_language'], f'Expected \'{main_language_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone_of_branch_update == rs['time_zone_of_branch'], f'Expected \'{time_zone_of_branch_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character_update == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character_update == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format_for_short_update == rs['date_format_for_short'], f'Expected \'{date_format_for_short_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format_update == rs['long_date_format'], f'Expected \'{long_date_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format_update == rs['time_format'], f'Expected \'{time_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert online_update == rs['online'], f'Expected \'{online_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ud_field1_update == rs['ud_field1'], f'Expected \'{ud_field1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_branch_name_update == rs['long_branch_name'], f'Expected \'{long_branch_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_branch
    def test_007_delete_branch(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_BRANCH(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = branch_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_branch
    def test_008_view_branch(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.add(
            old_branch_id=old_branch_id,
            branch_name=branch_name,
            branch_address=branch_address,
            branch_phone=branch_phone,
            home=home,
            office=office,
            cell=cell,
            facsimile=facsimile,
            telex=telex,
            tax_code=tax_code,
            base_currency_code=base_currency_code,
            base_currency_name=base_currency_name,
            local_currency_code=local_currency_code,
            local_currency_name=local_currency_name,
            bic=bic,
            domestic_bank_code=domestic_bank_code,
            internal_code=internal_code,
            country=country,
            main_language=main_language,
            time_zone_of_branch=time_zone_of_branch,
            thousand_separate_character=thousand_separate_character,
            decimal_separate_character=decimal_separate_character,
            date_format_for_short=date_format_for_short,
            long_date_format=long_date_format,
            time_format=time_format,
            online=online,
            ud_field1=ud_field1,
            long_branch_name=long_branch_name
        )
        rs = helper.ADM_INSERT_BRANCH(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            branch_code_new = rs['branch_code']
            fields_data = branch_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_BRANCH(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code_new == rs['branch_code'], f'Expected \'{branch_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert old_branch_id == rs['old_branch_id'], f'Expected \'{old_branch_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_name == rs['branch_name'], f'Expected \'{branch_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_address == rs['branch_address'], f'Expected \'{branch_address}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_phone == rs['branch_phone'], f'Expected \'{branch_phone}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert home == rs['home'], f'Expected \'{home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert office == rs['office'], f'Expected \'{office}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert cell == rs['cell'], f'Expected \'{cell}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert facsimile == rs['facsimile'], f'Expected \'{facsimile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert telex == rs['telex'], f'Expected \'{telex}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tax_code == rs['tax_code'], f'Expected \'{tax_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_code == rs['base_currency_code'], f'Expected \'{base_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert base_currency_name == rs['base_currency_name'], f'Expected \'{base_currency_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_code == rs['local_currency_code'], f'Expected \'{local_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert local_currency_name == rs['local_currency_name'], f'Expected \'{local_currency_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bic == rs['bic'], f'Expected \'{bic}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert domestic_bank_code == rs['domestic_bank_code'], f'Expected \'{domestic_bank_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert internal_code == rs['internal_code'], f'Expected \'{internal_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_zone_of_branch == rs['time_zone_of_branch'], f'Expected \'{time_zone_of_branch}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thousand_separate_character == rs['thousand_separate_character'], f'Expected \'{thousand_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert decimal_separate_character == rs['decimal_separate_character'], f'Expected \'{decimal_separate_character}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_format_for_short == rs['date_format_for_short'], f'Expected \'{date_format_for_short}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_date_format == rs['long_date_format'], f'Expected \'{long_date_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert time_format == rs['time_format'], f'Expected \'{time_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert online == rs['online'], f'Expected \'{online}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ud_field1 == rs['ud_field1'], f'Expected \'{ud_field1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert long_branch_name == rs['long_branch_name'], f'Expected \'{long_branch_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = branch_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = branch_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_BRANCH(fields_data)
            # check total_count search all after delete
            fields_data = branch_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_branch_check_page
    def test_009_simple_search_branch_check_page(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.simple_search(
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


    @pytest.mark.advanced_search_branch_check_page
    def test_010_advanced_search_branch_check_page(self, user):
        helper = BranchHelper(user)
        fields_data = branch_payload.advanced_search(
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