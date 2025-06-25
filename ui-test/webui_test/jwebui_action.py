import atexit
from webui_test.logging import log 
from time import sleep


from webui_test.running.config import BrowserConfig, WaitConfig
from selenium import webdriver
# from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import UnexpectedAlertPresentException, ElementNotVisibleException, MoveTargetOutOfBoundsException, WebDriverException, StaleElementReferenceException, NoAlertPresentException, NoSuchWindowException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_TEST_BROWSER=None

def start_browser():
    global _TEST_BROWSER
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
            chrome_options.add_argument("--disable-infobars")  # Optional
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-clipboard-access")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.accept_insecure_certs=True
            if BrowserConfig.headless: 
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--headless=new')
                chrome_options.add_argument('--window-size=1920,1080')
            _TEST_BROWSER = webdriver.Chrome(options=chrome_options)

        # Firefox
        elif BrowserConfig.name in ['firefox', 'ff']:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--start-maximized')
            if BrowserConfig.headless: 
                firefox_options.add_argument('--headless')
            _TEST_BROWSER = webdriver.Firefox(options=firefox_options)

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
            edge_prefs = {
                "profile.default_content_setting_values.clipboard": 2  # Disable clipboard access
            }
            edge_options.add_experimental_option("prefs", edge_prefs)
            edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            edge_options.accept_insecure_certs=True
            if BrowserConfig.headless: 
                # edge_options.add_argument('--headless')
                edge_options.add_argument('--headless=new')  # sử dụng chế độ headless mới
                edge_options.add_argument('--window-size=1920,1080')
            _TEST_BROWSER = webdriver.Edge(options=edge_options)
        else:
            raise NameError("Not found '{}' browser".format(BrowserConfig.name))

    atexit.register(kill_browser)
    log.warn(f"Start driver: '{_TEST_BROWSER}'")
    _TEST_BROWSER.implicitly_wait(WaitConfig.timeout_implicitly)
    return _TEST_BROWSER

def kill_browser():
    global _TEST_BROWSER
    log.warn(f"Killing driver: '{_TEST_BROWSER}'")
    if _TEST_BROWSER is not None:
        _TEST_BROWSER.quit()
        _TEST_BROWSER = None

def get_driver():
    global _TEST_BROWSER
    log.warn(f"Get driver: '{_TEST_BROWSER}'")
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
    log.warn(f"'_TEST_BROWSER' at 'restart_driver' method: '{_TEST_BROWSER}'")
    return _TEST_BROWSER

def wait(seconds=1):
    sleep(seconds)