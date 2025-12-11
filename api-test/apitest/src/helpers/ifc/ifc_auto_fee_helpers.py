from ...utilities.requestUtility import RequestUtility

class IFCAutoFeeHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/View', payload)

    def simple_search_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/SimpleSearch', payload)

    def advanced_search_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/AdvanceSearch', payload)

    def add_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/Create', payload)

    def update_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/Update', payload)

    def delete_ifc_auto_fee(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCAutoFee/Delete', payload)

# ====================================== Workflow id ======================================
# IFC - IFC Auto Fee
    def IFC_SEARCH_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_SEARCH_IFCAUTOFEE', fields_data)

    def IFC_ADSEARCH_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_ADSEARCH_IFCAUTOFEE', fields_data)

    def IFC_VIEW_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_VIEW_IFCAUTOFEE', fields_data)

    def IFC_INSERT_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_INSERT_IFCAUTOFEE', fields_data)

    def IFC_UPDATE_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_UPDATE_IFCAUTOFEE', fields_data)

    def IFC_DELETE_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'IFC_DELETE_IFCAUTOFEE', fields_data)