from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.payment.payment_catalog_helpers import PaymentCatalogHelper
from apitest.src.payloads.payment.payment_catalog_payload import PaymentCatalogPayload

payment_catalog_payload = PaymentCatalogPayload()

catalog_code="CATPMT02"
catalog_name="pmt cat name test"
output_format="I"
direction="I"
instrument="T"
purpose="O"
holding_days=0
catalog_status="N"
approve_user_account=0
message_type="MT103"
export_file="N"
payment_classification=""
send_mail="Y"
group_pmt_ins_code=""
tariff_code=0
accounting_group_id=0
message_status=""


catalog_name_update="pmt cat name test update"
output_format_update="I"
direction_update="I"
instrument_update="T"
purpose_update="O"
holding_days_update=0
catalog_status_update="N"
message_type_update="MT103"
export_file_update="N"
payment_classification_update="B"
send_mail_update="N"
group_pmt_ins_code_update="103"
tariff_code_update=10
accounting_group_id_update=102


# check type number
number_checklist = {
    "holding_days": {
        "data_type": int,
        "number_of_digits": 0
    },
    "tariff_code": {
        "data_type": int,
        "number_of_digits": 0
    },
    "user_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "accounting_group_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "approve_user_account": {
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

@pytest.mark.payment_catalog
class TestPaymentCatalog(object):


    @pytest.mark.simple_search_payment_catalog_before_add
    def test_001_simple_search_payment_catalog_before_add(self, user):
        global total_count
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.simple_search(
            page_size=50
        )
        rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
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


    @pytest.mark.advanced_search_payment_catalog_before_add
    def test_002_advanced_search_payment_catalog_before_add(self, user):
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.advanced_search(
            page_size=50
        )
        rs = helper.PMT_SEARCH_ADV_PMTCAT(fields_data)
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


    @pytest.mark.add_payment_catalog
    def test_003_add_payment_catalog(self, user):
        global id_new
        id_new = 0
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            output_format=output_format,
            direction=direction,
            instrument=instrument,
            purpose=purpose,
            holding_days=holding_days,
            catalog_status=catalog_status,
            approve_user_account=approve_user_account,
            message_type=message_type,
            export_file=export_file,
            payment_classification=payment_classification,
            send_mail=send_mail,
            group_pmt_ins_code=group_pmt_ins_code,
            tariff_code=tariff_code,
            accounting_group_id=accounting_group_id,
            message_status=message_status
        )
        rs = helper.PMT_INSERT_PMTCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert output_format == rs['output_format'], f'Expected \'{output_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direction == rs['direction'], f'Expected \'{direction}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instrument == rs['instrument'], f'Expected \'{instrument}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert purpose == rs['purpose'], f'Expected \'{purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_days == rs['holding_days'], f'Expected \'{holding_days}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert approve_user_account == rs['approve_user_account'], f'Expected \'{approve_user_account}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type == rs['message_type'], f'Expected \'{message_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert export_file == rs['export_file'], f'Expected \'{export_file}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert payment_classification == rs['payment_classification'], f'Expected \'{payment_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert send_mail == rs['send_mail'], f'Expected \'{send_mail}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_pmt_ins_code == rs['group_pmt_ins_code'], f'Expected \'{group_pmt_ins_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_id == rs['accounting_group_id'], f'Expected \'{accounting_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_status == rs['message_status'], f'Expected \'{message_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = payment_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_payment_catalog_after_add
    def test_004_simple_search_payment_catalog_after_add(self, user):
        search_rs = False
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = payment_catalog_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
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


    @pytest.mark.advanced_search_payment_catalog_after_add
    def test_005_advanced_search_payment_catalog_after_add(self, user):
        search_rs = False
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.advanced_search(
            page_size=50,
            catalog_name=search_text
        )
        rs = helper.PMT_SEARCH_ADV_PMTCAT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = payment_catalog_payload.advanced_search(
                    page_size=total_count_adv,
                    catalog_name=search_text
                )
                rs = helper.PMT_SEARCH_ADV_PMTCAT(fields_data)
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


    @pytest.mark.update_payment_catalog
    def test_006_update_payment_catalog(self, user):
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.update(
            id=id_new,
            catalog_name=catalog_name_update,
            output_format=output_format_update,
            direction=direction_update,
            instrument=instrument_update,
            purpose=purpose_update,
            holding_days=holding_days_update,
            catalog_status=catalog_status_update,
            message_type=message_type_update,
            export_file=export_file_update,
            payment_classification=payment_classification_update,
            send_mail=send_mail_update,
            group_pmt_ins_code=group_pmt_ins_code_update,
            tariff_code=tariff_code_update,
            accounting_group_id=accounting_group_id_update
        )
        rs = helper.PMT_UPDATE_PMTCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name_update == rs['catalog_name'], f'Expected \'{catalog_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert output_format_update == rs['output_format'], f'Expected \'{output_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direction_update == rs['direction'], f'Expected \'{direction_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instrument_update == rs['instrument'], f'Expected \'{instrument_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert purpose_update == rs['purpose'], f'Expected \'{purpose_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_days_update == rs['holding_days'], f'Expected \'{holding_days_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status_update == rs['catalog_status'], f'Expected \'{catalog_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type_update == rs['message_type'], f'Expected \'{message_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert export_file_update == rs['export_file'], f'Expected \'{export_file_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert payment_classification_update == rs['payment_classification'], f'Expected \'{payment_classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert send_mail_update == rs['send_mail'], f'Expected \'{send_mail_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_pmt_ins_code_update == rs['group_pmt_ins_code'], f'Expected \'{group_pmt_ins_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code_update == rs['tariff_code'], f'Expected \'{tariff_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_id_update == rs['accounting_group_id'], f'Expected \'{accounting_group_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_payment_catalog
    def test_007_delete_payment_catalog(self, user):
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.delete(
            id=id_new
        )
        rs = helper.PMT_DELETE_PMTCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = payment_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_payment_catalog
    def test_008_view_payment_catalog(self, user):
        helper = PaymentCatalogHelper(user)
        fields_data = payment_catalog_payload.add(
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            output_format=output_format,
            direction=direction,
            instrument=instrument,
            purpose=purpose,
            holding_days=holding_days,
            catalog_status=catalog_status,
            approve_user_account=approve_user_account,
            message_type=message_type,
            export_file=export_file,
            payment_classification=payment_classification,
            send_mail=send_mail,
            group_pmt_ins_code=group_pmt_ins_code,
            tariff_code=tariff_code,
            accounting_group_id=accounting_group_id,
            message_status=message_status
        )
        rs = helper.PMT_INSERT_PMTCAT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = payment_catalog_payload.view(
                id=id_new
            )
            rs = helper.PMT_VIEW_PMTCAT(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_code == rs['catalog_code'], f'Expected \'{catalog_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_name == rs['catalog_name'], f'Expected \'{catalog_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert output_format == rs['output_format'], f'Expected \'{output_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direction == rs['direction'], f'Expected \'{direction}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instrument == rs['instrument'], f'Expected \'{instrument}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert purpose == rs['purpose'], f'Expected \'{purpose}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert holding_days == rs['holding_days'], f'Expected \'{holding_days}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert catalog_status == rs['catalog_status'], f'Expected \'{catalog_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert approve_user_account == rs['approve_user_account'], f'Expected \'{approve_user_account}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type == rs['message_type'], f'Expected \'{message_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert export_file == rs['export_file'], f'Expected \'{export_file}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert payment_classification == rs['payment_classification'], f'Expected \'{payment_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert send_mail == rs['send_mail'], f'Expected \'{send_mail}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_pmt_ins_code == rs['group_pmt_ins_code'], f'Expected \'{group_pmt_ins_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert tariff_code == rs['tariff_code'], f'Expected \'{tariff_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert accounting_group_id == rs['accounting_group_id'], f'Expected \'{accounting_group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_status == rs['message_status'], f'Expected \'{message_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = payment_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = payment_catalog_payload.delete(
                id=id_new
            )
            rs = helper.PMT_DELETE_PMTCAT(fields_data)
            # check total_count search all after delete
            fields_data = payment_catalog_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_PMTCAT(fields_data)
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