from ...utilities.requestUtility import RequestUtility

class CalendarHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def advanced_search_calendar(self, payload):
        return self.requests_utility.post_admin(f'api/Calendar/Search', payload)

    def simple_search_calendar(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/Calendar/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def add_calendar(self, payload):
        return self.requests_utility.post_admin(f'api/Calendar/Create', payload)

    def view_calendar(self, id):
        return self.requests_utility.get_admin(f'api/Calendar/View/{id}')

    def update_calendar(self, payload):
        return self.requests_utility.put_admin(f'api/Calendar/Update', payload)

    def delete_calendar(self, payload):
        return self.requests_utility.delete_admin(f'api/Calendar/Delete', payload)

    def get_list_calendar(self, payload):
        return self.requests_utility.delete_admin(f'api/Calendar/GetListCalendar', payload)    