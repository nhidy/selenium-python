from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.payment.correspondent_bank_helpers import CorrespondentBankHelper
from apitest.src.payloads.payment.correspondent_bank_payload import CorrespondentBankPayload

correspondent_bank_payload = CorrespondentBankPayload()

bic_code="BIC004"
bank_name="bank name test"
country="VN"
city_name=""
address="address"
head_office_code=""
branch_code=""
bank_type="C"
vostro_account_1=""
vostro_account_2=""
vostro_account_3=""
more_description=""
partner="P"
bank_status="N"
instruction_bank=""
nostro_account_1=""
nostro_account_2=""
nostro_account_3=""
sending_share_fee_rate=0
recieving_share_fee_rate=0


bank_name_update="bank name test update"
country_update="VN"
city_name_update="city up"
address_update="address up"
head_office_code_update="HOUP"
branch_code_update="9999"
bank_type_update="D"
vostro_account_1_update="v1"
vostro_account_2_update="v2"
vostro_account_3_update="v3"
more_description_update="v4"
partner_update="V"
bank_status_update="B"
instruction_bank_update="U"
nostro_account_1_update="n1"
nostro_account_2_update="n2"
nostro_account_3_update="n3"
sending_share_fee_rate_update=12.52
recieving_share_fee_rate_update=100


