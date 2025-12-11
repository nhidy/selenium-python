from ...utilities.requestUtility import RequestUtility

class JobDefinitionHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_JobDefinition(self, data):
        return self.requests_utility.post(f'job/JobDefinition/SimpleSearch', data)
    
    def advance_search_JobDefinition(self, payload):
        return self.requests_utility.post(f'job/JobDefinition/search', payload)

    def get_JobDefinition(self, data):
        return self.requests_utility.post(f'job/JobDefinition/View', data)
    
    def add_JobDefinition(self, data):
        return self.requests_utility.post('job/JobDefinition', data)
    
    def update_JobDefinition(self, data):
        return self.requests_utility.post(f'job/JobDefinition/Update', data)
    
    def delete_JobDefinition(self, data):
        return self.requests_utility.post(f'job/JobDefinition/Delete', data)