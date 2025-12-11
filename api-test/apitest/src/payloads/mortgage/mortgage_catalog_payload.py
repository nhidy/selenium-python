from datetime import datetime

class MortgageCatalogPayload(object):
    def add(self, catalog_code=None, catalog_name=None, currency_code=None, collateral_asset_type=None, collateral_rate=None, classification=None, risk_rate=None, group_id=None, book_scope=None, depreciation_option=None, catalog_status=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not collateral_asset_type:
            collateral_asset_type = ''
        if not collateral_rate:
            collateral_rate = None
        if not classification:
            classification = ''
        if not risk_rate:
            risk_rate = None
        if not group_id:
            group_id = None
        if not book_scope:
            book_scope = ''
        if not depreciation_option:
            depreciation_option = ''
        if not catalog_status:
            catalog_status = ''
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "collateral_asset_type": collateral_asset_type,
            "collateral_rate": collateral_rate,
            "classification": classification,
            "risk_rate": risk_rate,
            "group_id": group_id,
            "book_scope": book_scope,
            "depreciation_option": depreciation_option,
            "catalog_status": catalog_status
        }
        return payload

    def update(self, id=None, catalog_name=None, currency_code=None, collateral_asset_type=None, collateral_rate=None, classification=None, risk_rate=None, group_id=None, book_scope=None, depreciation_option=None, catalog_status=None):
        if not id:
            id = 0
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not collateral_asset_type:
            collateral_asset_type = ''
        if not collateral_rate:
            collateral_rate = None
        if not classification:
            classification = ''
        if not risk_rate:
            risk_rate = None
        if not group_id:
            group_id = None
        if not book_scope:
            book_scope = ''
        if not depreciation_option:
            depreciation_option = ''
        if not catalog_status:
            catalog_status = ''
        payload = {
            "id": id,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "collateral_asset_type": collateral_asset_type,
            "collateral_rate": collateral_rate,
            "classification": classification,
            "risk_rate": risk_rate,
            "group_id": group_id,
            "book_scope": book_scope,
            "depreciation_option": depreciation_option,
            "catalog_status": catalog_status
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

    def advanced_search(self, catalog_code=None, catalog_name=None, currency_code=None, collateral_asset_type=None, classification=None, collateral_rate_from=None, collateral_rate_to=None, catalog_status=None, page_index=None, page_size=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not collateral_asset_type:
            collateral_asset_type = ''
        if not classification:
            classification = ''
        if not collateral_rate_from:
            collateral_rate_from = None
        if not collateral_rate_to:
            collateral_rate_to = None
        if not catalog_status:
            catalog_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "collateral_asset_type": collateral_asset_type,
            "classification": classification,
            "collateral_rate_from": collateral_rate_from,
            "collateral_rate_to": collateral_rate_to,
            "catalog_status": catalog_status,
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