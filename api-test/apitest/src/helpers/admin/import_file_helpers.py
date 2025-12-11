from ...utilities.requestUtility import RequestUtility

class ImportFileHelper(object):
    def __init__(self, o9):
        self.requests_utility = o9
    
    def list_search_files(self, data):
        return self.requests_utility.post('admin/ImportFile/SimpleSearch', data)

    
    def process_file(self, data):
        return self.requests_utility.post(f'admin/ImportFile/ProcessFile', data)
    
    def delete_file(self, data):
        return self.requests_utility.post(f'admin/ImportFile/DeleteFile', data)
    
    def file_status(self, data):
        return self.requests_utility.post('admin/ImportFile/status', data)

    def imported_file(self, data):
        return self.requests_utility.post('admin/ImportFile', data)
