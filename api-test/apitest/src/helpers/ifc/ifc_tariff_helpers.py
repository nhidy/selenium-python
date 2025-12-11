from ...utilities.requestUtility import RequestUtility

class IFCTariffHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/View', payload)

    def simple_search_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/SimpleSearch', payload)

    def advanced_search_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/AdvanceSearch', payload)

    def add_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/Create', payload)

    def update_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/Update', payload)

    def delete_ifc_tariff(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/Delete', payload)

    def get_list_ifc_by_tariff_code(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTariff/GetListIfcTariffByCode', payload)