import os
import sys
import time
from datetime import datetime
import inspect
import platform
import logging.handlers
from colorama import Fore, Style

DEFAULT_LOGS_DIR = os.path.join(os.getcwd(), "logs")
LOGS_DIR = os.environ.get("LOGS_PATH", DEFAULT_LOGS_DIR)

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
    print(f"Created logs directory: {LOGS_DIR}")

if os.path.exists(LOGS_DIR) is False:
    os.mkdir(LOGS_DIR)

now_time = str(datetime.now().strftime('%d%m%Y_%H%M%S'))
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, now_time + ".log"), encoding='utf-8')
print(f"The log file is created at: {os.path.join(LOGS_DIR, now_time + '.log')}")

_logger = logging.getLogger('webui_test')
_logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler(sys.stdout)

if platform.system().lower() == "windows": 
    _logger.addHandler(file_handler)
    _logger.addHandler(_handler) 
else: 
    _logger.addHandler(file_handler)
    _logger.addHandler(_handler) 

def debug(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(now + " [DEBUG] " + str(msg))

def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # _logger.info(Fore.GREEN + now + " [INFO] " + str(msg) + Style.RESET_ALL)
    _logger.info(now + " [INFO] " + str(msg))

def error(msg): 
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # _logger.error(Fore.RED + now + " [ERROR] " + str(msg) + Style.RESET_ALL)
    _logger.error(now + " [ERROR] " + str(msg))

def warn(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # _logger.warning(Fore.YELLOW + now + " [WARNING] " + str(msg) + Style.RESET_ALL)
    _logger.warning(now + " [WARNING] " + str(msg))

def _print(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # _logger.debug(Fore.BLUE + now + " [PRINT] " + str(msg) + Style.RESET_ALL)
    _logger.debug(now + " [PRINT] " + str(msg))

def set_level(level):
    _logger.setLevel(level)

def set_level_to_debug():
    _logger.setLevel(logging.DEBUG)

def set_level_to_info():
    _logger.setLevel(logging.INFO)

def set_level_to_warn():
    _logger.setLevel(logging.WARN)

def set_level_to_error():
    _logger.setLevel(logging.ERROR)