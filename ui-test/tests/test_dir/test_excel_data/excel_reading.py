
import webui_test 
from webui_test import data , jweb_excel
# from pandas import read_excel

# thay doi gia tri thanh "Available balance" khi case "test_00_check_spelling" PASS
available_bal_label="Avaiable balance"
my_sheet = 'Sheet1'
file_name = "D:/JWEB/JWebTestPython/demo/data_excel/data_transaction.xlsx"
username =""
password=""

class DPT_CWCTest(webui_test.TestCase):
    def get_url(self):
        return('http://192.168.1.246:8080/login/')
    
    def start_class(self):
        username =  self.get_value_excel( sheet= my_sheet, column= "Value", row= 7 , filename = file_name)
        password = self.get_value_excel( sheet= my_sheet, column= "Value", row= 8 , filename = file_name)
        self.login(username,password)
    
    def end_class(self):
        self.logout()
    
    def test_06_read_excel(self):
        data_file = self.open_file_excel(sheet = my_sheet, url_file_name=file_name)
        print(data_file)
        username =  self.get_value_excel_cell(data_file, column= "Value", row= 7 )
        print(username)
    
    def test_07_read_excel_fail(self):
        data_file = self.open_file_excel(sheet = my_sheet, url_file_name="file_name")
        print(data_file)
        username =  self.get_value_excel_cell(data_file, column= "Value", row= 7 )
        print(username)
        
if __name__ == "__main__":
    webui_test.main()