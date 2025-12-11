from ...utilities.requestUtility import RequestUtility

class CashHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def list_cashflow(self, payload):
        return self.requests_utility.post_cash(f'', payload)
        # cash/cashflow/List

    def list_cashflow_details(self, payload):
        return self.requests_utility.post_cash(f'', payload)
        # cash/cashflow/ListDetails

    # locale string resource (lsr)
    def delete_lsr(self, id):
        return self.requests_utility.delete_cash(f'api/LocaleStringResource/Delete/{id}')

    def get_all_lsr(self):
        return self.requests_utility.get_cash(f'api/LocaleStringResource/GetAll')

    def get_lsr_by_id(self, id):
        return self.requests_utility.get_cash(f'api/LocaleStringResource/GetById/{id}')

    def get_lsr_by_name(self, language):
        return self.requests_utility.get_cash(f'api/LocaleStringResource/GetByName/{language}')

    def add_lsr(self, payload):
        return self.requests_utility.post_cash(f'api/LocaleStringResource/Create', payload)

    def update_lsr(self, payload):
        return self.requests_utility.put_cash(f'api/LocaleStringResource/Update', payload)

    def get_lsr_by_resource(self, language):
        return self.requests_utility.get_cash(f'api/LocaleStringResource/GetResource/{language}')

    # log
    def get_all_log(self):
        return self.requests_utility.get_cash(f'api/Log/GetAll')

    def get_log_by_id(self, id):
        return self.requests_utility.get_cash(f'api/Log/GetById/{id}')

    def delete_log(self):
        return self.requests_utility.delete_cash(f'api/Log/Delete')

    # queue
    def get_queue(self):
        return self.requests_utility.get_cash(f'Queue/GetSampleStructureToSetup')

    def get_queue_status(self):
        return self.requests_utility.get_cash(f'Queue/GetStatus')

    # template
    def get_template(self, assembly_name, class_name):
        return self.requests_utility.get_cash(f'api/Template/GetInfo/{assembly_name}/{class_name}')