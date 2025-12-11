import webui_test
from datetime import datetime
import sys
import argparse
import traceback
import os
import unittest
import importlib.util
import json

sys.stdout.reconfigure(encoding='utf-8')

def str_to_bool(value):
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if str(value).lower() in ('yes', 'y', 'true', 't'):
        return True
    elif str(value).lower() in ('no', 'n', 'false', 'f'):
        return False
    else:
        if str(value).lower() == "null" or str(value) == "":
            return False
        raise argparse.ArgumentTypeError(f"Boolean value expected (true/false, Y/N, etc.), got '{value}'")

def parse_test_files(config_data):
    """Parse test_files from config data, handling both list and string formats."""
    test_files_order_list = []
    test_files = config_data.get("test_files")

    if test_files:
        if isinstance(test_files, list):
            test_files_order_list = [f.strip() for f in test_files if f.strip()]
        elif isinstance(test_files, str):
            test_files_order_list = [f.strip() for f in test_files.split(',') if f.strip()]
    
    return test_files_order_list

def run_test_suite_wrapper(config_data, test_files_order_list):
    env_vars = os.environ.copy()
    for key, value in config_data.items():
        env_vars[f"TEST_CONFIG_{key.upper()}"] = str(value) if value is not None else ""
    os.environ.update(env_vars)

    headless = str_to_bool(config_data.get("headless")) or False
    browser = config_data.get("browser") or "chrome"
    report_name = config_data.get("report_name") or ""
    release_version = config_data.get("release_version") or ""
    server_name = config_data.get("server_name") or ""
    f8_config = config_data.get("f8_config") or "S"
    app_name = config_data.get("app_name") or "Shwebank"
    folder_name = config_data.get("folder_name") or "shwebank_run_by_api"

    print(f"Folder containing the test script: {folder_name}")
    test_case_base_dir = os.path.join(os.path.dirname(__file__), 'test_dir', folder_name)

    combined_suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    print(f"Loading tests from directory: {test_case_base_dir}")
    print(f"Test files order requested: {test_files_order_list}")

    if not test_files_order_list:
        print("[INFO] No specific test file name provided. Exploring all tests in default directory.")
        try:
            final_suite = loader.discover(
                start_dir=test_case_base_dir,
                pattern='test_*.py',
                top_level_dir=test_case_base_dir
            )
            combined_suite.addTests(final_suite)
            print(f"Explored {final_suite.countTestCases()} test for default run.")
        except Exception as e:
            print(f"Error when exploring test in default mode from {test_case_base_dir}: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return {"passed": False, "total": 0, "failures": 1, "errors": 0, "skipped": 0, "log": f"Error while exploring default test: {e}"}
    else:
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

    report_filename = f"{release_version}-{server_name}-{report_name}_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html"

    try:
        test_run_result = webui_test.main(
            suite_to_run=combined_suite,
            browser=browser,
            headless=headless,
            report=report_filename,
            title=f"{release_version}-{server_name}-Test Report",
            description="Automated WEBUI Test Case Execution",
            f8_config=f8_config,
            app_name=app_name
        )
        print("All tests completed successfully.", file=sys.stdout)
        return test_run_result

    except Exception as e:
        print(f"An unexpected error occurred during test execution in run_by_api.py: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"passed": False, "total_tests": 0, "message": f"Fatal error: {e}"}

def load_config_from_file(config_file_path):
    """Load configuration from a JSON file."""
    try:
        with open(config_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading config file: {e}", file=sys.stderr)
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run UI tests with provided configuration.")
    parser.add_argument("--config-file", type=str, required=True, help="Path to the JSON configuration file.")
    args = parser.parse_args()

    try:
        config_data = load_config_from_file(args.config_file)
    except Exception:
        sys.exit(1)

    test_files_order_list = parse_test_files(config_data)

    try:
        final_result = run_test_suite_wrapper(config_data, test_files_order_list)
        print(json.dumps(final_result))
        sys.exit(0 if final_result.get("passed", False) else 1)
    except Exception as e:
        print(f"An unexpected error occurred in run_by_api.py's main block: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({"passed": False, "message": f"Fatal error: {e}"}))
        sys.exit(1)