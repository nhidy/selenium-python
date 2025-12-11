import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.credit_catalog_helpers import CreditCatalogHelper
from apitest.src.payloads.credit.credit_catalog_payload import CreditCatalogPayload

credit_catalog_payload = CreditCatalogPayload()

catalog_code="CATCRD0002"
catalog_name="cat name test"
currency_code="THB"
secure_currency_code="THB"
credit_type="B"
tenor_type="S"
is_syndicated="N"
interest_computation_mode="F"
secure_type="N"
secure_rate=0
principal_tenor=1
principal_tenor_unit="M"
interest_tenor=1
interest_tenor_unit="M"
fine_tenor=1
fine_tenor_unit="M"
credit_purpose="IN"
credit_classification="10"
credit_facility="LC"
discount_rate=0
re_discount_rate=0
disbursement_mode="R"
principal_grace_period=0
interest_grace_period=0
fine_grace_period=1
is_provision="N"
provision_tenor=0
provision_tenor_unit=""
rollover_option="N"
restruct="N"
holiday_interest_tenor=0
holiday_principal_due_on=0
holiday_fine_tenor=0
tariff_code=120
principal_decimal_rounding=5
interest_decimal_rounding=5
group_id=133
catalog_status="N"
principal_provision_rate0=0
principal_provision_rate1=3
principal_provision_rate2=30
principal_provision_rate3=50
principal_provision_rate4=100
interest_provision_rate0=0
interest_provision_rate1=0
interest_provision_rate2=0
interest_provision_rate3=0
interest_provision_rate4=0
subproduct="N"

catalog_name_update="cat name test update"
currency_code_update="THB"
secure_currency_code_update="THB"
credit_type_update="B"
tenor_type_update="S"
is_syndicated_update="N"
interest_computation_mode_update="F"
secure_type_update="N"
secure_rate_update=0
principal_tenor_update=0
principal_tenor_unit_update="B"
interest_tenor_update=1
interest_tenor_unit_update="M"
fine_tenor_update=1
fine_tenor_unit_update="M"
credit_purpose_update="IN"
credit_classification_update="10"
credit_facility_update="LC"
discount_rate_update=0
re_discount_rate_update=0
disbursement_mode_update="R"
principal_grace_period_update=0
interest_grace_period_update=0
fine_grace_period_update=1
is_provision_update="N"
provision_tenor_update=0
provision_tenor_unit_update=""
rollover_option_update="N"
restruct_update="N"
holiday_interest_tenor_update=0
holiday_principal_due_on_update=0
holiday_fine_tenor_update=0
tariff_code_update=120
principal_decimal_rounding_update=5
interest_decimal_rounding_update=5
group_id_update=133
catalog_status_update="N"
principal_provision_rate0_update=5
principal_provision_rate1_update=6
principal_provision_rate2_update=3.5
principal_provision_rate3_update=4.68
principal_provision_rate4_update=5.67
interest_provision_rate0_update=0.00000
interest_provision_rate1_update=0.00000
interest_provision_rate2_update=0.00000
interest_provision_rate3_update=0.00000
interest_provision_rate4_update=0.00000
subproduct_update="N"

