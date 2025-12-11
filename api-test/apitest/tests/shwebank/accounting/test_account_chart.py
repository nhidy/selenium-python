import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.accounting.account_chart_helpers import AccountChartHelper
from apitest.src.payloads.accounting.account_chart_payload import AccountChartPayload

account_chart_payload = AccountChartPayload()

bank_account_number="89988"
currency_code="USD"
branch_code="0999"
account_level=5
balance_side="D"
reverse_balance="N"
posting_side="C"
account_name="account name test"
short_account_name="short test"
laos_name="Laos Name"
thai_name="Thai Name"
khmer_name="Khmer Name"
vietnamese_name="Vietnamese Name"
account_classification="E"
account_categories="N"
account_group="E"
direct_posting="A"
is_visible="Y"
is_multi_currency=""
job_process_option="Y"
ref_account_number="ref account number"
references_number="references number"

account_name_update="account name test update"
short_account_name_update="short test update"
laos_name_update="Laos Name update"
thai_name_update="Thai Name update"
khmer_name_update="Khmer Name update"
vietnamese_name_update="Vietnamese Name update"
balance_side_update="B"
reverse_balance_update="Y"
posting_side_update="A"
account_classification_update="A"
account_categories_update="M"
account_group_update="N"
direct_posting_update="N"
is_visible_update="N"
job_process_option_update="N"
ref_account_number_update="ref account update"
references_number_update="references number update"


# check type number
number_checklist = {
    "account_level": {
        "data_type": int,
        "number_of_digits": 0
    },
    "id": {
        "data_type": int,
        "number_of_digits": 0
    }
}

