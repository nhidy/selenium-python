import webui_test
from datetime import datetime
import sys
import argparse
import traceback
import os
import unittest
import importlib.util
import json

def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'y', 'true', 't'):
        return True
    elif value.lower() in ('no', 'n', 'false', 'f'):
        return False
    else:
        if value is None or value.lower() == "null" or value == "":
            return False
        raise argparse.ArgumentTypeError(f"Boolean value expected (true/false, Y/N, etc.), got '{value}'")

def run_test_suite_wrapper(config_data, test_files_order_list):
    env_vars = os.environ.copy()
    for key, value in config_data.items():
        env_vars[f"TEST_CONFIG_{key.upper()}"] = str(value) if value is not None else ""
    os.environ.update(env_vars)

    headless = config_data.get("headless", False)
    browser = config_data.get("browser", "chrome")
    report_name = config_data.get("report_name", "")
    debug_mode = config_data.get("debug_mode", False)
    release_version = config_data.get("release_version", "")
    server_name = config_data.get("server_name", "")

    # From run_folder_by_api.py, relative path is ../tests/test_dir/shwebank_run_by_api/
    test_case_base_dir = os.path.join(os.path.dirname(__file__), 'test_dir', 'shwebank_run_by_api')

    combined_suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    print(f"Loading tests from directory: {test_case_base_dir}")
    print(f"Test files order requested: {test_files_order_list}")

    for test_file_name in test_files_order_list:
        module_path = os.path.join(test_case_base_dir, f"{test_file_name}.py")
        
        if not os.path.exists(module_path):
            print(f"Warning: Test file '{module_path}' not found. Skipping.", file=sys.stderr)
            continue

        try:
            spec = importlib.util.spec_from_file_location(test_file_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            combined_suite.addTests(loader.loadTestsFromModule(module))
            print(f"Successfully added tests from {test_file_name}.py to suite.")
        except ImportError as e:
            print(f"Error importing module '{test_file_name}' from '{module_path}': {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred while loading '{test_file_name}' from '{module_path}': {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

    if not combined_suite.countTestCases():
        print("No test cases found to run.", file=sys.stderr)
        return {"passed": False, "total_tests": 0, "message": "No test cases found to run."}

    report_filename = f"{release_version}_{server_name}_{report_name}_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html"

    try:
        test_run_result = webui_test.main(
            suite_to_run=combined_suite,
            browser=browser,
            debug=debug_mode,
            headless=headless,
            report=report_filename,
            title=f"{release_version}-{server_name}-Test Report",
            description="Automated WEBUI Test Case Execution"
        )
        print("All tests completed successfully.", file=sys.stdout)
        return test_run_result

    except Exception as e:
        print(f"An unexpected error occurred during test execution in run_folder_by_api.py: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"passed": False, "total_tests": 0, "message": f"Fatal error: {e}"}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run UI tests with provided configuration.")

    parser.add_argument("--release-version", type=str, default="", help="Release version to run tests.")
    parser.add_argument("--server-name", type=str, default="", help="Sever name to run tests on.")
    parser.add_argument("--run-on-url", type=str, default="", help="URL to run tests on.")
    parser.add_argument("--username-login", type=str, default="", help="Username for login.")
    parser.add_argument("--password-login", type=str, default="", help="Password for login.")
    parser.add_argument("--one-app", type=str, default="", help="One app parameter.")
    parser.add_argument("--browser", type=str, default="chrome", help="Browser to use (e.g., chrome, firefox).")
    parser.add_argument("--headless", type=str_to_bool, default=False, help="Run browser in headless mode (true/false, Y/N).")
    parser.add_argument("--customer-code", type=str, default="", help="Customer code.")
    parser.add_argument("--username-approve", type=str, default="", help="Username for approval.")
    parser.add_argument("--password-approve", type=str, default="", help="Password for approval.")
    parser.add_argument("--username-reverse", type=str, default="", help="Username for reverse.")
    parser.add_argument("--password-reverse", type=str, default="", help="Password for reverse.")
    parser.add_argument("--report-name", type=str, default="report", help="Specific report name.")
    parser.add_argument("--debug-mode", type=str_to_bool, default=False, help="Debug mode setting (optional (true/false, Y/N)).")
    parser.add_argument("--hour-to-run", type=int, default=None, help="Specific hour to run the test (optional int).")
    parser.add_argument("--minute-to-run", type=int, default=None, help="Specific minute to run the test (optional int).")
    parser.add_argument("--username-login-other-branch", type=str, default=None, help="Username other branch for login.")
    parser.add_argument("--password-login-other-branch", type=str, default=None, help="Password other branch for login.")
    parser.add_argument("--username-approve-other-branch", type=str, default=None, help="Username other branch for approval.")
    parser.add_argument("--password-approve-other-branch", type=str, default=None, help="Password other branch for approval.")
    parser.add_argument("--username-reverse-other-branch", type=str, default=None, help="Username other branch for reverse.")
    parser.add_argument("--password-reverse-other-branch", type=str, default=None, help="Password other branch for reverse.")
    parser.add_argument("--test-files-order", type=str, default="",  help="Comma-separated list of test file names (without .py extension) in the desired execution order. Example: 'test_login,test_create_user'")

    args = parser.parse_args()

    config_data = {
        "release_version": args.release_version,
        "server_name": args.server_name,
        "run_on_url": args.run_on_url,
        "username_login": args.username_login,
        "password_login": args.password_login,
        "one_app": args.one_app,
        "browser": args.browser,
        "headless": args.headless,
        "customer_code": args.customer_code,
        "username_approve": args.username_approve,
        "password_approve": args.password_approve,
        "username_reverse": args.username_reverse,
        "password_reverse": args.password_reverse,
        "report_name": args.report_name,
        "debug_mode": args.debug_mode,
        "hour_to_run": args.hour_to_run,
        "minute_to_run": args.minute_to_run,
        "username_login_other_branch": args.username_login_other_branch,
        "password_login_other_branch": args.password_login_other_branch,
        "username_approve_other_branch": args.username_approve_other_branch,
        "password_approve_other_branch": args.password_approve_other_branch,
        "username_reverse_other_branch": args.username_reverse_other_branch,
        "password_reverse_other_branch": args.password_reverse_other_branch
    }

    test_files_order_list = []
    if args.test_files_order:
        test_files_order_list = [f.strip() for f in args.test_files_order.split(',') if f.strip()]

    try:
        final_result = run_test_suite_wrapper(config_data, test_files_order_list)
        print(json.dumps(final_result))
        sys.exit(0 if final_result.get("passed", False) else 1)
    except Exception as e:
        print(f"An unexpected error occurred in run_folder_by_api.py's main block: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({"passed": False, "message": f"Fatal error: {e}"}))
        sys.exit(1)