from ...utilities.requestUtility import RequestUtility

class ForeignExchangeHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/SimpleSearch', payload)

    def advanced_search_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/AdvanceSearch', payload)

    def add_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/Create', payload)

    def view_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/View', payload)

    def update_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/Update', payload)

    def delete_fx_rate(self, payload):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/Delete', payload)

    def get_base_currency(self):
        return self.requests_utility.post_fx(f'api/ForeignExchangeRate/GetBaseCurrency')

    # locale string resource (lsr)
    def delete_lsr(self, id):
        return self.requests_utility.delete_fx(f'api/LocaleStringResource/Delete/{id}')

    def get_all_lsr(self):
        return self.requests_utility.get_fx(f'api/LocaleStringResource/GetAll')

    def get_lsr_by_id(self, id):
        return self.requests_utility.get_fx(f'api/LocaleStringResource/GetById/{id}')

    def get_lsr_by_name(self, language):
        return self.requests_utility.get_fx(f'api/LocaleStringResource/GetByName/{language}')

    def add_lsr(self, payload):
        return self.requests_utility.post_fx(f'api/LocaleStringResource/Create', payload)

    def update_lsr(self, payload):
        return self.requests_utility.put_fx(f'api/LocaleStringResource/Update', payload)

    def get_lsr_by_resource(self, language):
        return self.requests_utility.get_fx(f'api/LocaleStringResource/GetResource/{language}')

    # log
    def get_all_log(self):
        return self.requests_utility.get_fx(f'api/Log/GetAll')

    def get_log_by_id(self, id):
        return self.requests_utility.get_fx(f'api/Log/GetById/{id}')

    def delete_log(self):
        return self.requests_utility.delete_fx(f'api/Log/Delete')

    # queue
    def get_queue(self):
        return self.requests_utility.get_fx(f'Queue/GetSampleStructureToSetup')

    def get_queue_status(self):
        return self.requests_utility.get_fx(f'Queue/GetStatus')

    # template
    def get_template(self, assembly_name, class_name):
        return self.requests_utility.get_fx(f'api/Template/GetInfo/{assembly_name}/{class_name}')