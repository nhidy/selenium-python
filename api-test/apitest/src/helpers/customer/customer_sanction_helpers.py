from ...utilities.requestUtility import RequestUtility

class CustomerSanctionHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_customersanction(self, data):
        return self.requests_utility.post(f'customer/CheckCustomerSanction/SimpleSearch', data)
    
    def advance_search_customersanction(self, payload):
        return self.requests_utility.post(f'customer/CheckCustomerSanction/search', payload)

    def view_customer_sanction(self, data):
        return self.requests_utility.post(f'customer/CheckCustomerSanction/View', data)
    
    def check_sanction(self, data): 
        return self.requests_utility.post(f'customer/CheckCustomerSanction/CheckSanction', data)
    
    def check_repid_exist(self, data): 
        return self.requests_utility.post(f'customer/CheckCustomerSanction/CheckRepIdExist', data)

    # def list_customer_deposit(self, post): 
    #     return self.requests_utility.get(f'customer/customer/{id}/deposit')
    
    # def list_customer_credit(self, post): 
    #     return self.requests_utility.get(f'customer/customer/{id}/credit')
    
    # def list_customer_mortgage(self, post): 
    #     return self.requests_utility.get(f'customer/customer/{id}/mortgage')
    
    # def list_customer_provision(self, post): 
    #     return self.requests_utility.get(f'customer/customer/{id}/provision')

    def add_customersanction(self, data):
        return self.requests_utility.post('customer/CheckCustomerSanction', data)
    
    # def update_customer(self, data):
    #     return self.requests_utility.post(f'customer/CheckCustomerSanction/Update', data)
    
    def delete_customersanction(self, data):
        return self.requests_utility.post(f'customer/CheckCustomerSanction/Delete', data)

# ====================================== Workflow id ======================================
# Customer - Check Customer Sanction
    def CTM_DELETE_SNC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_DELETE_SNC', fields_data)

    def CTM_IMPORT_SANCTION(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_IMPORT_SANCTION', fields_data)

    def CTM_IMPORT_KEY_SANCTION(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_IMPORT_KEY_SANCTION', fields_data)

    def CTM_EXPORT_SANCTION(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_EXPORT_SANCTION', fields_data)