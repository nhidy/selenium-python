import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
value_date='2023-09-11T00:00:00Z'
total_amount=31000.43
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_ACT_MAN
class Test_SP_ACT_MAN(object):

    def test_sp_act_man_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        posting_data = [
            {
                "account_name": "GL test paygate of digital",
                "currency": "MMK",
                "posting_side": "D",
                "gl_account_number": "003101010666666601",
                "credit_amount": 0.0,
                "debit_amount": 1000.43,
                "cost_center": "",
                "product_code": "",
                "inter_company": ""
            },
            {
                "account_name": "GL test income of digital",
                "currency": "MMK",
                "posting_side": "C",
                "gl_account_number": "003101010555555501",
                "credit_amount": 1000.43,
                "debit_amount": 0.0,
                "cost_center": "",
                "product_code": "",
                "inter_company": ""
            },
            {
                "account_name": "Fixed Assets A/C - Other Fixed Assets (MMK)",
                "currency": "MMK",
                "posting_side": "D",
                "gl_account_number": "003107070100010101",
                "credit_amount": 0.0,
                "debit_amount": 30000.0,
                "cost_center": "",
                "product_code": "",
                "inter_company": ""
            },
            {
                "account_name": "Other Commission & Service Charges (MMK)",
                "currency": "MMK",
                "posting_side": "C",
                "gl_account_number": "003303090100030301",
                "credit_amount": 20000.0,
                "debit_amount": 0.0,
                "cost_center": "",
                "product_code": "",
                "inter_company": ""
            },
            {
                "account_name": "Reserve for Taxation (MMK)",
                "currency": "MMK",
                "posting_side": "C",
                "gl_account_number": "003210030100030301",
                "credit_amount": 10000.0,
                "debit_amount": 0.0,
                "cost_center": "",
                "product_code": "",
                "inter_company": ""
            }
        ]
        fields_data = sp_payload.ACT_MAN(
            posting_data=posting_data,
            value_date=value_date,
            total_amount=total_amount
        )
        rs = sp_helper.ACT_MAN(fields_data)
        step_code = 'ACT_MAN'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"