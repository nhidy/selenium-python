import atexit
from webui_test.logging import log 
from time import sleep
import os
import sys
import tempfile
import shutil

from webui_test.running.config import BrowserConfig, WaitConfig
from selenium import webdriver
# from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import UnexpectedAlertPresentException, ElementNotVisibleException, MoveTargetOutOfBoundsException, WebDriverException, StaleElementReferenceException, NoAlertPresentException, NoSuchWindowException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_TEST_BROWSER=None
_TEMP_DATA_DIR=None

def start_browser():
    global _TEST_BROWSER, _TEMP_DATA_DIR
    log.info(f"Starting browser: '{BrowserConfig.name}'")
    if _TEST_BROWSER is None:
        # Chrome
        if BrowserConfig.name is None or BrowserConfig.name in ["chrome", "google chrome", "gc"]:
            chrome_options = ChromeOptions() 
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--incognito") 
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-clipboard-access")
            _TEMP_DATA_DIR = tempfile.mkdtemp(prefix="selenium_chrome_profile_")
            chrome_options.add_argument(f"--user-data-dir={_TEMP_DATA_DIR}")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.accept_insecure_certs=True
            if BrowserConfig.headless: 
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--headless=new')
                chrome_options.add_argument('--window-size=1920,1080')
            log.info(f"TEMP_DATA_DIR={_TEMP_DATA_DIR}")
            chrome_service = ChromeService()
            _TEST_BROWSER = webdriver.Chrome(service=chrome_service, options=chrome_options)
            # _TEST_BROWSER = webdriver.Chrome(options=chrome_options)

        # Firefox
        elif BrowserConfig.name in ['firefox', 'ff']:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--start-maximized')
            _TEMP_DATA_DIR = tempfile.mkdtemp(prefix="selenium_firefox_profile_")
            firefox_options.add_argument(f"--user-data-dir={_TEMP_DATA_DIR}")
            if BrowserConfig.headless: 
                firefox_options.add_argument('--headless')
            log.info(f"TEMP_DATA_DIR={_TEMP_DATA_DIR}")
            firefox_service = FirefoxService()
            _TEST_BROWSER = webdriver.Firefox(service=firefox_service, options=firefox_options)
            # _TEST_BROWSER = webdriver.Firefox(options=firefox_options)

        # Edge
        elif BrowserConfig.name in ['edge', 'ed']:
            edge_options = EdgeOptions()
            edge_options.add_argument('--start-maximized')
            edge_options.add_argument('--ignore-ssl-errors=yes')
            edge_options.add_argument('--ignore-certificate-errors')
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-extensions")
            edge_options.add_argument("--incognito") 
            edge_options.add_argument("--disable-dev-shm-usage")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--disable-infobars")  # Optional
            edge_options.add_argument("--disable-notifications")
            edge_options.add_argument("--disable-clipboard-access")
            _TEMP_DATA_DIR = tempfile.mkdtemp(prefix="selenium_edge_profile_")
            edge_options.add_argument(f"--user-data-dir={_TEMP_DATA_DIR}")
            edge_prefs = {
                "profile.default_content_setting_values.clipboard": 2
            }
            edge_options.add_experimental_option("prefs", edge_prefs)
            edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            edge_options.accept_insecure_certs=True
            if BrowserConfig.headless: 
                # edge_options.add_argument('--headless')
                edge_options.add_argument('--headless=new')
                edge_options.add_argument('--window-size=1920,1080')
            log.info(f"TEMP_DATA_DIR={_TEMP_DATA_DIR}")
            edge_service = EdgeService()
            _TEST_BROWSER = webdriver.Edge(service=edge_service, options=edge_options)
            # _TEST_BROWSER = webdriver.Edge(options=edge_options)
        else:
            if _TEMP_DATA_DIR and os.path.exists(_TEMP_DATA_DIR):
                shutil.rmtree(_TEMP_DATA_DIR)
            raise NameError("Not found '{}' browser".format(BrowserConfig.name))

    atexit.register(kill_browser)
    log.warn(f"Start driver: '{_TEST_BROWSER}'")
    _TEST_BROWSER.implicitly_wait(WaitConfig.timeout_implicitly)
    return _TEST_BROWSER

def kill_browser():
    global _TEST_BROWSER, _TEMP_DATA_DIR
    log.warn(f"Killing driver: '{_TEST_BROWSER}'")
    if _TEST_BROWSER is not None:
        _TEST_BROWSER.quit()
        _TEST_BROWSER = None
    if _TEMP_DATA_DIR and os.path.exists(_TEMP_DATA_DIR):
        try:
            shutil.rmtree(_TEMP_DATA_DIR)
            print(f"Cleaned up temporary user data directory: {_TEMP_DATA_DIR}")
        except Exception as e:
            print(f"Error cleaning up temporary directory {_TEMP_DATA_DIR}: {e}", file=sys.stderr)

def get_driver():
    global _TEST_BROWSER
    if _TEST_BROWSER is not None:
        return _TEST_BROWSER
    else:
        return

def restart_driver():
    global _TEST_BROWSER
    log.warn("Restarting driver...")
    kill_browser()
    wait()
    _TEST_BROWSER = start_browser()
    log.warn("Driver restarted.")
    return _TEST_BROWSER

def wait(seconds=1):
    sleep(seconds)