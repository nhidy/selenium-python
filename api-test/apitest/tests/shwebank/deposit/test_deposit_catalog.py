import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.deposit.deposit_catalog_helpers import DepositCatalogHelper
from apitest.src.payloads.deposit.deposit_catalog_payload import DepositCatalogPayload

deposit_catalog_payload = DepositCatalogPayload()

catalog_code="CATDPT01"
catalog_name="cat name test"
currency_code="KHR"
secure_currency=""
deposit_type="C"
deposit_purpose="S"
deposit_classification="N"
passbook_or_statement_or_receipt="S"
minimum_deposit_amount=10.89
catalog_status="N"
user_created=0
user_approved=0
tenor=0
tenor_unit="M"
tenor2=0
tenor_unit2="M"
deposit_tenor=0
deposit_tenor_unit="M"
interest_tenor=0
interest_tenor_unit="M"
minimum_tenor=0
minimum_tenor_unit="Y"
multi_deposit="Y"
multi_withdraw="Y"
early_withdraw="N"
minimum_tenor_allow_early_withdrawal=0
minimum_tenor_allow_early_withdrawal_unit=""
credit_interest="N"
credit_interest_tenor=2
credit_interest_tenor_unit="Y"
crediting_interest=3
minimum_dormant_amount=309.22
dormant_period=2
dormant_period_unit="Y"
rollover="N"
rollover_to_catalog=0
interest_due_on_holiday=1
principal_due_on_holiday=1
statement_format="E"
statement_tenor=2
statement_tenor_unit="Y"
inital_depost_amount=5022.45
periodic_deposit_amount=0
periodic_deposit_tenor=2
periodic_deposit_tenor_unit="Y"
tariff_code=4
group_id=1

catalog_code_update="CATDPT02"
catalog_name_update="update cat test name"
currency_code_update="USD"
secure_currency_update=""
deposit_type_update="A"
deposit_purpose_update="A"
deposit_classification_update="V"
passbook_or_statement_or_receipt_update="P"
minimum_deposit_amount_update=20.56
catalog_status_update="B"
multi_deposit_update="N"
multi_withdraw_update="N"
credit_interest_update="Y"
credit_interest_tenor_update=1
credit_interest_tenor_unit_update="M"
crediting_interest_update=1
minimum_dormant_amount_update=1000.54
dormant_period_update=1
dormant_period_unit_update="M"
statement_format_update="D"
statement_tenor_update=1
statement_tenor_unit_update="M"
inital_depost_amount_update=10.52
tariff_code_update=1
group_id_update=2

