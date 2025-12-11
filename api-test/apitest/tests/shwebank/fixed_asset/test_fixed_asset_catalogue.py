import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.fixed_asset.fixed_asset_catalog_helpers import FixedAssetCatalogHelper
from apitest.src.payloads.fixed_asset.fixed_asset_catalog_payload import FixedAssetCatalogPayload
from apitest.src.helpers.neptune_helpers import NeptuneHelper

fixed_asset_catalogue_payload = FixedAssetCatalogPayload()

catalog_code="FACCAT91"
catalog_name="Test fac cat name"
fixed_asset_type="N"
fixed_asset_classification="C"
depreciation_method="M"
group_id=4
catalog_status="N"


catalog_name_update="Test fac cat name update"
fixed_asset_type_update="V"
fixed_asset_classification_update="A"
depreciation_method_update="Q"
group_id_update=7
catalog_status_update="B"


# check type number
number_checklist = {
    "id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "approve_user": {
        "data_type": int,
        "number_of_digits": 0
    },
    "group_id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text='Test'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.fixed_asset_catalogue
class TestFixedAssetCatalog(object):


    @pytest.mark.simple_search_fixed_asset_catalogue_before_add
    def test_001_simple_search_fixed_asset_catalogue_before_add(self, user):
        global total_count
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.simple_search(
            page_size=5
        )
        rs = helper.SQL_SEARCH_FACCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_name' in rs['items'][0], f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_type' in rs['items'][0], f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_classification' in rs['items'][0], f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'depreciation_method' in rs['items'][0], f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_status' in rs['items'][0], f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_fixed_asset_catalogue_before_add
    def test_002_advanced_search_fixed_asset_catalogue_before_add(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.advanced_search(
            page_size=5
        )
        rs = helper.SQL_ADSEARCH_FACCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_name' in rs['items'][0], f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_type' in rs['items'][0], f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fixed_asset_classification' in rs['items'][0], f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'depreciation_method' in rs['items'][0], f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_status' in rs['items'][0], f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_fixed_asset_catalogue
    def test_003_add_fixed_asset_catalogue(self, user):
        global id_new, user_id_new, approve_user_new
        id_new = 0
        user_id_new = -1
        approve_user_new = -1
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            group_id=group_id,
            catalog_status=catalog_status
        )
        rs = helper.SQL_INSERT_FACCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check key
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_name' in rs, f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_type' in rs, f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_classification' in rs, f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_method' in rs, f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_status' in rs, f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_type == rs['fixed_asset_type'], f'Expected \'{fixed_asset_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method == rs['depreciation_method'], f'Expected \'{depreciation_method}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            user_id_new = rs['user_id']
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            approve_user_new = rs['approve_user']
            check_data_type(rs)
            # check total_count search all
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_fixed_asset_catalogue_after_add
    def test_004_simple_search_fixed_asset_catalogue_after_add(self, user):
        search_rs = False
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.SQL_SEARCH_FACCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = fixed_asset_catalogue_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.SQL_SEARCH_FACCAT(fields_data)
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


    @pytest.mark.advanced_search_fixed_asset_catalogue_after_add
    def test_005_advanced_search_fixed_asset_catalogue_after_add(self, user):
        search_rs = False
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.advanced_search(
            page_size=50,
            catalog_code=catalog_code
        )
        rs = helper.SQL_ADSEARCH_FACCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with advanced search fail. Expected: \"{catalog_code}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = fixed_asset_catalogue_payload.advanced_search(
                    page_size=total_count_adv,
                    catalog_code=catalog_code
                )
                rs = helper.SQL_ADSEARCH_FACCAT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if catalog_code in rs['items'][i]['catalog_code']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {catalog_code}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_fixed_asset_catalogue
    def test_006_update_fixed_asset_catalogue(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.update(
            id=id_new,
            catalog_name=catalog_name_update,
            fixed_asset_type=fixed_asset_type_update,
            fixed_asset_classification=fixed_asset_classification_update,
            depreciation_method=depreciation_method_update,
            group_id=group_id_update,
            catalog_status=catalog_status_update
        )
        rs = helper.SQL_UPDATE_FACCAT(fields_data)
        try:
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_name' in rs, f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_type' in rs, f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_classification' in rs, f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_method' in rs, f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_status' in rs, f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name_update == rs['catalog_name'], f'Expected \'{catalog_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_type_update == rs['fixed_asset_type'], f'Expected \'{fixed_asset_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification_update == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method_update == rs['depreciation_method'], f'Expected \'{depreciation_method_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id_update == rs['group_id'], f'Expected \'{group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status_update == rs['catalog_status'], f'Expected \'{catalog_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_id_new == rs['user_id'], f'Expected \'{user_id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert approve_user_new == rs['approve_user'], f'Expected \'{approve_user_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_fixed_asset_catalogue
    def test_007_delete_fixed_asset_catalogue(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.delete(
            id=id_new
        )
        rs = helper.SQL_DELETE_FACCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_fixed_asset_catalogue
    def test_008_view_fixed_asset_catalogue(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            group_id=group_id,
            catalog_status=catalog_status
        )
        rs = helper.SQL_INSERT_FACCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            user_id_new = rs['user_id']
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            approve_user_new = rs['approve_user']
            fields_data = fixed_asset_catalogue_payload.view(
                id=id_new
            )
            rs = helper.SQL_VIEW_FACCAT(fields_data)
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_name' in rs, f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_type' in rs, f'Key \"fixed_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fixed_asset_classification' in rs, f'Key \"fixed_asset_classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_method' in rs, f'Key \"depreciation_method\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_status' in rs, f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_id' in rs, f'Key \"user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user' in rs, f'Key \"approve_user\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_code' in rs, f'Key \"user_created_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_name' in rs, f'Key \"user_created_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_code' in rs, f'Key \"user_approved_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_name' in rs, f'Key \"user_approved_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_type == rs['fixed_asset_type'], f'Expected \'{fixed_asset_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fixed_asset_classification == rs['fixed_asset_classification'], f'Expected \'{fixed_asset_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_method == rs['depreciation_method'], f'Expected \'{depreciation_method}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert approve_user_new == rs['approve_user'], f'Expected \'{approve_user_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_id_new == rs['user_id'], f'Expected \'{user_id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = fixed_asset_catalogue_payload.delete(
                id=id_new
            )
            rs = helper.SQL_DELETE_FACCAT(fields_data)
            # check total_count search all after delete
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_fixed_asset_catalogue_check_page
    def test_009_simple_search_fixed_asset_catalogue_check_page(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_SEARCH_FACCAT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_fixed_asset_catalogue_check_page
    def test_010_advanced_search_fixed_asset_catalogue_check_page(self, user):
        helper = FixedAssetCatalogHelper(user)
        fields_data = fixed_asset_catalogue_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_ADSEARCH_FACCAT(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.fixed_asset_catalogue_check_number_null
    def test_011_fixed_asset_catalogue_check_number_null(self, user):
        error_message_group_id ='GroupId is required.'
        global id_new
        id_new = 0
        helper = FixedAssetCatalogHelper(user)
        neptune_helper = NeptuneHelper(user)
        # check insert group_id=0
        fields_data = fixed_asset_catalogue_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            group_id=0,
            catalog_status=catalog_status
        )
        rs = neptune_helper.get_execution_info_res_body('SQL_INSERT_FACCAT', fields_data)
        assert 'group_id' in rs['execution_steps'][1]['p2_content']['response']['data'], f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert error_message_group_id == rs['execution_steps'][1]['p2_content']['response']['data']['group_id'], f'Expected \'{error_message_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        fields_data = fixed_asset_catalogue_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            group_id=group_id,
            catalog_status=catalog_status
        )
        rs = helper.SQL_INSERT_FACCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check total_count search all
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check update group_id=0
            fields_data = fixed_asset_catalogue_payload.update(
            id=id_new,
            catalog_name=catalog_name_update,
            fixed_asset_type=fixed_asset_type_update,
            fixed_asset_classification=fixed_asset_classification_update,
            depreciation_method=depreciation_method_update,
            group_id=0,
            catalog_status=catalog_status_update
            )
            rs = neptune_helper.get_execution_info_res_body('SQL_UPDATE_FACCAT', fields_data)
            assert 'group_id' in rs['execution_steps'][1]['p2_content']['response']['data'], f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert error_message_group_id == rs['execution_steps'][1]['p2_content']['response']['data']['group_id'], f'Expected \'{error_message_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = fixed_asset_catalogue_payload.delete(
                id=id_new
            )
            rs = helper.SQL_DELETE_FACCAT(fields_data)
            # check total_count search all after delete
            fields_data = fixed_asset_catalogue_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_FACCAT(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'