from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
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

class TaskStatus(BaseModel):
    task_id: str
    status: str
    stdout: Optional[str] = None
    exec_status: Optional[str] = None
    return_code: Optional[int] = None

class TestConfig(BaseModel):
    release_version: str = ""
    server_name: str = ""
    run_on_url: str = ""
    username_login: str = ""
    password_login: str = ""
    one_app: str = ""
    browser: str = ""
    headless: str = ""
    customer_code: str = ""
    username_approve: str = ""
    password_approve: str = ""
    username_reverse: str = ""
    password_reverse: str = ""
    test_suite: str = ""
    report_name: str = ""
    debug_mode: Optional[str] = None
    hour_to_run: Optional[int] = None
    minute_to_run: Optional[int] = None
    username_login_other_branch: Optional[str] = None
    password_login_other_branch: Optional[str] = None
    username_approve_other_branch: Optional[str] = None
    password_approve_other_branch: Optional[str] = None
    username_reverse_other_branch: Optional[str] = None
    password_reverse_other_branch: Optional[str] = None

class TestRunRequest(BaseModel):
    test_files: list[str]
    release_version: str = ""
    server_name: str = ""
    run_on_url: str = ""
    username_login: str = ""
    password_login: str = ""
    one_app: str = ""
    browser: str = ""
    headless: str = ""
    customer_code: str = ""
    username_approve: str = ""
    password_approve: str = ""
    username_reverse: str = ""
    password_reverse: str = ""
    report_name: str = ""
    debug_mode: Optional[str] = None
    hour_to_run: Optional[int] = None
    minute_to_run: Optional[int] = None
    username_login_other_branch: Optional[str] = None
    password_login_other_branch: Optional[str] = None
    username_approve_other_branch: Optional[str] = None
    password_approve_other_branch: Optional[str] = None
    username_reverse_other_branch: Optional[str] = None
    password_reverse_other_branch: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.on_event("startup")
async def startup_event():
    """Event called when FastAPI application starts."""
    load_test_history()

@app.post("/run_file")
async def run_file(config: TestConfig):
    task_id = str(uuid.uuid4())
    test_script_path = os.path.join(os.path.dirname(__file__), "tests", "run_file_by_api.py")
    test_script_dir = os.path.join(os.path.dirname(__file__), "tests")

    if not os.path.exists(test_script_path):
        raise HTTPException(status_code=404, detail=f"Test script not found at {test_script_path}")

    running_tasks[task_id] = {
        "task_id": task_id,
        "status": "running",
        "stdout": None,
        "exec_status": None,
        "return_code": None
    }

    asyncio.create_task(
        _run_script_in_background(task_id, test_script_path, test_script_dir, config)
    )

    return {"message": "Test script started in background", "task_id": task_id}

@app.get("/run_file_status/{task_id}", response_model=TaskStatus)
async def get_run_file_status(task_id: str):
    task_info = running_tasks.get(task_id)
    if not task_info:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return TaskStatus(**task_info)

async def _run_script_in_background(task_id: str, script_path: str, cwd_path: str, config: TestConfig):
    loop = asyncio.get_event_loop()

    try:
        cli_args = []
        for key, value in config.model_dump().items():
            if value is not None and value != "":
                cli_args.append(f"--{key.replace('_', '-')}")
                cli_args.append(str(value))

        command = [python_executable, script_path] + cli_args

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            executor,
            lambda: subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                cwd=cwd_path
            )
        )

        stdout_str = result.stdout if result.stdout else ""
        stderr_str = result.stderr if result.stderr else ""

        running_tasks[task_id].update({
            "status": "completed" if result.returncode == 0 else "failed",
            "stdout": stdout_str,
            "exec_status": stderr_str,
            "return_code": result.returncode
        })

    except Exception as e:
        error_details = traceback.format_exc()

        running_tasks[task_id].update({
            "status": "failed",
            "stdout": running_tasks[task_id].get("stdout"),
            "exec_status": f"Error during execution: {error_details}",
            "return_code": -1
        })

def run_tests_in_background(run_id: str, request_data: TestRunRequest):
    """
    Run script run_folder_by_api.py in a child process.
    """
    print(f"[{run_id}] Starting test run in background...")
    test_run_status[run_id] = "running"
    save_test_history()
    
    # From main.py, relative path is tests/run_folder_by_api.py
    script_path = os.path.join(os.path.dirname(__file__), 'tests', 'run_folder_by_api.py')
    
    command = [sys.executable, script_path]

    command.extend(["--release-version", request_data.release_version])
    command.extend(["--server-name", request_data.server_name])
    command.extend(["--run-on-url", request_data.run_on_url])
    command.extend(["--username-login", request_data.username_login])
    command.extend(["--password-login", request_data.password_login])
    command.extend(["--one-app", request_data.one_app])
    command.extend(["--browser", request_data.browser])
    command.extend(["--headless", str(request_data.headless).lower()])
    command.extend(["--customer-code", request_data.customer_code])
    command.extend(["--username-approve", request_data.username_approve])
    command.extend(["--password-approve", request_data.password_approve])
    command.extend(["--username-reverse", request_data.username_reverse])
    command.extend(["--password-reverse", request_data.password_reverse])
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

    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False)
        output_log = process.stdout + "\n" + process.stderr
        
        parsed_result = {}
        try:
            json_output_line = [line for line in process.stdout.splitlines() if line.strip().startswith('{') and line.strip().endswith('}')]
            if json_output_line:
                parsed_result = json.loads(json_output_line[-1])
        except json.JSONDecodeError:
            print(f"[{run_id}] Warning: Could not decode JSON from subprocess output. Output: {process.stdout}", file=sys.stderr)
            pass

        status = "completed" if process.returncode == 0 else "failed"
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

@app.post("/run_folder")
async def run_folder(request: TestRunRequest):
    """
    Triggers Selenium test cases to run in the specified order via `run_folder_by_api.py`. Test run in background.
    """
    if not request.test_files:
        raise HTTPException(status_code=400, detail="No test files specified in 'test_files' field.")

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

@app.get("/run_folder_status/{run_id}")
async def get_run_folder_status(run_id: str):
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
            # Quan trọng: Nếu không tạo được thư mục, không thể lưu lịch sử
            # Bạn có thể muốn thoát ứng dụng hoặc chuyển sang chế độ không ghi.
            return # Thoát hàm nếu không tạo được thư mục

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

if __name__ == "__main__":
    # if platform.system() == "Windows":
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")

    import uvicorn
    # Load lịch sử khi chạy ứng dụng (nếu chưa được load bởi @app.on_event)
    # Tuy nhiên, @app.on_event("startup") là cách tốt hơn cho ứng dụng FastAPI thực tế
    uvicorn.run(app, host="0.0.0.0", port=8000)
