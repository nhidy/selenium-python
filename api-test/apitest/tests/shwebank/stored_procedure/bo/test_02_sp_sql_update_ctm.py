import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
id=3082
title='02'
firstname='API'
lastname='TEST'
fullname='API TEST'
gender='02'
date_of_birth='1984-11-20T00:00:00Z'
paper_type='N'
paper_number='1/MaKaNa(N)096346'
legal_local_address_line1='27'
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
customer_sub_type='I'
approve_modify=True
father_name='TESTING'
customer_code='11001699'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_SQL_UPDATE_CTM
class Test_SP_SQL_UPDATE_CTM(object):

    def test_sp_sql_update_ctm_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.SQL_UPDATE_CTM(
            id=id,
            title=title,
            firstname=firstname,
            lastname=lastname,
            fullname=fullname,
            gender=gender,
            date_of_birth=date_of_birth,
            paper_type=paper_type,
            paper_number=paper_number,
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
            customer_sub_type=customer_sub_type,
            approve_modify=approve_modify,
            father_name=father_name,
            customer_code=customer_code
        )
        rs = sp_helper.SQL_UPDATE_CTM(fields_data)
        step_code = 'SQL_UPDATE_CTM'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"