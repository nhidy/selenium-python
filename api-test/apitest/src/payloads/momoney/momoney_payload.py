from datetime import datetime

class MomoneyPayload(object):
# ====================================== Workflow id deposit ======================================
    def DPT_MDP_MOMONEY(self, debit_account_number=None, credit_account_number=None, amount=None, fee1=None, fee2=None):
        if not debit_account_number:  # GL account
            debit_account_number = ''
        if not credit_account_number: # Deposit account
            credit_account_number = ''
        if not amount:
            amount = 0
        if not fee1:
            fee1 = 0
        if not fee2:
            fee2 = 0
        payload = {
            "transaction_data": {
                "debit_account_number": debit_account_number,
                "credit_account_number": credit_account_number,
                "amount": amount,
                "fee1": fee1,
                "fee2": fee2
            }
        }
        return payload

# ====================================== Workflow id withdrawal ======================================
    def DPT_MWR_MOMONEY(self, debit_account_number=None, credit_account_number=None, amount=None):
        if not debit_account_number: # Deposit account
            debit_account_number = ''
        if not credit_account_number: # GL account
            credit_account_number = ''
        if not amount:
            amount = 0
        payload = {
            "otp_verification": {
                "party_code": "Mo",
                "otp":"929103",
                "party_reference_id":"b53e4367-61b0-47c3-8974-5128c45955d7"
            },
            "transaction_data": {
                "debit_account_number": debit_account_number,
                "credit_account_number": credit_account_number,
                "amount": amount
            }
        }
        return payload

# ====================================== Workflow id transfer ======================================
    def DPT_TRF_MOMONEY(self, debit_account_number=None, credit_account_number=None, customer_name=None, currency_code=None, amount=None):
        if not debit_account_number:
            debit_account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not customer_name:
            customer_name = 'TEST API AUTO'
        if not currency_code:
            currency_code = 'MMK'
        if not amount:
            amount = 0
        payload = {
            "transaction_data": {
                "debit_account_number": debit_account_number,
                "credit_account_number": credit_account_number,
                "customer_name": customer_name,
                "currency_code": currency_code,
                "amount": amount
            }
        }
        return payload

    def DPT_TRF_FEE_MOMONEY(self, debit_account_number=None, credit_account_number=None, customer_name=None, currency_code=None, amount=None, fee1=None, fee2=None):
        if not debit_account_number:
            debit_account_number = ''
        if not credit_account_number:
            credit_account_number = ''
        if not customer_name:
            customer_name = 'TEST API AUTO'
        if not currency_code:
            currency_code = 'MMK'
        if not amount:
            amount = 0
        if not fee1:
            fee1 = 0
        if not fee2:
            fee2 = 0
        payload = {
            "transaction_data": {
                "debit_account_number": debit_account_number,
                "credit_account_number": credit_account_number,
                "customer_name": customer_name,
                "currency_code": currency_code,
                "amount": amount,
                "fee1": fee1,
                "fee2": fee2
            }
        }
        return payload