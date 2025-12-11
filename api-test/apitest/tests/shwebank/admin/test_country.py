import json
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.country_helpers import CountryHelper
from apitest.src.payloads.admin.country_payload import CountryPayload

country_payload = CountryPayload()

iso2_alpha="KH"
iso3_alpha="KHM"
country_name="Cambodia test"
country_name1="country 1"
country_name2="country 2"
country_name3="country 3"
country_short_name="Cambodian"
short_name1="short 1"
short_name2="short 2"
short_name3="short 3"
currency_code="KHR"
main_language="EN"
status_of_country="N"
order=1
region_of_country="A"

iso2_alpha_update="KU"
iso3_alpha_update="KHU"
country_name_update="Cambodia test up"
country_name1_update="country 1 up"
country_name2_update="country 2 up"
country_name3_update="country 3 up"
country_short_name_update="Cambodian"
short_name1_update="short 1 up"
short_name2_update="short 2 up"
short_name3_update="short 3 up"
currency_code_update="KHU"
main_language_update="EU"
status_of_country_update="B"
order_update=2
region_of_country_update="V"

# check type number
number_checklist = {
    "order": {
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

@pytest.mark.country
class TestCountry(object):


    @pytest.mark.simple_search_country_before_add
    def test_001_simple_search_country_before_add(self, user):
        global total_count
        helper = CountryHelper(user)
        fields_data = country_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'iso2_alpha' in rs['items'][0], f'Key \"iso2_alpha\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'iso3_alpha' in rs['items'][0], f'Key \"iso3_alpha\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'country_name' in rs['items'][0], f'Key \"country_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_country_before_add
    def test_002_advanced_search_country_before_add(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.advanced_search(
            page_size=5
        )
        rs = helper.ADM_ADVANCED_SEARCH_COUNTRY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'iso2_alpha' in rs['items'][0], f'Key \"iso2_alpha\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'iso3_alpha' in rs['items'][0], f'Key \"iso3_alpha\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'country_name' in rs['items'][0], f'Key \"country_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_country
    def test_003_add_country(self, user):
        global id_new
        id_new = 1
        helper = CountryHelper(user)
        fields_data = country_payload.add(
            iso2_alpha=iso2_alpha,
            iso3_alpha=iso3_alpha,
            country_name=country_name,
            country_name1=country_name1,
            country_name2=country_name2,
            country_name3=country_name3,
            country_short_name=country_short_name,
            short_name1=short_name1,
            short_name2=short_name2,
            short_name3=short_name3,
            currency_code=currency_code,
            main_language=main_language,
            status_of_country=status_of_country,
            order=order,
            region_of_country=region_of_country
        )
        rs = helper.ADM_INSERT_COUNTRY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']

            # check result
            assert iso2_alpha == rs['iso2_alpha'], f'Expected \'{iso2_alpha}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert iso3_alpha == rs['iso3_alpha'], f'Expected \'{iso3_alpha}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name == rs['country_name'], f'Expected \'{country_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name1 == rs['country_name1'], f'Expected \'{country_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name2 == rs['country_name2'], f'Expected \'{country_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name3 == rs['country_name3'], f'Expected \'{country_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_short_name == rs['country_short_name'], f'Expected \'{country_short_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name1 == rs['short_name1'], f'Expected \'{short_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name2 == rs['short_name2'], f'Expected \'{short_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name3 == rs['short_name3'], f'Expected \'{short_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_country == rs['status_of_country'], f'Expected \'{status_of_country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert region_of_country == rs['region_of_country'], f'Expected \'{region_of_country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)

            # check total_count search all
            fields_data = country_payload.simple_search(
                page_size=5
            )
            rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_country_after_add
    def test_004_simple_search_country_after_add(self, user):
        search_rs = False
        helper = CountryHelper(user)
        fields_data = country_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = country_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
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


    @pytest.mark.advanced_search_country_after_add
    def test_005_advanced_search_country_after_add(self, user):
        search_rs = False
        helper = CountryHelper(user)
        fields_data = country_payload.advanced_search(
            page_size=50,
            country_name=country_name
        )
        rs = helper.ADM_ADVANCED_SEARCH_COUNTRY(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{country_name}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = country_payload.advanced_search(
                    page_size=total_count_adv,
                    country_name=country_name
                )
                rs = helper.ADM_ADVANCED_SEARCH_COUNTRY(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if country_name in rs['items'][i]['country_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {country_name}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_country
    def test_006_update_country(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.update(
            id=id_new,
            iso2_alpha=iso2_alpha_update,
            iso3_alpha=iso3_alpha_update,
            country_name=country_name_update,
            country_name1=country_name1_update,
            country_name2=country_name2_update,
            country_name3=country_name3_update,
            country_short_name=country_short_name_update,
            short_name1=short_name1_update,
            short_name2=short_name2_update,
            short_name3=short_name3_update,
            currency_code=currency_code_update,
            main_language=main_language_update,
            status_of_country=status_of_country_update,
            order=order_update,
            region_of_country=region_of_country_update
        )
        rs = helper.ADM_UPDATE_COUNTRY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert iso2_alpha_update == rs['iso2_alpha'], f'Expected \'{iso2_alpha_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert iso3_alpha_update == rs['iso3_alpha'], f'Expected \'{iso3_alpha_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name_update == rs['country_name'], f'Expected \'{country_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name1_update == rs['country_name1'], f'Expected \'{country_name1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name2_update == rs['country_name2'], f'Expected \'{country_name2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name3_update == rs['country_name3'], f'Expected \'{country_name3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_short_name_update == rs['country_short_name'], f'Expected \'{country_short_name_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name1_update == rs['short_name1'], f'Expected \'{short_name1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name2_update == rs['short_name2'], f'Expected \'{short_name2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name3_update == rs['short_name3'], f'Expected \'{short_name3_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code_update == rs['currency_code'], f'Expected \'{currency_code_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language_update == rs['main_language'], f'Expected \'{main_language_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_country_update == rs['status_of_country'], f'Expected \'{status_of_country_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order_update == rs['order'], f'Expected \'{order_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert region_of_country_update == rs['region_of_country'], f'Expected \'{region_of_country_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_country
    def test_007_delete_country(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.delete(
            id=id_new
        )
        rs = helper.ADM_DELETE_COUNTRY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = country_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_country
    def test_008_view_country(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.add(
            iso2_alpha=iso2_alpha,
            iso3_alpha=iso3_alpha,
            country_name=country_name,
            country_name1=country_name1,
            country_name2=country_name2,
            country_name3=country_name3,
            country_short_name=country_short_name,
            short_name1=short_name1,
            short_name2=short_name2,
            short_name3=short_name3,
            currency_code=currency_code,
            main_language=main_language,
            status_of_country=status_of_country,
            order=order,
            region_of_country=region_of_country
        )
        rs = helper.ADM_INSERT_COUNTRY(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_new = rs['id']
            fields_data = country_payload.view(
                id=id_new
            )
            rs = helper.ADM_VIEW_COUNTRY(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert iso2_alpha == rs['iso2_alpha'], f'Expected \'{iso2_alpha}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert iso3_alpha == rs['iso3_alpha'], f'Expected \'{iso3_alpha}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name == rs['country_name'], f'Expected \'{country_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name1 == rs['country_name1'], f'Expected \'{country_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name2 == rs['country_name2'], f'Expected \'{country_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_name3 == rs['country_name3'], f'Expected \'{country_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_short_name == rs['country_short_name'], f'Expected \'{country_short_name}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name1 == rs['short_name1'], f'Expected \'{short_name1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name2 == rs['short_name2'], f'Expected \'{short_name2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert short_name3 == rs['short_name3'], f'Expected \'{short_name3}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert main_language == rs['main_language'], f'Expected \'{main_language}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert status_of_country == rs['status_of_country'], f'Expected \'{status_of_country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert order == rs['order'], f'Expected \'{order}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert region_of_country == rs['region_of_country'], f'Expected \'{region_of_country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after view
            fields_data = country_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = country_payload.delete(
                id=id_new
            )
            rs = helper.ADM_DELETE_COUNTRY(fields_data)
            # check total_count search all after delete
            fields_data = country_payload.simple_search(
                page_size=50
            )
            rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_country_check_page
    def test_009_simple_search_country_check_page(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_country_check_page
    def test_010_advanced_search_country_check_page(self, user):
        helper = CountryHelper(user)
        fields_data = country_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.ADM_ADVANCED_SEARCH_COUNTRY(fields_data)
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