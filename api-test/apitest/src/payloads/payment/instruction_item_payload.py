from datetime import datetime

class InstructionItemPayload(object):
    def add(self, pmt_inst_code=None, caption=None, maximum_length=None, datatype=None, field_type=None, field_mask=None, format=None, default_value=None, minimum_width=None, height=None, line_number=None, maximum_line=None, display_decimal=None, tooltip=None, tag=None):
        if not pmt_inst_code:
            pmt_inst_code = ''
        if not caption:
            caption = ''
        if not maximum_length:
            maximum_length = 0
        if not datatype:
            datatype = ''
        if not field_type:
            field_type = ''
        if not field_mask:
            field_mask = ''
        if not format:
            format = ''
        if not default_value:
            default_value = ''
        if not minimum_width:
            minimum_width = 0
        if not height:
            height = 0
        if not line_number:
            line_number = 0
        if not maximum_line:
            maximum_line = 0
        if not display_decimal:
            display_decimal = 0
        if not tooltip:
            tooltip = ''
        if not tag:
            tag = ''
        payload = {
            "pmt_inst_code": pmt_inst_code,
            "caption": caption,
            "maximum_length": maximum_length,
            "datatype": datatype,
            "field_type": field_type,
            "field_mask": field_mask,
            "format": format,
            "default_value": default_value,
            "minimum_width": minimum_width,
            "height": height,
            "line_number": line_number,
            "maximum_line": maximum_line,
            "display_decimal": display_decimal,
            "tooltip": tooltip,
            "tag": tag
        }
        return payload

    def update(self, id=None, pmt_inst_code=None, caption=None, maximum_length=None, datatype=None, field_type=None, field_mask=None, format=None, default_value=None, minimum_width=None, height=None, line_number=None, maximum_line=None, display_decimal=None, tooltip=None, tag=None):
        if not id:
            id = 0
        if not pmt_inst_code:
            pmt_inst_code = ''
        if not caption:
            caption = ''
        if not maximum_length:
            maximum_length = 0
        if not datatype:
            datatype = ''
        if not field_type:
            field_type = ''
        if not field_mask:
            field_mask = ''
        if not format:
            format = ''
        if not default_value:
            default_value = ''
        if not minimum_width:
            minimum_width = 0
        if not height:
            height = 0
        if not line_number:
            line_number = 0
        if not maximum_line:
            maximum_line = 0
        if not display_decimal:
            display_decimal = 0
        if not tooltip:
            tooltip = ''
        if not tag:
            tag = ''
        payload = {
            "id": id,
            "pmt_inst_code": pmt_inst_code,
            "caption": caption,
            "maximum_length": maximum_length,
            "datatype": datatype,
            "field_type": field_type,
            "field_mask": field_mask,
            "format": format,
            "default_value": default_value,
            "minimum_width": minimum_width,
            "height": height,
            "line_number": line_number,
            "maximum_line": maximum_line,
            "display_decimal": display_decimal,
            "tooltip": tooltip,
            "tag": tag
        }
        return payload

    def advanced_search(self, pmt_inst_code=None, caption=None, page_index=None, page_size=None):
        if not pmt_inst_code:
            pmt_inst_code = ''
        if not caption:
            caption = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "pmt_inst_code": pmt_inst_code,
            "caption": caption,
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