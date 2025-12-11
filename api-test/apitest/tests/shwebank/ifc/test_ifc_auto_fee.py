import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.ifc.ifc_auto_fee_helpers import IFCAutoFeeHelper
from apitest.src.payloads.ifc.ifc_auto_fee_payload import IFCAutoFeePayload

ifc_auto_fee_payload = IFCAutoFeePayload()

trans_code="DPT_OPN"
ifc_code=38
exchange=0
inuse=0

exchange_update=1
inuse_update=1

# check type number
number_checklist = {
    "ifc_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "exchange": {
        "data_type": int,
        "number_of_digits": 0
    },
    "inuse": {
        "data_type": int,
        "number_of_digits": 0
    },
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text='FEE'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.ifc_auto_fee
class TestIFCAutoFee(object):


    @pytest.mark.simple_search_ifc_auto_fee_before_add
    def test_001_simple_search_ifc_auto_fee_before_add(self, user):
        global total_count
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_ifc_auto_fee_before_add
    def test_002_advanced_search_ifc_auto_fee_before_add(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.advanced_search(
            page_size=5
        )
        rs = helper.IFC_ADSEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.add_ifc_auto_fee
    def test_003_add_ifc_auto_fee(self, user):
        global id_new
        id_new = 0
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.add(
            trans_code=trans_code,
            ifc_code=ifc_code,
            exchange=exchange,
            inuse=inuse
        )
        rs = helper.IFC_INSERT_IFCAUTOFEE(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']

        # check result
        assert trans_code == rs['trans_code'], f'Expected \'{trans_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_code == rs['ifc_code'], f'Expected \'{ifc_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert exchange == rs['exchange'], f'Expected \'{exchange}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inuse == rs['inuse'], f'Expected \'{inuse}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)

        # check total_count search all
        fields_data = ifc_auto_fee_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_ifc_auto_fee_after_add
    def test_004_simple_search_ifc_auto_fee_after_add(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
        assert 'items' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = ifc_auto_fee_payload.simple_search(
                page_size=total_count,
                search_text=search_text
            )
            rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
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


    @pytest.mark.advanced_search_ifc_auto_fee_after_add
    def test_005_advanced_search_ifc_auto_fee_after_add(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.advanced_search(
            page_size=50,
            trans_code=trans_code
        )
        rs = helper.IFC_ADSEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = ifc_auto_fee_payload.advanced_search(
                page_size=total_count,
                trans_code=trans_code
            )
            rs = helper.IFC_ADSEARCH_IFCAUTOFEE(fields_data)
            # check value
            search_rs = False
            for i in range(rs['total_count']):
                if trans_code in rs['items'][i]['trans_code']:
                    search_rs = True
                    break
            assert search_rs, f'Search with advanced search fail. Expected: {trans_code}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        else:
            assert rs['total_count'] != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_ifc_auto_fee
    def test_006_update_ifc_auto_fee(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.update(
            id=id_new,
            exchange=exchange_update,
            inuse=inuse_update
        )
        rs = helper.IFC_UPDATE_IFCAUTOFEE(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert exchange_update == rs['exchange'], f'Expected \'{exchange_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inuse_update == rs['inuse'], f'Expected \'{inuse_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert trans_code == rs['trans_code'], f'Expected \'{trans_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_code == rs['ifc_code'], f'Expected \'{ifc_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)


    @pytest.mark.delete_ifc_auto_fee
    def test_007_delete_ifc_auto_fee(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_IFCAUTOFEE(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = ifc_auto_fee_payload.simple_search(
                page_size=50
            )
            rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_ifc_auto_fee
    def test_008_view_ifc_auto_fee(self, user):
        helper = IFCAutoFeeHelper(user)
        fields_data = ifc_auto_fee_payload.add(
            trans_code=trans_code,
            ifc_code=ifc_code,
            exchange=exchange,
            inuse=inuse
        )
        rs = helper.IFC_INSERT_IFCAUTOFEE(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        fields_data = ifc_auto_fee_payload.view(
            id=id_new
        )
        rs = helper.IFC_VIEW_IFCAUTOFEE(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert trans_code == rs['trans_code'], f'Expected \'{trans_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_code == rs['ifc_code'], f'Expected \'{ifc_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert exchange == rs['exchange'], f'Expected \'{exchange}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inuse == rs['inuse'], f'Expected \'{inuse}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        # check total_count search all after view
        fields_data = ifc_auto_fee_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # delete data
        fields_data = ifc_auto_fee_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_IFCAUTOFEE(fields_data)
        # check total_count search all after delete
        fields_data = ifc_auto_fee_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'