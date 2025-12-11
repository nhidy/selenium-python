from datetime import datetime
import json
import random
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
from apitest.src.helpers.customer.customer_group_helpers import CustomerGroupHelper
from apitest.src.payloads.customer.customer_group_payload import CustomerGroupPayload

customer_single_payload = CustomerSinglePayload()
customer_group_payload = CustomerGroupPayload()

random_num = random.randrange(100, 1000)
working_date=str(datetime.now()) # "2022-05-09" 
hocifcd=""
customer_private_enterprise="E"
customer_private_individual="I"
title="01"
title_of_organization=""
suffix=""
firstname="FIRST"
lastname="LAST"
midname=""
fullname_enterprise="FIRST LAST (fullname) Enterprise test add"
fullname_individual="FIRST LAST (fullname) Individual test add"
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
paper_number_individual="0731311"+ str(random_num)
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
customer_credit_line=400005.96
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


hocifcd_update="old"
title_update=""
title_of_organization_update=""
suffix_update=""
firstname_update=""
lastname_update=""
midname_update=""
fullname_update="FIRST LAST (fullname) test update"
firstname_local_update=""
lastname_local_update=""
midname_local_update=""
shortname_update=""
gender_update=""
date_of_birth_update=datetime.fromisoformat("1998-02-25").strftime('%Y-%m-%dT%H:%M:%S')
place_of_birth_update=""
nation_update=""
country_update=""
paper_type_update=""
paper_number_update="0731212"+ str(random_num)
issue_date_of_paper_update=datetime.fromisoformat("2022-05-25").strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_paper_update=""
expire_date_of_paper_update=datetime.fromisoformat("2023-03-25").strftime('%Y-%m-%dT%H:%M:%S')
paper_type_sub_update=""
paper_number_sub_update=""
issue_date_of_sub_paper_update=datetime.fromisoformat("2024-06-25").strftime('%Y-%m-%dT%H:%M:%S')
issue_place_of_sub_paper_update=""
customer_group_type_update=""
customer_sub_group_type_update=""
sector_update="AX"
subsector_update="AXA"
resident_update="R"
address_local_legal_update="a"
province_legal_update="b"
village_legal_update="v"
sub_district_legal_update="c"
district_legal_update="s"
address_legal_update="e"
zipcode_legal_update="w"
address_local_contact_update="t"
province_contact_update="r"
village_contact_update="t"
sub_district_contact_update="4"
district_contact_update="3"
address_contact_update="r"
zipcode_contact_update="f"
phone_home_update=""
phone_mobile_update=""
email_update=""
education_update=""
marital_status_update=""
profession_update=""
business_type_update=""
financial_update=""
isic_code_update=""
managing_branch_code_update=""
classify_update=""
polists_update=""
repolists_update=""
country_of_income_update=""
fatca_status_update=""
government_id_update=""
international_id_update=""
oversea_juristic_id_update=""
gfmis_code_update=""
last_update_date_update=datetime.fromisoformat(working_date).strftime('%Y-%m-%dT%H:%M:%S')
group_id_update=""
customer_credit_line_update=0
currency_code_update=""
customer_type_update=""
primary_cif_update=""
mdm_amount_status_update=""
mdm_request_status_update=""
mdm_list_sub_type_code_update=""
mdm_list_sub_type_desc_update=""
mdm_matching_by_update=""
mdm_final_kyc_status_update=""
mdm_kyc_comment_code_update=""
mdm_kyc_comment_desc_update=""
kyc_level_update="3"
kyc_update_date_update=datetime.fromisoformat(working_date).strftime('%Y-%m-%dT%H:%M:%S')
kyc_override_update=""
kyc_override_descr_update=""