# check type number
number_checklist = {
    "user_created": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_approved": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tenor2": {
        "data_type": int,
        "number_of_digits": 0
    },
     "deposit_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_tenor_allow_early_withdrawal": {
        "data_type": int,
        "number_of_digits": 0
    },
    "credit_interest_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "crediting_interest": {
        "data_type": int,
        "number_of_digits": 0
    },
    "dormant_period": {
        "data_type": int,
        "number_of_digits": 0
    },
    "rollover_to_catalog": {
        "data_type": int,
        "number_of_digits": 0
    },
    "interest_due_on_holiday": {
        "data_type": int,
        "number_of_digits": 0
    },
    "principal_due_on_holiday": {
        "data_type": int,
        "number_of_digits": 0
    },
    "statement_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "periodic_deposit_tenor": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tariff_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "group_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "minimum_deposit_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "minimum_dormant_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "inital_depost_amount": {
        "data_type": float,
        "number_of_digits": 2
    },
    "periodic_deposit_amount": {
        "data_type": float,
        "number_of_digits": 2
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

@pytest.mark.deposit_catalog
class TestDepositCatalog(object):


    @pytest.mark.simple_search_deposit_catalog_before_add
    def test_001_simple_search_deposit_catalog_before_add(self, user):
        global total_count
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.simple_search(
            page_size=5
        )
        rs = helper.DPT_SEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.advanced_search_deposit_catalog_before_add
    def test_002_advanced_search_deposit_catalog_before_add(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.advanced_search(
            page_size=5
        )
        rs = helper.DPT_ADSEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        if len(rs['items']) > 0:
            assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            for i in range(len(rs['items'])): 
                check_data_type(rs['items'][i])


    @pytest.mark.add_deposit_catalog
    def test_003_add_deposit_catalog(self, user):
        global id_new
        id_new = 0
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            secure_currency=secure_currency,
            deposit_type=deposit_type,
            deposit_purpose=deposit_purpose,
            deposit_classification=deposit_classification,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt,
            minimum_deposit_amount=minimum_deposit_amount,
            catalog_status=catalog_status,
            user_created=user_created,
            user_approved=user_approved,
            tenor=tenor,
            tenor_unit=tenor_unit,
            tenor2=tenor2,
            tenor_unit2=tenor_unit2,
            deposit_tenor=deposit_tenor,
            deposit_tenor_unit=deposit_tenor_unit,
            interest_tenor=interest_tenor,
            interest_tenor_unit=interest_tenor_unit,
            minimum_tenor=minimum_tenor,
            minimum_tenor_unit=minimum_tenor_unit,
            multi_deposit=multi_deposit,
            multi_withdraw=multi_withdraw,
            early_withdraw=early_withdraw,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit,
            credit_interest=credit_interest,
            credit_interest_tenor=credit_interest_tenor,
            credit_interest_tenor_unit=credit_interest_tenor_unit,
            crediting_interest=crediting_interest,
            minimum_dormant_amount=minimum_dormant_amount,
            dormant_period=dormant_period,
            dormant_period_unit=dormant_period_unit,
            rollover=rollover,
            rollover_to_catalog=rollover_to_catalog,
            interest_due_on_holiday=interest_due_on_holiday,
            principal_due_on_holiday=principal_due_on_holiday,
            statement_format=statement_format,
            statement_tenor=statement_tenor,
            statement_tenor_unit=statement_tenor_unit,
            inital_depost_amount=inital_depost_amount,
            periodic_deposit_amount=periodic_deposit_amount,
            periodic_deposit_tenor=periodic_deposit_tenor,
            periodic_deposit_tenor_unit=periodic_deposit_tenor_unit,
            tariff_code=tariff_code,
            group_id=group_id
        )
        rs = helper.DPT_INSERT_CATALOG(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']

        # check result
        assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert secure_currency == rs['secure_currency'], f'Expected \'{secure_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_type == rs['deposit_type'], f'Expected \'{deposit_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_purpose == rs['deposit_purpose'], f'Expected \'{deposit_purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_classification == rs['deposit_classification'], f'Expected \'{deposit_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert passbook_or_statement_or_receipt == rs['passbook_or_statement_or_receipt'], f'Expected \'{passbook_or_statement_or_receipt}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_deposit_amount == rs['minimum_deposit_amount'], f'Expected \'{minimum_deposit_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_created == rs['user_created'], f'Expected \'{user_created}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_approved == rs['user_approved'], f'Expected \'{user_approved}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor == rs['tenor'], f'Expected \'{tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit == rs['tenor_unit'], f'Expected \'{tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor2 == rs['tenor2'], f'Expected \'{tenor2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit2 == rs['tenor_unit2'], f'Expected \'{tenor_unit2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor == rs['deposit_tenor'], f'Expected \'{deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor_unit == rs['deposit_tenor_unit'], f'Expected \'{deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor == rs['interest_tenor'], f'Expected \'{interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor_unit == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor == rs['minimum_tenor'], f'Expected \'{minimum_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_unit == rs['minimum_tenor_unit'], f'Expected \'{minimum_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_deposit == rs['multi_deposit'], f'Expected \'{multi_deposit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_withdraw == rs['multi_withdraw'], f'Expected \'{multi_withdraw}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert early_withdraw == rs['early_withdraw'], f'Expected \'{early_withdraw}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal == rs['minimum_tenor_allow_early_withdrawal'], f'Expected \'{minimum_tenor_allow_early_withdrawal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal_unit == rs['minimum_tenor_allow_early_withdrawal_unit'], f'Expected \'{minimum_tenor_allow_early_withdrawal_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest == rs['credit_interest'], f'Expected \'{credit_interest}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor == rs['credit_interest_tenor'], f'Expected \'{credit_interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor_unit == rs['credit_interest_tenor_unit'], f'Expected \'{credit_interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert crediting_interest == rs['crediting_interest'], f'Expected \'{crediting_interest}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_dormant_amount == rs['minimum_dormant_amount'], f'Expected \'{minimum_dormant_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period == rs['dormant_period'], f'Expected \'{dormant_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period_unit == rs['dormant_period_unit'], f'Expected \'{dormant_period_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover == rs['rollover'], f'Expected \'{rollover}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover_to_catalog == rs['rollover_to_catalog'], f'Expected \'{rollover_to_catalog}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_due_on_holiday == rs['interest_due_on_holiday'], f'Expected \'{interest_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert principal_due_on_holiday == rs['principal_due_on_holiday'], f'Expected \'{principal_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_format == rs['statement_format'], f'Expected \'{statement_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor == rs['statement_tenor'], f'Expected \'{statement_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor_unit == rs['statement_tenor_unit'], f'Expected \'{statement_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inital_depost_amount == rs['inital_depost_amount'], f'Expected \'{inital_depost_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_amount == rs['periodic_deposit_amount'], f'Expected \'{periodic_deposit_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor == rs['periodic_deposit_tenor'], f'Expected \'{periodic_deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor_unit == rs['periodic_deposit_tenor_unit'], f'Expected \'{periodic_deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)

        # check total_count search all
        fields_data = deposit_catalog_payload.simple_search(
            page_size=5
        )
        rs = helper.DPT_SEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_deposit_catalog_after_add
    def test_004_simple_search_deposit_catalog_after_add(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.DPT_SEARCH_CATALOG(fields_data)
        assert 'items' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = deposit_catalog_payload.simple_search(
                page_size=total_count,
                search_text=search_text
            )
            rs = helper.DPT_SEARCH_CATALOG(fields_data)
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


    @pytest.mark.advanced_search_deposit_catalog_after_add
    def test_005_advanced_search_deposit_catalog_after_add(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.advanced_search(
            page_size=50,
            catalog_name=search_text
        )
        rs = helper.DPT_ADSEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        total_count = rs['total_count']
        # check result
        if total_count != 0:
            # show all items
            fields_data = deposit_catalog_payload.advanced_search(
                page_size=total_count,
                catalog_name=search_text
            )
            rs = helper.DPT_ADSEARCH_CATALOG(fields_data)
            # check value
            search_rs = False
            for i in range(rs['total_count']):
                if search_text in rs['items'][i]['catalog_name']:
                    search_rs = True
                    break
            assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        else:
            assert rs['total_count'] != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_deposit_catalog
    def test_006_update_deposit_catalog(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.update(
            id=id_new,
            catalog_code=catalog_code_update,
            catalog_name=catalog_name_update,
            currency_code=currency_code_update,
            secure_currency=secure_currency_update,
            deposit_type=deposit_type_update,
            deposit_purpose=deposit_purpose_update,
            deposit_classification=deposit_classification_update,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_update,
            minimum_deposit_amount=minimum_deposit_amount_update,
            catalog_status=catalog_status_update,
            multi_deposit=multi_deposit_update,
            multi_withdraw=multi_withdraw_update,
            credit_interest=credit_interest_update,
            credit_interest_tenor=credit_interest_tenor_update,
            credit_interest_tenor_unit=credit_interest_tenor_unit_update,
            crediting_interest=crediting_interest_update,
            minimum_dormant_amount=minimum_dormant_amount_update,
            dormant_period=dormant_period_update,
            dormant_period_unit=dormant_period_unit_update,
            statement_format=statement_format_update,
            statement_tenor=statement_tenor_update,
            statement_tenor_unit=statement_tenor_unit_update,
            inital_depost_amount=inital_depost_amount_update,
            tariff_code=tariff_code_update,
            group_id=group_id_update
        )
        rs = helper.DPT_UPDATE_CATALOG(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_name_update == rs['catalog_name'], f'Expected \'{catalog_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert secure_currency_update == rs['secure_currency'], f'Expected \'{secure_currency_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_type_update == rs['deposit_type'], f'Expected \'{deposit_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_purpose_update == rs['deposit_purpose'], f'Expected \'{deposit_purpose_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_classification_update == rs['deposit_classification'], f'Expected \'{deposit_classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert passbook_or_statement_or_receipt_update == rs['passbook_or_statement_or_receipt'], f'Expected \'{passbook_or_statement_or_receipt_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_deposit_amount_update == rs['minimum_deposit_amount'], f'Expected \'{minimum_deposit_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_status_update == rs['catalog_status'], f'Expected \'{catalog_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_deposit_update == rs['multi_deposit'], f'Expected \'{multi_deposit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_withdraw_update == rs['multi_withdraw'], f'Expected \'{multi_withdraw_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_update == rs['credit_interest'], f'Expected \'{credit_interest_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor_update == rs['credit_interest_tenor'], f'Expected \'{credit_interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor_unit_update == rs['credit_interest_tenor_unit'], f'Expected \'{credit_interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert crediting_interest_update == rs['crediting_interest'], f'Expected \'{crediting_interest_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_dormant_amount_update == rs['minimum_dormant_amount'], f'Expected \'{minimum_dormant_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period_update == rs['dormant_period'], f'Expected \'{dormant_period_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period_unit_update == rs['dormant_period_unit'], f'Expected \'{dormant_period_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_format_update == rs['statement_format'], f'Expected \'{statement_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor_update == rs['statement_tenor'], f'Expected \'{statement_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor_unit_update == rs['statement_tenor_unit'], f'Expected \'{statement_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inital_depost_amount_update == rs['inital_depost_amount'], f'Expected \'{inital_depost_amount_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_code_update == rs['tariff_code'], f'Expected \'{tariff_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id_update == rs['group_id'], f'Expected \'{group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

        assert user_created == rs['user_created'], f'Expected \'{user_created}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_approved == rs['user_approved'], f'Expected \'{user_approved}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor == rs['tenor'], f'Expected \'{tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit == rs['tenor_unit'], f'Expected \'{tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor2 == rs['tenor2'], f'Expected \'{tenor2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit2 == rs['tenor_unit2'], f'Expected \'{tenor_unit2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor == rs['deposit_tenor'], f'Expected \'{deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor_unit == rs['deposit_tenor_unit'], f'Expected \'{deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor == rs['interest_tenor'], f'Expected \'{interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor_unit == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor == rs['minimum_tenor'], f'Expected \'{minimum_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_unit == rs['minimum_tenor_unit'], f'Expected \'{minimum_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert early_withdraw == rs['early_withdraw'], f'Expected \'{early_withdraw}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal == rs['minimum_tenor_allow_early_withdrawal'], f'Expected \'{minimum_tenor_allow_early_withdrawal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal_unit == rs['minimum_tenor_allow_early_withdrawal_unit'], f'Expected \'{minimum_tenor_allow_early_withdrawal_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover == rs['rollover'], f'Expected \'{rollover}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover_to_catalog == rs['rollover_to_catalog'], f'Expected \'{rollover_to_catalog}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_due_on_holiday == rs['interest_due_on_holiday'], f'Expected \'{interest_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert principal_due_on_holiday == rs['principal_due_on_holiday'], f'Expected \'{principal_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_amount == rs['periodic_deposit_amount'], f'Expected \'{periodic_deposit_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor == rs['periodic_deposit_tenor'], f'Expected \'{periodic_deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor_unit == rs['periodic_deposit_tenor_unit'], f'Expected \'{periodic_deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)


    @pytest.mark.delete_deposit_catalog
    def test_007_delete_deposit_catalog(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.delete(
            id=id_new
        )
        rs = helper.DPT_DELETE_CATALOG(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = deposit_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.DPT_SEARCH_CATALOG(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_deposit_catalog
    def test_008_view_deposit_catalog(self, user):
        helper = DepositCatalogHelper(user)
        fields_data = deposit_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            currency_code=currency_code,
            secure_currency=secure_currency,
            deposit_type=deposit_type,
            deposit_purpose=deposit_purpose,
            deposit_classification=deposit_classification,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt,
            minimum_deposit_amount=minimum_deposit_amount,
            catalog_status=catalog_status,
            user_created=user_created,
            user_approved=user_approved,
            tenor=tenor,
            tenor_unit=tenor_unit,
            tenor2=tenor2,
            tenor_unit2=tenor_unit2,
            deposit_tenor=deposit_tenor,
            deposit_tenor_unit=deposit_tenor_unit,
            interest_tenor=interest_tenor,
            interest_tenor_unit=interest_tenor_unit,
            minimum_tenor=minimum_tenor,
            minimum_tenor_unit=minimum_tenor_unit,
            multi_deposit=multi_deposit,
            multi_withdraw=multi_withdraw,
            early_withdraw=early_withdraw,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit,
            credit_interest=credit_interest,
            credit_interest_tenor=credit_interest_tenor,
            credit_interest_tenor_unit=credit_interest_tenor_unit,
            crediting_interest=crediting_interest,
            minimum_dormant_amount=minimum_dormant_amount,
            dormant_period=dormant_period,
            dormant_period_unit=dormant_period_unit,
            rollover=rollover,
            rollover_to_catalog=rollover_to_catalog,
            interest_due_on_holiday=interest_due_on_holiday,
            principal_due_on_holiday=principal_due_on_holiday,
            statement_format=statement_format,
            statement_tenor=statement_tenor,
            statement_tenor_unit=statement_tenor_unit,
            inital_depost_amount=inital_depost_amount,
            periodic_deposit_amount=periodic_deposit_amount,
            periodic_deposit_tenor=periodic_deposit_tenor,
            periodic_deposit_tenor_unit=periodic_deposit_tenor_unit,
            tariff_code=tariff_code,
            group_id=group_id
        )
        rs = helper.DPT_INSERT_CATALOG(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        id_new = rs['id']
        fields_data = deposit_catalog_payload.view(
            id=id_new
        )
        rs = helper.DPT_VIEW_CATALOG(fields_data)
        assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert secure_currency == rs['secure_currency'], f'Expected \'{secure_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_type == rs['deposit_type'], f'Expected \'{deposit_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_purpose == rs['deposit_purpose'], f'Expected \'{deposit_purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_classification == rs['deposit_classification'], f'Expected \'{deposit_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert passbook_or_statement_or_receipt == rs['passbook_or_statement_or_receipt'], f'Expected \'{passbook_or_statement_or_receipt}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_deposit_amount == rs['minimum_deposit_amount'], f'Expected \'{minimum_deposit_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_created == rs['user_created'], f'Expected \'{user_created}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert user_approved == rs['user_approved'], f'Expected \'{user_approved}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor == rs['tenor'], f'Expected \'{tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit == rs['tenor_unit'], f'Expected \'{tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor2 == rs['tenor2'], f'Expected \'{tenor2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tenor_unit2 == rs['tenor_unit2'], f'Expected \'{tenor_unit2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor == rs['deposit_tenor'], f'Expected \'{deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert deposit_tenor_unit == rs['deposit_tenor_unit'], f'Expected \'{deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor == rs['interest_tenor'], f'Expected \'{interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_tenor_unit == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor == rs['minimum_tenor'], f'Expected \'{minimum_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_unit == rs['minimum_tenor_unit'], f'Expected \'{minimum_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_deposit == rs['multi_deposit'], f'Expected \'{multi_deposit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert multi_withdraw == rs['multi_withdraw'], f'Expected \'{multi_withdraw}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert early_withdraw == rs['early_withdraw'], f'Expected \'{early_withdraw}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal == rs['minimum_tenor_allow_early_withdrawal'], f'Expected \'{minimum_tenor_allow_early_withdrawal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_tenor_allow_early_withdrawal_unit == rs['minimum_tenor_allow_early_withdrawal_unit'], f'Expected \'{minimum_tenor_allow_early_withdrawal_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest == rs['credit_interest'], f'Expected \'{credit_interest}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor == rs['credit_interest_tenor'], f'Expected \'{credit_interest_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert credit_interest_tenor_unit == rs['credit_interest_tenor_unit'], f'Expected \'{credit_interest_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert crediting_interest == rs['crediting_interest'], f'Expected \'{crediting_interest}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert minimum_dormant_amount == rs['minimum_dormant_amount'], f'Expected \'{minimum_dormant_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period == rs['dormant_period'], f'Expected \'{dormant_period}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert dormant_period_unit == rs['dormant_period_unit'], f'Expected \'{dormant_period_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover == rs['rollover'], f'Expected \'{rollover}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert rollover_to_catalog == rs['rollover_to_catalog'], f'Expected \'{rollover_to_catalog}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert interest_due_on_holiday == rs['interest_due_on_holiday'], f'Expected \'{interest_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert principal_due_on_holiday == rs['principal_due_on_holiday'], f'Expected \'{principal_due_on_holiday}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_format == rs['statement_format'], f'Expected \'{statement_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor == rs['statement_tenor'], f'Expected \'{statement_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert statement_tenor_unit == rs['statement_tenor_unit'], f'Expected \'{statement_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert inital_depost_amount == rs['inital_depost_amount'], f'Expected \'{inital_depost_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_amount == rs['periodic_deposit_amount'], f'Expected \'{periodic_deposit_amount}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor == rs['periodic_deposit_tenor'], f'Expected \'{periodic_deposit_tenor}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert periodic_deposit_tenor_unit == rs['periodic_deposit_tenor_unit'], f'Expected \'{periodic_deposit_tenor_unit}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        check_data_type(rs)
        # check total_count search all after view
        fields_data = deposit_catalog_payload.simple_search(
            page_size=50
        )
        rs = helper.DPT_SEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        # delete data
        fields_data = deposit_catalog_payload.delete(
            id=id_new
        )
        rs = helper.DPT_DELETE_CATALOG(fields_data)
        # check total_count search all after delete
        fields_data = deposit_catalog_payload.simple_search(
            page_size=50
        )
        rs = helper.DPT_SEARCH_CATALOG(fields_data)
        assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'