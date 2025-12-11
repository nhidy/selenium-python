import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.ifc.tariff_helpers import TariffHelper
from apitest.src.payloads.ifc.tariff_payload import TariffPayload

tariff_payload = TariffPayload()

tariff_name="tariff test name"
tariff_condition="condition"
tariff_description="description"
tariff_status="N"
ifc_list=[1, 4, 6]

tariff_name_update="tariff test name update"
tariff_condition_update="condition update"
tariff_description_update="description update"
tariff_status_update="C"
ifc_list_update=[7]

# check type number
number_checklist = {
    "tariff_code": {
        "data_type": int,
        "number_of_digits": 0
    },
     "ifc_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "ifc_value": {
        "data_type": float,
        "number_of_digits": 5
    },
    "ifc_tenor": {
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

@pytest.mark.tariff
class TestTariff(object):


    @pytest.mark.simple_search_tariff_before_add
    def test_001_simple_search_tariff_before_add(self, user):
        global total_count
        helper = TariffHelper(user)
        fields_data = tariff_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_tariff_before_add
    def test_002_advanced_search_tariff_before_add(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.advanced_search(
            page_size=5
        )
        rs = helper.IFC_ADSEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.add_tariff
    def test_003_add_tariff(self, user):
        global id_new, tariff_code_new
        id_new = 0
        tariff_code_new = 0
        helper = TariffHelper(user)
        fields_data = tariff_payload.add(
            tariff_name=tariff_name,
            tariff_condition=tariff_condition,
            tariff_description=tariff_description,
            tariff_status=tariff_status,
            ifc_list=ifc_list
        )
        rs = helper.IFC_INSERT_TARIFF(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        assert 'tariff_code' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        tariff_code_new = rs['tariff_code']

        # check result
        check_data_type(rs)
        assert tariff_name == rs['tariff_name'], f'Expected \'{tariff_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_condition == rs['tariff_condition'], f'Expected \'{tariff_condition}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_description == rs['tariff_description'], f'Expected \'{tariff_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_status == rs['tariff_status'], f'Expected \'{tariff_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'ifc_list' in rs, f'Key \"ifc_list\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # assert ifc_list == rs['ifc_list'], f'Expected \'{ifc_list}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        # check total_count search all
        fields_data = tariff_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_tariff_after_add
    def test_004_simple_search_tariff_after_add(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.IFC_SEARCH_TARIFF(fields_data)
        assert 'items' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = tariff_payload.simple_search(
                page_size=total_count,
                search_text=search_text
            )
            rs = helper.IFC_SEARCH_TARIFF(fields_data)
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


    @pytest.mark.advanced_search_tariff_after_add
    def test_005_advanced_search_tariff_after_add(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.advanced_search(
            page_size=50,
            tariff_name=search_text
        )
        rs = helper.IFC_ADSEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = tariff_payload.advanced_search(
                page_size=total_count,
                tariff_name=search_text
            )
            rs = helper.IFC_ADSEARCH_TARIFF(fields_data)
            # check value
            search_rs = False
            for i in range(rs['total_count']):
                if search_text in rs['items'][i]['tariff_name']:
                    search_rs = True
                    break
            assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        else:
            assert rs['total_count'] != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_tariff
    def test_006_update_tariff(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.update(
            id=id_new,
            tariff_code=tariff_code_new,
            tariff_name=tariff_name_update,
            tariff_condition=tariff_condition_update,
            tariff_description=tariff_description_update,
            tariff_status=tariff_status_update,
            ifc_list=ifc_list_update
        )
        rs = helper.IFC_UPDATE_TARIFF(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_code_new == rs['tariff_code'], f'Expected \'{tariff_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_name_update == rs['tariff_name'], f'Expected \'{tariff_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_condition_update == rs['tariff_condition'], f'Expected \'{tariff_condition_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_description_update == rs['tariff_description'], f'Expected \'{tariff_description_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_status_update == rs['tariff_status'], f'Expected \'{tariff_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'ifc_list' in rs, f'Key \"ifc_list\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # assert ifc_list_update == rs['ifc_list'], f'Expected \'{ifc_list_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_tariff
    def test_007_delete_tariff(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_TARIFF(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = tariff_payload.simple_search(
                page_size=50
            )
            rs = helper.IFC_SEARCH_TARIFF(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_tariff
    def test_008_view_tariff(self, user):
        helper = TariffHelper(user)
        fields_data = tariff_payload.add(
            tariff_name=tariff_name,
            tariff_condition=tariff_condition,
            tariff_description=tariff_description,
            tariff_status=tariff_status,
            ifc_list=ifc_list
        )
        rs = helper.IFC_INSERT_TARIFF(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        assert 'tariff_code' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        tariff_code_new = rs['tariff_code']
        fields_data = tariff_payload.view(
            id=id_new
        )
        rs = helper.IFC_VIEW_TARIFF(fields_data)
        # check result
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_code_new == rs['tariff_code'], f'Expected \'{tariff_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_name == rs['tariff_name'], f'Expected \'{tariff_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_condition == rs['tariff_condition'], f'Expected \'{tariff_condition}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_description == rs['tariff_description'], f'Expected \'{tariff_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_status == rs['tariff_status'], f'Expected \'{tariff_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'ifc_list' in rs, f'Key \"ifc_list\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # assert ifc_list == rs['ifc_list'], f'Expected \'{ifc_list}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # check total_count search all after view
        fields_data = tariff_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # delete data
        fields_data = tariff_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_TARIFF(fields_data)
        # check total_count search all after delete
        fields_data = tariff_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_TARIFF(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'