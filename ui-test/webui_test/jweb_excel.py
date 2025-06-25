from pandas import read_excel
from pandas import ExcelWriter
# from openpyxl import load_workbook
import os 

_URL_FILE = os.path.join(os.path.dirname(__file__), '../tests/data_excel/data_dpt_account.xlsx')

def get_value_from_excel(sheet_name, column, row, url_file_name=None):
    if url_file_name is None:
        url_file_name = _URL_FILE
    df = read_excel(url_file_name, sheet_name=sheet_name, dtype=str)
    return df[column][row-1]

def read_file_excel(sheet_name, url_file_name=None):
    if url_file_name is None:
        url_file_name = _URL_FILE
    return read_excel(url_file_name, sheet_name=sheet_name, dtype=str)

def get_value_cell_excel(df, column, row):
    return df[column][row-1]

def write_value_to_excel(new_value, sheet_name, column, row, url_file_name=None):
    if url_file_name is None:
        url_file_name=_URL_FILE
    # Load the sheet into a DataFrame
    df = read_excel(url_file_name, sheet_name=sheet_name, dtype=str)
    # Update the value at the specified row and column
    df.at[row-1, column] = new_value
    # Write the updated DataFrame back to the same Excel file
    with ExcelWriter(url_file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)