from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.ifc.ifc_definition_helpers import IFCDefinitionHelper
from apitest.src.payloads.ifc.ifc_definition_payload import IFCDefinitionPayload

ifc_definition_payload = IFCDefinitionPayload()

ifc_name="IFC test name"
ifc_type="C"
ifc_sub_type="CN"
value_base="I"
is_linked="N"
ifc_value=10.76321
ifc_linkage=7
ifc_operator="+"
margin_value=0.87732
value_type="F"
currency_code="USD"
floor_value=0.00601
ceiling_value=8000.00051
value_basic="BALANCE"
ifc_tenor=1
ifc_tenor_unit="Y"
ifc_condition="condition"
rounding_rule="R"
rounding_basis="A"
rounding_num=2
share_fee=0
ifc_status="N"
effect_value_date=datetime.fromisoformat("2022-03-15").strftime('%Y-%m-%dT%H:%M:%S')
effect_value=0.87763
group_id=0

ifc_name_update="update IFC test name"
ifc_sub_type_update="I"
value_base_update="A"
is_linked_update="Y"
ifc_value_update=4.63215
ifc_linkage_update=4
ifc_operator_update="%"
margin_value_update=0.65533
currency_code_update="KHR"
floor_value_update=0.00001
ceiling_value_update=7000.00001
value_basic_update="BALANCE-UPDATE"
ifc_tenor_update=3
ifc_tenor_unit_update="M"
ifc_condition_update="condition update"
rounding_rule_update="R"
rounding_basis_update="B"
rounding_num_update=5
share_fee_update=1
ifc_status_update="B"
effect_value_date_update=datetime.fromisoformat("2022-03-21").strftime('%Y-%m-%dT%H:%M:%S')
effect_value_update=0.87543
group_id_update=6

# check type number
number_checklist = {
    "ifc_code": {
        "data_type": int,
        "number_of_digits": 0
    },
     "ifc_linkage": {
        "data_type": int,
        "number_of_digits": 0
    },
    "ifc_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "rounding_num": {
        "data_type": int,
        "number_of_digits": 0
    },
    "share_fee": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_created": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_approved": {
        "data_type": int,
        "number_of_digits": 0
    },
    "group_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "ifc_value": {
        "data_type": float,
        "number_of_digits": 5
    },
    "margin_value": {
        "data_type": float,
        "number_of_digits": 5
    },
    "floor_value": {
        "data_type": float,
        "number_of_digits": 5
    },
    "ceiling_value": {
        "data_type": float,
        "number_of_digits": 5
    },
    "effect_value": {
        "data_type": float,
        "number_of_digits": 5
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

@pytest.mark.ifc_definition
class TestIFCDefinition(object):


    @pytest.mark.simple_search_ifc_definition_before_add
    def test_001_simple_search_ifc_definition_before_add(self, user):
        global total_count
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_ifc_definition_before_add
    def test_002_advanced_search_ifc_definition_before_add(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.advanced_search(
            page_size=5
        )
        rs = helper.IFC_ADSEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.add_ifc_definition
    def test_003_add_ifc_definition(self, user):
        global id_new, ifc_code_new, user_created_new, user_approved_new
        id_new = 0
        ifc_code_new = 0
        user_created_new = -1
        user_approved_new = -1
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.add(
            ifc_name=ifc_name,
            ifc_type=ifc_type,
            ifc_sub_type=ifc_sub_type,
            value_base=value_base,
            is_linked=is_linked,
            ifc_value=ifc_value,
            ifc_linkage=ifc_linkage,
            ifc_operator=ifc_operator,
            margin_value=margin_value,
            value_type=value_type,
            currency_code=currency_code,
            floor_value=floor_value,
            ceiling_value=ceiling_value,
            value_basic=value_basic,
            ifc_tenor=ifc_tenor,
            ifc_tenor_unit=ifc_tenor_unit,
            ifc_condition=ifc_condition,
            rounding_rule=rounding_rule,
            rounding_basis=rounding_basis,
            rounding_num=rounding_num,
            share_fee=share_fee,
            ifc_status=ifc_status,
            effect_value_date=effect_value_date,
            effect_value=effect_value,
            group_id=group_id
        )
        rs = helper.IFC_INSERT_IFC(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        assert 'ifc_code' in rs, f'Key \"ifc_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        ifc_code_new = rs['ifc_code']
        assert 'user_created' in rs, f'Key \"user_created\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        user_created_new = rs['user_created']
        assert 'user_approved' in rs, f'Key \"user_approved\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        user_approved_new = rs['user_approved']

        # check result
        assert ifc_name == rs['ifc_name'], f'Expected \'{ifc_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_type == rs['ifc_type'], f'Expected \'{ifc_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_sub_type == rs['ifc_sub_type'], f'Expected \'{ifc_sub_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_base == rs['value_base'], f'Expected \'{value_base}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert is_linked == rs['is_linked'], f'Expected \'{is_linked}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_value == rs['ifc_value'], f'Expected \'{ifc_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_linkage == rs['ifc_linkage'], f'Expected \'{ifc_linkage}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_operator == rs['ifc_operator'], f'Expected \'{ifc_operator}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert margin_value == rs['margin_value'], f'Expected \'{margin_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_type == rs['value_type'], f'Expected \'{value_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert floor_value == rs['floor_value'], f'Expected \'{floor_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ceiling_value == rs['ceiling_value'], f'Expected \'{ceiling_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_basic == rs['value_basic'], f'Expected \'{value_basic}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor == rs['ifc_tenor'], f'Expected \'{ifc_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor_unit == rs['ifc_tenor_unit'], f'Expected \'{ifc_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_condition == rs['ifc_condition'], f'Expected \'{ifc_condition}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_rule == rs['rounding_rule'], f'Expected \'{rounding_rule}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_basis == rs['rounding_basis'], f'Expected \'{rounding_basis}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_num == rs['rounding_num'], f'Expected \'{rounding_num}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert share_fee == rs['share_fee'], f'Expected \'{share_fee}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_status == rs['ifc_status'], f'Expected \'{ifc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value_date == rs['effect_value_date'], f'Expected \'{effect_value_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value == rs['effect_value'], f'Expected \'{effect_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)

        # check total_count search all
        fields_data = ifc_definition_payload.simple_search(
            page_size=5
        )
        rs = helper.IFC_SEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_ifc_definition_after_add
    def test_004_simple_search_ifc_definition_after_add(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.IFC_SEARCH_IFC(fields_data)
        assert 'items' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = ifc_definition_payload.simple_search(
                page_size=total_count,
                search_text=search_text
            )
            rs = helper.IFC_SEARCH_IFC(fields_data)
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


    @pytest.mark.advanced_search_ifc_definition_after_add
    def test_005_advanced_search_ifc_definition_after_add(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.advanced_search(
            page_size=50,
            ifc_name=search_text
        )
        rs = helper.IFC_ADSEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = ifc_definition_payload.advanced_search(
                page_size=total_count,
                ifc_name=search_text
            )
            rs = helper.IFC_ADSEARCH_IFC(fields_data)
            # check value
            search_rs = False
            for i in range(rs['total_count']):
                if search_text in rs['items'][i]['ifc_name']:
                    search_rs = True
                    break
            assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        else:
            assert rs['total_count'] != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_ifc_definition
    def test_006_update_ifc_definition(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.update(
            id=id_new,
            ifc_code=ifc_code_new, # khong duoc sua can fix lai
            ifc_name=ifc_name_update,
            ifc_sub_type=ifc_sub_type_update,
            value_base=value_base_update,
            is_linked=is_linked_update,
            ifc_value=ifc_value_update,
            ifc_linkage=ifc_linkage_update,
            ifc_operator=ifc_operator_update,
            margin_value=margin_value_update,
            currency_code=currency_code_update,
            floor_value=floor_value_update,
            ceiling_value=ceiling_value_update,
            value_basic=value_basic_update,
            ifc_tenor=ifc_tenor_update,
            ifc_tenor_unit=ifc_tenor_unit_update,
            ifc_condition=ifc_condition_update,
            rounding_rule=rounding_rule_update,
            rounding_basis=rounding_basis_update,
            rounding_num=rounding_num_update,
            share_fee=share_fee_update,
            ifc_status=ifc_status_update,
            effect_value_date=effect_value_date_update,
            effect_value=effect_value_update,
            group_id=group_id_update
        )
        rs = helper.IFC_UPDATE_IFC(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_code_new == rs['ifc_code'], f'Expected \'{ifc_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_name_update == rs['ifc_name'], f'Expected \'{ifc_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_sub_type_update == rs['ifc_sub_type'], f'Expected \'{ifc_sub_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_base_update == rs['value_base'], f'Expected \'{value_base_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert is_linked_update == rs['is_linked'], f'Expected \'{is_linked_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_value_update == rs['ifc_value'], f'Expected \'{ifc_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_linkage_update == rs['ifc_linkage'], f'Expected \'{ifc_linkage_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_operator_update == rs['ifc_operator'], f'Expected \'{ifc_operator_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert margin_value_update == rs['margin_value'], f'Expected \'{margin_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert floor_value_update == rs['floor_value'], f'Expected \'{floor_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ceiling_value_update == rs['ceiling_value'], f'Expected \'{ceiling_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_basic_update == rs['value_basic'], f'Expected \'{value_basic_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor_update == rs['ifc_tenor'], f'Expected \'{ifc_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor_unit_update == rs['ifc_tenor_unit'], f'Expected \'{ifc_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_condition_update == rs['ifc_condition'], f'Expected \'{ifc_condition_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_rule_update == rs['rounding_rule'], f'Expected \'{rounding_rule_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_basis_update == rs['rounding_basis'], f'Expected \'{rounding_basis_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_num_update == rs['rounding_num'], f'Expected \'{rounding_num_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert share_fee_update == rs['share_fee'], f'Expected \'{share_fee_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_status_update == rs['ifc_status'], f'Expected \'{ifc_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value_date_update == rs['effect_value_date'], f'Expected \'{effect_value_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value_update == rs['effect_value'], f'Expected \'{effect_value_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id_update == rs['group_id'], f'Expected \'{group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_created_new == rs['user_created'], f'Expected \'{user_created_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_approved_new == rs['user_approved'], f'Expected \'{user_approved_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)

    @pytest.mark.delete_ifc_definition
    def test_007_delete_ifc_definition(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_IFC(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)

            # check total_count search all after delete
            fields_data = ifc_definition_payload.simple_search(
                page_size=50
            )
            rs = helper.IFC_SEARCH_IFC(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_ifc_definition
    def test_008_view_ifc_definition(self, user):
        helper = IFCDefinitionHelper(user)
        fields_data = ifc_definition_payload.add(
            ifc_name=ifc_name,
            ifc_type=ifc_type,
            ifc_sub_type=ifc_sub_type,
            value_base=value_base,
            is_linked=is_linked,
            ifc_value=ifc_value,
            ifc_linkage=ifc_linkage,
            ifc_operator=ifc_operator,
            margin_value=margin_value,
            value_type=value_type,
            currency_code=currency_code,
            floor_value=floor_value,
            ceiling_value=ceiling_value,
            value_basic=value_basic,
            ifc_tenor=ifc_tenor,
            ifc_tenor_unit=ifc_tenor_unit,
            ifc_condition=ifc_condition,
            rounding_rule=rounding_rule,
            rounding_basis=rounding_basis,
            rounding_num=rounding_num,
            share_fee=share_fee,
            ifc_status=ifc_status,
            effect_value_date=effect_value_date,
            effect_value=effect_value,
            group_id=group_id
        )
        rs = helper.IFC_INSERT_IFC(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        assert 'ifc_code' in rs, f'Key \"ifc_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        ifc_code_new = rs['ifc_code']
        assert 'user_created' in rs, f'Key \"user_created\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        user_created_new = rs['user_created']
        assert 'user_approved' in rs, f'Key \"user_approved\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        user_approved_new = rs['user_approved']
        fields_data = ifc_definition_payload.view(
            id=id_new
        )
        rs = helper.IFC_VIEW_IFC(fields_data)
        # check result
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_name == rs['ifc_name'], f'Expected \'{ifc_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_type == rs['ifc_type'], f'Expected \'{ifc_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_sub_type == rs['ifc_sub_type'], f'Expected \'{ifc_sub_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_base == rs['value_base'], f'Expected \'{value_base}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert is_linked == rs['is_linked'], f'Expected \'{is_linked}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_value == rs['ifc_value'], f'Expected \'{ifc_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_linkage == rs['ifc_linkage'], f'Expected \'{ifc_linkage}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_operator == rs['ifc_operator'], f'Expected \'{ifc_operator}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert margin_value == rs['margin_value'], f'Expected \'{margin_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_type == rs['value_type'], f'Expected \'{value_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert floor_value == rs['floor_value'], f'Expected \'{floor_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ceiling_value == rs['ceiling_value'], f'Expected \'{ceiling_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert value_basic == rs['value_basic'], f'Expected \'{value_basic}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor == rs['ifc_tenor'], f'Expected \'{ifc_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_tenor_unit == rs['ifc_tenor_unit'], f'Expected \'{ifc_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_condition == rs['ifc_condition'], f'Expected \'{ifc_condition}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_rule == rs['rounding_rule'], f'Expected \'{rounding_rule}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_basis == rs['rounding_basis'], f'Expected \'{rounding_basis}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rounding_num == rs['rounding_num'], f'Expected \'{rounding_num}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert share_fee == rs['share_fee'], f'Expected \'{share_fee}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_status == rs['ifc_status'], f'Expected \'{ifc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value_date == rs['effect_value_date'], f'Expected \'{effect_value_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert effect_value == rs['effect_value'], f'Expected \'{effect_value}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert ifc_code_new == rs['ifc_code'], f'Expected \'{ifc_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_created_new == rs['user_created'], f'Expected \'{user_created_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_approved_new == rs['user_approved'], f'Expected \'{user_approved_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        
        # check total_count search all after view
        fields_data = ifc_definition_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # delete data
        fields_data = ifc_definition_payload.delete(
            id=id_new
        )
        rs = helper.IFC_DELETE_IFC(fields_data)
        # check total_count search all after delete
        fields_data = ifc_definition_payload.simple_search(
            page_size=50
        )
        rs = helper.IFC_SEARCH_IFC(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'