# check type number
number_checklist = {
    "customer_credit_line": {
        "data_type": float,
        "number_of_digits": 3
    },
    "branchid": {
        "data_type": int,
        "number_of_digits": 0
    },
    "staff_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "approve_user_id": {
        "data_type": int,
        "number_of_digits": 0
    },
    "customer_realation_staff_id": {
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

@pytest.mark.customer_single
class TestCustomerSingle(object):


    @pytest.mark.simple_search_customer_single_before_add
    def test_001_simple_search_customer_single_before_add(self, user):
        global total_count
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.simple_search(
            page_size=5
        )
        rs = helper.SQL_SEARCH_CTM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['items'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['items'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'shortname' in rs['items'][0], f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'paper_number' in rs['items'][0], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'date_of_birth' in rs['items'][0], f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'gender' in rs['items'][0], f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_status' in rs['items'][0], f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'nation' in rs['items'][0], f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'resident' in rs['items'][0], f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'old_id_of_customer' in rs['items'][0], f'Key \"old_id_of_customer\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_id' in rs['items'][0], f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'contact_local_address' in rs['items'][0], f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_single_before_add
    def test_002_advanced_search_customer_single_before_add(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.advanced_search(
            page_size=5
        )
        rs = helper.SQL_ADSEARCH_CTM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['items'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['items'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'shortname' in rs['items'][0], f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'paper_number' in rs['items'][0], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'date_of_birth' in rs['items'][0], f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'gender' in rs['items'][0], f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_status' in rs['items'][0], f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'nation' in rs['items'][0], f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'resident' in rs['items'][0], f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'old_id_of_customer' in rs['items'][0], f'Key \"old_id_of_customer\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_id' in rs['items'][0], f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'contact_local_address' in rs['items'][0], f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_customer_single_enterprise
    def test_003_add_customer_single_enterprise(self, user):
        global id_enterprise_new, customer_code_enterprise_new, id_group_new
        id_enterprise_new = 0
        customer_code_enterprise_new = ''
        id_group_new = 0
        helper = CustomerSingleHelper(user)
        helper_group = CustomerGroupHelper(user)
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
        rs = helper.SQL_INSERT_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_enterprise_new = rs['id']
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            customer_code_enterprise_new = rs['customer_code']
            assert 'hocifcd' in rs, f'Key \"hocifcd\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_private' in rs, f'Key \"customer_private\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title' in rs, f'Key \"title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title_of_organization' in rs, f'Key \"title_of_organization\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'suffix' in rs, f'Key \"suffix\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname' in rs, f'Key \"firstname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname' in rs, f'Key \"lastname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname' in rs, f'Key \"midname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fullname' in rs, f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname_local' in rs, f'Key \"firstname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname_local' in rs, f'Key \"lastname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname_local' in rs, f'Key \"midname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'shortname' in rs, f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gender' in rs, f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'date_of_birth' in rs, f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'place_of_birth' in rs, f'Key \"place_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'nation' in rs, f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country' in rs, f'Key \"country\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs, f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs, f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_paper' in rs, f'Key \"issue_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_paper' in rs, f'Key \"issucde_place_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expire_date_of_paper' in rs, f'Key \"expire_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type_sub' in rs, f'Key \"paper_type_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number_sub' in rs, f'Key \"paper_number_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_sub_paper' in rs, f'Key \"issue_date_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_sub_paper' in rs, f'Key \"issue_place_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_group_type' in rs, f'Key \"customer_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_sub_group_type' in rs, f'Key \"customer_sub_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'categories' in rs, f'Key \"categories\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sector' in rs, f'Key \"sector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'subsector' in rs, f'Key \"subsector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'resident' in rs, f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['legal_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['legal_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'contact_local_address' in rs, f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['contact_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['contact_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['contact_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['contact_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['contact_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['contact_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['contact_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_home' in rs, f'Key \"phone_home\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_mobile' in rs, f'Key \"phone_mobile\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'email' in rs, f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'education' in rs, f'Key \"education\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'marital_status' in rs, f'Key \"marital_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'profession' in rs, f'Key \"profession\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'business_type' in rs, f'Key \"business_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'financial' in rs, f'Key \"financial\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'isic_code' in rs, f'Key \"isic_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'managing_branch_code' in rs, f'Key \"managing_branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_status' in rs, f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'classify' in rs, f'Key \"classify\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'polists' in rs, f'Key \"polists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'repolists' in rs, f'Key \"repolists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country_of_income' in rs, f'Key \"country_of_income\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fatca_status' in rs, f'Key \"fatca_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'government_id' in rs, f'Key \"government_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'international_id' in rs, f'Key \"international_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'oversea_juristic_id' in rs, f'Key \"oversea_juristic_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gfmis_code' in rs, f'Key \"gfmis_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branchid' in rs, f'Key \"branchid\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_credit_line' in rs, f'Key \"customer_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_type' in rs, f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'primary_cif' in rs, f'Key \"primary_cif\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_amount_status' in rs, f'Key \"mdm_amount_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_request_status' in rs, f'Key \"mdm_request_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_code' in rs, f'Key \"mdm_list_sub_type_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_desc' in rs, f'Key \"mdm_list_sub_type_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_matching_by' in rs, f'Key \"mdm_matching_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_final_kyc_status' in rs, f'Key \"mdm_final_kyc_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_code' in rs, f'Key \"mdm_kyc_comment_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_desc' in rs, f'Key \"mdm_kyc_comment_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_level' in rs, f'Key \"kyc_level\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_update_date' in rs, f'Key \"kyc_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check result
            assert hocifcd == rs['hocifcd'], f'Expected \'{hocifcd}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_private_enterprise == rs['customer_private'], f'Expected \'{customer_private_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title == rs['title'], f'Expected \'{title}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title_of_organization == rs['title_of_organization'], f'Expected \'{title_of_organization}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert suffix == rs['suffix'], f'Expected \'{suffix}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname == rs['firstname'], f'Expected \'{firstname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname == rs['lastname'], f'Expected \'{lastname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname == rs['midname'], f'Expected \'{midname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fullname_enterprise == rs['fullname'], f'Expected \'{fullname_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname_local == rs['firstname_local'], f'Expected \'{firstname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname_local == rs['lastname_local'], f'Expected \'{lastname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname_local == rs['midname_local'], f'Expected \'{midname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert shortname == rs['shortname'], f'Expected \'{shortname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gender == rs['gender'], f'Expected \'{gender}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_of_birth == rs['date_of_birth'], f'Expected \'{date_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert place_of_birth == rs['place_of_birth'], f'Expected \'{place_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert nation == rs['nation'], f'Expected \'{nation}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type == rs['paper_type'], f'Expected \'{paper_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_enterprise == rs['paper_number'], f'Expected \'{paper_number_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_paper == rs['issue_date_of_paper'], f'Expected \'{issue_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_paper == rs['issue_place_of_paper'], f'Expected \'{issue_place_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date_of_paper == rs['expire_date_of_paper'], f'Expected \'{expire_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_sub == rs['paper_type_sub'], f'Expected \'{paper_type_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_sub == rs['paper_number_sub'], f'Expected \'{paper_number_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_sub_paper == rs['issue_date_of_sub_paper'], f'Expected \'{issue_date_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_sub_paper == rs['issue_place_of_sub_paper'], f'Expected \'{issue_place_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_group_type == rs['customer_group_type'], f'Expected \'{customer_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_sub_group_type == rs['customer_sub_group_type'], f'Expected \'{customer_sub_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subsector == rs['subsector'], f'Expected \'{subsector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident == rs['resident'], f'Expected \'{resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_legal == rs['legal_local_address']['address_local'], f'Expected \'{address_local_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_legal == rs['legal_local_address']['province'], f'Expected \'{province_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal == rs['legal_local_address']['village'], f'Expected \'{village_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal == rs['legal_local_address']['district'], f'Expected \'{district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal == rs['legal_local_address']['address'], f'Expected \'{address_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_legal == rs['legal_local_address']['zipcode'], f'Expected \'{zipcode_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_contact == rs['contact_local_address']['address_local'], f'Expected \'{address_local_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_contact == rs['contact_local_address']['province'], f'Expected \'{province_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_contact == rs['contact_local_address']['village'], f'Expected \'{village_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_contact == rs['contact_local_address']['sub_district'], f'Expected \'{sub_district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_contact == rs['contact_local_address']['district'], f'Expected \'{district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_contact == rs['contact_local_address']['address'], f'Expected \'{address_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_contact == rs['contact_local_address']['zipcode'], f'Expected \'{zipcode_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_home == rs['phone_home'], f'Expected \'{phone_home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_mobile == rs['phone_mobile'], f'Expected \'{phone_mobile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert email == rs['email'], f'Expected \'{email}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert education == rs['education'], f'Expected \'{education}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert marital_status == rs['marital_status'], f'Expected \'{marital_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert profession == rs['profession'], f'Expected \'{profession}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert business_type == rs['business_type'], f'Expected \'{business_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert financial == rs['financial'], f'Expected \'{financial}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert isic_code == rs['isic_code'], f'Expected \'{isic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert managing_branch_code == rs['managing_branch_code'], f'Expected \'{managing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_status == rs['customer_status'], f'Expected \'{customer_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classify == rs['classify'], f'Expected \'{classify}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert polists == rs['polists'], f'Expected \'{polists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert repolists == rs['repolists'], f'Expected \'{repolists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_of_income == rs['country_of_income'], f'Expected \'{country_of_income}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fatca_status == rs['fatca_status'], f'Expected \'{fatca_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert government_id == rs['government_id'], f'Expected \'{government_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert international_id == rs['international_id'], f'Expected \'{international_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert oversea_juristic_id == rs['oversea_juristic_id'], f'Expected \'{oversea_juristic_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gfmis_code == rs['gfmis_code'], f'Expected \'{gfmis_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branchid == rs['branchid'], f'Expected \'{branchid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_credit_line == rs['customer_credit_line'], f'Expected \'{customer_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert primary_cif == rs['primary_cif'], f'Expected \'{primary_cif}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_amount_status == rs['mdm_amount_status'], f'Expected \'{mdm_amount_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_request_status == rs['mdm_request_status'], f'Expected \'{mdm_request_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_code == rs['mdm_list_sub_type_code'], f'Expected \'{mdm_list_sub_type_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_desc == rs['mdm_list_sub_type_desc'], f'Expected \'{mdm_list_sub_type_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_matching_by == rs['mdm_matching_by'], f'Expected \'{mdm_matching_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_final_kyc_status == rs['mdm_final_kyc_status'], f'Expected \'{mdm_final_kyc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_code == rs['mdm_kyc_comment_code'], f'Expected \'{mdm_kyc_comment_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_desc == rs['mdm_kyc_comment_desc'], f'Expected \'{mdm_kyc_comment_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert kyc_level == rs['kyc_level'], f'Expected \'{kyc_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert kyc_update_date == rs['kyc_update_date'], f'Expected \'{kyc_update_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = customer_single_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check relation customer information in customer relation management
            fields_data = customer_group_payload.advanced_search(
                page_size=5,
                group_code=customer_code_enterprise_new
            )
            rs = helper_group.SQL_ADSEARCH_CTMGRP(fields_data)
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            search_rs = False
            total_item = len(rs['items'])
            if total_item > 0:
                for i in range(total_item):
                    if customer_code_enterprise_new in rs['items'][i]['group_code']:
                        id_group_new = rs['items'][i]['id']
                        search_rs = True
                        break
                assert search_rs, f'Search customer relation management fail. Expected: {customer_code_enterprise_new}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                assert total_item != 0, f'Search customer relation management fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.add_customer_single_individual
    def test_004_add_customer_single_individual(self, user):
        global id_individual_new, customer_code_individual_new
        id_individual_new = 0
        customer_code_individual_new = ''
        helper = CustomerSingleHelper(user)
        helper_group = CustomerGroupHelper(user)
        fields_data = customer_single_payload.add(
            hocifcd=hocifcd,
            customer_private=customer_private_individual,
            title=title,
            title_of_organization=title_of_organization,
            suffix=suffix,
            firstname=firstname,
            lastname=lastname,
            midname=midname,
            fullname=fullname_individual,
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
            paper_number=paper_number_individual,
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
        rs = helper.SQL_INSERT_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_individual_new = rs['id']
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            customer_code_individual_new = rs['customer_code']
            assert 'hocifcd' in rs, f'Key \"hocifcd\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_private' in rs, f'Key \"customer_private\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title' in rs, f'Key \"title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title_of_organization' in rs, f'Key \"title_of_organization\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'suffix' in rs, f'Key \"suffix\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname' in rs, f'Key \"firstname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname' in rs, f'Key \"lastname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname' in rs, f'Key \"midname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fullname' in rs, f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname_local' in rs, f'Key \"firstname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname_local' in rs, f'Key \"lastname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname_local' in rs, f'Key \"midname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'shortname' in rs, f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gender' in rs, f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'date_of_birth' in rs, f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'place_of_birth' in rs, f'Key \"place_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'nation' in rs, f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country' in rs, f'Key \"country\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs, f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs, f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_paper' in rs, f'Key \"issue_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_paper' in rs, f'Key \"issucde_place_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expire_date_of_paper' in rs, f'Key \"expire_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type_sub' in rs, f'Key \"paper_type_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number_sub' in rs, f'Key \"paper_number_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_sub_paper' in rs, f'Key \"issue_date_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_sub_paper' in rs, f'Key \"issue_place_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_group_type' in rs, f'Key \"customer_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_sub_group_type' in rs, f'Key \"customer_sub_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'categories' in rs, f'Key \"categories\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sector' in rs, f'Key \"sector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'subsector' in rs, f'Key \"subsector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'resident' in rs, f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['legal_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['legal_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'contact_local_address' in rs, f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['contact_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['contact_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['contact_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['contact_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['contact_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['contact_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['contact_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_home' in rs, f'Key \"phone_home\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_mobile' in rs, f'Key \"phone_mobile\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'email' in rs, f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'education' in rs, f'Key \"education\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'marital_status' in rs, f'Key \"marital_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'profession' in rs, f'Key \"profession\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'business_type' in rs, f'Key \"business_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'financial' in rs, f'Key \"financial\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'isic_code' in rs, f'Key \"isic_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'managing_branch_code' in rs, f'Key \"managing_branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_status' in rs, f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'classify' in rs, f'Key \"classify\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'polists' in rs, f'Key \"polists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'repolists' in rs, f'Key \"repolists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country_of_income' in rs, f'Key \"country_of_income\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fatca_status' in rs, f'Key \"fatca_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'government_id' in rs, f'Key \"government_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'international_id' in rs, f'Key \"international_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'oversea_juristic_id' in rs, f'Key \"oversea_juristic_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gfmis_code' in rs, f'Key \"gfmis_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branchid' in rs, f'Key \"branchid\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_credit_line' in rs, f'Key \"customer_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_type' in rs, f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'primary_cif' in rs, f'Key \"primary_cif\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_amount_status' in rs, f'Key \"mdm_amount_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_request_status' in rs, f'Key \"mdm_request_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_code' in rs, f'Key \"mdm_list_sub_type_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_desc' in rs, f'Key \"mdm_list_sub_type_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_matching_by' in rs, f'Key \"mdm_matching_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_final_kyc_status' in rs, f'Key \"mdm_final_kyc_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_code' in rs, f'Key \"mdm_kyc_comment_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_desc' in rs, f'Key \"mdm_kyc_comment_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_level' in rs, f'Key \"kyc_level\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_update_date' in rs, f'Key \"kyc_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # check result
            assert hocifcd == rs['hocifcd'], f'Expected \'{hocifcd}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_private_individual == rs['customer_private'], f'Expected \'{customer_private_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title == rs['title'], f'Expected \'{title}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title_of_organization == rs['title_of_organization'], f'Expected \'{title_of_organization}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert suffix == rs['suffix'], f'Expected \'{suffix}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname == rs['firstname'], f'Expected \'{firstname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname == rs['lastname'], f'Expected \'{lastname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname == rs['midname'], f'Expected \'{midname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fullname_individual == rs['fullname'], f'Expected \'{fullname_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname_local == rs['firstname_local'], f'Expected \'{firstname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname_local == rs['lastname_local'], f'Expected \'{lastname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname_local == rs['midname_local'], f'Expected \'{midname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert shortname == rs['shortname'], f'Expected \'{shortname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gender == rs['gender'], f'Expected \'{gender}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_of_birth == rs['date_of_birth'], f'Expected \'{date_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert place_of_birth == rs['place_of_birth'], f'Expected \'{place_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert nation == rs['nation'], f'Expected \'{nation}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type == rs['paper_type'], f'Expected \'{paper_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_individual == rs['paper_number'], f'Expected \'{paper_number_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_paper == rs['issue_date_of_paper'], f'Expected \'{issue_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_paper == rs['issue_place_of_paper'], f'Expected \'{issue_place_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date_of_paper == rs['expire_date_of_paper'], f'Expected \'{expire_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_sub == rs['paper_type_sub'], f'Expected \'{paper_type_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_sub == rs['paper_number_sub'], f'Expected \'{paper_number_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_sub_paper == rs['issue_date_of_sub_paper'], f'Expected \'{issue_date_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_sub_paper == rs['issue_place_of_sub_paper'], f'Expected \'{issue_place_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_group_type == rs['customer_group_type'], f'Expected \'{customer_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_sub_group_type == rs['customer_sub_group_type'], f'Expected \'{customer_sub_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subsector == rs['subsector'], f'Expected \'{subsector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident == rs['resident'], f'Expected \'{resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_legal == rs['legal_local_address']['address_local'], f'Expected \'{address_local_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_legal == rs['legal_local_address']['province'], f'Expected \'{province_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal == rs['legal_local_address']['village'], f'Expected \'{village_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal == rs['legal_local_address']['district'], f'Expected \'{district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal == rs['legal_local_address']['address'], f'Expected \'{address_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_legal == rs['legal_local_address']['zipcode'], f'Expected \'{zipcode_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_contact == rs['contact_local_address']['address_local'], f'Expected \'{address_local_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_contact == rs['contact_local_address']['province'], f'Expected \'{province_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_contact == rs['contact_local_address']['village'], f'Expected \'{village_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_contact == rs['contact_local_address']['sub_district'], f'Expected \'{sub_district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_contact == rs['contact_local_address']['district'], f'Expected \'{district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_contact == rs['contact_local_address']['address'], f'Expected \'{address_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_contact == rs['contact_local_address']['zipcode'], f'Expected \'{zipcode_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_home == rs['phone_home'], f'Expected \'{phone_home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_mobile == rs['phone_mobile'], f'Expected \'{phone_mobile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert email == rs['email'], f'Expected \'{email}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert education == rs['education'], f'Expected \'{education}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert marital_status == rs['marital_status'], f'Expected \'{marital_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert profession == rs['profession'], f'Expected \'{profession}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert business_type == rs['business_type'], f'Expected \'{business_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert financial == rs['financial'], f'Expected \'{financial}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert isic_code == rs['isic_code'], f'Expected \'{isic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert managing_branch_code == rs['managing_branch_code'], f'Expected \'{managing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_status == rs['customer_status'], f'Expected \'{customer_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classify == rs['classify'], f'Expected \'{classify}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert polists == rs['polists'], f'Expected \'{polists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert repolists == rs['repolists'], f'Expected \'{repolists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_of_income == rs['country_of_income'], f'Expected \'{country_of_income}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fatca_status == rs['fatca_status'], f'Expected \'{fatca_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert government_id == rs['government_id'], f'Expected \'{government_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert international_id == rs['international_id'], f'Expected \'{international_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert oversea_juristic_id == rs['oversea_juristic_id'], f'Expected \'{oversea_juristic_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gfmis_code == rs['gfmis_code'], f'Expected \'{gfmis_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branchid == rs['branchid'], f'Expected \'{branchid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_credit_line == rs['customer_credit_line'], f'Expected \'{customer_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert primary_cif == rs['primary_cif'], f'Expected \'{primary_cif}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_amount_status == rs['mdm_amount_status'], f'Expected \'{mdm_amount_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_request_status == rs['mdm_request_status'], f'Expected \'{mdm_request_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_code == rs['mdm_list_sub_type_code'], f'Expected \'{mdm_list_sub_type_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_desc == rs['mdm_list_sub_type_desc'], f'Expected \'{mdm_list_sub_type_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_matching_by == rs['mdm_matching_by'], f'Expected \'{mdm_matching_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_final_kyc_status == rs['mdm_final_kyc_status'], f'Expected \'{mdm_final_kyc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_code == rs['mdm_kyc_comment_code'], f'Expected \'{mdm_kyc_comment_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_desc == rs['mdm_kyc_comment_desc'], f'Expected \'{mdm_kyc_comment_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert kyc_level == rs['kyc_level'], f'Expected \'{kyc_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert kyc_update_date == rs['kyc_update_date'], f'Expected \'{kyc_update_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all
            fields_data = customer_single_payload.simple_search(
                page_size=5
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 2) == rs['total_count'], f'Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check relation customer information in customer relation management
            fields_data = customer_group_payload.advanced_search(
                page_size=5,
                group_code=customer_code_individual_new
            )
            rs = helper_group.SQL_ADSEARCH_CTMGRP(fields_data)
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            search_rs = True
            total_item = len(rs['items'])
            if total_item > 0:
                for i in range(total_item):
                    if customer_code_enterprise_new in rs['items'][i]['group_code']:
                        search_rs = False
                        break
                assert search_rs, f'Search customer relation management fail. Expected: {customer_code_enterprise_new} not exitsed, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == len(rs['items']), f'Expected 0 items, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_single_after_add
    def test_005_simple_search_customer_single_after_add(self, user):
        search_rs = False
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.simple_search(
            page_size=5,
            search_text=search_text
        )
        rs = helper.SQL_SEARCH_CTM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 2) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with simple search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_sp = rs['total_count']
                # show all items
                fields_data = customer_single_payload.simple_search(
                    page_size=total_count_sp,
                    search_text=search_text
                )
                rs = helper.SQL_SEARCH_CTM(fields_data)
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


    @pytest.mark.advanced_search_customer_single_after_add
    def test_006_advanced_search_customer_single_after_add(self, user):
        search_rs = False
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.advanced_search(
            page_size=50,
            fullname=search_text
        )
        rs = helper.SQL_ADSEARCH_CTM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if (total_count + 2) == rs['total_count'] or rs['total_count'] == 0:
                assert search_rs, f'Search with advanced search fail. Expected: \"{search_text}\", Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                total_count_adv = rs['total_count']
                # show all items
                fields_data = customer_single_payload.advanced_search(
                    page_size=total_count_adv,
                    fullname=search_text
                )
                rs = helper.SQL_ADSEARCH_CTM(fields_data)
                # check value
                total_item = len(rs['items'])
                if total_item > 0:
                    for i in range(total_item):
                        if search_text in rs['items'][i]['fullname']:
                            search_rs = True
                            break
                    assert search_rs, f'Search with advanced search fail. Expected: {search_text}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                else:
                    assert total_item != 0, f'Search with advanced search fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_customer_single_enterprise
    def test_007_delete_customer_single_enterprise(self, user):
        helper = CustomerSingleHelper(user)
        helper_group = CustomerGroupHelper(user)
        fields_data = customer_single_payload.delete(
            id=id_enterprise_new
        )
        rs = helper.SQL_DELETE_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_enterprise_new == rs['id'], f'Expected \'{id_enterprise_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # Delete data test
            # fields_data = customer_group_payload.delete(
            #     id=id_group_new
            # )
            # rs = helper_group.SQL_DELETE_CTMGRP(fields_data)
            # assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert id_group_new == rs['id'], f'Expected \'{id_group_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.delete_customer_single_individual
    def test_008_delete_customer_single_individual(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.delete(
            id=id_individual_new
        )
        rs = helper.SQL_DELETE_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_individual_new == rs['id'], f'Expected \'{id_individual_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # check total_count search all after delete
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_customer_single_enterprise
    def test_009_view_customer_single_enterprise(self, user):
        helper = CustomerSingleHelper(user)
        helper_group = CustomerGroupHelper(user)
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
        rs = helper.SQL_INSERT_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_enterprise_new = rs['id']
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            customer_code_enterprise_new = rs['customer_code']
            fields_data = customer_single_payload.view(
                id=id_enterprise_new
            )
            rs = helper.SQL_VIEW_CTM(fields_data)
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'hocifcd' in rs, f'Key \"hocifcd\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_private' in rs, f'Key \"customer_private\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title' in rs, f'Key \"title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title_of_organization' in rs, f'Key \"title_of_organization\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'suffix' in rs, f'Key \"suffix\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname' in rs, f'Key \"firstname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname' in rs, f'Key \"lastname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname' in rs, f'Key \"midname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fullname' in rs, f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname_local' in rs, f'Key \"firstname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname_local' in rs, f'Key \"lastname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname_local' in rs, f'Key \"midname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'shortname' in rs, f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gender' in rs, f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'date_of_birth' in rs, f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'place_of_birth' in rs, f'Key \"place_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'nation' in rs, f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country' in rs, f'Key \"country\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs, f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs, f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_paper' in rs, f'Key \"issue_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_paper' in rs, f'Key \"issue_place_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expire_date_of_paper' in rs, f'Key \"expire_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type_sub' in rs, f'Key \"paper_type_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number_sub' in rs, f'Key \"paper_number_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_sub_paper' in rs, f'Key \"issue_date_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_sub_paper' in rs, f'Key \"issue_place_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_group_type' in rs, f'Key \"customer_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_sub_group_type' in rs, f'Key \"customer_sub_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'categories' in rs, f'Key \"categories\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sector' in rs, f'Key \"sector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'subsector' in rs, f'Key \"subsector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'resident' in rs, f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['legal_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['legal_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'contact_local_address' in rs, f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['contact_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['contact_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['contact_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['contact_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['contact_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['contact_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['contact_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_home' in rs, f'Key \"phone_home\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_mobile' in rs, f'Key \"phone_mobile\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'email' in rs, f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'education' in rs, f'Key \"education\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'marital_status' in rs, f'Key \"marital_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'profession' in rs, f'Key \"profession\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'business_type' in rs, f'Key \"business_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'financial' in rs, f'Key \"financial\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'isic_code' in rs, f'Key \"isic_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'managing_branch_code' in rs, f'Key \"managing_branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_status' in rs, f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'classify' in rs, f'Key \"classify\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'polists' in rs, f'Key \"polists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'repolists' in rs, f'Key \"repolists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country_of_income' in rs, f'Key \"country_of_income\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fatca_status' in rs, f'Key \"fatca_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'government_id' in rs, f'Key \"government_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'international_id' in rs, f'Key \"international_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'oversea_juristic_id' in rs, f'Key \"oversea_juristic_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gfmis_code' in rs, f'Key \"gfmis_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'opendate' in rs, f'Key \"opendate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_date' in rs, f'Key \"approve_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'last_update_date' in rs, f'Key \"last_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branchid' in rs, f'Key \"branchid\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'staff_id' in rs, f'Key \"staff_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user_id' in rs, f'Key \"approve_user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_credit_line' in rs, f'Key \"customer_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_type' in rs, f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'primary_cif' in rs, f'Key \"primary_cif\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_amount_status' in rs, f'Key \"mdm_amount_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_request_status' in rs, f'Key \"mdm_request_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_code' in rs, f'Key \"mdm_list_sub_type_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_desc' in rs, f'Key \"mdm_list_sub_type_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_matching_by' in rs, f'Key \"mdm_matching_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_final_kyc_status' in rs, f'Key \"mdm_final_kyc_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_code' in rs, f'Key \"mdm_kyc_comment_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_desc' in rs, f'Key \"mdm_kyc_comment_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_level' in rs, f'Key \"kyc_level\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_update_date' in rs, f'Key \"kyc_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_override' in rs, f'Key \"kyc_override\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_override_descr' in rs, f'Key \"kyc_override_descr\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_code' in rs, f'Key \"user_created_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_name' in rs, f'Key \"user_created_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_code' in rs, f'Key \"user_approved_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_name' in rs, f'Key \"user_approved_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_enterprise_new == rs['id'], f'Expected \'{id_enterprise_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_code_enterprise_new == rs['customer_code'], f'Expected \'{customer_code_enterprise_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert hocifcd == rs['hocifcd'], f'Expected \'{hocifcd}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_private_enterprise == rs['customer_private'], f'Expected \'{customer_private_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title == rs['title'], f'Expected \'{title}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title_of_organization == rs['title_of_organization'], f'Expected \'{title_of_organization}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert suffix == rs['suffix'], f'Expected \'{suffix}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname == rs['firstname'], f'Expected \'{firstname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname == rs['lastname'], f'Expected \'{lastname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname == rs['midname'], f'Expected \'{midname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fullname_enterprise == rs['fullname'], f'Expected \'{fullname_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname_local == rs['firstname_local'], f'Expected \'{firstname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname_local == rs['lastname_local'], f'Expected \'{lastname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname_local == rs['midname_local'], f'Expected \'{midname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert shortname == rs['shortname'], f'Expected \'{shortname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gender == rs['gender'], f'Expected \'{gender}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_of_birth == rs['date_of_birth'], f'Expected \'{date_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert place_of_birth == rs['place_of_birth'], f'Expected \'{place_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert nation == rs['nation'], f'Expected \'{nation}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type == rs['paper_type'], f'Expected \'{paper_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_enterprise == rs['paper_number'], f'Expected \'{paper_number_enterprise}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_paper == rs['issue_date_of_paper'], f'Expected \'{issue_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_paper == rs['issue_place_of_paper'], f'Expected \'{issue_place_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date_of_paper == rs['expire_date_of_paper'], f'Expected \'{expire_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_sub == rs['paper_type_sub'], f'Expected \'{paper_type_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_sub == rs['paper_number_sub'], f'Expected \'{paper_number_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_sub_paper == rs['issue_date_of_sub_paper'], f'Expected \'{issue_date_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_sub_paper == rs['issue_place_of_sub_paper'], f'Expected \'{issue_place_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_group_type == rs['customer_group_type'], f'Expected \'{customer_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_sub_group_type == rs['customer_sub_group_type'], f'Expected \'{customer_sub_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subsector == rs['subsector'], f'Expected \'{subsector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident == rs['resident'], f'Expected \'{resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_legal == rs['legal_local_address']['address_local'], f'Expected \'{address_local_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_legal == rs['legal_local_address']['province'], f'Expected \'{province_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal == rs['legal_local_address']['village'], f'Expected \'{village_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal == rs['legal_local_address']['district'], f'Expected \'{district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal == rs['legal_local_address']['address'], f'Expected \'{address_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_legal == rs['legal_local_address']['zipcode'], f'Expected \'{zipcode_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_contact == rs['contact_local_address']['address_local'], f'Expected \'{address_local_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_contact == rs['contact_local_address']['province'], f'Expected \'{province_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_contact == rs['contact_local_address']['village'], f'Expected \'{village_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_contact == rs['contact_local_address']['sub_district'], f'Expected \'{sub_district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_contact == rs['contact_local_address']['district'], f'Expected \'{district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_contact == rs['contact_local_address']['address'], f'Expected \'{address_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_contact == rs['contact_local_address']['zipcode'], f'Expected \'{zipcode_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_home == rs['phone_home'], f'Expected \'{phone_home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_mobile == rs['phone_mobile'], f'Expected \'{phone_mobile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert email == rs['email'], f'Expected \'{email}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert education == rs['education'], f'Expected \'{education}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert marital_status == rs['marital_status'], f'Expected \'{marital_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert profession == rs['profession'], f'Expected \'{profession}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert business_type == rs['business_type'], f'Expected \'{business_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert financial == rs['financial'], f'Expected \'{financial}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert isic_code == rs['isic_code'], f'Expected \'{isic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert managing_branch_code == rs['managing_branch_code'], f'Expected \'{managing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_status == rs['customer_status'], f'Expected \'{customer_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classify == rs['classify'], f'Expected \'{classify}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert polists == rs['polists'], f'Expected \'{polists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert repolists == rs['repolists'], f'Expected \'{repolists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_of_income == rs['country_of_income'], f'Expected \'{country_of_income}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fatca_status == rs['fatca_status'], f'Expected \'{fatca_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert government_id == rs['government_id'], f'Expected \'{government_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert international_id == rs['international_id'], f'Expected \'{international_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert oversea_juristic_id == rs['oversea_juristic_id'], f'Expected \'{oversea_juristic_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gfmis_code == rs['gfmis_code'], f'Expected \'{gfmis_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branchid == rs['branchid'], f'Expected \'{branchid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_credit_line == rs['customer_credit_line'], f'Expected \'{customer_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert primary_cif == rs['primary_cif'], f'Expected \'{primary_cif}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_amount_status == rs['mdm_amount_status'], f'Expected \'{mdm_amount_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_request_status == rs['mdm_request_status'], f'Expected \'{mdm_request_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_code == rs['mdm_list_sub_type_code'], f'Expected \'{mdm_list_sub_type_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_desc == rs['mdm_list_sub_type_desc'], f'Expected \'{mdm_list_sub_type_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_matching_by == rs['mdm_matching_by'], f'Expected \'{mdm_matching_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_final_kyc_status == rs['mdm_final_kyc_status'], f'Expected \'{mdm_final_kyc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_code == rs['mdm_kyc_comment_code'], f'Expected \'{mdm_kyc_comment_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_desc == rs['mdm_kyc_comment_desc'], f'Expected \'{mdm_kyc_comment_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert kyc_level == rs['kyc_level'], f'Expected \'{kyc_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert kyc_update_date == rs['kyc_update_date'], f'Expected \'{kyc_update_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # chek get list relation customer information
            fields_data = customer_single_payload.get_list_relation_customer(
                group_code=customer_code_enterprise_new
            )
            rs = helper.SQL_RELATION_CTMGRP(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 2 == rs['total_count'], f'Expected total_count: \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'customer_code' in rs['items'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['items'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_type' in rs['items'][0], f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'date_of_birth' in rs['items'][0], f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'paper_type' in rs['items'][0], f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'paper_number' in rs['items'][0], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 2 == len(rs['items']), f'Expected len items = \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after view
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = customer_single_payload.delete(
                id=id_enterprise_new
            )
            rs = helper.SQL_DELETE_CTM(fields_data)
            # check total_count search all after delete
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data test
            fields_data = customer_group_payload.advanced_search(
                page_size=5,
                group_code=customer_code_enterprise_new
            )
            rs = helper_group.SQL_ADSEARCH_CTMGRP(fields_data)
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            search_rs = False
            total_item = len(rs['items'])
            if total_item > 0:
                for i in range(total_item):
                    if customer_code_enterprise_new in rs['items'][i]['group_code']:
                        id_group_new = rs['items'][i]['id']
                        search_rs = True
                        break
                assert search_rs, f'Search customer relation management fail. Expected: {customer_code_enterprise_new}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            else:
                assert total_item != 0, f'Search customer relation management fail. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
             # Delete data test
            fields_data = customer_group_payload.delete(
                id=id_group_new
            )
            rs = helper_group.SQL_DELETE_CTMGRP(fields_data)
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert id_group_new == rs['id'], f'Expected \'{id_group_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.view_customer_single_individual
    def test_010_view_customer_single_individual(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.add(
            hocifcd=hocifcd,
            customer_private=customer_private_individual,
            title=title,
            title_of_organization=title_of_organization,
            suffix=suffix,
            firstname=firstname,
            lastname=lastname,
            midname=midname,
            fullname=fullname_individual,
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
            paper_number=paper_number_individual,
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
        rs = helper.SQL_INSERT_CTM(fields_data)
        try:
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            id_individual_new = rs['id']
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            customer_code_individual_new = rs['customer_code']
            fields_data = customer_single_payload.view(
                id=id_individual_new
            )
            rs = helper.SQL_VIEW_CTM(fields_data)
            # check key
            assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'hocifcd' in rs, f'Key \"hocifcd\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_private' in rs, f'Key \"customer_private\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title' in rs, f'Key \"title\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'title_of_organization' in rs, f'Key \"title_of_organization\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'suffix' in rs, f'Key \"suffix\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname' in rs, f'Key \"firstname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname' in rs, f'Key \"lastname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname' in rs, f'Key \"midname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fullname' in rs, f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'firstname_local' in rs, f'Key \"firstname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'lastname_local' in rs, f'Key \"lastname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'midname_local' in rs, f'Key \"midname_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'shortname' in rs, f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gender' in rs, f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'date_of_birth' in rs, f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'place_of_birth' in rs, f'Key \"place_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'nation' in rs, f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country' in rs, f'Key \"country\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type' in rs, f'Key \"paper_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number' in rs, f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_paper' in rs, f'Key \"issue_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_paper' in rs, f'Key \"issue_place_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'expire_date_of_paper' in rs, f'Key \"expire_date_of_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_type_sub' in rs, f'Key \"paper_type_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'paper_number_sub' in rs, f'Key \"paper_number_sub\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_date_of_sub_paper' in rs, f'Key \"issue_date_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'issue_place_of_sub_paper' in rs, f'Key \"issue_place_of_sub_paper\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_group_type' in rs, f'Key \"customer_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_sub_group_type' in rs, f'Key \"customer_sub_group_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'categories' in rs, f'Key \"categories\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sector' in rs, f'Key \"sector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'subsector' in rs, f'Key \"subsector\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'resident' in rs, f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'legal_local_address' in rs, f'Key \"legal_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['legal_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['legal_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['legal_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['legal_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['legal_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['legal_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['legal_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'contact_local_address' in rs, f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address_local' in rs['contact_local_address'], f'Key \"address_local\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'province' in rs['contact_local_address'], f'Key \"province\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'village' in rs['contact_local_address'], f'Key \"village\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'sub_district' in rs['contact_local_address'], f'Key \"sub_district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'district' in rs['contact_local_address'], f'Key \"district\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'address' in rs['contact_local_address'], f'Key \"address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'zipcode' in rs['contact_local_address'], f'Key \"zipcode\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_home' in rs, f'Key \"phone_home\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'phone_mobile' in rs, f'Key \"phone_mobile\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'email' in rs, f'Key \"email\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'education' in rs, f'Key \"education\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'marital_status' in rs, f'Key \"marital_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'profession' in rs, f'Key \"profession\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'business_type' in rs, f'Key \"business_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'financial' in rs, f'Key \"financial\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'isic_code' in rs, f'Key \"isic_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'managing_branch_code' in rs, f'Key \"managing_branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_status' in rs, f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'classify' in rs, f'Key \"classify\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'polists' in rs, f'Key \"polists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'repolists' in rs, f'Key \"repolists\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'country_of_income' in rs, f'Key \"country_of_income\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'fatca_status' in rs, f'Key \"fatca_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'government_id' in rs, f'Key \"government_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'international_id' in rs, f'Key \"international_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'oversea_juristic_id' in rs, f'Key \"oversea_juristic_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'gfmis_code' in rs, f'Key \"gfmis_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'opendate' in rs, f'Key \"opendate\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_date' in rs, f'Key \"approve_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'last_update_date' in rs, f'Key \"last_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branchid' in rs, f'Key \"branchid\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'staff_id' in rs, f'Key \"staff_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'approve_user_id' in rs, f'Key \"approve_user_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'group_id' in rs, f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_credit_line' in rs, f'Key \"customer_credit_line\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'currency_code' in rs, f'Key \"currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'customer_type' in rs, f'Key \"customer_type\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'primary_cif' in rs, f'Key \"primary_cif\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_amount_status' in rs, f'Key \"mdm_amount_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_request_status' in rs, f'Key \"mdm_request_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_code' in rs, f'Key \"mdm_list_sub_type_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_list_sub_type_desc' in rs, f'Key \"mdm_list_sub_type_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_matching_by' in rs, f'Key \"mdm_matching_by\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_final_kyc_status' in rs, f'Key \"mdm_final_kyc_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_code' in rs, f'Key \"mdm_kyc_comment_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'mdm_kyc_comment_desc' in rs, f'Key \"mdm_kyc_comment_desc\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_level' in rs, f'Key \"kyc_level\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_update_date' in rs, f'Key \"kyc_update_date\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_override' in rs, f'Key \"kyc_override\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'kyc_override_descr' in rs, f'Key \"kyc_override_descr\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'branch_code' in rs, f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_code' in rs, f'Key \"user_created_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_created_name' in rs, f'Key \"user_created_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_code' in rs, f'Key \"user_approved_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'user_approved_name' in rs, f'Key \"user_approved_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check value
            assert id_individual_new == rs['id'], f'Expected \'{id_individual_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_code_individual_new == rs['customer_code'], f'Expected \'{customer_code_individual_new}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert hocifcd == rs['hocifcd'], f'Expected \'{hocifcd}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_private_individual == rs['customer_private'], f'Expected \'{customer_private_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title == rs['title'], f'Expected \'{title}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert title_of_organization == rs['title_of_organization'], f'Expected \'{title_of_organization}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert suffix == rs['suffix'], f'Expected \'{suffix}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname == rs['firstname'], f'Expected \'{firstname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname == rs['lastname'], f'Expected \'{lastname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname == rs['midname'], f'Expected \'{midname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fullname_individual == rs['fullname'], f'Expected \'{fullname_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert firstname_local == rs['firstname_local'], f'Expected \'{firstname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert lastname_local == rs['lastname_local'], f'Expected \'{lastname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert midname_local == rs['midname_local'], f'Expected \'{midname_local}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert shortname == rs['shortname'], f'Expected \'{shortname}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gender == rs['gender'], f'Expected \'{gender}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert date_of_birth == rs['date_of_birth'], f'Expected \'{date_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert place_of_birth == rs['place_of_birth'], f'Expected \'{place_of_birth}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert nation == rs['nation'], f'Expected \'{nation}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country == rs['country'], f'Expected \'{country}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type == rs['paper_type'], f'Expected \'{paper_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_individual == rs['paper_number'], f'Expected \'{paper_number_individual}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_paper == rs['issue_date_of_paper'], f'Expected \'{issue_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_paper == rs['issue_place_of_paper'], f'Expected \'{issue_place_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert expire_date_of_paper == rs['expire_date_of_paper'], f'Expected \'{expire_date_of_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_type_sub == rs['paper_type_sub'], f'Expected \'{paper_type_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert paper_number_sub == rs['paper_number_sub'], f'Expected \'{paper_number_sub}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_date_of_sub_paper == rs['issue_date_of_sub_paper'], f'Expected \'{issue_date_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert issue_place_of_sub_paper == rs['issue_place_of_sub_paper'], f'Expected \'{issue_place_of_sub_paper}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_group_type == rs['customer_group_type'], f'Expected \'{customer_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_sub_group_type == rs['customer_sub_group_type'], f'Expected \'{customer_sub_group_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert categories == rs['categories'], f'Expected \'{categories}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sector == rs['sector'], f'Expected \'{sector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert subsector == rs['subsector'], f'Expected \'{subsector}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert resident == rs['resident'], f'Expected \'{resident}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_legal == rs['legal_local_address']['address_local'], f'Expected \'{address_local_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_legal == rs['legal_local_address']['province'], f'Expected \'{province_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_legal == rs['legal_local_address']['village'], f'Expected \'{village_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_legal == rs['legal_local_address']['sub_district'], f'Expected \'{sub_district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_legal == rs['legal_local_address']['district'], f'Expected \'{district_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_legal == rs['legal_local_address']['address'], f'Expected \'{address_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_legal == rs['legal_local_address']['zipcode'], f'Expected \'{zipcode_legal}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_local_contact == rs['contact_local_address']['address_local'], f'Expected \'{address_local_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert province_contact == rs['contact_local_address']['province'], f'Expected \'{province_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert village_contact == rs['contact_local_address']['village'], f'Expected \'{village_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert sub_district_contact == rs['contact_local_address']['sub_district'], f'Expected \'{sub_district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert district_contact == rs['contact_local_address']['district'], f'Expected \'{district_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert address_contact == rs['contact_local_address']['address'], f'Expected \'{address_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert zipcode_contact == rs['contact_local_address']['zipcode'], f'Expected \'{zipcode_contact}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_home == rs['phone_home'], f'Expected \'{phone_home}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert phone_mobile == rs['phone_mobile'], f'Expected \'{phone_mobile}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert email == rs['email'], f'Expected \'{email}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert education == rs['education'], f'Expected \'{education}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert marital_status == rs['marital_status'], f'Expected \'{marital_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert profession == rs['profession'], f'Expected \'{profession}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert business_type == rs['business_type'], f'Expected \'{business_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert financial == rs['financial'], f'Expected \'{financial}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert isic_code == rs['isic_code'], f'Expected \'{isic_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert managing_branch_code == rs['managing_branch_code'], f'Expected \'{managing_branch_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_status == rs['customer_status'], f'Expected \'{customer_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert classify == rs['classify'], f'Expected \'{classify}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert polists == rs['polists'], f'Expected \'{polists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert repolists == rs['repolists'], f'Expected \'{repolists}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert country_of_income == rs['country_of_income'], f'Expected \'{country_of_income}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert fatca_status == rs['fatca_status'], f'Expected \'{fatca_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert government_id == rs['government_id'], f'Expected \'{government_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert international_id == rs['international_id'], f'Expected \'{international_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert oversea_juristic_id == rs['oversea_juristic_id'], f'Expected \'{oversea_juristic_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert gfmis_code == rs['gfmis_code'], f'Expected \'gfmis_code\' = \'{gfmis_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert branchid == rs['branchid'], f'Expected \'{branchid}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert group_id == rs['group_id'], f'Expected \'{group_id}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_credit_line == rs['customer_credit_line'], f'Expected \'{customer_credit_line}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert currency_code == rs['currency_code'], f'Expected \'{currency_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert customer_type == rs['customer_type'], f'Expected \'{customer_type}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert primary_cif == rs['primary_cif'], f'Expected \'{primary_cif}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_amount_status == rs['mdm_amount_status'], f'Expected \'{mdm_amount_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_request_status == rs['mdm_request_status'], f'Expected \'{mdm_request_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_code == rs['mdm_list_sub_type_code'], f'Expected \'{mdm_list_sub_type_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_list_sub_type_desc == rs['mdm_list_sub_type_desc'], f'Expected \'{mdm_list_sub_type_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_matching_by == rs['mdm_matching_by'], f'Expected \'{mdm_matching_by}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_final_kyc_status == rs['mdm_final_kyc_status'], f'Expected \'{mdm_final_kyc_status}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_code == rs['mdm_kyc_comment_code'], f'Expected \'{mdm_kyc_comment_code}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert mdm_kyc_comment_desc == rs['mdm_kyc_comment_desc'], f'Expected \'{mdm_kyc_comment_desc}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert kyc_level == rs['kyc_level'], f'Expected \'{kyc_level}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert kyc_update_date == rs['kyc_update_date'], f'Expected \'{kyc_update_date}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            check_data_type(rs)
            # chek get list relation customer information
            fields_data = customer_single_payload.get_list_relation_customer(
                group_code=customer_code_individual_new
            )
            rs = helper.SQL_RELATION_CTMGRP(fields_data)
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == rs['total_count'], f'Expected total_count: \'{0}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 0 == len(rs['items']), f'Expected 0 items, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # check total_count search all after view
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count + 1) == rs['total_count'], f'Check total_count after view fail. Expected \'{total_count + 1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # delete data
            fields_data = customer_single_payload.delete(
                id=id_individual_new
            )
            rs = helper.SQL_DELETE_CTM(fields_data)
            # check total_count search all after delete
            fields_data = customer_single_payload.simple_search(
                page_size=50
            )
            rs = helper.SQL_SEARCH_CTM(fields_data)
            assert 'total_count' in rs, f'Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert (total_count) == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.simple_search_customer_single_check_page
    def test_011_simple_search_customer_single_check_page(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.simple_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_SEARCH_CTM(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.advanced_search_customer_single_check_page
    def test_012_advanced_search_customer_single_check_page(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.advanced_search(
            page_size=2,
            page_index=1
        )
        rs = helper.SQL_ADSEARCH_CTM(fields_data)
        try:
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert len(rs['items']) <= 2, f'Expected len(\'items\') <= \'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_size'] == 2, f'Expected page_size=\'{2}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert rs['page_index'] == 1, f'Expected page_index=\'{1}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


    @pytest.mark.lookup_customer_single
    def test_013_lookup_customer_single(self, user):
        helper = CustomerSingleHelper(user)
        fields_data = customer_single_payload.lookup_customer_single(
        )
        rs = helper.SQL_LOOKUP_CTM(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # assert total_count == rs['total_count'], f'Expected \'{total_count}\', Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_code' in rs['items'][0], f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'fullname' in rs['items'][0], f'Key \"fullname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'shortname' in rs['items'][0], f'Key \"shortname\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'paper_number' in rs['items'][0], f'Key \"paper_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'date_of_birth' in rs['items'][0], f'Key \"date_of_birth\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'gender' in rs['items'][0], f'Key \"gender\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'customer_status' in rs['items'][0], f'Key \"customer_status\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'nation' in rs['items'][0], f'Key \"nation\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'resident' in rs['items'][0], f'Key \"resident\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'old_id_of_customer' in rs['items'][0], f'Key \"old_id_of_customer\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'group_id' in rs['items'][0], f'Key \"group_id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'contact_local_address' in rs['items'][0], f'Key \"contact_local_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                for i in range(len(rs['items'])): 
                    check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


def check_data_type(rs):
    set_incorrect_data_type = set()
    for key, value in rs.items():
        if key in number_checklist:
            if not(isinstance(value, number_checklist[key]['data_type'])):
                set_incorrect_data_type.add(key)
    assert len(set_incorrect_data_type) == 0, f'Data type is incorrect. List fields incorrectly: {set_incorrect_data_type}, Actual response Json: {json.dumps(rs, indent=4, sort_keys=True)}'