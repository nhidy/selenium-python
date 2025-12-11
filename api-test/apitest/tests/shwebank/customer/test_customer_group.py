from datetime import datetime
import json
import random
import pytest

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.customer.customer_group_helpers import CustomerGroupHelper
from apitest.src.payloads.customer.customer_group_payload import CustomerGroupPayload
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload

customer_group_payload = CustomerGroupPayload()
customer_single_payload = CustomerSinglePayload()

random_num = random.randrange(100, 1000)
working_date="2022-05-05"
hocifcd=""
customer_private_enterprise="E"
title="01"
title_of_organization=""
suffix=""
firstname="FIRST"
lastname="LAST"
midname=""
fullname_enterprise="FIRST LAST (fullname) Enterprise test add"
firstname_local=""
lastname_local=""
midname_local=""
shortname=""
gender=""
date_of_birth=datetime.fromisoformat("1992-02-25").strftime('%Y-%m-%dT%H:%M:%S')
place_of_birth="Place of birth (pob)"
nation="KH"
country="VN"
paper_type="I"
paper_number_enterprise="0731211"+ str(random_num)
issue_date_of_paper=datetime.fromisoformat("2022-03-21").strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_paper="id place sd"
expire_date_of_paper=datetime.fromisoformat("2023-03-22").strftime('%Y-%m-%dT%H:%M:%S')
paper_type_sub=""
paper_number_sub=""
issue_date_of_sub_paper=datetime.fromisoformat("2024-03-25").strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_sub_paper=""
customer_group_type=""
customer_sub_group_type=""
categories="C1"
sector="AX"
subsector="AXA"
resident="R"
address_local_legal="a lo"
province_legal="b"
village_legal="v"
sub_district_legal="s"
district_legal="d"
address_legal="a"
zipcode_legal="z"
address_local_contact="a lo c"
province_contact="b c"
village_contact="v c"
sub_district_contact="s c"
district_contact="d c"
address_contact="a c"
zipcode_contact="z c"
phone_home=""
phone_mobile=""
email=""
education=""
marital_status=""
profession="010101"
business_type="01010"
financial=""
isic_code=""
managing_branch_code="0999"
customer_status="P"
classify="N"
polists="N"
repolists="N"
country_of_income="AD"
fatca_status="N"
government_id=""
international_id=""
oversea_juristic_id=""
gfmis_code="98"
branchid=2
group_id=""
customer_credit_line=0
currency_code="USD"
customer_type="227"
primary_cif="N"
mdm_amount_status="1"
mdm_request_status="SUCCESS"
mdm_list_sub_type_code="PEPFR"
mdm_list_sub_type_desc=""
mdm_matching_by="IWLLA"
mdm_final_kyc_status="System: ระบบพบข้อมูลลูกค้าตรงกับ"
mdm_kyc_comment_code=""
mdm_kyc_comment_desc="KYCSTATUS: 3 CHECKLEVEL: 7 CUSTOMERID:  CPRIVATE: I RESIDENT: R REPOLISTS: N POLISTS: N NATION: KH COUNTRY:  ISICCD:  BUCD: 01010 PROFESSION: 010101"
kyc_level="3"
kyc_update_date=datetime.fromisoformat(working_date).strftime('%Y-%m-%dT%H:%M:%S')
relation_customer_id1=1
relation_customer_id2=2

relation_customer_id1_update=1
relation_customer_id2_update=3
position1_update="A"
position2_update="-"
list_members_update=[
    {
        "customer_id": relation_customer_id1_update,
        "position": position1_update
    },
    {
        "customer_id": relation_customer_id2_update,
        "position": position2_update
    }
]

