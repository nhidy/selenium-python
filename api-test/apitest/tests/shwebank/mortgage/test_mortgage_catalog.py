import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.mortgage.mortgage_catalog_helpers import MortgageCatalogHelper
from apitest.src.payloads.mortgage.mortgage_catalog_payload import MortgageCatalogPayload

mortgage_catalog_payload = MortgageCatalogPayload()

catalog_code="CATMTG02"
catalog_name="cat name test"
currency_code="USD"
collateral_asset_type="B"
collateral_rate=0
classification=""
risk_rate=0
group_id=0
book_scope="A"
depreciation_option="Y"
catalog_status="N"


catalog_name_update="update cat name test"
currency_code_update="KHR"
collateral_asset_type_update="R"
collateral_rate_update=60
classification_update="V"
risk_rate_update=10
group_id_update=104
book_scope_update="B"
depreciation_option_update="N"
catalog_status_update="B"


# check type number
number_checklist = {
    "collateral_rate": {
        "data_type": float,
        "number_of_digits": 2
    },
    "risk_rate": {
        "data_type": float,
        "number_of_digits": 2
    },
    "created_by": {
        "data_type": int,
        "number_of_digits": 0
    },
    "group_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "approved_by": {
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

@pytest.mark.mortgage_catalog
class TestMortgageCatalog(object):


    @pytest.mark.simple_search_mortgage_catalog_before_add
    def test_001_simple_search_mortgage_catalog_before_add(self, user):
        global total_count
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.simple_search(
            page_size=50
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_name' in rs['items'][0], f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_code' in rs['items'][0], f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'collateral_asset_type' in rs['items'][0], f'Key \"collateral_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'classification' in rs['items'][0], f'Key \"classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'collateral_rate' in rs['items'][0], f'Key \"collateral_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_status' in rs['items'][0], f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_mortgage_catalog_before_add
    def test_002_advanced_search_mortgage_catalog_before_add(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.advanced_search(
            page_size=50
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_code' in rs['items'][0], f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_name' in rs['items'][0], f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'currency_code' in rs['items'][0], f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'collateral_asset_type' in rs['items'][0], f'Key \"collateral_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'classification' in rs['items'][0], f'Key \"classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'collateral_rate' in rs['items'][0], f'Key \"collateral_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'catalog_status' in rs['items'][0], f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_mortgage_catalog
    def test_003_add_mortgage_catalog(self, user):
        global id_new, created_by_new
        id_new = 0
        created_by_new = -1
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            collateral_asset_type=collateral_asset_type,
            collateral_rate=collateral_rate,
            classification=classification,
            risk_rate=risk_rate,
            group_id=group_id,
            book_scope=book_scope,
            depreciation_option=depreciation_option,
            catalog_status=catalog_status
        )
        rs = helper.MTG_INSERT_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'created_by' in rs, f'Key \"created_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            created_by_new = rs['created_by']
            # check result
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_asset_type == rs['collateral_asset_type'], f'Expected \'{collateral_asset_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_rate == rs['collateral_rate'], f'Expected \'{collateral_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classification == rs['classification'], f'Expected \'{classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert risk_rate == rs['risk_rate'], f'Expected \'{risk_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert book_scope == rs['book_scope'], f'Expected \'{book_scope}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert depreciation_option == rs['depreciation_option'], f'Expected \'{depreciation_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert 0 < rs['created_by'], f'Expected > \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = mortgage_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_mortgage_catalog_after_add
    def test_004_simple_search_mortgage_catalog_after_add(self, user):
        search_rs = False
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = mortgage_catalog_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
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


    @pytest.mark.advanced_search_mortgage_catalog_after_add
    def test_005_advanced_search_mortgage_catalog_after_add(self, user):
        search_rs = False
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.advanced_search(
            page_size=50,
            catalog_name=search_text
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
            #     assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # else:
            #     total_count_adv = rs['total_count']
            #     # show all items
            #     fields_data = mortgage_catalog_payload.advanced_search(
            #         page_size=total_count_adv,
            #         catalog_name=search_text
            #     )
            #     rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(fields_data)
            #     # check value
            #     total_item = len(rs['items'])
            #     if total_item > 0:
            #         for i in range(total_item):
            #             if search_text in rs['items'][i]['catalog_name']:
            #                 search_rs = True
            #                 break
            #         assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     else:
            #         assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_mortgage_catalog
    def test_006_update_mortgage_catalog(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.update(
            id=id_new,
            catalog_name=catalog_name_update,
            currency_code=currency_code_update,
            collateral_asset_type=collateral_asset_type_update,
            collateral_rate=collateral_rate_update,
            classification=classification_update,
            risk_rate=risk_rate_update,
            group_id=group_id_update,
            book_scope=book_scope_update,
            depreciation_option=depreciation_option_update,
            catalog_status=catalog_status_update
        )
        rs = helper.MTG_UPDATE_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name_update == rs['catalog_name'], f'Expected \'{catalog_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_asset_type_update == rs['collateral_asset_type'], f'Expected \'{collateral_asset_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_rate_update == rs['collateral_rate'], f'Expected \'{collateral_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classification_update == rs['classification'], f'Expected \'{classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert risk_rate_update == rs['risk_rate'], f'Expected \'{risk_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id_update == rs['group_id'], f'Expected \'{group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert book_scope_update == rs['book_scope'], f'Expected \'{book_scope_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_option_update == rs['depreciation_option'], f'Expected \'{depreciation_option_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status_update == rs['catalog_status'], f'Expected \'{catalog_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by' in rs, f'Key \"created_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert created_by_new == rs['created_by'], f'Expected \'{created_by_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_mortgage_catalog
    def test_007_delete_mortgage_catalog(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.delete(
            id=id_new
        )
        rs = helper.MTG_DELETE_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = mortgage_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_mortgage_catalog
    def test_008_view_mortgage_catalog(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            collateral_asset_type=collateral_asset_type,
            collateral_rate=collateral_rate,
            classification=classification,
            risk_rate=risk_rate,
            group_id=group_id,
            book_scope=book_scope,
            depreciation_option=depreciation_option,
            catalog_status=catalog_status
        )
        rs = helper.MTG_INSERT_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            assert 'created_by' in rs, f'Key \"created_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            created_by_new = rs['created_by']
            fields_data = mortgage_catalog_payload.view(
                id=id_new
            )
            rs = helper.MTG_VIEW_MORTGAGE_CATALOG(fields_data)
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_code' in rs, f'Key \"catalog_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_name' in rs, f'Key \"catalog_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_asset_type' in rs, f'Key \"collateral_asset_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'classification' in rs, f'Key \"classification\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'collateral_rate' in rs, f'Key \"collateral_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'risk_rate' in rs, f'Key \"risk_rate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'book_scope' in rs, f'Key \"book_scope\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'depreciation_option' in rs, f'Key \"depreciation_option\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'catalog_status' in rs, f'Key \"catalog_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by' in rs, f'Key \"created_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by' in rs, f'Key \"approved_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by_code' in rs, f'Key \"created_by_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'created_by_name' in rs, f'Key \"created_by_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by_code' in rs, f'Key \"approved_by_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approved_by_name' in rs, f'Key \"approved_by_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert created_by_new == rs['created_by'], f'Expected \'{created_by_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_asset_type == rs['collateral_asset_type'], f'Expected \'{collateral_asset_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert collateral_rate == rs['collateral_rate'], f'Expected \'{collateral_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classification == rs['classification'], f'Expected \'{classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert risk_rate == rs['risk_rate'], f'Expected \'{risk_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert book_scope == rs['book_scope'], f'Expected \'{book_scope}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert depreciation_option == rs['depreciation_option'], f'Expected \'{depreciation_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = mortgage_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = mortgage_catalog_payload.delete(
                id=id_new
            )
            rs = helper.MTG_DELETE_MORTGAGE_CATALOG(fields_data)
            # check total_count search all after delete
            fields_data = mortgage_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_mortgage_catalog_check_page
    def test_009_simple_search_mortgage_catalog_check_page(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_mortgage_catalog_check_page
    def test_010_advanced_search_mortgage_catalog_check_page(self, user):
        helper = MortgageCatalogHelper(user)
        fields_data = mortgage_catalog_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    # @pytest.mark.mortgage_catalog_check_number_null
    # def test_011_mortgage_catalog_check_number_null(self, user):
    #     global id_new
    #     id_new = 0
    #     helper = MortgageCatalogHelper(user)
    #     # check insert
    #     fields_data = mortgage_catalog_payload.add(
    #         catalog_code=catalog_code,
    #         catalog_name=catalog_name,
    #         currency_code=currency_code,
    #         collateral_asset_type=collateral_asset_type,
    #         classification=classification,
    #         book_scope=book_scope,
    #         depreciation_option=depreciation_option,
    #         catalog_status=catalog_status
    #     )
    #     rs = helper.MTG_INSERT_MORTGAGE_CATALOG(fields_data)
    #     try:
    #         assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         id_new = rs['id']
    #         # check result
    #         assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert collateral_asset_type == rs['collateral_asset_type'], f'Expected \'{collateral_asset_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert classification == rs['classification'], f'Expected \'{classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert book_scope == rs['book_scope'], f'Expected \'{book_scope}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert depreciation_option == rs['depreciation_option'], f'Expected \'{depreciation_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    #         assert 0 == rs['collateral_rate'], f'Expected collateral_rate = \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert 0 == rs['risk_rate'], f'Expected risk_rate = \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert None == rs['group_id'], f'Expected group_id = \'{None}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    #         check_data_type(rs)
    #         # check total_count search all
    #         fields_data = mortgage_catalog_payload.simple_search(
    #             page_size=50
    #         )
    #         rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
    #         assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         # check update
    #         fields_data = mortgage_catalog_payload.update(
    #             id=id_new,
    #             catalog_name=catalog_name_update,
    #             currency_code=currency_code_update,
    #             collateral_asset_type=collateral_asset_type_update,
    #             classification=classification_update,
    #             book_scope=book_scope_update,
    #             depreciation_option=depreciation_option_update,
    #             catalog_status=catalog_status_update
    #         )
    #         rs = helper.MTG_UPDATE_MORTGAGE_CATALOG(fields_data)
    #         assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert 0 == rs['collateral_rate'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert 0 == rs['risk_rate'], f'Expected \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert None == rs['group_id'], f'Expected \'{None}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         # delete data
    #         fields_data = mortgage_catalog_payload.delete(
    #             id=id_new
    #         )
    #         rs = helper.MTG_DELETE_MORTGAGE_CATALOG(fields_data)
    #         # check total_count search all after delete
    #         fields_data = mortgage_catalog_payload.simple_search(
    #             page_size=50
    #         )
    #         rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(fields_data)
    #         assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     except:
    #         assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'