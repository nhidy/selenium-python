from datetime import datetime
import json
import random
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
from apitest.src.helpers.customer.customer_fo_helpers import CustomerFOHelper
from apitest.src.payloads.customer.customer_fo_payload import CustomerFOPayload

customer_single_payload = CustomerSinglePayload()
customer_fo_payload = CustomerFOPayload()

random_num = random.randrange(100, 1000)
working_date="2022-12-10" 
hocifcd=""
customer_private_enterprise="E"
customer_private_individual="I"
title="01"
title_of_organization=""
suffix=""
firstname="FIRST"
lastname="LAST"
midname=""
fullname_enterprise="TEST AUTO Enterprise "
fullname_individual="TEST AUTO Individual "
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
description="Approve customer"

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
class TestAddCustomerSingle(object):

    @pytest.mark.add_and_approve_customer_single
    def test_001_add_and_approve_customer_single(self, user):
        i = 1
        while i < 20000:
            helper_bo = CustomerSingleHelper(user)
            helper_fo = CustomerFOHelper(user)
            # add enterprise customer
            global id_enterprise_new, customer_code_enterprise_new, id_individual_new, customer_code_individual_new
            id_enterprise_new = 0
            customer_code_enterprise_new = ''
            id_individual_new = 0
            customer_code_individual_new = ''
            fields_data_enterprise = customer_single_payload.add(
                hocifcd=hocifcd,
                customer_private=customer_private_enterprise,
                title=title,
                title_of_organization=title_of_organization,
                suffix=suffix,
                firstname=firstname,
                lastname=lastname,
                midname=midname,
                fullname=fullname_enterprise + str(i),
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
                paper_number=paper_number_enterprise + str(i),
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
            rs = helper_bo.SQL_INSERT_CTM(fields_data_enterprise)
            try:
                assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                id_enterprise_new = rs['id']
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                customer_code_enterprise_new = rs['customer_code']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # approve enterprise customer
            fields_data_approve_enterprise = customer_fo_payload.ctm_apr(
                customer_code=customer_code_enterprise_new,
                customer_name=fullname_enterprise + str(i),
                customer_status=customer_status,
                description=description
            )
            try:
                rs = helper_fo.CTM_APR(fields_data_approve_enterprise)
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # add individual customer
            fields_data_individual = customer_single_payload.add(
                hocifcd=hocifcd,
                customer_private=customer_private_individual,
                title=title,
                title_of_organization=title_of_organization,
                suffix=suffix,
                firstname=firstname,
                lastname=lastname,
                midname=midname,
                fullname=fullname_individual + str(i),
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
                paper_number=paper_number_individual + str(i + 1),
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
            rs = helper_bo.SQL_INSERT_CTM(fields_data_individual)
            try:
                assert 'id' in rs, f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                id_individual_new = rs['id']
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                customer_code_individual_new = rs['customer_code']
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # approve individual customer
            fields_data_approve_individual = customer_fo_payload.ctm_apr(
                customer_code=customer_code_individual_new,
                customer_name=fullname_individual + str(i),
                customer_status=customer_status,
                description=description
            )
            try:
                rs = helper_fo.CTM_APR(fields_data_approve_individual)
                assert 'customer_code' in rs, f'Key \"customer_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            i += 1