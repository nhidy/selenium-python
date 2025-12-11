from ...utilities.requestUtility import RequestUtility

class PaymentQueueForInwardHelper(object):
    def __init__(self, user):
        self.requests_utility = user
    # Payment Queue At Center

    def simple_search_payment_queue_for_inward(self, term=None, page_index=None, page_size=None):
        if not term:
            term = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/QueueForInward/Search?term={term}&pageIndex={page_index}&pageSize={page_size}')

    def advanced_search_payment_queue_for_inward(self, payload):
        return self.requests_utility.post_payment(f'api/QueueForInward/Search', payload)

    def add_payment_queue_for_inward(self, payload):
        return self.requests_utility.post_payment(f'api/QueueForInward/Create', payload)

    def view_payment_queue_for_inward(self, id):
        return self.requests_utility.get_payment(f'api/QueueForInward/View/{id}')

    def approve_payment_queue_for_inward(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/PaymentQueueCenter/approve

    def reject_payment_queue_for_inward(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/PaymentQueueCenter/reject