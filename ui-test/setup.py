# import re
from setuptools import setup, find_packages 

setup(
    name='webui_test',
    version="2.0.0",
    author="NhiDY",
    author_email="nhidy@jits.vn",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # 'selenium==4.24.0',
        # 'numpy',
        # 'parameterized',
        # 'colorama',
        # 'openpyxl',
        # 'PyYAML',
        # 'unittest-xml-reporting',
        # 'jinja2',
        # 'markupsafe',
        # 'fastapi',
        # 'uvicorn',
        # 'pandas',
        # 'pyautogui'
    ], 
    scripts=[
        'webui_test/running/html/charts_script.html',
        'webui_test/running/html/heading.html',
        'webui_test/running/html/report.html',
        'webui_test/running/html/stylesheet.html',
        'webui_test/running/html/template.html'
    ]
)