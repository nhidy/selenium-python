from ...utilities.requestUtility import RequestUtility

class TariffHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/View', payload)

    def simple_search_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/SimpleSearch', payload)

    def advanced_search_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/AdvanceSearch', payload)

    def add_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/Create', payload)

    def update_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/Update', payload)

    def delete_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/Tariff/Delete', payload)

    def list_ifc(self, payload):
        return self.requests_utility.post_ifc(f'', payload)
        # ifc/tariff/ListIFC

# ====================================== Workflow id ======================================
# IFC - Tariff
    def IFC_SEARCH_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_SEARCH_TARIFF', fields_data)

    def IFC_ADSEARCH_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_ADSEARCH_TARIFF', fields_data)

    def IFC_VIEW_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_VIEW_TARIFF', fields_data)

    def IFC_INSERT_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_INSERT_TARIFF', fields_data)

    def IFC_UPDATE_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_UPDATE_TARIFF', fields_data)

    def IFC_DELETE_TARIFF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_DELETE_TARIFF', fields_data)