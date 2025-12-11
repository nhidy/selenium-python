from ...utilities.requestUtility import RequestUtility

class JobStepHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_JobStep(self, data):
        return self.requests_utility.post(f'job/JobStep/SimpleSearch', data)
    
    def advance_search_JobStep(self, payload):
        return self.requests_utility.post(f'job/JobStep/search', payload)

    def get_JobStep(self, data):
        return self.requests_utility.post(f'job/JobStep/View', data)
    
    def add_JobStep(self, data):
        return self.requests_utility.post('job/JobStep', data)
    
    def update_JobStep(self, data):
        return self.requests_utility.post(f'job/JobStep/Update', data)
    
    def delete_JobStep(self, data):
        return self.requests_utility.post(f'job/JobStep/Delete', data)