from ...utilities.requestUtility import RequestUtility

class PaymentQueueForOutwardHelper(object):
    def __init__(self, user):
        self.requests_utility = user
    # Payment Queue

    def simple_search_payment_queue_for_outward(self, term=None, page_index=None, page_size=None):
        if not term:
            term = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/QueueForOutward/Search?term={term}&pageIndex={page_index}&pageSize={page_size}')

    def advanced_search_payment_queue_for_outward(self, payload):
        return self.requests_utility.post_payment(f'api/QueueForOutward/Search', payload)

    def add_payment_queue_for_outward(self, payload):
        return self.requests_utility.post_payment(f'api/QueueForOutward/Create', payload)

    def view_payment_queue_for_outward(self, message_code=None):
        if not message_code:
            message_code = ''
        return self.requests_utility.get_payment(f'api/QueueForOutward/View?MessageCode={message_code}')

    def approve_payment_queue_for_outward(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/PaymentQueue/approve

    def reject_payment_queue_for_outward(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/PaymentQueue/reject