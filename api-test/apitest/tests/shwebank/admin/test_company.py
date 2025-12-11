import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.company_helpers import CompanyHelper
from apitest.src.payloads.admin.company_payload import CompanyPayload

company_payload = CompanyPayload()

company_code="COM123"
company_name="Company name test"
company_type="I"
company_status="N"
gatway_user_name=""
gatway_password=""
descr=""
message_type_field=""
processing_code_field=""
message_standard=""
message_format=""
message_transport_protocol=""
uri=""
user_name=""
password=""


company_code_update="COM234"
company_name_update="Update company name test"
company_type_update="I"
company_status_update="N"
gatway_user_name_update=""
gatway_password_update=""
descr_update=""
message_type_field_update=""
processing_code_field_update=""
message_standard_update=""
message_format_update=""
message_transport_protocol_update=""
uri_update=""
user_name_update=""
password_update=""

# check type number
number_checklist = {
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

@pytest.mark.company
class TestCompany(object):


    @pytest.mark.simple_search_company_before_add
    def test_001_simple_search_company_before_add(self, user):
        global total_count
        helper = CompanyHelper(user)
        fields_data = company_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
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


    @pytest.mark.advanced_search_company_before_add
    def test_002_advanced_search_company_before_add(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_COMPANY(fields_data)
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


    @pytest.mark.add_company
    def test_003_add_company(self, user):
        global id_new
        id_new = 0
        helper = CompanyHelper(user)
        fields_data = company_payload.add(
            company_code=company_code,
            company_name=company_name,
            company_type=company_type,
            company_status=company_status,
            gatway_user_name=gatway_user_name,
            gatway_password=gatway_password,
            descr=descr,
            message_type_field=message_type_field,
            processing_code_field=processing_code_field,
            message_standard=message_standard,
            message_format=message_format,
            message_transport_protocol=message_transport_protocol,
            uri=uri,
            user_name=user_name,
            password=password
        )
        rs = helper.ADM_INSERT_COMPANY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert company_code == rs['company_code'], f'Expected \'{company_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_name == rs['company_name'], f'Expected \'{company_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_type == rs['company_type'], f'Expected \'{company_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_status == rs['company_status'], f'Expected \'{company_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_user_name == rs['gatway_user_name'], f'Expected \'{gatway_user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_password == rs['gatway_password'], f'Expected \'{gatway_password}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert descr == rs['descr'], f'Expected \'{descr}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type_field == rs['message_type_field'], f'Expected \'{message_type_field}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert processing_code_field == rs['processing_code_field'], f'Expected \'{processing_code_field}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_standard == rs['message_standard'], f'Expected \'{message_standard}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_format == rs['message_format'], f'Expected \'{message_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_transport_protocol == rs['message_transport_protocol'], f'Expected \'{message_transport_protocol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert uri == rs['uri'], f'Expected \'{uri}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name == rs['user_name'], f'Expected \'{user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password == rs['password'], f'Expected \'{password}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = company_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_company_after_add
    def test_004_simple_search_company_after_add(self, user):
        search_rs = False
        helper = CompanyHelper(user)
        fields_data = company_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # check all result
                fields_data = company_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
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


    @pytest.mark.advanced_search_company_after_add
    def test_005_advanced_search_company_after_add(self, user):
        search_rs = False
        helper = CompanyHelper(user)
        fields_data = company_payload.advanced_search(
            page_size=50,
            company_name=search_text
        )
        rs = helper.ADM_ADVANCED_SEARCH_COMPANY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = company_payload.advanced_search(
                    page_size=total_count_adv,
                    company_name=search_text
                )
                rs = helper.ADM_ADVANCED_SEARCH_COMPANY(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['company_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with simple search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_company
    def test_006_update_company(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.update(
            id=id_new,
            company_code=company_code_update,
            company_name=company_name_update,
            company_type=company_type_update,
            company_status=company_status_update,
            gatway_user_name=gatway_user_name_update,
            gatway_password=gatway_password_update,
            descr=descr_update,
            message_type_field=message_type_field_update,
            processing_code_field=processing_code_field_update,
            message_standard=message_standard_update,
            message_format=message_format_update,
            message_transport_protocol=message_transport_protocol_update,
            uri=uri_update,
            user_name=user_name_update,
            password=password_update
        )
        rs = helper.ADM_UPDATE_COMPANY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_code_update == rs['company_code'], f'Expected \'{company_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_name_update == rs['company_name'], f'Expected \'{company_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_type_update == rs['company_type'], f'Expected \'{company_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_status_update == rs['company_status'], f'Expected \'{company_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_user_name_update == rs['gatway_user_name'], f'Expected \'{gatway_user_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_password_update == rs['gatway_password'], f'Expected \'{gatway_password_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert descr_update == rs['descr'], f'Expected \'{descr_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type_field_update == rs['message_type_field'], f'Expected \'{message_type_field_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert processing_code_field_update == rs['processing_code_field'], f'Expected \'{processing_code_field_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_standard_update == rs['message_standard'], f'Expected \'{message_standard_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_format_update == rs['message_format'], f'Expected \'{message_format_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_transport_protocol_update == rs['message_transport_protocol'], f'Expected \'{message_transport_protocol_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert uri_update == rs['uri'], f'Expected \'{uri_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name_update == rs['user_name'], f'Expected \'{user_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password_update == rs['password'], f'Expected \'{password_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_company
    def test_007_delete_company(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_COMPANY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = company_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_company
    def test_008_view_company(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.add(
            company_code=company_code,
            company_name=company_name,
            company_type=company_type,
            company_status=company_status,
            gatway_user_name=gatway_user_name,
            gatway_password=gatway_password,
            descr=descr,
            message_type_field=message_type_field,
            processing_code_field=processing_code_field,
            message_standard=message_standard,
            message_format=message_format,
            message_transport_protocol=message_transport_protocol,
            uri=uri,
            user_name=user_name,
            password=password
        )
        rs = helper.ADM_INSERT_COMPANY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = company_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_COMPANY(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_code == rs['company_code'], f'Expected \'{company_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_name == rs['company_name'], f'Expected \'{company_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_type == rs['company_type'], f'Expected \'{company_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert company_status == rs['company_status'], f'Expected \'{company_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_user_name == rs['gatway_user_name'], f'Expected \'{gatway_user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gatway_password == rs['gatway_password'], f'Expected \'{gatway_password}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert descr == rs['descr'], f'Expected \'{descr}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_type_field == rs['message_type_field'], f'Expected \'{message_type_field}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert processing_code_field == rs['processing_code_field'], f'Expected \'{processing_code_field}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_standard == rs['message_standard'], f'Expected \'{message_standard}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_format == rs['message_format'], f'Expected \'{message_format}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert message_transport_protocol == rs['message_transport_protocol'], f'Expected \'{message_transport_protocol}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert uri == rs['uri'], f'Expected \'{uri}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert user_name == rs['user_name'], f'Expected \'{user_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert password == rs['password'], f'Expected \'{password}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = company_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = company_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_COMPANY(fields_data)
            # check total_count search all after delete
            fields_data = company_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_company_check_page
    def test_009_simple_search_company_check_page(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_COMPANY(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_company_check_page
    def test_010_advanced_search_company_check_page(self, user):
        helper = CompanyHelper(user)
        fields_data = company_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_COMPANY(fields_data)
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