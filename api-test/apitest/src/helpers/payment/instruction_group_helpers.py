from ...utilities.requestUtility import RequestUtility

class InstructionGroupHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_instruction_group(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/InstructionGroup/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_instruction_group(self, payload):
        return self.requests_utility.post_payment(f'api/InstructionGroup/Search', payload)

    def add_instruction_group(self, payload):
        return self.requests_utility.post_payment(f'api/InstructionGroup/Create', payload)

    def view_instruction_group(self, id):
        return self.requests_utility.get_payment(f'api/InstructionGroup/View/{id}')

    def update_instruction_group(self, payload):
        return self.requests_utility.put_payment(f'api/InstructionGroup/Update', payload)

    def delete_instruction_group(self, id=None):
        if not id:
            id = 0
        return self.requests_utility.delete_payment(f'api/InstructionGroup/Delete?id={id}')