from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi.responses import FileResponse
import subprocess
import os
import uuid
import asyncio
import sys
import shutil
import platform
from concurrent.futures import ThreadPoolExecutor
import threading
import json
import traceback


executor = ThreadPoolExecutor(max_workers=5)
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

python_executable = shutil.which("python") or sys.executable
if not python_executable:
    print("CRITICAL ERROR: Python executable not found!")
    sys.exit(1)

app = FastAPI(
    title="Selenium Test Runner API",
    description="API to run Selenium test cases in a specified order.",
    version="1.0.0"
)
running_tasks = {}
test_run_results = {}
test_run_status = {}

DEFAULT_HISTORY_DIR = os.path.join(os.getcwd(), "test_history")
HISTORY_DIR = os.environ.get("TEST_HISTORY_PATH", DEFAULT_HISTORY_DIR)
HISTORY_FILE = os.path.join(HISTORY_DIR, "runs.json")

DEFAULT_REPORTS_DIR = os.path.join(os.getcwd(), "reports")
REPORTS_DIR = os.environ.get("REPORTS_PATH", DEFAULT_REPORTS_DIR)

DEFAULT_LOGS_DIR = os.path.join(os.getcwd(), "logs")
LOGS_DIR = os.environ.get("LOGS_PATH", DEFAULT_LOGS_DIR)

class TestRunRequest(BaseModel):
    test_files: list[str]
    release_version: str = ""
    server_name: str = ""
    run_on_url: str = ""
    username_login: str = ""
    password_login: str = ""
    one_app: Optional[str] = None
    browser: Optional[str] = None
    headless: Optional[str] = None
    customer_code: str = ""
    customer_code_corporate: str = ""
    username_approve: str = ""
    password_approve: str = ""
    username_reverse: str = ""
    password_reverse: str = ""
    report_name: str = ""
    f8_config: Optional[str] = None
    debug_mode: Optional[str] = None
    hour_to_run: Optional[int] = None
    minute_to_run: Optional[int] = None
    username_login_other_branch: Optional[str] = None
    password_login_other_branch: Optional[str] = None
    username_approve_other_branch: Optional[str] = None
    password_approve_other_branch: Optional[str] = None
    username_reverse_other_branch: Optional[str] = None
    password_reverse_other_branch: Optional[str] = None
    app_name: Optional[str] = None
    folder_name: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.on_event("startup")
async def startup_event():
    """Event called when FastAPI application starts."""
    if not os.path.exists(HISTORY_DIR):
        try:
            os.makedirs(HISTORY_DIR)
            print(f"'test_history' folder created: {HISTORY_DIR}")
        except OSError as e:
            print(f"Error creating 'test_history' folder {HISTORY_DIR}: {e}", file=sys.stderr)
            
    if not os.path.exists(REPORTS_DIR):
        try:
            os.makedirs(REPORTS_DIR)
            print(f"'reports' folder created: {REPORTS_DIR}")
        except OSError as e:
            print(f"Error creating 'reports' folder {REPORTS_DIR}: {e}", file=sys.stderr)

    if not os.path.exists(LOGS_DIR):
        try:
            os.makedirs(LOGS_DIR)
            print(f"'logs' folder created: {LOGS_DIR}")
        except OSError as e:
            print(f"Error creating 'logs' folder {LOGS_DIR}: {e}", file=sys.stderr)

    load_test_history()

def run_tests_in_background(run_id: str, request_data: TestRunRequest):
    """
    Run script run_by_api.py in a child process.
    """
    print(f"[{run_id}] Starting test run in background...")
    test_run_status[run_id] = "running"
    save_test_history()
    
    # From main.py, relative path is tests/run_by_api.py
    script_path = os.path.join(os.path.dirname(__file__), 'tests', 'run_by_api.py')
    
    command = [sys.executable, script_path]

    command.extend(["--release-version", request_data.release_version])
    command.extend(["--server-name", request_data.server_name])
    command.extend(["--run-on-url", request_data.run_on_url])
    command.extend(["--username-login", request_data.username_login])
    command.extend(["--password-login", request_data.password_login])
    if request_data.one_app is not None:
        command.extend(["--one-app", request_data.one_app])
    if request_data.browser is not None:
        command.extend(["--browser", request_data.browser])
    if request_data.headless is not None:
        command.extend(["--headless", str(request_data.headless).lower()])
    command.extend(["--customer-code", request_data.customer_code])
    command.extend(["--customer-code-corporate", request_data.customer_code_corporate])
    command.extend(["--username-approve", request_data.username_approve])
    command.extend(["--password-approve", request_data.password_approve])
    command.extend(["--username-reverse", request_data.username_reverse])
    command.extend(["--password-reverse", request_data.password_reverse])
    if request_data.test_files:
        command.extend(["--test-files-order", ",".join(request_data.test_files)])
    command.extend(["--report-name", request_data.report_name])
    if request_data.debug_mode is not None:
        command.extend(["--debug-mode", str(request_data.debug_mode).lower()])
    if request_data.hour_to_run is not None:
        command.extend(["--hour-to-run", str(request_data.hour_to_run)])
    if request_data.minute_to_run is not None:
        command.extend(["--minute-to-run", str(request_data.minute_to_run)])
    if request_data.username_login_other_branch is not None:
        command.extend(["--username-login-other-branch", request_data.username_login_other_branch])
    if request_data.password_login_other_branch is not None:
        command.extend(["--password-login-other-branch", request_data.password_login_other_branch])
    if request_data.username_approve_other_branch is not None:
        command.extend(["--username-approve-other-branch", request_data.username_approve_other_branch])
    if request_data.password_approve_other_branch is not None:
        command.extend(["--password-approve-other-branch", request_data.password_approve_other_branch])
    if request_data.username_reverse_other_branch is not None:
        command.extend(["--username-reverse-other-branch", request_data.username_reverse_other_branch])
    if request_data.password_reverse_other_branch is not None:
        command.extend(["--password-reverse-other-branch", request_data.password_reverse_other_branch])
    if request_data.f8_config is not None:
        command.extend(["--f8-config", request_data.f8_config])
    if request_data.app_name is not None:
        command.extend(["--app-name", request_data.app_name])
    if request_data.folder_name is not None:
        command.extend(["--folder-name", request_data.folder_name])

    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        # output_log = process.stdout + "\n" + process.stderr
        output_log = process.stderr
        # output_log = ""
        
        parsed_result = {}
        try:
            json_output_line = [line for line in process.stdout.splitlines() if line.strip().startswith('{') and line.strip().endswith('}')]
            if json_output_line:
                parsed_result = json.loads(json_output_line[-1])
        except json.JSONDecodeError:
            print(f"[{run_id}] Warning: Could not decode JSON from subprocess output. Output: {process.stdout}", file=sys.stderr)
            pass

        status = "completed" if process.returncode == 0 else "failed"
        # status = "completed"
        passed = parsed_result.get("passed", False)

        test_run_results[run_id] = {
            "status": status,
            "passed": passed,
            "output_log": output_log,
            **parsed_result
        }
        test_run_status[run_id] = status
        print(f"[{run_id}] Test run finished with status: {status}. Passed: {passed}")

    except Exception as e:
        full_traceback = traceback.format_exc()
        test_run_results[run_id] = {
            "status": "failed",
            "passed": False,
            "output_log": f"An unexpected error occurred while running subprocess: {e}\n{full_traceback}"
        }
        test_run_status[run_id] = "failed"
        print(f"[{run_id}] Exception while trying to run subprocess: {e}\n{full_traceback}")
    finally:
        save_test_history()

@app.post("/run_test")
async def run_test(request: TestRunRequest):
    """
    Triggers Selenium test cases to run in the specified order via `run_by_api.py`. Test run in background.
    """
    run_id = str(uuid.uuid4())

    test_run_results[run_id] = {
        "timestamp": datetime.now().isoformat(),
        "status": "pending",
        "passed": False,
        "request_data": request.dict()
    }
    test_run_status[run_id] = "pending"
    save_test_history()

    threading.Thread(
        target=run_tests_in_background,
        args=(run_id, request)
    ).start()

    return {"message": "Test run initiated", "run_id": run_id, "status": "running"}

@app.get("/get_test_status/{run_id}")
async def get_run_test_status(run_id: str):
    """
    Check status and get test results of run under folder.
    """
    status = test_run_status.get(run_id, "not_found")
    result = test_run_results.get(run_id, None)

    if status == "not_found":
        raise HTTPException(status_code=404, detail="Run ID not found.")
    
    return {"run_id": run_id, "status": status, "result": result}

def load_test_history():
    """Load history test from JSON file when application starts."""
    global test_run_results, test_run_status
    if not os.path.exists(HISTORY_DIR):
        try:
            os.makedirs(HISTORY_DIR)
            print(f"Created history directory: {HISTORY_DIR}")
        except OSError as e:
            print(f"Error creating history directory {HISTORY_DIR}: {e}", file=sys.stderr)
            return

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                test_run_results = loaded_data.get("results", {})
                test_run_status = loaded_data.get("status", {})
                print(f"Loaded {len(test_run_results)} test runs from {HISTORY_FILE}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {HISTORY_FILE}: {e}. Starting with empty history.", file=sys.stderr)
            backup_file = f"{HISTORY_FILE}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            try:
                shutil.copyfile(HISTORY_FILE, backup_file)
                print(f"Backed up corrupted history file to {backup_file}", file=sys.stderr)
            except Exception as copy_e:
                print(f"Error backing up corrupted file: {copy_e}", file=sys.stderr)
            test_run_results = {}
            test_run_status = {}
        except Exception as e:
            print(f"An unexpected error occurred while loading test history: {e}. Starting with empty history.", file=sys.stderr)
            test_run_results = {}
            test_run_status = {}
    else:
        print(f"No existing history file found at {HISTORY_FILE}. Starting with empty history.")

