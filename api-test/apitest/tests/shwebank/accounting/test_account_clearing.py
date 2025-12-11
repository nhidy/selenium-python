import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.accounting.account_clearing_helpers import AccountClearingHelper
from apitest.src.payloads.accounting.account_clearing_payload import AccountClearingPayload

account_clearing_payload = AccountClearingPayload()

branch_code="0999"
currency_id="VND"
clearing_branch_code="0848"
clearing_type="I"
account_number="00999VND296519020888876"

branch_code_update="0848"
currency_id_update="SAG"
clearing_branch_code_update="0999"
clearing_type_update="B"
account_number_update="00999VND296519020888848"

# check type number
number_checklist = {
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text = '8888'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.account_clearing
class TestAccountClearing(object):


    @pytest.mark.simple_search_account_clearing_before_add
    def test_001_simple_search_account_clearing_before_add(self, user):
        global total_count
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.simple_search(
            page_size=5
        )
        rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_account_clearing_before_add
    def test_002_advanced_search_account_clearing_before_add(self, user):
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.advanced_search(
            page_size=5
        )
        rs = helper.ACT_ACCLR_SER_ADVANCE(fields_data)
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


    @pytest.mark.add_account_clearing
    def test_003_add_account_clearing(self, user):
        global id_new
        id_new = 0
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.add(
            branch_code=branch_code,
            currency_id=currency_id,
            clearing_branch_code=clearing_branch_code,
            clearing_type=clearing_type,
            account_number=account_number
        )
        rs = helper.ACT_ACCLR_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_id == rs['currency_code'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_branch_code == rs['clearing_branch_code'], f'Expected \'{clearing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_type == rs['clearing_type'], f'Expected \'{clearing_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = account_clearing_payload.simple_search(
                page_size=5
            )
            rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_clearing_after_add
    def test_004_simple_search_account_clearing_after_add(self, user):
        search_rs = False
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = account_clearing_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_account_clearing_after_add
    def test_005_advanced_search_account_clearing_after_add(self, user):
        search_rs = False
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.advanced_search(
            page_size=5,
            account_number=account_number
        )
        rs = helper.ACT_ACCLR_SER_ADVANCE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{account_number}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = account_clearing_payload.advanced_search(
                    page_size=total_count_adv,
                    account_number=account_number
                )
                rs = helper.ACT_ACCLR_SER_ADVANCE(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if account_number in rs['items'][i]['account_number']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {account_number}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_account_clearing
    def test_006_update_account_clearing(self, user):
        search_rs = False
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.update(
            id=id_new,
            branch_code=branch_code_update,
            currency_id=currency_id_update,
            clearing_branch_code=clearing_branch_code_update,
            clearing_type=clearing_type_update,
            account_number=account_number_update,
        )
        rs = helper.ACT_ACCLR_UPD(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code_update == rs['branch_code'], f'Expected \'{branch_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_id_update == rs['currency_code'], f'Expected \'{currency_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_branch_code_update == rs['clearing_branch_code'], f'Expected \'{clearing_branch_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_type_update == rs['clearing_type'], f'Expected \'{clearing_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number_update == rs['account_number'], f'Expected \'{account_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_account_clearing
    def test_007_delete_account_clearing(self, user):
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.delete(
            id=id_new
        )
        rs = helper.ACT_ACCLR_DEL(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = account_clearing_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_account_clearing
    def test_008_view_account_clearing(self, user):
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.add(
            branch_code=branch_code,
            currency_id=currency_id,
            clearing_branch_code=clearing_branch_code,
            clearing_type=clearing_type,
            account_number=account_number
        )
        rs = helper.ACT_ACCLR_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = account_clearing_payload.view(
                id=id_new
            )
            rs = helper.ACT_ACCLR_VIEW(fields_data)
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_id == rs['currency_code'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_branch_code == rs['clearing_branch_code'], f'Expected \'{clearing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert clearing_type == rs['clearing_type'], f'Expected \'{clearing_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = account_clearing_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = account_clearing_payload.delete(
                id=id_new
            )
            rs = helper.ACT_ACCLR_DEL(fields_data)
            # check total_count search all after delete
            fields_data = account_clearing_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_clearing_check_page
    def test_009_simple_search_account_clearing_check_page(self, user):
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACCLR_SER_SIMPLE(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_account_clearing_check_page
    def test_010_advanced_search_account_clearing_check_page(self, user):
        helper = AccountClearingHelper(user)
        fields_data = account_clearing_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACCLR_SER_ADVANCE(fields_data)
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