class FixedAssetAccountPayload(object):
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

    def advanced_search(self, account_number=None, fixed_asset_account_name=None, booking_currency_code=None, catalog_code=None, fixed_asset_type=None, fixed_asset_status=None, page_index=None, page_size=None):
        if not account_number:
            account_number = ''
        if not fixed_asset_account_name:
            fixed_asset_account_name = ''
        if not booking_currency_code:
            booking_currency_code = ''
        if not catalog_code:
            catalog_code = ''
        if not fixed_asset_type:
            fixed_asset_type = ''
        if not fixed_asset_status:
            fixed_asset_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "account_number": account_number,
            "fixed_asset_account_name": fixed_asset_account_name,
            "booking_currency_code": booking_currency_code,
            "catalog_code": catalog_code,
            "fixed_asset_type": fixed_asset_type,
            "fixed_asset_status": fixed_asset_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def update(self, id=None, fixed_asset_account_name=None, reference_number=None, fixed_asset_classification=None, depreciation_method=None, fixed_asset_life_time=None, fixed_asset_life_time_unit=None, provider_name=None, owner=None):
        if not id:
            id = 0
        if not fixed_asset_account_name:
            fixed_asset_account_name = ''
        if not reference_number:
            reference_number = ''
        if not fixed_asset_classification:
            fixed_asset_classification = ''
        if not depreciation_method:
            depreciation_method = ''
        if not fixed_asset_life_time:
            fixed_asset_life_time = None
        if not fixed_asset_life_time_unit:
            fixed_asset_life_time_unit = ''
        if not provider_name:
            provider_name = ''
        if not owner:
            owner = ''
        payload = {
            "id": id,
            "fixed_asset_account_name": fixed_asset_account_name,
            "reference_number": reference_number,
            "fixed_asset_classification": fixed_asset_classification,
            "depreciation_method": depreciation_method,
            "fixed_asset_life_time": fixed_asset_life_time,
            "fixed_asset_life_time_unit": fixed_asset_life_time_unit,
            "provider_name": provider_name,
            "owner": owner
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload