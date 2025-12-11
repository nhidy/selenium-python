from ...utilities.requestUtility import RequestUtility

class IFCDefinitionHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/View', payload)

    def simple_search_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/SimpleSearch', payload)

    def advanced_search_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/AdvanceSearch', payload)

    def add_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/Create', payload)

    def update_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/Update', payload)

    def delete_ifc_definition(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCDefinition/Delete', payload)

    def list_group_id(self, payload):
        return self.requests_utility.post_ifc(f'', payload)

# ====================================== Workflow id ======================================
# IFC - IFC Definition
    def IFC_SEARCH_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_SEARCH_IFC', fields_data)

    def IFC_ADSEARCH_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_ADSEARCH_IFC', fields_data)

    def IFC_VIEW_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_VIEW_IFC', fields_data)

    def IFC_INSERT_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_INSERT_IFC', fields_data)

    def IFC_UPDATE_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_UPDATE_IFC', fields_data)

    def IFC_DELETE_IFC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_DELETE_IFC', fields_data)