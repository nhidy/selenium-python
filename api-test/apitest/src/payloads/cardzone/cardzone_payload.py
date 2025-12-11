from datetime import datetime

class CardzonePayload(object):
# ====================================== Workflow id deposit ======================================
    def DPT_MDP_ATM_DPT_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MDP_ATM_IBFT2_BNB_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MDP_POS_VOID_ONUS_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '4789'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MDP_POS_VOID_OFF_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '7993'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MDP_MINI_WDR_OFF_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MDP_MINI_CLS_WDR_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_ECOM_VOID_ONUS_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '7523'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

# ====================================== Workflow id withdrawal ======================================
    def DPT_MWR_ATM_WDR_ONUS_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_ATM_WDR_OFF_ISS_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_ATM_IBFT2_ISS_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_ATM_TOPUP_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = {"cati": "10010003"}
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_POS_SALE_ONUS_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '8299'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_POS_SALE_OFF_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '5814'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_POS_CAV_ONUS_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '9311'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_ECOM_SALE_ONUS_CZ(self, mcc_code=None, account_number=None, amount=None, cardzone_message=None):
        if not mcc_code:
            mcc_code = '9311'
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "mcc_code": mcc_code,
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_MWR_MINI_CLS_RES_CZ(self, account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

# ====================================== Workflow id transfer ======================================
    def DPT_TRF_MINI_WDR_ONUS_CZ(self, account_number=None, credit_account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "credit_account_number": credit_account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_TRF_ATM_IBFT_ONUS_CZ(self, account_number=None, credit_account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = {"cati": "002001"}
        payload = {
            "account_number": account_number,
            "credit_account_number": credit_account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_TRF_ATM_IBFT1_CZ(self, account_number=None, credit_account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "credit_account_number": credit_account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload

    def DPT_TRF_MINI_DPT_CZ(self, account_number=None, credit_account_number=None, amount=None, cardzone_message=None):
        if not account_number:
            account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not amount:
            amount = 0
        if not cardzone_message:
            cardzone_message = ''
        payload = {
            "account_number": account_number,
            "credit_account_number": credit_account_number,
            "amount": amount,
            "cardzone_message": cardzone_message
        }
        return payload