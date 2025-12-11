import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.cash.denomination_helpers import DenominationHelper
from apitest.src.payloads.cash.denomination_payload import DenominationPayload

denomination_payload = DenominationPayload()

currency_id="USD"
face_value=3
face_type="N"
face_description="face test description"
order=1


currency_id_update="KHR"
face_value_update=4
face_type_update="N"
face_description_update="test description update"
order_update=6

# check type number
number_checklist = {
    "face_value": {
        "data_type": int,
        "number_of_digits": 0
    },
    "order": {
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

@pytest.mark.denomination
class TestDenomination(object):


    @pytest.mark.simple_search_denomination_before_add
    def test_001_simple_search_denomination_before_add(self, user):
        global total_count
        helper = DenominationHelper(user)
        fields_data = denomination_payload.simple_search(
            page_size=5
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_denomination_before_add
    def test_002_advanced_search_denomination_before_add(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.advanced_search(
            page_size=5
        )
        rs = helper.CSH_DENOM_SER_ADVANCE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.add_denomination
    def test_003_add_denomination(self, user):
        global id_new
        id_new = 0
        helper = DenominationHelper(user)
        fields_data = denomination_payload.add(
            currency_id=currency_id,
            face_value=face_value,
            face_type=face_type,
            face_description=face_description,
            order=order
        )
        rs = helper.CSH_DENOM_INS(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']

        # check result
        assert currency_id == rs['currency_id'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_value == rs['face_value'], f'Expected \'{face_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_type == rs['face_type'], f'Expected \'{face_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_description == rs['face_description'], f'Expected \'{face_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)

        # check total_count search all
        fields_data = denomination_payload.simple_search(
            page_size=5
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_denomination_after_add
    def test_004_simple_search_denomination_after_add(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
        assert 'items' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = denomination_payload.simple_search(
                page_size=total_count,
                search_text=search_text
            )
            rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
            # check value
            search_rs = False
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
                assert rs['total_count'] != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_denomination_after_add
    def test_005_advanced_search_denomination_after_add(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.advanced_search(
            page_size=50,
            currency_id=currency_id
        )
        rs = helper.CSH_DENOM_SER_ADVANCE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = denomination_payload.advanced_search(
                page_size=total_count,
                currency_id=currency_id
            )
            rs = helper.CSH_DENOM_SER_ADVANCE(fields_data)
            # check value
            search_rs = False
            for i in range(rs['total_count']):
                if currency_id in rs['items'][i]['currency_id']:
                    search_rs = True
                    break
            assert search_rs, f'Search with advanced search fail. Expected: {currency_id}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        else:
            assert rs['total_count'] != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_denomination
    def test_006_update_denomination(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.update(
            id=id_new,
            currency_id=currency_id_update,
            face_value=face_value_update,
            face_type=face_type_update,
            face_description=face_description_update,
            order=order_update
        )
        rs = helper.CSH_DENOM_UPD(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_id_update == rs['currency_id'], f'Expected \'{currency_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_value_update == rs['face_value'], f'Expected \'{face_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_type_update == rs['face_type'], f'Expected \'{face_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_description_update == rs['face_description'], f'Expected \'{face_description_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert order_update == rs['order'], f'Expected \'{order_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)


    @pytest.mark.delete_denomination
    def test_007_delete_denomination(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.delete(
            id=id_new
        )
        rs = helper.CSH_DENOM_DEL(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = denomination_payload.simple_search(
                page_size=50
            )
            rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_denomination
    def test_008_view_denomination(self, user):
        helper = DenominationHelper(user)
        fields_data = denomination_payload.add(
            currency_id=currency_id,
            face_value=face_value,
            face_type=face_type,
            face_description=face_description,
            order=order
        )
        rs = helper.CSH_DENOM_INS(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        fields_data = denomination_payload.view(
            id=id_new
        )
        rs = helper.CSH_DENOM_VIEW(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_id == rs['currency_id'], f'Expected \'{currency_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_value == rs['face_value'], f'Expected \'{face_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_type == rs['face_type'], f'Expected \'{face_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert face_description == rs['face_description'], f'Expected \'{face_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        # check total_count search all after view
        fields_data = denomination_payload.simple_search(
            page_size=50
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # delete data
        fields_data = denomination_payload.delete(
            id=id_new
        )
        rs = helper.CSH_DENOM_DEL(fields_data)
        # check total_count search all after delete
        fields_data = denomination_payload.simple_search(
            page_size=50
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'