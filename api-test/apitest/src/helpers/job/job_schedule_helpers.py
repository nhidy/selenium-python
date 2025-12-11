from ...utilities.requestUtility import RequestUtility

class JobScheduleHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def search_JobSchedule(self, data):
        return self.requests_utility.post(f'job/JobSchedule/SimpleSearch', data)
    
    def advance_search_JobSchedule(self, payload):
        return self.requests_utility.post(f'job/JobSchedule/search', payload)

    def get_JobSchedule(self, data):
        return self.requests_utility.post(f'job/JobSchedule/View', data)
    
    def add_JobSchedule(self, data):
        return self.requests_utility.post('job/JobSchedule', data)
    
    def update_JobSchedule(self, data):
        return self.requests_utility.post(f'job/JobSchedule/Update', data)
    
    def delete_JobSchedule(self, data):
        return self.requests_utility.post(f'job/JobSchedule/Delete', data)