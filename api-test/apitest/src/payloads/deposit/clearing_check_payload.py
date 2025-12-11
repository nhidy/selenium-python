from datetime import datetime

class ClearingCheckPayload(object):
    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def simple_search(self, search_text=None, page_size=None, page_index=None):
        if not search_text:
            search_text = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "search_text": search_text,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, id=None, date=None, tran_seference_id=None, account_number_def=None, ddorgl=None, cheque_no=None, clearing_status=None, amount=None, fee_amount=None, vatamt=None, currency_code=None, openflt=None, currflt=None, issue_bank=None, idate=None, cbnk=None, refno=None, drawer_name=None, clearing_date=None, chqdesc=None, clrac=None, txcode=None, fltamt=None, clearing_type=None, ben_currency=None, ben_amount=None):
        if not id:
            id = 0
        if not date:
            date = ''
        if not tran_seference_id:
            tran_seference_id = ''
        if not account_number_def:
            account_number_def = ''
        if not ddorgl:
            ddorgl = ''
        if not cheque_no:
            cheque_no = ''
        if not clearing_status:
            clearing_status = ''
        if not amount:
            amount = 0
        if not fee_amount:
            fee_amount = 0
        if not vatamt:
            vatamt = 0
        if not currency_code:
            currency_code = ''
        if not openflt:
            openflt = 0
        if not currflt:
            currflt = 0
        if not issue_bank:
            issue_bank = ''
        if not idate:
            idate = ''
        if not cbnk:
            cbnk = ''
        if not refno:
            refno = ''
        if not drawer_name:
            drawer_name = ''
        if not clearing_date:
            clearing_date = ''
        if not chqdesc:
            chqdesc = ''
        if not clrac:
            clrac = ''
        if not txcode:
            txcode = ''
        if not fltamt:
            fltamt = 0
        if not clearing_type:
            clearing_type = ''
        if not ben_currency:
            ben_currency = ''
        if not ben_amount:
            ben_amount = 0
        payload = {
            "id": id,
            "date": date,
            "tran_seference_id": tran_seference_id,
            "account_number_def": account_number_def,
            "ddorgl": ddorgl,
            "cheque_no": cheque_no,
            "clearing_status": clearing_status,
            "amount": amount,
            "fee_amount": fee_amount,
            "vatamt": vatamt,
            "currency_code": currency_code,
            "openflt": openflt,
            "currflt": currflt,
            "issue_bank": issue_bank,
            "idate": idate,
            "cbnk": cbnk,
            "refno": refno,
            "drawer_name": drawer_name,
            "clearing_date": clearing_date,
            "chqdesc": chqdesc,
            "clrac": clrac,
            "txcode": txcode,
            "fltamt": fltamt,
            "clearing_type": clearing_type,
            "ben_currency": ben_currency,
            "ben_amount": ben_amount
        }
        return payload

    def update(self, id=None, date=None, tran_seference_id=None, account_number_def=None, ddorgl=None, cheque_no=None, clearing_status=None, amount=None, fee_amount=None, vatamt=None, currency_code=None, openflt=None, currflt=None, issue_bank=None, idate=None, cbnk=None, refno=None, drawer_name=None, clearing_date=None, chqdesc=None, clrac=None, txcode=None, fltamt=None, clearing_type=None, ben_currency=None, ben_amount=None):
        if not id:
            id = 0
        if not date:
            date = ''
        if not tran_seference_id:
            tran_seference_id = ''
        if not account_number_def:
            account_number_def = ''
        if not ddorgl:
            ddorgl = ''
        if not cheque_no:
            cheque_no = ''
        if not clearing_status:
            clearing_status = ''
        if not amount:
            amount = 0
        if not fee_amount:
            fee_amount = 0
        if not vatamt:
            vatamt = 0
        if not currency_code:
            currency_code = ''
        if not openflt:
            openflt = 0
        if not currflt:
            currflt = 0
        if not issue_bank:
            issue_bank = ''
        if not idate:
            idate = ''
        if not cbnk:
            cbnk = ''
        if not refno:
            refno = ''
        if not drawer_name:
            drawer_name = ''
        if not clearing_date:
            clearing_date = ''
        if not chqdesc:
            chqdesc = ''
        if not clrac:
            clrac = ''
        if not txcode:
            txcode = ''
        if not fltamt:
            fltamt = 0
        if not clearing_type:
            clearing_type = ''
        if not ben_currency:
            ben_currency = ''
        if not ben_amount:
            ben_amount = 0
        payload = {
            "id": id,
            "date": date,
            "tran_seference_id": tran_seference_id,
            "account_number_def": account_number_def,
            "ddorgl": ddorgl,
            "cheque_no": cheque_no,
            "clearing_status": clearing_status,
            "amount": amount,
            "fee_amount": fee_amount,
            "vatamt": vatamt,
            "currency_code": currency_code,
            "openflt": openflt,
            "currflt": currflt,
            "issue_bank": issue_bank,
            "idate": idate,
            "cbnk": cbnk,
            "refno": refno,
            "drawer_name": drawer_name,
            "clearing_date": clearing_date,
            "chqdesc": chqdesc,
            "clrac": clrac,
            "txcode": txcode,
            "fltamt": fltamt,
            "clearing_type": clearing_type,
            "ben_currency": ben_currency,
            "ben_amount": ben_amount
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload