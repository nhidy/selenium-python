import os
import time
import unittest
from xmlrunner import XMLTestRunner
import inspect
from webui_test.logging import log
from webui_test.running.HTMLTestRunner import HTMLTestRunner
from webui_test.running.config import BrowserConfig

webui_test_str = "WebUI Test"

def main(path=None, browser=None, report=None, title="WebUI Test Report", description="WEBUI Test Case Execution", debug=False, rerun=0, save_last_run=False, timeout=10, xmlrunner=False, headless=False, suite_to_run=None):
        #   window_size="1920,1080"):
    suits = None
    if suite_to_run:
        # Nếu suite_to_run được cung cấp, sử dụng nó trực tiếp
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

    # if debug is False: 
    #     for filename in os.listdir(os.getcwd()): 
    #         if filename == "reports": 
    #             break
    #     else: 
    #         os.mkdir(os.path.join(os.getcwd(), "reports"))

    #     if report is None:
    #         now = time.strftime("%Y_%m_%d_%H_%M_%S")
    #         if xmlrunner is False:
    #             report = os.path.join(os.getcwd(), "reports", now + "_result.html")
    #             BrowserConfig.report_path = report 
    #         else: 
    #             report = os.path.join(os.getcwd(), "reports", now + ".xml")
    #             BrowserConfig.report_path = report 
    #     else: 
    #         report = os.path.join(os.getcwd(), "reports", report)
    
    #     with(open(report, 'wb')) as fp:
    #         log.info(webui_test_str)
    #         if xmlrunner is False: 
    #             runner = HTMLTestRunner(stream=fp, title=title, description=description, browser=BrowserConfig.name)
    #             runner.run(suits, rerun=rerun, save_last_run=save_last_run)
    #         else: 
    #             runner = XMLTestRunner(output=fp)
    #             runner.run(suits) 
    #     log.info("generated html file: file:///{}".format(report))
    
    # else: 
    #     runner = unittest.TextTestRunner(verbosity=2) 
    #     log.info("A run the test in debug mode without generating HTML report!")
    #     log.info(webui_test_str)
    #     runner.run(suits)


    if not debug:
        reports_dir = os.path.join(os.getcwd(), "reports")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        final_report_path = None
        if report is None:
            now = time.strftime("%Y_%m_%d_%H_%M_%S")
            if not xmlrunner:
                final_report_path = os.path.join(reports_dir, now + "_result.html")
            else:
                final_report_path = os.path.join(reports_dir, now + ".xml")
        else:
            final_report_path = os.path.join(reports_dir, report)

        BrowserConfig.report_path = final_report_path
        log.info(f"Report will be generated at: {final_report_path}")

        with(open(final_report_path, 'wb')) as fp:
            log.info(webui_test_str)
            if not xmlrunner:
                runner = HTMLTestRunner(stream=fp, title=title, description=description, browser=BrowserConfig.name)
                result = runner.run(suits, rerun=rerun, save_last_run=save_last_run)
            else:
                runner = XMLTestRunner(output=fp)
                result = runner.run(suits)
        
        log.info("Generated html file: file:///{}".format(final_report_path))

    else:
        runner = unittest.TextTestRunner(verbosity=2)
        log.info("Running the test in debug mode without generating HTML report!")
        log.info(webui_test_str)
        result = runner.run(suits)

    # Trả về kết quả của lần chạy test
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