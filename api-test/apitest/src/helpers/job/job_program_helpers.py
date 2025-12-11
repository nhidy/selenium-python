from ...utilities.requestUtility import RequestUtility

class JobProgramHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_JobPrograms(self, data):
        return self.requests_utility.post(f'job/JobProgram/SimpleSearch', data)
    
    def advance_search_JobPrograms(self, payload):
        return self.requests_utility.post(f'job/JobProgram/search', payload)

    def get_JobProgram(self, data):
        return self.requests_utility.post(f'job/JobProgram/View', data)
    
    def add_JobProgram(self, data):
        return self.requests_utility.post('job/JobProgram', data)
    
    def update_JobProgram(self, data):
        return self.requests_utility.post(f'job/JobProgram/Update', data)
    
    def delete_JobProgram(self, data):
        return self.requests_utility.post(f'job/JobProgram/delete', data)
    