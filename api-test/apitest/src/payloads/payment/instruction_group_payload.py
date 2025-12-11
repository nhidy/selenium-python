from datetime import datetime

class InstructionGroupPayload(object):
    def add(self, group_pmt_ins_code=None, pmt_inst_name=None):
        if not group_pmt_ins_code:
            group_pmt_ins_code = ''
        if not pmt_inst_name:
            pmt_inst_name = ''
        payload = {
            "group_pmt_ins_code": group_pmt_ins_code,
            "pmt_inst_name": pmt_inst_name
        }
        return payload

    def update(self, id=None, group_pmt_ins_code=None, pmt_inst_name=None):
        if not id:
            id = 0
        if not group_pmt_ins_code:
            group_pmt_ins_code = ''
        if not pmt_inst_name:
            pmt_inst_name = ''
        payload = {
            "id": id,
            "group_pmt_ins_code": group_pmt_ins_code,
            "pmt_inst_name": pmt_inst_name
        }
        return payload

    def advanced_search(self, group_pmt_ins_code=None, pmt_inst_name=None, page_index=None, page_size=None):
        if not group_pmt_ins_code:
            group_pmt_ins_code = ''
        if not pmt_inst_name:
            pmt_inst_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "group_pmt_ins_code": group_pmt_ins_code,
            "pmt_inst_name": pmt_inst_name,
            "page_index": page_index,
            "page_size": page_size
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