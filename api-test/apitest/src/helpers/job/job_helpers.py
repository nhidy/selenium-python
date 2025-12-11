from ...utilities.requestUtility import RequestUtility

class JobHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def list_instances(self, data):
        return self.requests_utility.post(f'job/ListInstances', data)

    def list_details(self, data):
        return self.requests_utility.post(f'job/ListDetails', data)
    
    def list_errors(self, data):
        return self.requests_utility.post(f'job/ListErrors', data)
    
    def list_job_stopat(self, data):
        return self.requests_utility.post(f'job/stopat', data)
    
    def list_job_check(self, data):
        return self.requests_utility.post(f'job/check', data)
    
