# Install requirements 
- py -m pip install pytest
- py -m pip install pytest-html
- py -m pip install requests
- py -m pip install pycryptodome
- py -m pip install tabulate
- py -m pip install pyodbc
- py -m pip install pandas
- py -m pip install setuptools

# Build source, change to folder contain setup.py
python setup.py install 

# Test all, change to folder apitest/tests
pytest

# Test marks, change to folder apitest/tests
pytest -m mark_name

# test file test_, change to folder
Example:
cd apitest\tests\shwebank\common\
cd apitest\tests\shwebank\regression_testing\
py.test test_admin_service.py --html=reports/test_admin_service.html --self-contained-html

# Output html report 
pytest --html=reports/file-name.html --self-contained-html
- Note: `--self-contained-html` create a self-contained report, which can be more convenient when sharing your results.

# Debug, place breakpoint
import pdb; pdb.set_trace()
continue-> press c Enter

# Print in temimal
py.test --capture=tee-sys [test_file]

# Install library pytest-repeat
pip install pytest-repeat

## Test repeat
pytest --count=100 -m mark_name
