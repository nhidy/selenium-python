from ...utilities.requestUtility import RequestUtility

class AccountChartHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/View', payload)

    def simple_search_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/SimpleSearch', payload)

    def advanced_search_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/AdvanceSearch', payload)

    def add_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/Create', payload)

    def update_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/Update', payload)

    def delete_account_chart(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/Delete', payload)

    def open_account(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountChart/OpenAccount', payload)

    def load_children(self, payload):
        return self.requests_utility.post_accounting(f'', payload)
        # accounting/accountchart/LoadChildren

# ====================================== Workflow id ======================================
# Accounting - Account Chart
    def ACT_ACCHRT_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_SER_SIMPLE', fields_data)

    def ACT_ACCHRT_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_SER_ADVANCE', fields_data)

    def ACT_ACCHRT_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_VIEW', fields_data)

    def ACT_ACCHRT_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_INS', fields_data)

    def ACT_ACCHRT_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_UPD', fields_data)

    def ACT_ACCHRT_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_DEL', fields_data)