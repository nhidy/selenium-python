import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
description='Cash denomination'
remaining_cash_balance=1211520617.74
closing_cash_balance=1211561017.74
denom_cash_balance=40400.0
last_total_amount=0
currency_code='MMK'
total_amount=40400.0
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_CSH_DNM
class Test_SP_CSH_DNM(object):

    def test_sp_csh_dnm_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        cash_denom_list = [
            {
                "face_type": "A",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 1/-",
                "face_value": 1.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "B",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 5/-",
                "face_value": 5.0,
                "sheet": 40.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 200.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "C",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 10/-",
                "face_value": 10.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "D",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 20/-",
                "face_value": 20.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "E",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 50/-",
                "face_value": 50.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "F",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 100/-",
                "face_value": 100.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "G",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 200/-",
                "face_value": 200.0,
                "sheet": 1.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 200.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "H",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 500/-",
                "face_value": 500.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "I",
                "face_type_caption": "Denomination and Pieces CBM(Lion) 1000/-",
                "face_value": 1000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "J",
                "face_type_caption": "Denomination and Pieces CBM(K.L) 200/-",
                "face_value": 200.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "K",
                "face_type_caption": "Denomination and Pieces CBM(K.L) 500/-",
                "face_value": 500.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "L",
                "face_type_caption": "Denomination and Pieces CBM(K.L) 1000/-",
                "face_value": 1000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "M",
                "face_type_caption": "Denomination and Pieces CBM(R.W.E) 5000/-",
                "face_value": 5000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "X",
                "face_type_caption": "Denomination and Pieces CBM(R.W.E) 10000/-",
                "face_value": 10000.0,
                "sheet": 4.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 40000.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "O",
                "face_type_caption": "Denomination and Pieces CBM(R.W.E.N) 5000/-",
                "face_value": 5000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "P",
                "face_type_caption": "Denomination and Pieces CBM(R.W.E.N) 10000/-",
                "face_value": 10000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Q",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 50/-",
                "face_value": 50.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "R",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 100/-",
                "face_value": 100.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "S",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 200/-",
                "face_value": 200.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "T",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 500/-",
                "face_value": 500.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "U",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 1000/-",
                "face_value": 1000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "V",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 5000/-",
                "face_value": 5000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "W",
                "face_type_caption": "Denomination and Pieces CBM(NBD) 10000/-",
                "face_value": 10000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Y",
                "face_type_caption": "Denomination and Pieces CBM 20000/-",
                "face_value": 20000.0,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.01,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.02,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.05,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.1,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.25,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            },
            {
                "face_type": "Z",
                "face_type_caption": "Coin",
                "face_value": 0.5,
                "sheet": 0.0,
                "last_amount": 0.0,
                "amount_in_safe": 0.0,
                "amount": 0.0,
                "last_sheet": 0.0,
                "soli_notes": 0.0
            }
        ]
        fields_data = sp_payload.CSH_DNM(
            description=description,
            remaining_cash_balance=remaining_cash_balance,
            closing_cash_balance=closing_cash_balance,
            denom_cash_balance=denom_cash_balance,
            last_total_amount=last_total_amount,
            currency_code=currency_code,
            total_amount=total_amount,
            cash_denom_list=cash_denom_list
        )
        rs = sp_helper.CSH_DNM(fields_data)
        step_code = 'CSH_DNM'
        data_actual = RequestUtility.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))

        assert '', f"Expected: ..., Actual: response Json:"