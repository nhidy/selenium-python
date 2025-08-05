from setuptools import setup, find_packages 

setup(
    name='webui_test',
    version="2.0.0",
    author="NhiDY",
    author_email="nhidy@jits.vn",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[], 
    scripts=[
        'webui_test/running/html/charts_script.html',
        'webui_test/running/html/heading.html',
        'webui_test/running/html/report.html',
        'webui_test/running/html/stylesheet.html',
        'webui_test/running/html/template.html'
    ]
)