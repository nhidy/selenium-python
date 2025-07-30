import webui_test
from datetime import datetime
import sys
import argparse
import traceback
import os

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

def run_test_suite(config_data):
    env_vars = os.environ.copy()
    for key, value in config_data.items():
        env_vars[f"TEST_CONFIG_{key.upper()}"] = str(value) if value is not None else ""
    os.environ.update(env_vars)

    return config_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run UI tests with provided configuration.")

    parser.add_argument("--release-version", type=str, default="", help="Release version to run tests.")
    parser.add_argument("--server-name", type=str, default="", help="Sever name to run tests on.")
    parser.add_argument("--run-on-url", type=str, default="", help="URL to run tests on.")
    parser.add_argument("--username-login", type=str, default="", help="Username for login.")
    parser.add_argument("--password-login", type=str, default="", help="Password for login.")
    parser.add_argument("--one-app", type=str, default="", help="One app parameter.")
    parser.add_argument("--browser", type=str, default="", help="Browser to use (e.g., chrome, firefox).")
    parser.add_argument("--headless", type=str_to_bool, default=False, help="Run browser in headless mode (true/false, Y/N).")
    parser.add_argument("--customer-code", type=str, default="", help="Customer code.")
    parser.add_argument("--username-approve", type=str, default="", help="Username for approval.")
    parser.add_argument("--password-approve", type=str, default="", help="Password for approval.")
    parser.add_argument("--username-reverse", type=str, default="", help="Username for reverse.")
    parser.add_argument("--password-reverse", type=str, default="", help="Password for reverse.")
    parser.add_argument("--test-suite", type=str, default="", help="Specific test suite to run.")
    parser.add_argument("--report-name", type=str, default="", help="Specific report name.")
    parser.add_argument("--debug-mode", type=str_to_bool, default=False, help="Debug mode setting (optional (true/false, Y/N)).")
    parser.add_argument("--hour-to-run", type=int, default=None, help="Specific hour to run the test (optional int).")
    parser.add_argument("--minute-to-run", type=int, default=None, help="Specific minute to run the test (optional int).")
    parser.add_argument("--username-login-other-branch", type=str, default=None, help="Username other branch for login.")
    parser.add_argument("--password-login-other-branch", type=str, default=None, help="Password other branch for login.")
    parser.add_argument("--username-approve-other-branch", type=str, default=None, help="Username other branch for approval.")
    parser.add_argument("--password-approve-other-branch", type=str, default=None, help="Password other branch for approval.")
    parser.add_argument("--username-reverse-other-branch", type=str, default=None, help="Username other branch for reverse.")
    parser.add_argument("--password-reverse-other-branch", type=str, default=None, help="Password other branch for reverse.")

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
        "test_suite": args.test_suite,
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
    try:
        processed_config = run_test_suite(config_data)
        headless = processed_config["headless"]
        browser = processed_config["browser"]
        test_suite = processed_config["test_suite"]
        report_name = processed_config["report_name"]
        debug_mode = processed_config["debug_mode"]
        hour_to_run = processed_config["hour_to_run"]
        minute_to_run = processed_config["minute_to_run"]
        release_version = processed_config["release_version"]
        server_name = processed_config["server_name"]

        path_test_suite = f"./test_dir/shwebank_run_by_api/{test_suite}.py"
        webui_test.main(path=path_test_suite, browser=browser, debug=debug_mode, headless=headless, report=f"{release_version}_{server_name}_{report_name}_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
        print("All tests completed successfully.", file=sys.stdout)
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred in run_file_by_api.py's main block: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)