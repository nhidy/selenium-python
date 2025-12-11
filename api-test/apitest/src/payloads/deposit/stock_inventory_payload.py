from datetime import datetime

class StockInventoryPayload(object):
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

    def advanced_search(self, stkno=None, stkprf=None, stkfrn=None, stkton=None, bkstatus=None, cfmsts=None, brname=None, usrname=None, slsts=None, pslsts=None, stktypect=None, stktype=None, refac=None, stkfr=None, stkto=None, page_index=None, page_size=None):
        if not stkno:
            stkno = ''
        if not stkprf:
            stkprf = ''
        if not stkfrn:
            stkfrn = None
        if not stkton:
            stkton = None
        if not bkstatus:
            bkstatus = ''
        if not cfmsts:
            cfmsts = ''
        if not brname:
            brname = ''
        if not usrname:
            usrname = ''
        if not slsts:
            slsts = ''
        if not pslsts:
            pslsts = ''
        if not stktypect:
            stktypect = ''
        if not stktype:
            stktype = ''
        if not refac:
            refac = ''
        if not stkfr:
            stkfr = ''
        if not stkto:
            stkto = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "stkno": stkno,
            "stkprf": stkprf,
            "stkfrn": stkfrn,
            "stkton": stkton,
            "bkstatus": bkstatus,
            "cfmsts": cfmsts,
            "brname": brname,
            "usrname": usrname,
            "slsts": slsts,
            "pslsts": pslsts,
            "stktypect": stktypect,
            "stktype": stktype,
            "refac": refac,
            "stkfr": stkfr,
            "stkto": stkto,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, id=None, module=None, stock_type=None, from_serial=None, to_serial=None, stock_prefix=None, no_of_leaves=None, no_of_books=None):
        if not id:
            id = 0
        if not module:
            module = ''
        if not stock_type:
            stock_type = ''
        if not from_serial:
            from_serial = ''
        if not to_serial:
            to_serial = ''
        if not stock_prefix:
            stock_prefix = ''
        if not no_of_leaves:
            no_of_leaves = 0
        if not no_of_books:
            no_of_books = 0
        payload = {
            "id": id,
            "module": module,
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "stock_prefix": stock_prefix,
            "no_of_leaves": no_of_leaves,
            "no_of_books": no_of_books
        }
        return payload

    def update(self, id=None, stock_no=None, stock_prefix=None, from_serial=None, to_serial=None, no_of_leaves=None, no_of_books=None, stock_type=None, module=None, book_status=None, confirm_status=None, stock_leaves_status=None, pslsts=None, ref_account_no=None, branchid=None, user_created=None, user_approved=None, assigned_teller_id=None, last_date=None, issuing_name=None, amount=None, currency=None, beneficiary_name=None, contact=None, purpose=None):
        if not id:
            id = 0
        if not stock_no:
            stock_no = ''
        if not stock_prefix:
            stock_prefix = ''
        if not from_serial:
            from_serial = ''
        if not to_serial:
            to_serial = ''
        if not no_of_leaves:
            no_of_leaves = 0
        if not no_of_books:
            no_of_books = 0
        if not stock_type:
            stock_type = ''
        if not module:
            module = ''
        if not book_status:
            book_status = ''
        if not confirm_status:
            confirm_status = ''
        if not stock_leaves_status:
            stock_leaves_status = ''
        if not pslsts:
            pslsts = ''
        if not ref_account_no:
            ref_account_no = ''
        if not branchid:
            branchid = 0
        if not user_created:
            user_created = 0
        if not user_approved:
            user_approved = 0
        if not assigned_teller_id:
            assigned_teller_id = 0
        if not last_date:
            last_date = ''
        if not issuing_name:
            issuing_name = ''
        if not amount:
            amount = 0
        if not currency:
            currency = ''
        if not beneficiary_name:
            beneficiary_name = ''
        if not contact:
            contact = ''
        if not purpose:
            purpose = ''
        payload = {
            "id": id,
            "stock_no": stock_no,
            "stock_prefix": stock_prefix,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "no_of_leaves": no_of_leaves,
            "no_of_books": no_of_books,
            "stock_type": stock_type,
            "module": module,
            "book_status": book_status,
            "confirm_status": confirm_status,
            "stock_leaves_status": stock_leaves_status,
            "pslsts": pslsts,
            "ref_account_no": ref_account_no,
            "branchid": branchid,
            "user_created": user_created,
            "user_approved": user_approved,
            "assigned_teller_id": assigned_teller_id,
            "last_date": last_date,
            "issuing_name": issuing_name,
            "amount": amount,
            "currency": currency,
            "beneficiary_name": beneficiary_name,
            "contact": contact,
            "purpose": purpose
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload