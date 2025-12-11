from ...utilities.requestUtility import RequestUtility

class InstructionItemHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_instruction_item(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/InstructionItem/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_instruction_item(self, payload):
        return self.requests_utility.post_payment(f'api/InstructionItem/Search', payload)

    def add_instruction_item(self, payload):
        return self.requests_utility.post_payment(f'api/InstructionItem/Create', payload)

    def view_instruction_item(self, id):
        return self.requests_utility.get_payment(f'api/InstructionItem/View/{id}')

    def update_instruction_item(self, payload):
        return self.requests_utility.put_payment(f'api/InstructionItem/Update', payload)

    def delete_instruction_item(self, id=None):
        if not id:
            id = 0
        return self.requests_utility.delete_payment(f'api/InstructionItem/Delete?id={id}')