search_text = 'test'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.account_chart
class TestAccountChart(object):


    @pytest.mark.simple_search_account_chart_before_add
    def test_001_simple_search_account_chart_before_add(self, user):
        global total_count
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.simple_search(
            page_size=5
        )
        rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
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


    @pytest.mark.advanced_search_account_chart_before_add
    def test_002_advanced_search_account_chart_before_add(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.advanced_search(
            page_size=5
        )
        rs = helper.ACT_ACCHRT_SER_ADVANCE(fields_data)
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


    @pytest.mark.add_account_chart
    def test_003_add_account_chart(self, user):
        global id_new
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.add(
            bank_account_number=bank_account_number,
            currency_code=currency_code,
            branch_code=branch_code,
            account_level=account_level,
            balance_side=balance_side,
            reverse_balance=reverse_balance,
            posting_side=posting_side,
            account_name=account_name,
            short_account_name=short_account_name,
            laos_name=laos_name,
            thai_name=thai_name,
            khmer_name=khmer_name,
            vietnamese_name=vietnamese_name,
            account_classification=account_classification,
            account_categories=account_categories,
            account_group=account_group,
            direct_posting=direct_posting,
            is_visible=is_visible,
            is_multi_currency=is_multi_currency,
            job_process_option=job_process_option,
            ref_account_number=ref_account_number,
            references_number=references_number
        )
        rs = helper.ACT_ACCHRT_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            # check result
            assert bank_account_number == rs['bank_account_number'], f'Expected \'{bank_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_level == rs['account_level'], f'Expected \'{account_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert balance_side == rs['balance_side'], f'Expected \'{balance_side}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reverse_balance == rs['reverse_balance'], f'Expected \'{reverse_balance}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert posting_side == rs['posting_side'], f'Expected \'{posting_side}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name == rs['account_name'], f'Expected \'{account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_account_name == rs['short_account_name'], f'Expected \'{short_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laos_name == rs['multi_value_name']['laos_name'], f'Expected \'{laos_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thai_name == rs['multi_value_name']['thai_name'], f'Expected \'{thai_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer_name == rs['multi_value_name']['khmer_name'], f'Expected \'{khmer_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese_name == rs['multi_value_name']['vietnamese_name'], f'Expected \'{vietnamese_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_classification == rs['account_classification'], f'Expected \'{account_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_categories == rs['account_categories'], f'Expected \'{account_categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_group == rs['account_group'], f'Expected \'{account_group}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direct_posting == rs['direct_posting'], f'Expected \'{direct_posting}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_visible == rs['is_visible'], f'Expected \'{is_visible}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_multi_currency == rs['is_multi_currency'], f'Expected \'{is_multi_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert job_process_option == rs['job_process_option'], f'Expected \'{job_process_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ref_account_number == rs['ref_account_number'], f'Expected \'{ref_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert references_number == rs['references_number'], f'Expected \'{references_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = account_chart_payload.simple_search(
                page_size=5
            )
            rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_chart_after_add
    def test_004_simple_search_account_chart_after_add(self, user):
        search_rs = False
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.simple_search(
            page_size=5,
            search_text=bank_account_number
        )
        rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = account_chart_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
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
    

    @pytest.mark.advanced_search_account_chart_after_add
    def test_005_advanced_search_account_chart_after_add(self, user):
        search_rs = False
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.advanced_search(
            page_size=50,
            bank_account_number=bank_account_number
        )
        rs = helper.ACT_ACCHRT_SER_ADVANCE(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{bank_account_number}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = account_chart_payload.advanced_search(
                    page_size=total_count_adv,
                    bank_account_number=bank_account_number
                )
                rs = helper.ACT_ACCHRT_SER_ADVANCE(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if bank_account_number in rs['items'][i]['bank_account_number']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {bank_account_number}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_account_chart
    def test_006_update_account_chart(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.update(
            id=id_new,
            account_name=account_name_update,
            short_account_name=short_account_name_update,
            laos_name=laos_name_update,
            thai_name=thai_name_update,
            khmer_name=khmer_name_update,
            vietnamese_name=vietnamese_name_update,
            balance_side=balance_side_update,
            reverse_balance=reverse_balance_update,
            posting_side=posting_side_update,
            account_classification=account_classification_update,
            account_categories=account_categories_update,
            account_group=account_group_update,
            direct_posting=direct_posting_update,
            is_visible=is_visible_update,
            job_process_option=job_process_option_update,
            ref_account_number=ref_account_number_update,
            references_number=references_number_update
        )
        rs = helper.ACT_ACCHRT_UPD(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name_update == rs['account_name'], f'Expected \'{account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_account_name_update == rs['short_account_name'], f'Expected \'{short_account_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laos_name_update == rs['multi_value_name']['laos_name'], f'Expected \'{laos_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thai_name_update == rs['multi_value_name']['thai_name'], f'Expected \'{thai_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer_name_update == rs['multi_value_name']['khmer_name'], f'Expected \'{khmer_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese_name_update == rs['multi_value_name']['vietnamese_name'], f'Expected \'{vietnamese_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert balance_side_update == rs['balance_side'], f'Expected \'{balance_side_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reverse_balance_update == rs['reverse_balance'], f'Expected \'{reverse_balance_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert posting_side_update == rs['posting_side'], f'Expected \'{posting_side_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_classification_update == rs['account_classification'], f'Expected \'{account_classification_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_categories_update == rs['account_categories'], f'Expected \'{account_categories_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_group_update == rs['account_group'], f'Expected \'{account_group_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direct_posting_update == rs['direct_posting'], f'Expected \'{direct_posting_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_visible_update == rs['is_visible'], f'Expected \'{is_visible_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert job_process_option_update == rs['job_process_option'], f'Expected \'{job_process_option_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ref_account_number_update == rs['ref_account_number'], f'Expected \'{ref_account_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert references_number_update == rs['references_number'], f'Expected \'{references_number_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_account_chart
    def test_007_delete_account_chart(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.delete(
            id=id_new
        )
        rs = helper.ACT_ACCHRT_DEL(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = account_chart_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_account_chart
    def test_008_view_account_chart(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.add(
            bank_account_number=bank_account_number,
            currency_code=currency_code,
            branch_code=branch_code,
            account_level=account_level,
            balance_side=balance_side,
            reverse_balance=reverse_balance,
            posting_side=posting_side,
            account_name=account_name,
            short_account_name=short_account_name,
            laos_name=laos_name,
            thai_name=thai_name,
            khmer_name=khmer_name,
            vietnamese_name=vietnamese_name,
            account_classification=account_classification,
            account_categories=account_categories,
            account_group=account_group,
            direct_posting=direct_posting,
            is_visible=is_visible,
            is_multi_currency=is_multi_currency,
            job_process_option=job_process_option,
            ref_account_number=ref_account_number,
            references_number=references_number
        )
        rs = helper.ACT_ACCHRT_INS(fields_data)
        try:
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = account_chart_payload.view(
                id=id_new
            )
            rs = helper.ACT_ACCHRT_VIEW(fields_data)
            assert 'id' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert bank_account_number == rs['bank_account_number'], f'Expected \'{bank_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branch_code == rs['branch_code'], f'Expected \'{branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_level == rs['account_level'], f'Expected \'{account_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert balance_side == rs['balance_side'], f'Expected \'{balance_side}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert reverse_balance == rs['reverse_balance'], f'Expected \'{reverse_balance}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert posting_side == rs['posting_side'], f'Expected \'{posting_side}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_name == rs['account_name'], f'Expected \'{account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_account_name == rs['short_account_name'], f'Expected \'{short_account_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert laos_name == rs['multi_value_name']['laos_name'], f'Expected \'{laos_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert thai_name == rs['multi_value_name']['thai_name'], f'Expected \'{thai_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert khmer_name == rs['multi_value_name']['khmer_name'], f'Expected \'{khmer_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert vietnamese_name == rs['multi_value_name']['vietnamese_name'], f'Expected \'{vietnamese_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_classification == rs['account_classification'], f'Expected \'{account_classification}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_categories == rs['account_categories'], f'Expected \'{account_categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert account_group == rs['account_group'], f'Expected \'{account_group}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert direct_posting == rs['direct_posting'], f'Expected \'{direct_posting}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_visible == rs['is_visible'], f'Expected \'{is_visible}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert is_multi_currency == rs['is_multi_currency'], f'Expected \'{is_multi_currency}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert job_process_option == rs['job_process_option'], f'Expected \'{job_process_option}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert ref_account_number == rs['ref_account_number'], f'Expected \'{ref_account_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert references_number == rs['references_number'], f'Expected \'{references_number}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = account_chart_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = account_chart_payload.delete(
                id=id_new
            )
            rs = helper.ACT_ACCHRT_DEL(fields_data)
            # check total_count search all after delete
            fields_data = account_chart_payload.simple_search(
                page_size=50
            )
            rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_account_chart_check_page
    def test_009_simple_search_account_chart_check_page(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_account_chart_check_page
    def test_010_advanced_search_account_chart_check_page(self, user):
        helper = AccountChartHelper(user)
        fields_data = account_chart_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ACT_ACCHRT_SER_ADVANCE(fields_data)
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