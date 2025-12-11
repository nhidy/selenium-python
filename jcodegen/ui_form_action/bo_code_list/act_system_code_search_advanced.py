


# system_code_table
# Choose name: system_code_table_advanced_search
def system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
    self.close_all_form()
    self.click_menu('System Code Table', 'Accounting System Code Table')
    self.wait_for_button_available('Search')
    self.assert_form_title('ACT-System Code Table-Search')
    if code_id:
        self.adv_search_text('Code Id', code_id)
    if code_name:
        self.adv_search_text('Code Name', code_name)
    if caption_of_code:
        self.adv_search_text('Caption Of Code', caption_of_code)
    if index:
        self.adv_search('Index', index)
    if index_form:
        self.adv_search_group('Index Form', index_form)
    if index_to:
        self.adv_search_group('Index To', index_to)
    if field_link:
        self.adv_search_text('Field Link', field_link)
    self.click_button_search_advanced()
    self.wait_loading()

# TEST CASE: ADVANCED SEARCH
def test_000_system_code_table_advanced_search_success(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    code_id_test = None
    code_name_test = None
    caption_of_code_test = None
    index_test = None
    index_form_test = None
    index_to_test = None
    field_link_test = None

    system_code_table_advanced_search_result = self.system_code_table_advanced_search(
        code_id=code_id_test,
        code_name=code_name_test,
        caption_of_code=caption_of_code_test,
        index=index_test,
        index_form=index_form_test,
        index_to=index_to_test,
        field_link=field_link_test,
    )
