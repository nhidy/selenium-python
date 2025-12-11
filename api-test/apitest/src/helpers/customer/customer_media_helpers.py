from ...utilities.requestUtility import RequestUtility

class CustomerMediaHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_CustomerMedias(self, data):
        return self.requests_utility.post(f'customer/media/SimpleSearch', data)
    
    def advance_search_CustomerMedias(self, payload):
        return self.requests_utility.post(f'customer/media/search', payload)

    def view_CustomerMedia_by_id(self, data):
        return self.requests_utility.post(f'customer/media/View', data)
    
    def list_GetApproveMedia(self): 
        return self.requests_utility.post(f'customer/media/GetApproveMedia')
    
    def list_GetInformation(self, data): 
        return self.requests_utility.post(f'customer/media/GetInformation', data)

    
    # def list_CustomerMedia_credit(self, post): 
    #     return self.requests_utility.get(f'CustomerMedia/CustomerMedia/{id}/credit')
    
    # def list_CustomerMedia_mortgage(self, post): 
    #     return self.requests_utility.get(f'CustomerMedia/CustomerMedia/{id}/mortgage')
    
    # def list_CustomerMedia_provision(self, post): 
    #     return self.requests_utility.get(f'CustomerMedia/CustomerMedia/{id}/provision')

    def add_CustomerMedia(self, data):
        return self.requests_utility.post('customer/media', data)

    def approve_media(self, data): 
        return self.requests_utility.post(f'customer/media/ApproveMedia', data)
    
    def update_CustomerMedia(self, data):
        return self.requests_utility.post(f'customer/media/Update', data)
    
    def delete_CustomerMedia(self, data):
        return self.requests_utility.post(f'customer/media/Delete', data)