def save_test_history():
    """Save test history to JSON file."""
    if not os.path.exists(HISTORY_DIR):
        print(f"Cannot save history: directory {HISTORY_DIR} does not exist.", file=sys.stderr)
        return
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                "results": test_run_results,
                "status": test_run_status
            }, f, indent=4, ensure_ascii=False)
        print(f"Saved test history to {HISTORY_FILE}")
    except Exception as e:
        print(f"Error saving test history to {HISTORY_FILE}: {e}", file=sys.stderr)

@app.get("/test-history")
async def get_test_history():
    """
    Get all test history.
    """
    return test_run_results

@app.post("/clear-history")
async def clear_history():
    """
    Delete all test history (in memory and files).
    """
    global test_run_results, test_run_status
    test_run_results = {}
    test_run_status = {}
    save_test_history()
    return {"message": "Test history cleared."}

@app.get("/reports")
async def list_reports():
    """
    Returns a list of all available report file names in the reports directory.
    """
    try:
        if not os.path.exists(REPORTS_DIR):
            return {"message": "Report folder does not exist.", "reports": []}

        report_files = [f for f in os.listdir(REPORTS_DIR) if os.path.isfile(os.path.join(REPORTS_DIR, f))]
        report_files = sorted([f for f in report_files if f.endswith(('.html', '.xml'))])
        
        return {"reports": report_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while getting report list: {e}")

@app.get("/reports/download/{report_name}")
async def download_report(report_name: str):
    """
    Download a specific report by file name.
    """
    report_path = os.path.join(REPORTS_DIR, report_name)

    if not os.path.exists(report_path) or not os.path.isfile(report_path):
        raise HTTPException(status_code=404, detail=f"No report found: {report_name}")
    
    if not report_name.endswith(('.html', '.xml')):
         raise HTTPException(status_code=400, detail="Only supports downloading HTML or XML report files.")

    try:
        return FileResponse(path=report_path, filename=report_name, media_type="application/octet-stream")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading report '{report_name}': {e}")

@app.delete("/reports/clear_all")
async def clear_all_reports():
    """
    Delete all files in the reports folder.
    """
    if not os.path.exists(REPORTS_DIR):
        raise HTTPException(status_code=404, detail=f"The reports directory does not exist: {REPORTS_DIR}")

    try:
        for item in os.listdir(REPORTS_DIR):
            item_path = os.path.join(REPORTS_DIR, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        return {"message": f"All files and subfolders in '{REPORTS_DIR}' have been successfully deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while deleting all reports: {e}")

@app.get("/logs")
async def list_logs():
    """
    Returns a list of all log file names available in the logs directory.
    """
    try:
        if not os.path.exists(LOGS_DIR):
            return {"message": "The logs directory does not exist.", "logs": []}

        log_files = [f for f in os.listdir(LOGS_DIR) if os.path.isfile(os.path.join(LOGS_DIR, f))]
        log_files = sorted([f for f in log_files if f.endswith(('.log', '.txt'))])
        
        return {"logs": log_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting logs list: {e}")

@app.get("/logs/download/{log_name}")
async def download_log(log_name: str):
    """
    Download a specific log file by file name.
    """
    log_path = os.path.join(LOGS_DIR, log_name)

    if not os.path.exists(log_path) or not os.path.isfile(log_path):
        raise HTTPException(status_code=404, detail=f"Log file not found: {log_name}")
    
    if not log_name.endswith(('.log', '.txt')):
         raise HTTPException(status_code=400, detail="Only supports downloading log files (.log, .txt).")

    try:
        return FileResponse(path=log_path, filename=log_name, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading log file '{log_name}': {e}")

@app.delete("/logs/clear_all")
async def clear_all_logs():
    """
    Delete all files in the logs folder.
    """
    if not os.path.exists(LOGS_DIR):
        raise HTTPException(status_code=404, detail=f"The logs directory does not exist: {LOGS_DIR}")

    try:
        for item in os.listdir(LOGS_DIR):
            item_path = os.path.join(LOGS_DIR, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

        return {"message": f"All files and subdirectories in '{LOGS_DIR}' have been successfully deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error when deleting all logs: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
