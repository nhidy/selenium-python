from ...utilities.requestUtility import RequestUtility

class PaymentCatalogHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_payment_catalog(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/Catalog/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_payment_catalog(self, payload):
        return self.requests_utility.post_payment(f'api/Catalog/Search', payload)

    def add_payment_catalog(self, payload):
        return self.requests_utility.post_payment(f'api/Catalog/Create', payload)

    def view_payment_catalog(self, id):
        return self.requests_utility.get_payment(f'api/Catalog/View/{id}')

    def update_payment_catalog(self, payload):
        return self.requests_utility.put_payment(f'api/Catalog/Update', payload)

    def delete_payment_catalog(self, id=None):
        if not id:
            id = 0
        return self.requests_utility.delete_payment(f'api/Catalog/Delete?id={id}')

    def list_instruction(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/CatalogueDefinition/ListInstruction

    def list_tariff(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/CatalogueDefinition/ListTariff

    def list_group_id(self, payload):
        return self.requests_utility.post_payment(f'', payload)

# ====================================== Workflow id ======================================
# Payment - Catalogue Definition
    def PMT_SEARCH_SP_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_SP_PMTCAT', fields_data)

    def PMT_SEARCH_ADV_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_ADV_PMTCAT', fields_data)

    def PMT_VIEW_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_VIEW_PMTCAT', fields_data)

    def PMT_INSERT_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_INSERT_PMTCAT', fields_data)

    def PMT_UPDATE_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_UPDATE_PMTCAT', fields_data)

    def PMT_DELETE_PMTCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_DELETE_PMTCAT', fields_data)