# check type number
number_checklist = {
    "secure_rate": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "fine_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "discount_rate": {
        "data_type": int,
        "number_of_digits": 0
    },
    "re_discount_rate": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_grace_period": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_grace_period": {
        "data_type": int,
        "number_of_digits": 0
    },
    "fine_grace_period": {
        "data_type": int,
        "number_of_digits": 0
    },
    "provision_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "holiday_interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "holiday_principal_due_on": {
        "data_type": int,
        "number_of_digits": 0
    },
    "holiday_fine_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tariff_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_decimal_rounding": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_decimal_rounding": {
        "data_type": int,
        "number_of_digits": 0
    },
    "group_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_provision_rate0": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate1": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate2": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate3": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate4": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate0": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate1": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate2": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate3": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate4": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate_0": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate_1": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate_2": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate_3": {
        "data_type": float,
        "number_of_digits": 4
    },
    "principal_provision_rate_4": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate_0": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate_1": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate_2": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate_3": {
        "data_type": float,
        "number_of_digits": 4
    },
    "interest_provision_rate_4": {
        "data_type": float,
        "number_of_digits": 4
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

@pytest.mark.credit_catalog
class TestCreditCatalog(object):


    @pytest.mark.simple_search_credit_catalog_before_add
    def test_001_simple_search_credit_catalog_before_add(self, user):
        global total_count
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.simple_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
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


    @pytest.mark.advanced_search_credit_catalog_before_add
    def test_002_advanced_search_credit_catalog_before_add(self, user):
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.advanced_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_ADV_CRDCAT(fields_data)
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


    @pytest.mark.add_credit_catalog
    def test_003_add_credit_catalog(self, user):
        global id_new
        id_new = 0
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            secure_currency_code=secure_currency_code,
            credit_type=credit_type,
            tenor_type=tenor_type,
            is_syndicated=is_syndicated,
            interest_computation_mode=interest_computation_mode,
            secure_type=secure_type,
            secure_rate=secure_rate,
            principal_tenor=principal_tenor,
            principal_tenor_unit=principal_tenor_unit,
            interest_tenor=interest_tenor,
            interest_tenor_unit=interest_tenor_unit,
            fine_tenor=fine_tenor,
            fine_tenor_unit=fine_tenor_unit,
            credit_purpose=credit_purpose,
            credit_classification=credit_classification,
            credit_facility=credit_facility,
            discount_rate=discount_rate,
            re_discount_rate=re_discount_rate,
            disbursement_mode=disbursement_mode,
            principal_grace_period=principal_grace_period,
            interest_grace_period=interest_grace_period,
            fine_grace_period=fine_grace_period,
            is_provision=is_provision,
            provision_tenor=provision_tenor,
            provision_tenor_unit=provision_tenor_unit,
            rollover_option=rollover_option,
            restruct=restruct,
            holiday_interest_tenor=holiday_interest_tenor,
            holiday_principal_due_on=holiday_principal_due_on,
            holiday_fine_tenor=holiday_fine_tenor,
            tariff_code=tariff_code,
            principal_decimal_rounding=principal_decimal_rounding,
            interest_decimal_rounding=interest_decimal_rounding,
            group_id=group_id,
            catalog_status=catalog_status,
            principal_provision_rate0=principal_provision_rate0,
            principal_provision_rate1=principal_provision_rate1,
            principal_provision_rate2=principal_provision_rate2,
            principal_provision_rate3=principal_provision_rate3,
            principal_provision_rate4=principal_provision_rate4,
            interest_provision_rate0=interest_provision_rate0,
            interest_provision_rate1=interest_provision_rate1,
            interest_provision_rate2=interest_provision_rate2,
            interest_provision_rate3=interest_provision_rate3,
            interest_provision_rate4=interest_provision_rate4,
            subproduct=subproduct
        )
        print('fields_data:' + '\n\t', json.dumps(fields_data, indent=4, sort_keys=True))
        rs = helper.CRD_INSERT_CRDCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_currency_code == rs['secure_currency_code'], f'Expected \'{secure_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_type == rs['credit_type'], f'Expected \'{credit_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tenor_type == rs['tenor_type'], f'Expected \'{tenor_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_syndicated == rs['is_syndicated'], f'Expected \'{is_syndicated}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_computation_mode == rs['interest_computation_mode'], f'Expected \'{interest_computation_mode}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_type == rs['secure_type'], f'Expected \'{secure_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_rate == rs['secure_rate'], f'Expected \'{secure_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor == rs['principal_tenor'], f'Expected \'{principal_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor_unit == rs['principal_tenor_unit'], f'Expected \'{principal_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor == rs['interest_tenor'], f'Expected \'{interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor_unit == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor == rs['fine_tenor'], f'Expected \'{fine_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor_unit == rs['fine_tenor_unit'], f'Expected \'{fine_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_purpose == rs['credit_purpose'], f'Expected \'{credit_purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_classification == rs['credit_classification'], f'Expected \'{credit_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_facility == rs['credit_facility'], f'Expected \'{credit_facility}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert discount_rate == rs['discount_rate'], f'Expected \'{discount_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert re_discount_rate == rs['re_discount_rate'], f'Expected \'{re_discount_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert disbursement_mode == rs['disbursement_mode'], f'Expected \'{disbursement_mode}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_grace_period == rs['principal_grace_period'], f'Expected \'{principal_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_grace_period == rs['interest_grace_period'], f'Expected \'{interest_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_grace_period == rs['fine_grace_period'], f'Expected \'{fine_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_provision == rs['is_provision'], f'Expected \'{is_provision}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor == rs['provision_tenor'], f'Expected \'{provision_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor_unit == rs['provision_tenor_unit'], f'Expected \'{provision_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rollover_option == rs['rollover_option'], f'Expected \'{rollover_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert restruct == rs['restruct'], f'Expected \'{restruct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_interest_tenor == rs['holiday_interest_tenor'], f'Expected \'{holiday_interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_principal_due_on == rs['holiday_principal_due_on'], f'Expected \'{holiday_principal_due_on}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_fine_tenor == rs['holiday_fine_tenor'], f'Expected \'{holiday_fine_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_decimal_rounding == rs['principal_decimal_rounding'], f'Expected \'{principal_decimal_rounding}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_decimal_rounding == rs['interest_decimal_rounding'], f'Expected \'{interest_decimal_rounding}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate0 == rs['principal_provision_rate_0'], f'Expected \'{principal_provision_rate0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate1 == rs['principal_provision_rate_1'], f'Expected \'{principal_provision_rate1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate2 == rs['principal_provision_rate_2'], f'Expected \'{principal_provision_rate2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate3 == rs['principal_provision_rate_3'], f'Expected \'{principal_provision_rate3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate4 == rs['principal_provision_rate_4'], f'Expected \'{principal_provision_rate4}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate0 == rs['interest_provision_rate_0'], f'Expected \'{interest_provision_rate0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate1 == rs['interest_provision_rate_1'], f'Expected \'{interest_provision_rate1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate2 == rs['interest_provision_rate_2'], f'Expected \'{interest_provision_rate2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate3 == rs['interest_provision_rate_3'], f'Expected \'{interest_provision_rate3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate4 == rs['interest_provision_rate_4'], f'Expected \'{interest_provision_rate4}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct == rs['subproduct'], f'Expected \'{subproduct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = credit_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_credit_catalog_after_add
    def test_004_simple_search_credit_catalog_after_add(self, user):
        search_rs = False
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.simple_search(
            page_size=50,
            search_text=catalog_code
        )
        rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{catalog_code}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = credit_catalog_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=catalog_code
                )
                rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item): 
                        list_item = rs['items'][i].items()
                        for key, value in list_item:
                            if catalog_code in str(value):
                                search_rs = True
                                break
                    assert search_rs, f'Search with simple search fail. Expected: {catalog_code}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_credit_catalog_after_add
    def test_005_advanced_search_credit_catalog_after_add(self, user):
        search_rs = False
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.advanced_search(
            page_size=50,
            catalog_name=search_text
        )
        rs = helper.CRD_SEARCH_ADV_CRDCAT(fields_data)
        try:
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = credit_catalog_payload.advanced_search(
                    page_size=total_count_adv,
                    catalog_name=search_text
                )
                rs = helper.CRD_SEARCH_ADV_CRDCAT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['catalog_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_credit_catalog
    def test_006_update_credit_catalog(self, user):
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.update(
            id=id_new,
            catalog_name=catalog_name_update,
            currency_code=currency_code_update,
            secure_currency_code=secure_currency_code_update,
            credit_type=credit_type_update,
            tenor_type=tenor_type_update,
            is_syndicated=is_syndicated_update,
            interest_computation_mode=interest_computation_mode_update,
            secure_type=secure_type_update,
            secure_rate=secure_rate_update,
            principal_tenor=principal_tenor_update,
            principal_tenor_unit=principal_tenor_unit_update,
            interest_tenor=interest_tenor_update,
            interest_tenor_unit=interest_tenor_unit_update,
            fine_tenor=fine_tenor_update,
            fine_tenor_unit=fine_tenor_unit_update,
            credit_purpose=credit_purpose_update,
            credit_classification=credit_classification_update,
            credit_facility=credit_facility_update,
            discount_rate=discount_rate_update,
            re_discount_rate=re_discount_rate_update,
            disbursement_mode=disbursement_mode_update,
            principal_grace_period=principal_grace_period_update,
            interest_grace_period=interest_grace_period_update,
            fine_grace_period=fine_grace_period_update,
            is_provision=is_provision_update,
            provision_tenor=provision_tenor_update,
            provision_tenor_unit=provision_tenor_unit_update,
            rollover_option=rollover_option_update,
            restruct=restruct_update,
            holiday_interest_tenor=holiday_interest_tenor_update,
            holiday_principal_due_on=holiday_principal_due_on_update,
            holiday_fine_tenor=holiday_fine_tenor_update,
            tariff_code=tariff_code_update,
            principal_decimal_rounding=principal_decimal_rounding_update,
            interest_decimal_rounding=interest_decimal_rounding_update,
            group_id=group_id_update,
            catalog_status=catalog_status_update,
            principal_provision_rate0=principal_provision_rate0_update,
            principal_provision_rate1=principal_provision_rate1_update,
            principal_provision_rate2=principal_provision_rate2_update,
            principal_provision_rate3=principal_provision_rate3_update,
            principal_provision_rate4=principal_provision_rate4_update,
            interest_provision_rate0=interest_provision_rate0_update,
            interest_provision_rate1=interest_provision_rate1_update,
            interest_provision_rate2=interest_provision_rate2_update,
            interest_provision_rate3=interest_provision_rate3_update,
            interest_provision_rate4=interest_provision_rate4_update,
            subproduct=subproduct_update
        )
        rs = helper.CRD_UPDATE_CRDCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            assert catalog_name_update == rs['catalog_name'], f'Expected \'{catalog_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_currency_code_update == rs['secure_currency_code'], f'Expected \'{secure_currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_type_update == rs['credit_type'], f'Expected \'{credit_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tenor_type_update == rs['tenor_type'], f'Expected \'{tenor_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_syndicated_update == rs['is_syndicated'], f'Expected \'{is_syndicated_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_computation_mode_update == rs['interest_computation_mode'], f'Expected \'{interest_computation_mode_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_type_update == rs['secure_type'], f'Expected \'{secure_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_rate_update == rs['secure_rate'], f'Expected \'{secure_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor_update == rs['principal_tenor'], f'Expected \'{principal_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor_unit_update == rs['principal_tenor_unit'], f'Expected \'{principal_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor_update == rs['interest_tenor'], f'Expected \'{interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor_unit_update == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor_update == rs['fine_tenor'], f'Expected \'{fine_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor_unit_update == rs['fine_tenor_unit'], f'Expected \'{fine_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_purpose_update == rs['credit_purpose'], f'Expected \'{credit_purpose_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_classification_update == rs['credit_classification'], f'Expected \'{credit_classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_facility_update == rs['credit_facility'], f'Expected \'{credit_facility_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert discount_rate_update == rs['discount_rate'], f'Expected \'{discount_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert re_discount_rate_update == rs['re_discount_rate'], f'Expected \'{re_discount_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert disbursement_mode_update == rs['disbursement_mode'], f'Expected \'{disbursement_mode_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_grace_period_update == rs['principal_grace_period'], f'Expected \'{principal_grace_period_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_grace_period_update == rs['interest_grace_period'], f'Expected \'{interest_grace_period_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_grace_period_update == rs['fine_grace_period'], f'Expected \'{fine_grace_period_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_provision_update == rs['is_provision'], f'Expected \'{is_provision_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor_update == rs['provision_tenor'], f'Expected \'{provision_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor_unit_update == rs['provision_tenor_unit'], f'Expected \'{provision_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rollover_option_update == rs['rollover_option'], f'Expected \'{rollover_option_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert restruct_update == rs['restruct'], f'Expected \'{restruct_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_interest_tenor_update == rs['holiday_interest_tenor'], f'Expected \'{holiday_interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_principal_due_on_update == rs['holiday_principal_due_on'], f'Expected \'{holiday_principal_due_on_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_fine_tenor_update == rs['holiday_fine_tenor'], f'Expected \'{holiday_fine_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code_update == rs['tariff_code'], f'Expected \'{tariff_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_decimal_rounding_update == rs['principal_decimal_rounding'], f'Expected \'{principal_decimal_rounding_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_decimal_rounding_update == rs['interest_decimal_rounding'], f'Expected \'{interest_decimal_rounding_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id_update == rs['group_id'], f'Expected \'{group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status_update == rs['catalog_status'], f'Expected \'{catalog_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate0_update == rs['principal_provision_rate_0'], f'Expected \'{principal_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate1_update == rs['principal_provision_rate_1'], f'Expected \'{principal_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate2_update == rs['principal_provision_rate_2'], f'Expected \'{principal_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate3_update == rs['principal_provision_rate_3'], f'Expected \'{principal_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate4_update == rs['principal_provision_rate_4'], f'Expected \'{principal_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate0_update == rs['interest_provision_rate_0'], f'Expected \'{interest_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate1_update == rs['interest_provision_rate_1'], f'Expected \'{interest_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate2_update == rs['interest_provision_rate_2'], f'Expected \'{interest_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate3_update == rs['interest_provision_rate_3'], f'Expected \'{interest_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate4_update == rs['interest_provision_rate_4'], f'Expected \'{interest_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct_update == rs['subproduct'], f'Expected \'{subproduct_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_credit_catalog
    def test_007_delete_credit_catalog(self, user):
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.delete(
            id=id_new
        )
        rs = helper.CRD_DELETE_CRDCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = credit_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_credit_catalog
    def test_008_view_credit_catalog(self, user):
        helper = CreditCatalogHelper(user)
        fields_data = credit_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            secure_currency_code=secure_currency_code,
            credit_type=credit_type,
            tenor_type=tenor_type,
            is_syndicated=is_syndicated,
            interest_computation_mode=interest_computation_mode,
            secure_type=secure_type,
            secure_rate=secure_rate,
            principal_tenor=principal_tenor,
            principal_tenor_unit=principal_tenor_unit,
            interest_tenor=interest_tenor,
            interest_tenor_unit=interest_tenor_unit,
            fine_tenor=fine_tenor,
            fine_tenor_unit=fine_tenor_unit,
            credit_purpose=credit_purpose,
            credit_classification=credit_classification,
            credit_facility=credit_facility,
            discount_rate=discount_rate,
            re_discount_rate=re_discount_rate,
            disbursement_mode=disbursement_mode,
            principal_grace_period=principal_grace_period,
            interest_grace_period=interest_grace_period,
            fine_grace_period=fine_grace_period,
            is_provision=is_provision,
            provision_tenor=provision_tenor,
            provision_tenor_unit=provision_tenor_unit,
            rollover_option=rollover_option,
            restruct=restruct,
            holiday_interest_tenor=holiday_interest_tenor,
            holiday_principal_due_on=holiday_principal_due_on,
            holiday_fine_tenor=holiday_fine_tenor,
            tariff_code=tariff_code,
            principal_decimal_rounding=principal_decimal_rounding,
            interest_decimal_rounding=interest_decimal_rounding,
            group_id=group_id,
            catalog_status=catalog_status,
            principal_provision_rate0=principal_provision_rate0,
            principal_provision_rate1=principal_provision_rate1,
            principal_provision_rate2=principal_provision_rate2,
            principal_provision_rate3=principal_provision_rate3,
            principal_provision_rate4=principal_provision_rate4,
            interest_provision_rate0=interest_provision_rate0,
            interest_provision_rate1=interest_provision_rate1,
            interest_provision_rate2=interest_provision_rate2,
            interest_provision_rate3=interest_provision_rate3,
            interest_provision_rate4=interest_provision_rate4,
            subproduct=subproduct
        )
        rs = helper.CRD_INSERT_CRDCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = credit_catalog_payload.view(
                id=id_new
            )
            rs = helper.CRD_VIEW_CRDCAT(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check result
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_currency_code == rs['secure_currency_code'], f'Expected \'{secure_currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_type == rs['credit_type'], f'Expected \'{credit_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tenor_type == rs['tenor_type'], f'Expected \'{tenor_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_syndicated == rs['is_syndicated'], f'Expected \'{is_syndicated}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_computation_mode == rs['interest_computation_mode'], f'Expected \'{interest_computation_mode}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_type == rs['secure_type'], f'Expected \'{secure_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert secure_rate == rs['secure_rate'], f'Expected \'{secure_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor == rs['principal_tenor'], f'Expected \'{principal_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_tenor_unit == rs['principal_tenor_unit'], f'Expected \'{principal_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor == rs['interest_tenor'], f'Expected \'{interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_tenor_unit == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor == rs['fine_tenor'], f'Expected \'{fine_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_tenor_unit == rs['fine_tenor_unit'], f'Expected \'{fine_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_purpose == rs['credit_purpose'], f'Expected \'{credit_purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_classification == rs['credit_classification'], f'Expected \'{credit_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert credit_facility == rs['credit_facility'], f'Expected \'{credit_facility}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert discount_rate == rs['discount_rate'], f'Expected \'{discount_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert re_discount_rate == rs['re_discount_rate'], f'Expected \'{re_discount_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert disbursement_mode == rs['disbursement_mode'], f'Expected \'{disbursement_mode}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_grace_period == rs['principal_grace_period'], f'Expected \'{principal_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_grace_period == rs['interest_grace_period'], f'Expected \'{interest_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fine_grace_period == rs['fine_grace_period'], f'Expected \'{fine_grace_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_provision == rs['is_provision'], f'Expected \'{is_provision}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor == rs['provision_tenor'], f'Expected \'{provision_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert provision_tenor_unit == rs['provision_tenor_unit'], f'Expected \'{provision_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rollover_option == rs['rollover_option'], f'Expected \'{rollover_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert restruct == rs['restruct'], f'Expected \'{restruct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_interest_tenor == rs['holiday_interest_tenor'], f'Expected \'{holiday_interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_principal_due_on == rs['holiday_principal_due_on'], f'Expected \'{holiday_principal_due_on}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holiday_fine_tenor == rs['holiday_fine_tenor'], f'Expected \'{holiday_fine_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_decimal_rounding == rs['principal_decimal_rounding'], f'Expected \'{principal_decimal_rounding}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_decimal_rounding == rs['interest_decimal_rounding'], f'Expected \'{interest_decimal_rounding}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate0 == rs['principal_provision_rate_0'], f'Expected \'{principal_provision_rate0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate1 == rs['principal_provision_rate_1'], f'Expected \'{principal_provision_rate1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate2 == rs['principal_provision_rate_2'], f'Expected \'{principal_provision_rate2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate3 == rs['principal_provision_rate_3'], f'Expected \'{principal_provision_rate3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert principal_provision_rate4 == rs['principal_provision_rate_4'], f'Expected \'{principal_provision_rate4}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate0 == rs['interest_provision_rate_0'], f'Expected \'{interest_provision_rate0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate1 == rs['interest_provision_rate_1'], f'Expected \'{interest_provision_rate1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate2 == rs['interest_provision_rate_2'], f'Expected \'{interest_provision_rate2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate3 == rs['interest_provision_rate_3'], f'Expected \'{interest_provision_rate3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert interest_provision_rate4 == rs['interest_provision_rate_4'], f'Expected \'{interest_provision_rate4}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subproduct == rs['subproduct'], f'Expected \'{subproduct}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = credit_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = credit_catalog_payload.delete(
                id=id_new
            )
            rs = helper.CRD_DELETE_CRDCAT(fields_data)
            # check total_count search all after delete
            fields_data = credit_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CRDCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
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