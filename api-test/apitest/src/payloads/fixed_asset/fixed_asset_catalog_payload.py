class FixedAssetCatalogPayload(object):
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

    def advanced_search(self, catalog_code=None, catalog_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalog_status=None, page_index=None, page_size=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not fixed_asset_type:
            fixed_asset_type = ''
        if not fixed_asset_classification:
            fixed_asset_classification = ''
        if not depreciation_method:
            depreciation_method = ''
        if not catalog_status:
            catalog_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "fixed_asset_type": fixed_asset_type,
            "fixed_asset_classification": fixed_asset_classification,
            "depreciation_method": depreciation_method,
            "catalog_status": catalog_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, catalog_code=None, catalog_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, group_id=None, approve_user=None, catalog_status=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not fixed_asset_type:
            fixed_asset_type = ''
        if not fixed_asset_type:
            fixed_asset_classification = ''
        if not depreciation_method:
            depreciation_method = ''
        if not group_id:
            group_id = 0
        if not catalog_status:
            catalog_status = ''
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "fixed_asset_type": fixed_asset_type,
            "fixed_asset_classification": fixed_asset_classification,
            "depreciation_method": depreciation_method,
            "group_id": group_id,
            "catalog_status": catalog_status
        }
        return payload

    def update(self, id=None, catalog_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalog_status=None, group_id=None):
        if not id:
            id = 0
        if not catalog_name:
            catalog_name = ''
        if not fixed_asset_type:
            fixed_asset_type = ''
        if not fixed_asset_classification:
            fixed_asset_classification = ''
        if not depreciation_method:
            depreciation_method = ''
        if not catalog_status:
            catalog_status = ''
        if not group_id:
            group_id = 0
        payload = {
            "id": id,
            "catalog_name": catalog_name,
            "fixed_asset_type": fixed_asset_type,
            "fixed_asset_classification": fixed_asset_classification,
            "depreciation_method": depreciation_method,
            "catalog_status": catalog_status,
            "group_id": group_id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload