import os
import sys
import time
import unittest
import inspect
from webui_test.logging import log
from webui_test.running.HTMLTestRunner import HTMLTestRunner
from webui_test.running.config import BrowserConfig, F8Config

webui_test_str = "WebUI Test"

DEFAULT_REPORTS_DIR = os.path.join(os.getcwd(), "reports")
REPORTS_DIR = os.environ.get("REPORTS_PATH", DEFAULT_REPORTS_DIR)

if not os.path.exists(REPORTS_DIR):
    try:
        os.makedirs(REPORTS_DIR)
        print(f"Created reports directory: {REPORTS_DIR}")
    except OSError as e:
        print(f"Error create reports directory {REPORTS_DIR}: {e}", file=sys.stderr)

def main(path=None, browser=None, report=None, title="WebUI Test Report", description="WEBUI Test Case Execution", debug=False, rerun=0, save_last_run=False, headless=False, suite_to_run=None, f8_config=None, app_name=None):
        #   window_size="1920,1080"):
    if f8_config is not None:
        F8Config.view_mode = f8_config
    else:
        F8Config.view_mode = "S"
    if app_name is not None:
        BrowserConfig.app_name = app_name
    else:
        BrowserConfig.app_name = "Shwebank"
    log.debug(f"HEADLESS MODE: '{headless}'")
    log.debug(f"F8CONFIG.VIEW_MODE: '{F8Config.view_mode}'")
    log.debug(f"BROWSERCONFIG.APP_NAME: '{BrowserConfig.app_name}'")
    suits = None
    if suite_to_run:
        suits = suite_to_run
        log.info("Running provided TestSuite.")
    elif path is None: 
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_dir = os.path.dirname(os.path.abspath(ins.filename))
        file_path = ins.filename 
        if "\\" in file_path: 
            this_file = file_path.split("\\")[-1]
        elif "/" in file_path: 
            this_file = file_path.split("/")[-1]
        else: 
            this_file = file_path 
        suits = unittest.defaultTestLoader.discover(file_dir, this_file)
        log.info(f"Discovered tests from current file: {this_file}")
    else:
        if len(path) > 3: 
            if path[-3:] == ".py": 
                BrowserConfig.run_file = True
                if "/" in path: 
                    path_list = path.split("/")
                    path_dir = path.replace(path_list[-1], "")
                    suits = unittest.defaultTestLoader.discover(path_dir, pattern=path_list[-1])
                else: 
                    suits = unittest.defaultTestLoader.discover(os.getcwd(), pattern=path)
                log.info(f"Discovered tests from single file: {path}")
            else: 
                BrowserConfig.run_file = False
                suits = unittest.defaultTestLoader.discover(path)
                log.info(f"Discovered tests from directory: {path}")
        else: 
            suits = unittest.defaultTestLoader.discover(path)

    if suits is None or suits.countTestCases() == 0:
        log.error("No test cases found to run.")
        return False

    if browser is None: 
        BrowserConfig.name = "chrome"
    else: 
        BrowserConfig.name = browser 
    BrowserConfig.headless = headless
    # BrowserConfig.window_size = window_size

    if not debug:
        final_report_path = None
        if report is None:
            now = time.strftime("%Y_%m_%d_%H_%M_%S")
            final_report_path = os.path.join(REPORTS_DIR, now + "_result.html")
        else:
            final_report_path = os.path.join(REPORTS_DIR, report)

        BrowserConfig.report_path = final_report_path
        log.info(f"Report will be generated at: {final_report_path}")

        with(open(final_report_path, 'wb')) as fp:
            log.info(webui_test_str)
            runner = HTMLTestRunner(stream=fp, title=title, description=description, browser=BrowserConfig.name)
            result = runner.run(suits, rerun=rerun, save_last_run=save_last_run)
        
        log.info("Generated html file: file:///{}".format(final_report_path))

    else:
        runner = unittest.TextTestRunner(verbosity=2)
        log.info("Running the test in debug mode without generating HTML report!")
        log.info(webui_test_str)
        result = runner.run(suits)

    return {
        "total_tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "successful": result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped),
        "passed": result.wasSuccessful(),
        "report_path": final_report_path if not debug else None
    }

if __name__ == '__main__':
    main()