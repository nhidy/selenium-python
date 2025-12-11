


# system_code_table
# Choose name: system_code_table_simple_search
def system_code_table_simple_search(self, text):
    self.close_all_form()
    self.click_menu('System Code Table', 'Accounting System Code Table')
    self.wait_for_button_available('Search')
    self.assert_form_title('ACT-System Code Table-Search')
    self.simple_search(text=text, placeholder='Search Text')
    self.wait_loading()

# TEST CASE: SIMPLE SEARCH
def test_000_system_code_table_simple_search_success(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    search_text_test = None

    system_code_table_simple_search_result = self.system_code_table_simple_search(
        search_text=search_text_test,
    )
