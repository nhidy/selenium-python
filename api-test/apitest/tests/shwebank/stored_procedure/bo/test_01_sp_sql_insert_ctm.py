import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
customer_private='I'
title='02'
firstname='API'
lastname='TEST'
fullname='API TEST'
gender='02'
date_of_birth='1984-11-20T00:00:00Z'
nation='MM'
paper_type='N'
paper_number='1/MaKaNa(N)096346'
categories='C1'
legal_local_address_line1='23'
legal_local_address_line2='Nguyen Huu Tho'
legal_local_address_line3='7'
legal_local_address_line4='Tan Hung'
contact_local_address_line1='24'
contact_local_address_line2='Nguyen Huu Tho'
contact_local_address_line3='7'
contact_local_address_line4='Tan Hung'
introducer_1_name='Name 1'
introducer_1_account_no='098764454'
introducer_2_name='Name 2'
introducer_2_account_no='098768943'
phone_mobile='0987445235'
profession='01'
business_type='01'
managing_branch_code='003'
customer_status='P'
branch_code='003'
staff_code='nhidoan'
customer_sub_type='I'
father_name='TESTING'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_SQL_INSERT_CTM
class Test_SP_SQL_INSERT_CTM(object):

    def test_sp_sql_insert_ctm_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.SQL_INSERT_CTM(
            customer_private=customer_private,
            title=title,
            firstname=firstname,
            lastname=lastname,
            fullname=fullname,
            gender=gender,
            date_of_birth=date_of_birth,
            nation=nation,
            paper_type=paper_type,
            paper_number=paper_number,
            categories=categories,
            legal_local_address_line1=legal_local_address_line1,
            legal_local_address_line2=legal_local_address_line2,
            legal_local_address_line3=legal_local_address_line3,
            legal_local_address_line4=legal_local_address_line4,
            contact_local_address_line1=contact_local_address_line1,
            contact_local_address_line2=contact_local_address_line2,
            contact_local_address_line3=contact_local_address_line3,
            contact_local_address_line4=contact_local_address_line4,
            introducer_1_name=introducer_1_name,
            introducer_1_account_no=introducer_1_account_no,
            introducer_2_name=introducer_2_name,
            introducer_2_account_no=introducer_2_account_no,
            phone_mobile=phone_mobile,
            profession=profession,
            business_type=business_type,
            managing_branch_code=managing_branch_code,
            customer_status=customer_status,
            branch_code=branch_code,
            staff_code=staff_code,
            customer_sub_type=customer_sub_type,
            father_name=father_name
        )
        rs = sp_helper.SQL_INSERT_CTM(fields_data)
        step_code_01 = 'SQL_INSERT_CTM'
        data_actual_01 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_01)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))

        step_code_02 = 'CTM_INSERT_EXT_FIELD'
        data_actual_02 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_02)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"