# check type number
number_checklist = {
    "group_line": {
        "data_type": float,
        "number_of_digits": 2
    },
    "customer_id": {
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

@pytest.mark.customer_group
class TestCustomerGroup(object):


    @pytest.mark.simple_search_customer_group_before_add
    def test_001_simple_search_customer_group_before_add(self, user):
        global total_count
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.simple_search(
            page_size=5
        )
        rs = helper.SQL_SEARCH_CTMGRP(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_code' in rs['items'][0], f'Key \"group_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_name' in rs['items'][0], f'Key \"group_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_group_before_add
    def test_002_advanced_search_customer_group_before_add(self, user):
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.advanced_search(
            page_size=5
        )
        rs = helper.SQL_ADSEARCH_CTMGRP(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_code' in rs['items'][0], f'Key \"group_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_name' in rs['items'][0], f'Key \"group_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_customer_group
    def test_003_add_customer_group(self, user):
        global id_enterprise_new, customer_code_enterprise_new, id_new, group_code_new
        id_enterprise_new = 0
        customer_code_enterprise_new = ''
        id_new = 0
        group_code_new = ''
        helper = CustomerGroupHelper(user)
        helper_single = CustomerSingleHelper(user)
        fields_data = customer_single_payload.add(
            hocifcd=hocifcd,
            customer_private=customer_private_enterprise,
            title=title,
            title_of_organization=title_of_organization,
            suffix=suffix,
            firstname=firstname,
            lastname=lastname,
            midname=midname,
            fullname=fullname_enterprise,
            firstname_local=firstname_local,
            lastname_local=lastname_local,
            midname_local=midname_local,
            shortname=shortname,
            gender=gender,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            nation=nation,
            country=country,
            paper_type=paper_type,
            paper_number=paper_number_enterprise,
            issue_date_of_paper=issue_date_of_paper,
            issue_place_of_paper=issue_place_of_paper,
            expire_date_of_paper=expire_date_of_paper,
            paper_type_sub=paper_type_sub,
            paper_number_sub=paper_number_sub,
            issue_date_of_sub_paper=issue_date_of_sub_paper,
            issue_place_of_sub_paper=issue_place_of_sub_paper,
            customer_group_type=customer_group_type,
            customer_sub_group_type=customer_sub_group_type,
            categories=categories,
            sector=sector,
            subsector=subsector,
            resident=resident,
            address_local_legal=address_local_legal,
            province_legal=province_legal,
            village_legal=village_legal,
            sub_district_legal=sub_district_legal,
            district_legal=district_legal,
            address_legal=address_legal,
            zipcode_legal=zipcode_legal,
            address_local_contact=address_local_contact,
            province_contact=province_contact,
            village_contact=village_contact,
            sub_district_contact=sub_district_contact,
            district_contact=district_contact,
            address_contact=address_contact,
            zipcode_contact=zipcode_contact,
            phone_home=phone_home,
            phone_mobile=phone_mobile,
            email=email,
            education=education,
            marital_status=marital_status,
            profession=profession,
            business_type=business_type,
            financial=financial,
            isic_code=isic_code,
            managing_branch_code=managing_branch_code,
            customer_status=customer_status,
            classify=classify,
            polists=polists,
            repolists=repolists,
            country_of_income=country_of_income,
            fatca_status=fatca_status,
            government_id=government_id,
            international_id=international_id,
            oversea_juristic_id=oversea_juristic_id,
            gfmis_code=gfmis_code,
            branchid=branchid,
            group_id=group_id,
            customer_credit_line=customer_credit_line,
            currency_code=currency_code,
            customer_type=customer_type,
            primary_cif=primary_cif,
            mdm_amount_status=mdm_amount_status,
            mdm_request_status=mdm_request_status,
            mdm_list_sub_type_code=mdm_list_sub_type_code,
            mdm_list_sub_type_desc=mdm_list_sub_type_desc,
            mdm_matching_by=mdm_matching_by,
            mdm_final_kyc_status=mdm_final_kyc_status,
            mdm_kyc_comment_code=mdm_kyc_comment_code,
            mdm_kyc_comment_desc=mdm_kyc_comment_desc,
            kyc_level=kyc_level,
            kyc_update_date=kyc_update_date,
            relation_customer_id1=relation_customer_id1,
            relation_customer_id2=relation_customer_id2
        )
        rs = helper_single.SQL_INSERT_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_enterprise_new = rs['id']
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            customer_code_enterprise_new = rs['customer_code']
            # check add group
            fields_data = customer_group_payload.advanced_search(
                page_size=5,
                group_code=customer_code_enterprise_new
            )
            rs = helper.SQL_ADSEARCH_CTMGRP(fields_data)
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            search_rs = False
            total_item = len(rs['items'])
            if total_item > 0:
                for i in range(total_item):
                    if customer_code_enterprise_new in rs['items'][i]['group_code']:
                        id_new = rs['items'][i]['id']
                        group_code_new = rs['items'][i]['group_code']
                        search_rs = True
                        break
                assert search_rs, f'Search customer relation management fail. Expected: {customer_code_enterprise_new}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                assert total_item != 0, f'Search customer relation management fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all
            fields_data = customer_group_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_CTMGRP(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_group_after_add
    def test_004_simple_search_customer_group_after_add(self, user):
        search_rs = False
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.SQL_SEARCH_CTMGRP(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = customer_group_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.SQL_SEARCH_CTMGRP(fields_data)
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


    @pytest.mark.advanced_search_customer_group_after_add
    def test_005_advanced_search_customer_group_after_add(self, user):
        search_rs = False
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.advanced_search(
            page_size=50,
            group_name=search_text
        )
        rs = helper.SQL_ADSEARCH_CTMGRP(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 1) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = customer_group_payload.advanced_search(
                    page_size=total_count_adv,
                    group_name=search_text
                )
                rs = helper.SQL_ADSEARCH_CTMGRP(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['group_name']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.update_customer_group
    def test_006_update_customer_group(self, user):
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.update(
            id=id_new,
            list_members=list_members_update

        )
        rs = helper.SQL_UPDATE_CTMGRP(fields_data)
        try:
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_code' in rs, f'Key \"group_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_name' in rs, f'Key \"group_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'list_members' in rs, f'Key \"list_members\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_code_new == rs['group_code'], f'Expected \'{group_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['list_members']) > 0:
                assert 'customer_id' in rs['list_members'][0], f'Key \"customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['list_members'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['list_members'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'position' in rs['list_members'][0], f'Key \"position\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                check_data_type(rs['list_members'][0])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_customer_group
    def test_007_view_customer_group(self, user):
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.view(
            id=id_new
        )
        rs = helper.SQL_VIEW_CTMGRP(fields_data)
        try:
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_code' in rs, f'Key \"group_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_name' in rs, f'Key \"group_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'list_members' in rs, f'Key \"list_members\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check value
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_code_new == rs['group_code'], f'Expected \'{group_code_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['list_members']) == 2:
                # Check item 1
                assert 'customer_id' in rs['list_members'][0], f'Key \"customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['list_members'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['list_members'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'position' in rs['list_members'][0], f'Key \"position\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                check_data_type(rs['list_members'][0])
                assert relation_customer_id1_update == rs['list_members'][0]['customer_id'], f'Expected \'{relation_customer_id1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert position1_update == rs['list_members'][0]['position'], f'Expected \'{position1_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                # Check item 2
                assert 'customer_id' in rs['list_members'][1], f'Key \"customer_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['list_members'][1], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['list_members'][1], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'position' in rs['list_members'][1], f'Key \"position\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                check_data_type(rs['list_members'][1])
                assert relation_customer_id2_update == rs['list_members'][1]['customer_id'], f'Expected \'{relation_customer_id2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert position2_update == rs['list_members'][1]['position'], f'Expected \'{position2_update}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                assert len(rs['list_members']) == 2, f'View list_members fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after view
            fields_data = customer_group_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTMGRP(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.get_list_detail_customer_code
    def test_008_get_list_detail_customer_code(self, user):
        helper_single = CustomerSingleHelper(user)
        fields_data = customer_single_payload.get_list_detail_customer_code(
            customer_code=group_code_new
        )
        rs = helper_single.SQL_LOOKUP_LISTNOT_CTM(fields_data)
        try:
            # check key
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            search_rs = True
            # check value
            total_item = len(rs['items'])
            if total_item > 0:
                assert 'customer_code' in rs['items'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['items'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(total_item):
                    check_data_type(rs)
                    if group_code_new in rs['items'][i]['customer_code']:
                        search_rs = False
                        break
                assert search_rs, f'Get list detail customer code fail. Expected: {group_code_new}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                assert total_item != 0, f'Get list detail customer code fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_customer_group
    def test_009_delete_customer_group(self, user):
        helper = CustomerGroupHelper(user)
        helper_single = CustomerSingleHelper(user)
        fields_data = customer_group_payload.delete(
            id=id_new
        )
        rs = helper.SQL_DELETE_CTMGRP(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_new == rs['id'], f'Expected \'{id_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = customer_group_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTMGRP(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data test
            fields_data = customer_single_payload.delete(
            id=id_enterprise_new
            )
            rs = helper_single.SQL_DELETE_CTM(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_enterprise_new == rs['id'], f'Expected \'{id_enterprise_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_group_check_page
    def test_010_simple_search_customer_group_check_page(self, user):
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_SEARCH_CTMGRP(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_group_check_page
    def test_011_advanced_search_customer_group_check_page(self, user):
        helper = CustomerGroupHelper(user)
        fields_data = customer_group_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_ADSEARCH_CTMGRP(fields_data)
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