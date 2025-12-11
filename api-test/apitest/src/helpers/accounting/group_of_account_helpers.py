from ...utilities.requestUtility import RequestUtility

class GroupOfAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/View', payload)

    def simple_search_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/SimpleSearch', payload)

    def advanced_search_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/AdvanceSearch', payload)

    def add_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/Create', payload)

    def update_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/Update', payload)

    def delete_group_of_account(self, payload):
        return self.requests_utility.post_accounting(f'api/GroupOfAccount/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Group Of Account
    def ACT_ACGRP_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_SER_SIMPLE', fields_data)

    def ACT_ACGRP_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_SER_ADVANCE', fields_data)

    def ACT_ACGRP_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_VIEW', fields_data)

    def ACT_ACGRP_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_INS', fields_data)

    def ACT_ACGRP_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_UPD', fields_data)

    def ACT_ACGRP_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRP_DEL', fields_data)