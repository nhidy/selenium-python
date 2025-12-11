from ...utilities.requestUtility import RequestUtility

class PoManagementHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_po_management(self, message_code=None, page=None, limit=None):
        if not message_code:
            message_code = ''
        if not page:
            page = 0
        if not limit:
            limit = 2147483647
        return self.requests_utility.get_payment(f'api/PoManagement/Search?MessageCode={message_code}&PageIndex={page}&limit={limit}')

    def add_po_management(self, payload):
        return self.requests_utility.post_payment(f'api/PoManagement/Create', payload)

    def view_po_management(self, id):
        return self.requests_utility.get_payment(f'api/PoManagement/View/{id}')

    def update_po_management(self, payload):
        return self.requests_utility.put_payment(f'api/PoManagement/Update', payload)

    def delete_po_management(self, id):
        return self.requests_utility.delete_payment(f'api/PoManagement/Delete/{id}')