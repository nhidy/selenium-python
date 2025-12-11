from datetime import datetime

class CodeListPayload(object):
    def add(self, code_id=None, code_name=None, caption=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_group=None, code_index=None, code_value=None, ftag=None, visible=None):
        if not code_id:
            code_id = ''
        if not code_name:
            code_name = ''
        if not caption:
            caption = ''
        if not english:
            english = ''
        if not vietnamese:
            vietnamese = ''
        if not laothian:
            laothian = ''
        if not khmer:
            khmer = ''
        if not myanmar:
            myanmar = ''
        if not code_group:
            code_group = ''
        if not code_index:
            code_index = 0
        if not code_value:
            code_value = ''
        if not ftag:
            ftag = ''
        if not visible:
            visible = 0
        payload = {
            "code_id": code_id,
            "code_name": code_name,
            "caption": caption,
            "mcaption": {
                "english": english,
                "vietnamese": vietnamese,
                "laothian": laothian,
                "khmer": khmer,
                "myanmar": myanmar
            },
            "code_group": code_group,
            "code_index": code_index,
            "code_value": code_value,
            "ftag": ftag,
            "visible": visible
        }
        return payload

    def update(self, id=None, code_id=None, code_name=None, caption=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_group=None, code_index=None, code_value=None, ftag=None, visible=None):
        if not id:
            id = 0
        if not code_id:
            code_id = ''
        if not code_name:
            code_name = ''
        if not caption:
            caption = ''
        if not english:
            english = ''
        if not vietnamese:
            vietnamese = ''
        if not laothian:
            laothian = ''
        if not khmer:
            khmer = ''
        if not myanmar:
            myanmar = ''
        if not code_group:
            code_group = ''
        if not code_index:
            code_index = 0
        if not code_value:
            code_value = ''
        if not ftag:
            ftag = ''
        if not visible:
            visible = 0
        payload = {
            "id": id,
            "code_id": code_id,
            "code_name": code_name,
            "caption": caption,
            "mcaption": {
                "english": english,
                "vietnamese": vietnamese,
                "laothian": laothian,
                "khmer": khmer,
                "myanmar": myanmar
            },
            "code_group": code_group,
            "code_index": code_index,
            "code_value": code_value,
            "ftag": ftag,
            "visible": visible
        }
        return payload

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, code_id=None, code_name=None, caption=None, code_group=None, code_index=None, code_index_from=None, code_index_to=None, ftag=None, page_index=None, page_size=None):
        if not code_id:
            code_id = ''
        if not code_name:
            code_name = ''
        if not caption:
            caption = ''
        if not code_group:
            code_group = ''
        if not code_index:
            code_index = None
        if not code_index_from:
            code_index_from = None
        if not code_index_to:
            code_index_to = None
        if not ftag:
            ftag = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "code_id": code_id,
            "code_name": code_name,
            "caption": caption,
            "code_group": code_group,
            "code_index": code_index,
            "code_index_from": code_index_from,
            "code_index_to": code_index_to,
            "ftag": ftag,
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