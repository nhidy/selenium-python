import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.accounting.extension_account_helpers import ExtensionAccountHelper
from apitest.src.payloads.accounting.extension_account_payload import ExtensionAccountPayload

extension_account_payload = ExtensionAccountPayload()

accounting_group_id=333
replace_by_code="{REF}"
replace_by="12365"
account_name="TEST"
sector="S"
resident_status="R"
categories="A"
account_resident="R"
subproduct="S"

replace_by_code_update="{UPE}"
replace_by_update="65785"
account_name_update="TEST_UP"
sector_update="A"
resident_status_update="N"
categories_update="C1"
account_resident_update="E"
subproduct_update="W"

# check type number
number_checklist = {
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text = 'TEST'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.extension_account
class TestExtensionAccount(object):


    @pytest.mark.simple_search_extension_account_before_add
    def test_001_simple_search_extension_account_before_add(self, user):
        global total_count
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.simple_search(
            page_size=5
        )
        rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_extension_account_before_add
    def test_002_advanced_search_extension_account_before_add(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.advanced_search(
            page_size=5
        )
        rs = helper.ACT_ACGLDEF_SER_ADVANCE(fields_data)
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


    @pytest.mark.add_extension_account
    def test_003_add_extension_account(self, user):
        global id_new
        id_new = 0
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.add(
            accounting_group_id=accounting_group_id,
            replace_by_code=replace_by_code,
            replace_by=replace_by,
            account_name=account_name,
            sector=sector,
            resident_status=resident_status,
            categories=categories,
            account_resident=account_resident,
            subproduct=subproduct
        )
        rs = helper.ACT_ACGLDEF_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert accounting_group_id == rs['accounting_group_id'], f'Expected \'{accounting_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by_code == rs['replace_by_code'], f'Expected \'{replace_by_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by == rs['replace_by'], f'Expected \'{replace_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name == rs['account_name'], f'Expected \'{account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['condition']['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident_status == rs['condition']['resident_status'], f'Expected \'{resident_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['condition']['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_resident == rs['condition']['account_resident'], f'Expected \'{account_resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct == rs['condition']['subproduct'], f'Expected \'{subproduct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = extension_account_payload.simple_search(
                page_size=5
            )
            rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_extension_account_after_add
    def test_004_simple_search_extension_account_after_add(self, user):
        search_rs = False
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.simple_search(
            page_size=5,
            search_text=account_name
        )
        rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = extension_account_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_extension_account_after_add
    def test_005_advanced_search_extension_account_after_add(self, user):
        search_rs = False
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.advanced_search(
            page_size=50,
            account_name=account_name
        )
        rs = helper.ACT_ACGLDEF_SER_ADVANCE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{account_name}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = extension_account_payload.advanced_search(
                    page_size=total_count_adv,
                    account_name=account_name
                )
                rs = helper.ACT_ACGLDEF_SER_ADVANCE(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if account_name in rs['items'][i]['account_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {account_name}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_extension_account
    def test_006_update_extension_account(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.update(
            id=id_new,
            accounting_group_id=accounting_group_id,
            replace_by_code=replace_by_code_update,
            replace_by=replace_by_update,
            account_name=account_name_update,
            sector=sector_update,
            resident_status=resident_status_update,
            categories=categories_update,
            account_resident=account_resident_update,
            subproduct=subproduct_update
        )
        rs = helper.ACT_ACGLDEF_UPD(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by_code_update == rs['replace_by_code'], f'Expected \'{replace_by_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by_update == rs['replace_by'], f'Expected \'{replace_by_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector_update == rs['condition']['sector'], f'Expected \'{sector_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident_status_update == rs['condition']['resident_status'], f'Expected \'{resident_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories_update == rs['condition']['categories'], f'Expected \'{categories_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_resident_update == rs['condition']['account_resident'], f'Expected \'{account_resident_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct_update == rs['condition']['subproduct'], f'Expected \'{subproduct_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_id == rs['accounting_group_id'], f'Expected \'{accounting_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_extension_account
    def test_007_delete_extension_account(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.delete(
            id=id_new
        )
        rs = helper.ACT_ACGLDEF_DEL(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = extension_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_extension_account
    def test_008_view_extension_account(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.add(
            accounting_group_id=accounting_group_id,
            replace_by_code=replace_by_code,
            replace_by=replace_by,
            account_name=account_name,
            sector=sector,
            resident_status=resident_status,
            categories=categories,
            account_resident=account_resident,
            subproduct=subproduct
        )
        rs = helper.ACT_ACGLDEF_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = extension_account_payload.view(
                id=id_new
            )
            rs = helper.ACT_ACGLDEF_VIEW(fields_data)
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_id == rs['accounting_group_id'], f'Expected \'{accounting_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by_code == rs['replace_by_code'], f'Expected \'{replace_by_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert replace_by == rs['replace_by'], f'Expected \'{replace_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name == rs['account_name'], f'Expected \'{account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['condition']['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident_status == rs['condition']['resident_status'], f'Expected \'{resident_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['condition']['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_resident == rs['condition']['account_resident'], f'Expected \'{account_resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct == rs['condition']['subproduct'], f'Expected \'{subproduct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = extension_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = extension_account_payload.delete(
                id=id_new
            )
            rs = helper.ACT_ACGLDEF_DEL(fields_data)
            # check total_count search all after delete
            fields_data = extension_account_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_extension_account_check_page
    def test_009_simple_search_extension_account_check_page(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACGLDEF_SER_SIMPLE(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_extension_account_check_page
    def test_010_advanced_search_extension_account_check_page(self, user):
        helper = ExtensionAccountHelper(user)
        fields_data = extension_account_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACGLDEF_SER_ADVANCE(fields_data)
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