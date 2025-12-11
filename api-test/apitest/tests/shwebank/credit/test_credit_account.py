from datetime import datetime
import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.credit.credit_account_helpers import CreditAccountHelper
from apitest.src.payloads.credit.credit_account_payload import CreditAccountPayload

credit_account_payload = CreditAccountPayload()

account_number="099901020000050"
def_account_number="00999USDCRD00000025"
account_name_update="NHUNG TT - Short 3 test update"
secure_type_update="N"
secure_rate_update=0
principal_tenor_update=0
principal_tenor_unit_update="M"
interest_tenor_update=0
interest_tenor_unit_update="M"
credit_purpose_update=""
disbursement_mode_update="R"
is_provision_update="Y"
restruct_update="A"
limit_from_third_party_update=0
operative_limit_from_third_party_update=0
interest_first_date_update="2022-03-02T08:59:05.521Z"
from_date_update="2022-03-02T08:59:05.521Z"
to_date_update="2022-03-02T08:59:05.521Z"
ranking_status_update="A"
staff_id_update=0
remark_update=""
reference_number_update=""
is_restructured_update="Y"
principal_provision_rate0_update=0
principal_provision_rate1_update=0
principal_provision_rate2_update=0
principal_provision_rate3_update=0
principal_provision_rate4_update=0
interest_provision_rate0_update=0
interest_provision_rate1_update=0
interest_provision_rate2_update=0
interest_provision_rate3_update=0
interest_provision_rate4_update=0
business_purpose_code_update="D"
provision_of_other_update=""
id_new=1

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
    "limit_from_third_party": {
        "data_type": int,
        "number_of_digits": 0
    },
    "operative_limit_from_third_party": {
        "data_type": int,
        "number_of_digits": 0
    },
    "staff_id": {
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

@pytest.mark.credit_account
class TestCreditAccount(object):


    @pytest.mark.simple_search_credit_account
    def test_001_simple_search_credit_account(self, user):
        global total_count
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.simple_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_SP_CREDIT(fields_data)
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


    @pytest.mark.advanced_search_credit_account
    def test_002_advanced_search_credit_account(self, user):
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.advanced_search(
            page_size=50
        )
        rs = helper.CRD_SEARCH_ADV_CREDIT(fields_data)
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


    # @pytest.mark.update_credit_account
    # def test_003_update_credit_account(self, user):
    #     helper = CreditAccountHelper(user)
    #     fields_data = credit_account_payload.update(
    #         id=id_new,
    #         account_number="account_number",
    #         def_account_number="def_account_number",
    #         account_name=account_name_update,
    #         secure_type=secure_type_update,
    #         secure_rate=secure_rate_update,
    #         principal_tenor=principal_tenor_update,
    #         principal_tenor_unit=principal_tenor_unit_update,
    #         interest_tenor=interest_tenor_update,
    #         interest_tenor_unit=interest_tenor_unit_update,
    #         credit_purpose=credit_purpose_update,
    #         disbursement_mode=disbursement_mode_update,
    #         is_provision=is_provision_update,
    #         restruct=restruct_update,
    #         limit_from_third_party=limit_from_third_party_update,
    #         operative_limit_from_third_party=operative_limit_from_third_party_update,
    #         interest_first_date=interest_first_date_update,
    #         from_date=from_date_update,
    #         to_date=to_date_update,
    #         ranking_status=ranking_status_update,
    #         staff_id=staff_id_update,
    #         remark=remark_update,
    #         reference_number=reference_number_update,
    #         is_restructured=is_restructured_update,
    #         principal_provision_rate0=principal_provision_rate0_update,
    #         principal_provision_rate1=principal_provision_rate1_update,
    #         principal_provision_rate2=principal_provision_rate2_update,
    #         principal_provision_rate3=principal_provision_rate3_update,
    #         principal_provision_rate4=principal_provision_rate4_update,
    #         interest_provision_rate0=interest_provision_rate0_update,
    #         interest_provision_rate1=interest_provision_rate1_update,
    #         interest_provision_rate2=interest_provision_rate2_update,
    #         interest_provision_rate3=interest_provision_rate3_update,
    #         interest_provision_rate4=interest_provision_rate4_update,
    #         business_purpose_code=business_purpose_code_update,
    #         provision_of_other=provision_of_other_update,

    #     )
    #     rs = helper.CRD_UPDATE_CREDIT(fields_data)
    #     try:
    #         assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert def_account_number == rs['def_account_number'], f'Expected \'{def_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert secure_type_update == rs['secure_type'], f'Expected \'{secure_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert secure_rate_update == rs['secure_rate'], f'Expected \'{secure_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_tenor_update == rs['principal_tenor'], f'Expected \'{principal_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_tenor_unit_update == rs['principal_tenor_unit'], f'Expected \'{principal_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_tenor_update == rs['interest_tenor'], f'Expected \'{interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_tenor_unit_update == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert credit_purpose_update == rs['credit_purpose'], f'Expected \'{credit_purpose_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert disbursement_mode_update == rs['disbursement_mode'], f'Expected \'{disbursement_mode_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert is_provision_update == rs['is_provision'], f'Expected \'{is_provision_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert restruct_update == rs['restruct'], f'Expected \'{restruct_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert limit_from_third_party_update == rs['limit_from_third_party'], f'Expected \'{limit_from_third_party_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert operative_limit_from_third_party_update == rs['operative_limit_from_third_party'], f'Expected \'{operative_limit_from_third_party_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_first_date_update == rs['interest_first_date'], f'Expected \'{interest_first_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert from_date_update == rs['from_date'], f'Expected \'{from_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert to_date_update == rs['to_date'], f'Expected \'{to_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert ranking_status_update == rs['ranking_status'], f'Expected \'{ranking_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert staff_id_update == rs['staff_id'], f'Expected \'{staff_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert reference_number_update == rs['reference_number'], f'Expected \'{reference_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert is_restructured_update == rs['is_restructured'], f'Expected \'{is_restructured_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_provision_rate0_update == rs['principal_provision_rate0'], f'Expected \'{principal_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_provision_rate1_update == rs['principal_provision_rate1'], f'Expected \'{principal_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_provision_rate2_update == rs['principal_provision_rate2'], f'Expected \'{principal_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_provision_rate3_update == rs['principal_provision_rate3'], f'Expected \'{principal_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert principal_provision_rate4_update == rs['principal_provision_rate4'], f'Expected \'{principal_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_provision_rate0_update == rs['interest_provision_rate0'], f'Expected \'{interest_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_provision_rate1_update == rs['interest_provision_rate1'], f'Expected \'{interest_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_provision_rate2_update == rs['interest_provision_rate2'], f'Expected \'{interest_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_provision_rate3_update == rs['interest_provision_rate3'], f'Expected \'{interest_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert interest_provision_rate4_update == rs['interest_provision_rate4'], f'Expected \'{interest_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert business_purpose_code_update == rs['business_purpose_code'], f'Expected \'{business_purpose_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         assert provision_of_other_update == rs['provision_of_other'], f'Expected \'{provision_of_other_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #         check_data_type(rs)
    #     except:
    #         assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_credit_account_after_update
    def test_004_simple_search_credit_account_after_update(self, user):
        search_rs = False
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.simple_search(
            page_size=50,
            search_text=search_text
        )
        rs = helper.CRD_SEARCH_SP_CREDIT(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = credit_account_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.CRD_SEARCH_SP_CREDIT(fields_data)
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


    @pytest.mark.advanced_search_credit_account_after_update
    def test_005_advanced_search_credit_account_after_update(self, user):
        search_rs = False
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.advanced_search(
            page_size=50,
            account_name=search_text
        )
        rs = helper.CRD_SEARCH_ADV_CREDIT(fields_data)
        try:
            if (total_count) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = credit_account_payload.advanced_search(
                    page_size=total_count_adv,
                    account_name=search_text
                )
                rs = helper.CRD_SEARCH_ADV_CREDIT(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['account_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_credit_account
    def test_006_view_credit_account(self, user):
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.view(
            id=id_new
        )
        rs = helper.CRD_VIEW_CREDIT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_number == rs['account_number'], f'Expected \'{account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert def_account_number == rs['def_account_number'], f'Expected \'{def_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert secure_type_update == rs['secure_type'], f'Expected \'{secure_type_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert secure_rate_update == rs['secure_rate'], f'Expected \'{secure_rate_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_tenor_update == rs['principal_tenor'], f'Expected \'{principal_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_tenor_unit_update == rs['principal_tenor_unit'], f'Expected \'{principal_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_tenor_update == rs['interest_tenor'], f'Expected \'{interest_tenor_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_tenor_unit_update == rs['interest_tenor_unit'], f'Expected \'{interest_tenor_unit_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert credit_purpose_update == rs['credit_purpose'], f'Expected \'{credit_purpose_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert disbursement_mode_update == rs['disbursement_mode'], f'Expected \'{disbursement_mode_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert is_provision_update == rs['is_provision'], f'Expected \'{is_provision_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert restruct_update == rs['restruct'], f'Expected \'{restruct_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert limit_from_third_party_update == rs['limit_from_third_party'], f'Expected \'{limit_from_third_party_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert operative_limit_from_third_party_update == rs['operative_limit_from_third_party'], f'Expected \'{operative_limit_from_third_party_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_first_date_update == rs['interest_first_date'], f'Expected \'{interest_first_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert from_date_update == rs['from_date'], f'Expected \'{from_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert to_date_update == rs['to_date'], f'Expected \'{to_date_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert ranking_status_update == rs['ranking_status'], f'Expected \'{ranking_status_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert staff_id_update == rs['staff_id'], f'Expected \'{staff_id_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert remark_update == rs['remark'], f'Expected \'{remark_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert reference_number_update == rs['reference_number'], f'Expected \'{reference_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert is_restructured_update == rs['is_restructured'], f'Expected \'{is_restructured_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_provision_rate0_update == rs['principal_provision_rate0'], f'Expected \'{principal_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_provision_rate1_update == rs['principal_provision_rate1'], f'Expected \'{principal_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_provision_rate2_update == rs['principal_provision_rate2'], f'Expected \'{principal_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_provision_rate3_update == rs['principal_provision_rate3'], f'Expected \'{principal_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert principal_provision_rate4_update == rs['principal_provision_rate4'], f'Expected \'{principal_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_provision_rate0_update == rs['interest_provision_rate0'], f'Expected \'{interest_provision_rate0_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_provision_rate1_update == rs['interest_provision_rate1'], f'Expected \'{interest_provision_rate1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_provision_rate2_update == rs['interest_provision_rate2'], f'Expected \'{interest_provision_rate2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_provision_rate3_update == rs['interest_provision_rate3'], f'Expected \'{interest_provision_rate3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert interest_provision_rate4_update == rs['interest_provision_rate4'], f'Expected \'{interest_provision_rate4_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert business_purpose_code_update == rs['business_purpose_code'], f'Expected \'{business_purpose_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert provision_of_other_update == rs['provision_of_other'], f'Expected \'{provision_of_other_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check_data_type(rs)
            # check total_count search all after view
            fields_data = credit_account_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CREDIT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_credit_account
    def test_007_delete_credit_account(self, user):
        helper = CreditAccountHelper(user)
        fields_data = credit_account_payload.delete(
            id=id_new
        )
        rs = helper.CRD_DELETE_CREDIT(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after delete
            fields_data = credit_account_payload.simple_search(
                page_size=50
            )
            rs = helper.CRD_SEARCH_SP_CREDIT(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count - 1) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'