# check type number
number_checklist = {
    "sending_share_fee_rate": {
        "data_type": float,
        "number_of_digits": 2
    },
    "recieving_share_fee_rate": {
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

@pytest.mark.correspondent_bank
class TestCorrespondentBank(object):


    @pytest.mark.simple_search_correspondent_bank_before_add
    def test_001_simple_search_correspondent_bank_before_add(self, user):
        global total_count
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.simple_search(
            page_size=5
        )
        rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
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


    @pytest.mark.advanced_search_correspondent_bank_before_add
    def test_002_advanced_search_correspondent_bank_before_add(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.advanced_search(
            page_size=5
        )
        rs = helper.PMT_SEARCH_ADV_AGENTBANK(fields_data)
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


    @pytest.mark.add_correspondent_bank
    def test_003_add_correspondent_bank(self, user):
        global id_new
        id_new = 0
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.add(
            bic_code=bic_code,
            bank_name=bank_name,
            country=country,
            city_name=city_name,
            address=address,
            head_office_code=head_office_code,
            branch_code=branch_code,
            bank_type=bank_type,
            vostro_account_1=vostro_account_1,
            vostro_account_2=vostro_account_2,
            vostro_account_3=vostro_account_3,
            more_description=more_description,
            partner=partner,
            bank_status=bank_status,
            instruction_bank=instruction_bank,
            nostro_account_1=nostro_account_1,
            nostro_account_2=nostro_account_2,
            nostro_account_3=nostro_account_3,
            sending_share_fee_rate=sending_share_fee_rate,
            recieving_share_fee_rate=recieving_share_fee_rate
        )
        rs = helper.PMT_INSERT_AGENTBANK(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert bic_code == rs['bic_code'], f'Expected \'{bic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_name == rs['bank_name'], f'Expected \'{bank_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert city_name == rs['city_name'], f'Expected \'{city_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address == rs['address'], f'Expected \'{address}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert head_office_code == rs['head_office_code'], f'Expected \'{head_office_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_type == rs['bank_type'], f'Expected \'{bank_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_1 == rs['vostro_account']['vostro_account_1'], f'Expected \'{vostro_account_1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_2 == rs['vostro_account']['vostro_account_2'], f'Expected \'{vostro_account_2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_3 == rs['vostro_account']['vostro_account_3'], f'Expected \'{vostro_account_3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert more_description == rs['more_description'], f'Expected \'{more_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert partner == rs['partner'], f'Expected \'{partner}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_status == rs['bank_status'], f'Expected \'{bank_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instruction_bank == rs['instruction_bank'], f'Expected \'{instruction_bank}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_1 == rs['nostro_account']['nostro_account_1'], f'Expected \'{nostro_account_1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_2 == rs['nostro_account']['nostro_account_2'], f'Expected \'{nostro_account_2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_3 == rs['nostro_account']['nostro_account_3'], f'Expected \'{nostro_account_3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sending_share_fee_rate == rs['sending_share_fee_rate'], f'Expected \'{sending_share_fee_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert recieving_share_fee_rate == rs['recieving_share_fee_rate'], f'Expected \'{recieving_share_fee_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = correspondent_bank_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_correspondent_bank_after_add
    def test_004_simple_search_correspondent_bank_after_add(self, user):
        search_rs = False
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = correspondent_bank_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
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


    @pytest.mark.advanced_search_correspondent_bank_after_add
    def test_005_advanced_search_correspondent_bank_after_add(self, user):
        search_rs = False
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.advanced_search(
            page_size=50,
            bank_name=search_text
        )
        rs = helper.PMT_SEARCH_ADV_AGENTBANK(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = correspondent_bank_payload.advanced_search(
                    page_size=total_count_adv,
                    bank_name=search_text
                )
                rs = helper.PMT_SEARCH_ADV_AGENTBANK(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['bank_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_correspondent_bank
    def test_006_update_correspondent_bank(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.update(
            id=id_new,
            bank_name=bank_name_update,
            country=country_update,
            city_name=city_name_update,
            address=address_update,
            head_office_code=head_office_code_update,
            branch_code=branch_code_update,
            bank_type=bank_type_update,
            vostro_account_1=vostro_account_1_update,
            vostro_account_2=vostro_account_2_update,
            vostro_account_3=vostro_account_3_update,
            more_description=more_description_update,
            partner=partner_update,
            bank_status=bank_status_update,
            instruction_bank=instruction_bank_update,
            nostro_account_1=nostro_account_1_update,
            nostro_account_2=nostro_account_2_update,
            nostro_account_3=nostro_account_3_update,
            sending_share_fee_rate=sending_share_fee_rate_update,
            recieving_share_fee_rate=recieving_share_fee_rate_update
        )
        rs = helper.PMT_UPDATE_AGENTBANK(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bic_code == rs['bic_code'], f'Expected \'{bic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_name_update == rs['bank_name'], f'Expected \'{bank_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_update == rs['country'], f'Expected \'{country_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert city_name_update == rs['city_name'], f'Expected \'{city_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_update == rs['address'], f'Expected \'{address_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert head_office_code_update == rs['head_office_code'], f'Expected \'{head_office_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code_update == rs['branch_code'], f'Expected \'{branch_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_type_update == rs['bank_type'], f'Expected \'{bank_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_1_update == rs['vostro_account']['vostro_account_1'], f'Expected \'{vostro_account_1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_2_update == rs['vostro_account']['vostro_account_2'], f'Expected \'{vostro_account_2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_3_update == rs['vostro_account']['vostro_account_3'], f'Expected \'{vostro_account_3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert more_description_update == rs['more_description'], f'Expected \'{more_description_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert partner_update == rs['partner'], f'Expected \'{partner_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_status_update == rs['bank_status'], f'Expected \'{bank_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instruction_bank_update == rs['instruction_bank'], f'Expected \'{instruction_bank_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_1_update == rs['nostro_account']['nostro_account_1'], f'Expected \'{nostro_account_1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_2_update == rs['nostro_account']['nostro_account_2'], f'Expected \'{nostro_account_2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_3_update == rs['nostro_account']['nostro_account_3'], f'Expected \'{nostro_account_3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sending_share_fee_rate_update == rs['sending_share_fee_rate'], f'Expected \'{sending_share_fee_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert recieving_share_fee_rate_update == rs['recieving_share_fee_rate'], f'Expected \'{recieving_share_fee_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_correspondent_bank
    def test_007_delete_correspondent_bank(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.delete(
            id=id_new
        )
        rs = helper.PMT_DELETE_AGENTBANK(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = correspondent_bank_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_correspondent_bank
    def test_008_view_correspondent_bank(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.add(
            bic_code=bic_code,
            bank_name=bank_name,
            country=country,
            city_name=city_name,
            address=address,
            head_office_code=head_office_code,
            branch_code=branch_code,
            bank_type=bank_type,
            vostro_account_1=vostro_account_1,
            vostro_account_2=vostro_account_2,
            vostro_account_3=vostro_account_3,
            more_description=more_description,
            partner=partner,
            bank_status=bank_status,
            instruction_bank=instruction_bank,
            nostro_account_1=nostro_account_1,
            nostro_account_2=nostro_account_2,
            nostro_account_3=nostro_account_3,
            sending_share_fee_rate=sending_share_fee_rate,
            recieving_share_fee_rate=recieving_share_fee_rate
        )
        rs = helper.PMT_INSERT_AGENTBANK(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = correspondent_bank_payload.view(
                id=id_new
            )
            rs = helper.PMT_VIEW_AGENTBANK(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bic_code == rs['bic_code'], f'Expected \'{bic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_name == rs['bank_name'], f'Expected \'{bank_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert city_name == rs['city_name'], f'Expected \'{city_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address == rs['address'], f'Expected \'{address}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert head_office_code == rs['head_office_code'], f'Expected \'{head_office_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_type == rs['bank_type'], f'Expected \'{bank_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_1 == rs['vostro_account']['vostro_account_1'], f'Expected \'{vostro_account_1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_2 == rs['vostro_account']['vostro_account_2'], f'Expected \'{vostro_account_2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert vostro_account_3 == rs['vostro_account']['vostro_account_3'], f'Expected \'{vostro_account_3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert more_description == rs['more_description'], f'Expected \'{more_description}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert partner == rs['partner'], f'Expected \'{partner}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_status == rs['bank_status'], f'Expected \'{bank_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert instruction_bank == rs['instruction_bank'], f'Expected \'{instruction_bank}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_1 == rs['nostro_account']['nostro_account_1'], f'Expected \'{nostro_account_1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_2 == rs['nostro_account']['nostro_account_2'], f'Expected \'{nostro_account_2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert nostro_account_3 == rs['nostro_account']['nostro_account_3'], f'Expected \'{nostro_account_3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sending_share_fee_rate == rs['sending_share_fee_rate'], f'Expected \'{sending_share_fee_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert recieving_share_fee_rate == rs['recieving_share_fee_rate'], f'Expected \'{recieving_share_fee_rate}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = correspondent_bank_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = correspondent_bank_payload.delete(
                id=id_new
            )
            rs = helper.PMT_DELETE_AGENTBANK(fields_data)
            # check total_count search all after delete
            fields_data = correspondent_bank_payload.simple_search(
                page_size=50
            )
            rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_correspondent_bank_check_page
    def test_009_simple_search_correspondent_bank_check_page(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.PMT_SEARCH_SP_AGENTBANK(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_correspondent_bank_check_page
    def test_010_advanced_search_correspondent_bank_check_page(self, user):
        helper = CorrespondentBankHelper(user)
        fields_data = correspondent_bank_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.PMT_SEARCH_ADV_AGENTBANK(fields_data)
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