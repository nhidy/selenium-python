from ...utilities.requestUtility import RequestUtility

class FundTransferViaFastHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_fund_transfer_via_fast(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/FundTransferViaFast/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_fund_transfer_via_fast(self, payload):
        return self.requests_utility.post_payment(f'api/FundTransferViaFast/Search', payload)

    def add_fund_transfer_via_fast(self, payload):
        return self.requests_utility.post_payment(f'api/FundTransferViaFast/Create', payload)

    def view_fund_transfer_via_fast(self, id):
        return self.requests_utility.get_payment(f'api/FundTransferViaFast/View/{id}')

    def approve_fund_transfer_via_fast(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/FundTransferViaFast/approve

    def reject_fund_transfer_via_fast(self,   payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/FundTransferViaFast/reject

    def check_office_fund_transfer_via_fast(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/FundTransferViaFast/checkofficer