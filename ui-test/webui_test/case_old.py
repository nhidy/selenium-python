from inspect import cleandoc
import os
import unittest
import sys
from time import sleep
from webui_test.jwebui_action import *
from webui_test.logging import log

from webui_test.running.config import BrowserConfig, WaitConfig
from webui_test.jweb_excel import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException

_TEST_BROWSER=None
test_suite_stopped=False

def setUpModule():
    global _TEST_BROWSER
    if _TEST_BROWSER is None:
        _TEST_BROWSER = start_browser()

def tearDownModule():
    global _TEST_BROWSER
    if _TEST_BROWSER is not None:
        kill_browser()
        _TEST_BROWSER = None

class TestCase(unittest.TestCase):
    def start_class(self):
        self.driver = get_driver()
        pass

    def end_class(self):
        self.driver = get_driver()
        pass

    @classmethod
    def setUpClass(cls):
        global _TEST_BROWSER
        if BrowserConfig.run_file:
            log.warn('Run file')
            if _TEST_BROWSER is None: 
                cls.driver = start_browser()
                _TEST_BROWSER = cls.driver
                cls.started_browser = True
            else: 
                cls.driver = _TEST_BROWSER
                cls.started_browser = False
            cls().go_to(cls().get_url())
            cls().wait_page_login()
            cls().start_class()
        else:
            log.warn('Run somthing else')
            cls.driver = _TEST_BROWSER 
            cls.started_browser = False
            cls().start_class()

    @classmethod
    def tearDownClass(cls):
        global _TEST_BROWSER
        if BrowserConfig.run_file:
            cls().end_class()
            if cls.started_browser:
                if _TEST_BROWSER is not None:
                    kill_browser()
        else:
            cls().end_class()
            kill_browser()

    def start(self):
        self.driver = get_driver()
        # log.debug("2. Go to 'start' method")
        pass

    def end(self):
        self.driver = get_driver()
        # log.debug("4. Go to 'end' method")
        pass

    def stop(self):
        global test_suite_stopped
        test_suite_stopped = True
        log.error("The data used for testing is incorrect.")
        # log.debug("Go to 'stop' method")

    def setUp(self):
        self.driver = get_driver()
        # log.debug("1. Go to 'setUp' method")
        if test_suite_stopped:
            # log.debug(f"Go to 'skipTest'")
            self.skipTest('Skipping because the data used for testing is incorrect.')
        self.start()

    def tearDown(self):
        self.driver = get_driver()
        # log.debug("3. Go to 'tearDown' method")
        self.end()

    def get_url(self):
        # log.debug("Go to 'get_url' method")
        return

    def go_to(self, url):
        BrowserConfig.url_env = url
        if self.driver:
            self.driver.get(url)
            log.debug(f"Go to 'go_to' method, url: {url}")

    def wait(self, seconds=1):
        sleep(seconds)

    def restart_browser(self):
        global _TEST_BROWSER
        type(self).driver = restart_driver()
        _TEST_BROWSER = type(self).driver
        self.driver = get_driver()
        self.go_to(BrowserConfig.url_env)
        self.wait_page_login()

    def screen_size(self):
        width = self.driver.get_window_size()['width']
        if width > 996:
            return 'desktop'
        elif width > 768:
            return 'desktop_small'
        elif width > 575:
            return 'tablet'
        elif width > 350:
            return 'mobile'
        else:
            return 'mobile_small'

    def take_screenshot(self, path):
        result = self.driver.get_screenshot_as_file(path)
        if result:
            log.info(f"Take screenshot '{path}'.")
        else:
            log.error('Take screenshot failed.')

    def get_value_excel(self, sheet, column, row, filename=None):
        return get_value_from_excel(sheet, column, row, filename)

    def open_file_excel(self, sheet, url_file_name=None):
        return read_file_excel(sheet_name=sheet, url_file_name=url_file_name)

    def get_value_excel_cell(self, data_file, column, row):
        return get_value_cell_excel(data_file, column, row)

    def write_value_to_excel(self, new_value, sheet_name, column, row, url_file_name=None):
        return write_value_to_excel(new_value, sheet_name, column, row, url_file_name=url_file_name)

# ================================= Using Selenium 4.x =================================
# ================= xpath =================
    def wait_for_element_visibility_by_xpath(self, xpath, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            log.info(f"Element with xpath '{xpath}' visible.")
            return element  # The element is visible
        except TimeoutException:
            log.warn(f"The element with xpath '{xpath}' was NOT visible.")
            return None

    def wait_for_element_enabled_by_xpath(self, xpath, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            log.info(f"Element with xpath '{xpath}' enabled.")
            return element  # The element is enabled
        except TimeoutException:
            log.warn(f"The element with xpath '{xpath}' was NOT enabled.")
            return None

    def wait_until_element_disappears_by_xpath(self, xpath, max_wait_time=WaitConfig.timeout_explicit):
        try:
            is_invisible = WebDriverWait(self.driver, max_wait_time).until(
                EC.invisibility_of_element_located((By.XPATH, xpath))
            )
            if is_invisible:
                log.info(f"Element with xpath '{xpath}' disappeared.")
                return True  # Return True if the element disappears
        except TimeoutException:
            log.warn(f"Element with xpath '{xpath}' did NOT disappear.")
            return False

    def wait_for_element_unobscured_by_xpath(self, xpath, timeout=WaitConfig.timeout_explicit):
        # Get the element you want to interact with
        element = self.wait_for_element_visibility_by_xpath(xpath, timeout=timeout)
        if element is None:
            return None
        if BrowserConfig.name in ['firefox', 'ff']:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            location = element.location_once_scrolled_into_view
            self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            is_obscured = self.driver.execute_script("""
                var element = arguments[0];
                var rect = element.getBoundingClientRect();
                var x = rect.left + (rect.width / 2);
                var y = rect.top + (rect.height / 2);
                return document.elementFromPoint(x, y) !== element;
            """, element)
            if is_obscured:
                log.warn(f"Element with xpath {xpath} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                log.info(f"Element with xpath '{xpath}' is no longer obscured.")
                break
        if not is_obscured:
            log.info("Element is unobstructed.")
            return element
        else:
            log.warn(f"Element with xpath '{xpath}' is still obscured.")
            return None

    def wait_for_element_by_xpath(self, xpath):
        # Get the element you want to interact with
        element = self.driver.find_element(By.XPATH, xpath)
        if element is None:
            return None
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            is_obscured = self.driver.execute_script("""
                var element = arguments[0];
                var rect = element.getBoundingClientRect();
                var x = rect.left + (rect.width / 2);
                var y = rect.top + (rect.height / 2);
                return document.elementFromPoint(x, y) !== element;
            """, element)
            if is_obscured:
                log.warn(f"Element with xpath {xpath} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                log.info(f"Element with xpath '{xpath}' is no longer obscured.")
                break
        if not is_obscured:
            log.info("Element is unobstructed.")
            return element
        else:
            log.warn(f"Element with xpath '{xpath}' is still obscured.")
            return None

    def is_displayed_by_xpath(self, xpath):
        try:
            is_displayed = self.driver.find_element(By.XPATH, xpath).is_displayed()
            if is_displayed:
                return True
            else:
                return False
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check element displayed by xpath failed. Exception: {e}")

# ================= css =================
    def wait_for_element_visibility_by_css(self, css_selector, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            log.info(f"Element with CSS selector '{css_selector}' visible.")
            return element  # The element is visible
        except TimeoutException:
            log.warn(f"Element with CSS selector '{css_selector}' was NOT visible.")
            return None

    def wait_for_element_enabled_by_css(self, css_selector, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            log.info(f"Element with CSS selector '{css_selector}' enabled.")
            return element  # The element is enabled
        except TimeoutException:
            log.warn(f"Element with CSS selector '{css_selector}' was NOT enabled.")
            return None

    def wait_until_element_disappears_by_css(self, css_selector, max_wait_time=WaitConfig.timeout_explicit):
        try:
            is_invisible = WebDriverWait(self.driver, max_wait_time).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            if is_invisible:
                log.info(f"Element with CSS selector '{css_selector}' disappeared.")
                return True  # Return True if the element disappears
        except TimeoutException:
            log.warn(f"Element with CSS selector '{css_selector}' did NOT disappear.")
            return False

    def wait_for_element_unobscured_by_css(self, css_selector, timeout=WaitConfig.timeout_explicit):
        # Get the element you want to interact with
        element = self.wait_for_element_visibility_by_css(css_selector, timeout=timeout)
        if element is None:
            return None
        if BrowserConfig.name in ['firefox', 'ff']:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            location = element.location_once_scrolled_into_view
            self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            is_obscured = self.driver.execute_script("""
                var element = arguments[0];
                var rect = element.getBoundingClientRect();
                var x = rect.left + (rect.width / 2);
                var y = rect.top + (rect.height / 2);
                return document.elementFromPoint(x, y) !== element;
            """, element)
            if is_obscured:
                log.warn(f"Element with CSS selector {css_selector} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                log.info(f"Element with CSS selector '{css_selector}' is no longer obscured.")
                break
        if not is_obscured:
            log.info("Element is unobstructed.")
            return element # return True
        else:
            log.warn(f"Element with CSS selector '{css_selector}' is still obscured.")
            return None # return False

    def wait_for_element_by_css(self, css_selector):
        # Get the element you want to interact with
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        if element is None:
            return None
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            is_obscured = self.driver.execute_script("""
                var element = arguments[0];
                var rect = element.getBoundingClientRect();
                var x = rect.left + (rect.width / 2);
                var y = rect.top + (rect.height / 2);
                return document.elementFromPoint(x, y) !== element;
            """, element)
            if is_obscured:
                log.warn(f"Element with css_selector {css_selector} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                log.info(f"Element with css_selector '{css_selector}' is no longer obscured.")
                break
        if not is_obscured:
            log.info("Element is unobstructed.")
            return element
        else:
            log.warn(f"Element with css_selector '{css_selector}' is still obscured.")
            return None

    def is_displayed_by_css(self, css_selector):
        try:
            is_displayed = self.driver.find_element(By.CSS_SELECTOR, css_selector).is_displayed()
            if is_displayed:
                return True
            else:
                return False
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check element displayed by css failed. Exception: {e}")

# ================= other =================
    def wait_loading(self, max_wait_time=60):
        loading_xpath = "//div[contains(@class, 'malibu-desktop-uFormLoading')]"
        log.warn(f"Start wait_loading.")
        if self.wait_until_element_disappears_by_xpath(loading_xpath, max_wait_time):
            log.warn("Loading icon element has disappeared.")
        else:
            log.error(f"Loading icon element did NOT disappear.")

    def wait_process_bar_loading(self, max_wait_time=60):
        loading_xpath = "//div[contains(@class, 'malibu-desktop-uLoading')]"
        log.warn(f"Start wait_process_bar_loading.")
        if self.wait_until_element_disappears_by_xpath(loading_xpath, max_wait_time):
            log.warn("Loading bar element has disappeared.")
        else:
            log.error(f"Loading bar element did NOT disappear.")

    def wait_app_loading(self, max_wait_time=60):
        loading_xpath = "//div[contains(text(),'Login successfully')]"
        log.warn(f"Start wait_app_loading.")
        if self.wait_until_element_disappears_by_xpath(loading_xpath, max_wait_time):
            log.warn(f"Loading app element has disappeared.")
        else:
            log.error(f"Loading app element did NOT disappear.")

    def wait_page_login(self, max_wait_time=WaitConfig.timeout_explicit):
        if self.driver.title == 'Loading...':
            time_number = 1
            while time_number <= max_wait_time:
                # self.wait()
                self.wait_process_bar_loading()
                # Refresh the page every 5 seconds
                if time_number % 5 == 0:
                    self.driver.refresh()
                # Check if the title has changed to 'Login'
                if self.driver.title == 'Login':
                    login_button_xpath = "//span[@class='malibu-desktop-uLogin_button-title' and text()='Login']"
                    self.wait_for_element_unobscured_by_xpath(login_button_xpath)
                    break
                time_number += 1
            else:
                log.warn(f"Login page did NOT load within {max_wait_time} seconds.")

    def key_escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()

    def key_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()

    def common(self, xpath=None, css=None, method=None, action=None, value=None, clear_text=None, need_tab=None, need_enter=None, info=None, error=None, warn=None, timeout=WaitConfig.timeout_explicit):
        """
        Performs a common interaction with a web element based on provided locators and actions.

        Args:
            xpath (str, optional): XPath locator for the element.
            css (str, optional): CSS selector for the element.
            method (str, optional): Waiting method for the element.
                Possible values: 'unobscured', 'visibility', 'enabled'.
            action (str, optional): Action to perform on the element.
                Possible values: 'send_keys', 'click', 'get_text', 'get_value'.
            value (str, optional): Value to send to the element when action is 'send_keys'.
            clear_text (str, optional): Flag to clear the text of the element before sending keys.
                Possible value: 'Y'.
            need_tab (str, optional): Flag to send a TAB key press after sending keys.
                Possible value: 'Y'.
            need_enter (str, optional): Flag to send an ENTER key press after sending keys.
                Possible value: 'Y'.
            info (str, optional): Information message to log upon successful interaction.
            error (str, optional): Error message to log if the element is not found.
            warn (str, optional): Warning message to log if the element is not found.
            timeout (int, optional): Explicit wait timeout in seconds.
                Defaults to WaitConfig.timeout_explicit.

        Returns:
            Returns the text or value of the element if action is 'get_text' or 'get_value', otherwise returns None.
        """
        def get_element():
            if xpath:
                if method == 'unobscured':
                    return self.wait_for_element_unobscured_by_xpath(xpath, timeout)
                if method == 'visibility':
                    return self.wait_for_element_visibility_by_xpath(xpath, timeout)
                if method == 'enabled':
                    return self.wait_for_element_enabled_by_xpath(xpath, timeout)
                if method == 'find':
                    return self.wait_for_element_by_xpath(xpath)
            elif css:
                if method == 'unobscured':
                    return self.wait_for_element_unobscured_by_css(css, timeout)
                if method == 'visibility':
                    return self.wait_for_element_visibility_by_css(css, timeout)
                if method == 'enabled':
                    return self.wait_for_element_enabled_by_css(css, timeout)
                if method == 'find':
                    return self.wait_for_element_by_css(css)
            return None
        element = get_element()
        if element is not None:
            if action == 'send_keys':
                if clear_text == 'Y':
                    self.clear_text(element)
                element.send_keys(value)
                if need_tab == 'Y':
                    element.send_keys(Keys.TAB)
                if need_enter == 'Y':
                    element.send_keys(Keys.ENTER)
                if info:
                    log.info(info)
            elif action == 'click':
                element.click()
                if info:
                    log.info(info)
            elif action == 'get_text':
                if info:
                    log.info(info)
                return element.text
            elif action == 'get_value':
                if info:
                    log.info(info)
                return element.get_attribute('value')
        else:
            if error:
                log.error(error)
            if warn:
                log.warn(warn)
            return None

# ================= handle button =================
    def wait_for_button_available(self, button_name):
        button_name_xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        # button_name_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        try:
            button_element = self.wait_for_element_unobscured_by_xpath(button_name_xpath)
            if button_element is None:
                log.warn(f"'{button_name}' button NOT found.")
            else:
                log.info(f"'{button_name}' button available.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"'{button_name_xpath}' button NOT available. Exception: {e}")

    def click_button(self, button_name):
        button_name_xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        # button_name_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        self.common(xpath=button_name_xpath, method='unobscured', action='click', info=f"Clicked on '{button_name}' button.", error=f"Click on '{button_name_xpath}' button failed.")

    def click_button_in_popup(self, button_name):
        button_name_xpath = f"//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        self.common(xpath=button_name_xpath, method='unobscured', action='click', info=f"Clicked on '{button_name}' button.", error=f"Click on '{button_name_xpath}' button failed.")

    def click_button_in_tab(self, button_name):
        # button_name_xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//div[contains(@class,'malibu-desktop-uFormTab-content') and @style='opacity: 1;']//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        button_name_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//div[contains(@class,'malibu-desktop-uFormTab-content') and @style='opacity: 1;']//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='{button_name}']"
        self.common(xpath=button_name_xpath, method='unobscured', action='click', info=f"Clicked on '{button_name}' button.", error=f"Click on '{button_name_xpath}' button failed.")

    def click_radio_button(self, radio_button_name):
        radio_button_name_xpath = f"//div[@class='malibu-desktop-uRadioButton-title' and text()='{radio_button_name}']"
        self.common(xpath=radio_button_name_xpath, method='unobscured', action='click', info=f"Clicked on '{radio_button_name}' radio button.", error=f"Click on '{radio_button_name_xpath}' radio button failed.")

    def assert_button_disable(self, button_name):
        button_name_xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//span[@class='malibu-desktop-uButton-title' and text()='{button_name}']/parent::div/parent::div[contains(@class,'disable')]"
        # button_name_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//span[@class='malibu-desktop-uButton-title' and text()='{button_name}']/parent::div/parent::div[contains(@class,'disable')]"
        try:
            button = self.wait_for_element_visibility_by_xpath(button_name_xpath)
            self.assertTrue(self.check_disable(button), f"The '{button_name}' button not disable.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check disable '{button_name_xpath}' button failed. Exception: {e}")
            self.assertTrue(False, f"Check disable '{button_name}' button failed.")

    def click_icon(self, icon):
        icon_xpath = f"//div[@class='malibu-desktop-uInput-icon']/i[@class='material-icons-outlined' and text()='{icon}']"
        self.common(xpath=icon_xpath, method='visibility', action='click', info="Clicked icon.", error=f"Click icon '{icon}' failed.")

    def scroll_down(self, pixels=1000):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_up(self, pixels=1000):
        self.driver.execute_script(f"window.scrollBy(0, -{pixels});")

    def switch_to_core_banking(self):
        for handle in self.driver.window_handles: # Iterate over all open windows
            self.driver.switch_to.window(handle)
            if 'Core Banking' in self.driver.title: # Check if the current window is 'Core Banking'
                return  # Stop once we've switched to 'Core Banking'
        # If no window has 'Core Banking' in its title, you can raise an exception or handle the case
        raise Exception("No window with title 'Core Banking' found")

    def close_voucher(self):
        core_banking_window = None # Store the window handle of the 'Core Banking' window, if found
        # Iterate over all open windows
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if 'Core Banking' in self.driver.title: # Check if the current window is 'Core Banking'
                core_banking_window = handle  # Save this handle to avoid closing it
            else:
                self.driver.close() # Close all windows that are not 'Core Banking'
        if core_banking_window: # Switch back to 'Core Banking' window if it's found
            self.driver.switch_to.window(core_banking_window)

    def click_clear_search(self):
        clear_search_xpath = "//div[@class='malibu-desktop-uHeaderMoreOption-search-clear']/i"
        try:
            # Try to find the element, return None if not found
            clear_search_element = self.driver.find_element(By.XPATH, clear_search_xpath)
            # If element exists, wait until it is unobscured and then click
            if clear_search_element:
                self.common(xpath=clear_search_xpath, method='unobscured', action='click', info='Clicked clear search icon at header.')
            else:
                log.warn("Clear search icon at header not found.")
        except NoSuchElementException:
            log.warn("Clear search icon does not exist.")

    def open_fo(self, transaction_code, transaction_name):
        transaction_name = str(transaction_name).strip()
        self.click_clear_search()
        search_xpath = "//input[contains(@placeholder,'Search here or Use')]"
        self.common(xpath=search_xpath, method='unobscured', action='send_keys', value=transaction_code)
        option_xpath = f"//div[@class='malibu-desktop-uHeaderMoreOption-search-content-tab_function']/div/div/li//span[contains(text(),'{transaction_name}')]"
        self.common(xpath=option_xpath, method='unobscured', action='click', info=f"Opened '{transaction_code}' transaction.")

    def scroll_to_element(self, element):
        if element is None:
            log.error(f"Can NOT scroll to element '{element}'.")
            return False
        if BrowserConfig.name in ['firefox', 'ff']:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            log.info(f"Can scroll to element '{element}' in firefox browser.")
            return True
        else:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            location = element.location_once_scrolled_into_view
            self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            log.info(f"Can scroll to element '{element}' in other browser.")
            return True

    def scroll_to_top_page(self):
        element = self.driver.find_element(By.TAG_NAME, 'body')
        if element is None:
            log.error(f"Can NOT scroll to top page.")
            return False
        if BrowserConfig.name in ['firefox', 'ff']:
            # self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)
            element.send_keys(Keys.HOME)
            log.info(f"Can scroll to top page in firefox browser.")
            return True
        else:
            # actions = ActionChains(self.driver)
            # actions.move_to_element(element).perform()
            element.send_keys(Keys.HOME)
            log.info(f"Can scroll to top page in other browser.")
            return True

    def scroll_to_bottom_page(self):
        element = self.driver.find_element(By.TAG_NAME, 'body')
        if element is None:
            log.error(f"Can NOT scroll to bottom page.")
            return False
        if BrowserConfig.name in ['firefox', 'ff']:
            # self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)
            element.send_keys(Keys.END)
            log.info(f"Can scroll to bottom page in firefox browser.")
            return True
        else:
            # actions = ActionChains(self.driver)
            # actions.move_to_element(element).perform()
            element.send_keys(Keys.END)
            log.info(f"Can scroll to bottom page in other browser.")
            return True

# ================= handle lookup =================
    def lookup_data(self, title, column_name, value, use_search="Y"):
        icon_xpath = f"//legend[@title='{title}']/parent::fieldset/following-sibling::div[@class='malibu-desktop-uInput-icon']/i"
        self.common(xpath=icon_xpath, method='unobscured', action='click')
        self.wait_loading()
        table_xpath ="//div[@class='malibu-desktop-uModal-background' and not(@style='display: none;')]//div[@class='malibu-desktop-uModal-content-content']//table[@class='malibu-desktop-uTable-info']"
        if use_search == "Y":
            # 1. click icon search
            icon_search_xpath = f"{table_xpath}/thead/tr/th/div/div/span[text()='{column_name}']/following-sibling::div/span"
            self.common(xpath=icon_search_xpath, method='unobscured', action='click')
            self.wait_loading()
            # 2. enter value for search
            input_search_xpath = f"{table_xpath}/thead/tr/th/div/div/span[text()='{column_name}']/parent::div/parent::div/following-sibling::input"
            self.common(xpath=input_search_xpath, method='unobscured', action='send_keys', value=value)
        # 3. click choose value
        action_xpath = f"{table_xpath}/tbody/tr/td[@data-title='{column_name}']/div[text()='{value}']/parent::td/preceding-sibling::td/div/i"
        self.common(xpath=action_xpath, method='unobscured', action='click', error='Lookup data failed.')
        self.wait_loading()

    def write_search_table_column(self, text, into, index=0, css='malibu-desktop-uTable-info', press_right=0):
        # screen_type = screen_size()
        # if screen_type == 'desktop' or screen_type == 'desktop_small' or screen_type == 'tablet' :	
        #     css = css
        # else:
        #     css = 'malibu-mobile-uTable-info'
        # table = self.get_tables_with_css(css)[index]
        # heads = table.find_elements(By.XPATH, './thead/tr/th')
        # for i in range(len(heads)):
        #     caption = heads[i].find_elements(By.XPATH, './/*[contains(text(), "{}")]'.format(into))
        #     if len(caption) > 0:
        #         # find if input already show or not
        #         if press_right > 0 :
        #             click(table)
        #             self.wait()
        #             tab_count = 1
        #             while (tab_count <= press_right):
        #                 press(ARROW_RIGHT)
        #                 tab_count = tab_count + 1

        #         input = heads[i].find_elements(By.XPATH, './/input[contains(@class, "show")]')
        #         if len(input) == 0:
                    
        #             # find search icon then click 
        #             span = heads[i].find_elements(By.XPATH, './/*[contains(text(), "search")]')
        #             if len(span) > 0:
        #                 click(span[0])
        #         input = heads[i].find_elements(By.XPATH, './/input')
        #         input[0].send_keys(text)
                
                return

# ================= handle notification =================
    def get_text_notification(self, timeout=None):
        if timeout is None:
            timeout=WaitConfig.timeout_explicit
        message_xpath = "//div[@class='malibu-desktop-uNotification-title']"
        return self.common(xpath=message_xpath, method='visibility', action='get_text', info=f"Get text from notification success.", error=f"Get text from notification failed.", timeout=timeout)

    def click_close_notification(self):
        close_xpath = "//div[@class='malibu-desktop-uNotification-close']/i"
        self.common(xpath=close_xpath, method='visibility', action='click', info=f"Closed notification.", warn=f"Close notification failed.")

    def assert_notification(self, expected_message=None):
        if expected_message is None: 
            raise AssertionError("The assertion message cannot be empty.")
        actual_message = self.get_text_notification()
        self.assertEqual(expected_message, actual_message)
        self.wait_loading()
        self.click_close_notification()

# ================= handle special functions =================
    def open_app(self, app_name):
        app_name_xpath = f"//div[@class='malibu-desktop-uChooseApp-item-title' and text()='{app_name}']"
        self.common(xpath=app_name_xpath, method='unobscured', action='click', info=f"Clicked on {app_name} button.", error=f"Click action in choose app {app_name_xpath} failed.")

    def login(self, username, password, one_app='N', app_name="Shwebank"):
        try:
            email_input = self.wait_for_element_visibility_by_css("input[placeholder='Enter your account name']")
            password_input = self.wait_for_element_visibility_by_css("input[placeholder='Enter your System password']")
            email_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            available_app_xpath = "//div[@class='malibu-desktop-uChooseApp-title']/div[text()='Available Applications']"
            self.wait_for_element_visibility_by_xpath(available_app_xpath)
            if one_app=='N':
                self.open_app(app_name)
            self.wait_app_loading()
            self.wait_process_bar_loading()
            search_xpath = "//input[contains(@placeholder,'Search here or Use')]"
            self.wait_for_element_unobscured_by_xpath(search_xpath)
            self.is_logged = True
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Login screen failed. Exception: {e}")

    def approve_in_popup(self, username, password, reason=None):
        try:
            self.assert_form_title_popup('Approve')
            self.wait_for_button_available('Accept')
            self.write_text_textarea_non_tab('User Name', username, clear_text='Y')
            self.wait_loading()
            self.write_text_textarea_non_tab('Password', password)
            self.wait_loading()
            if reason is not None:
                self.write_text_textarea_non_tab('Reason', reason, clear_text='Y')
            self.wait_loading()
            self.click_button('Accept')
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Approve in popup failed. Exception: {e}")

    def fo_approve_in_popup(self, username, password, reason=None):
        try:
            if self.get_text_form_title_popup(timeout=30) is not None:
                self.assert_form_title_popup('Approval Require')
                self.wait_for_button_available('Accept')
                self.write_text_textarea_non_tab('User Name', username, clear_text='Y')
                self.write_text_textarea_non_tab('Password', password)
                if reason is not None:
                    self.write_text_textarea_non_tab('Reason', reason, clear_text='Y')
                self.wait_loading()
                self.click_button('Accept')
            else:
                log.warn('This transaction does not require approval.')
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Approve in popup failed, in transaction screen. Exception: {e}")

    def logout(self):
        avatar_xpath = "//div[@class='malibu-desktop-uHeaderItemMoreOption-avatar-div']/div[@class='malibu-desktop-uHeaderItemMoreOption-avatar']"
        self.common(xpath=avatar_xpath, method='visibility', action='click')
        logout_xpath = "//span[@class='malibu-desktop-uHeaderItemMoreOption-span' and text()='Log out']"
        self.common(xpath=logout_xpath, method='visibility', action='click', info="Logout successful.", error="Logout failed.")

    def open_transaction_journal(self):
        self.click_menu('Front Office', 'Transaction Journal')

    def get_text_form_title_header_popup(self):
        title_xpath = "//div[@class='malibu-desktop-uModal-background' and not(@style='display: none;')]//div[@class='malibu-desktop-form-uModalHeader-header-title']"
        return self.common(xpath=title_xpath, method='visibility', action='get_text', error=f"Get text title header of popup failed.")

    def assert_form_title_header_popup(self, expected_title=None):
        if expected_title is None: 
            raise AssertionError("The assertion form title cannot be empty.")
        actual_title = self.get_text_form_title_header_popup()
        self.assertEqual(expected_title, actual_title)

    def get_text_form_title_popup(self, timeout=5):
        title_xpath = "//div[@class='malibu-desktop-uModal-content-content']/div/div[contains(@class,'malibu-desktop-uForm')]/div[@class='malibu-desktop-uForm-title']"
        return self.common(xpath=title_xpath, method='visibility', action='get_text', error=f"Get text title popup failed.", timeout=timeout)

    def assert_form_title_popup(self, expected_title=None):
        if expected_title is None: 
            raise AssertionError("The assertion form title cannot be empty.")
        actual_title = self.get_text_form_title_popup()
        self.assertEqual(expected_title, actual_title)

    def close_popup(self):
        xpath = "//div[@class='malibu-desktop-uModal-background' and not(@style='display: none;')]//div[@class='malibu-desktop-form-uModalHeader-header']/div[@class='malibu-desktop-form-uModalHeader-header-close']/i"
        # self.common(xpath=xpath, method='visibility', action='click', info=f"Clicked close popup.", error=f"Click close popup failed.")
        try:
            close_popup_element = self.driver.find_element(By.XPATH, xpath)
            if close_popup_element:
                self.common(xpath=xpath, method='visibility', action='click', info=f"Clicked close popup.", error=f"Click close popup failed.")
            else:
                log.warn("Close popup icon not found.")
        except NoSuchElementException:
            log.warn("Close popup icon does not exist.")

    def close_bank(self, username, password):
        try:
            self.click_menu('Administration', 'Bank Administration', 'Bank Open/close')
            self.wait_for_button_available('Close Bank')
            self.click_button('Close Bank')
            self.assert_form_title_popup('Approve')
            self.wait_for_button_available('Accept')
            self.write_text_textarea_non_tab('User Name', username, clear_text='Y')
            self.write_text_textarea_non_tab('Password', password, clear_text='Y')
            self.wait_loading()
            self.click_button('Accept')
            log.info(f"Closed bank.")
        except:
            log.error(f"Close bank failed.")

    def open_bank(self, username, password):
        try:
            self.click_menu('Administration', 'Bank Administration', 'Bank Open/close')
            self.wait_for_button_available('Open Bank')
            self.click_button('Open Bank')
            self.assert_form_title_popup('Approve')
            self.wait_for_button_available('Accept')
            self.write_text_textarea_non_tab('User Name', username, clear_text='Y')
            self.write_text_textarea_non_tab('Password', password, clear_text='Y')
            self.wait_loading()
            self.click_button('Accept')
            log.info(f"Opened bank.")
        except:
            log.error(f"Open bank failed.")

    def start_batch(self, username, password, day_to=None):
        try:
            self.click_menu('Job', 'Job Process')
            self.wait_for_button_available('Start')
            self.bo_click_tab('Step Summary')
            if day_to is not None:
                self.click_radio_button('Number Running')
                self.write_date_input_in_tab('To Date', day_to)
            self.click_button('Start')
            self.assert_form_title_popup('Approve')
            self.wait_for_button_available('Accept')
            self.write_text_textarea_non_tab('User Name', username, clear_text='Y')
            self.write_text_textarea_non_tab('Password', password, clear_text='Y')
            self.wait_loading()
            self.click_button('Accept')
            log.info(f"Started batch.")
        except:
            log.error(f"Start batch failed.")

    def get_batch_process(self):
        xpath_input = "//div[@class='O9_jobProcess-row-2']/div[@class='malibu-desktop-uProgressBar']/label/input[@class='malibu-desktop-uProgressBar-number-percent-input']"
        return self.get_text_by_xpath_input(xpath_input)

    def run_batch(self, username, password, day_to=None): 
        self.close_bank(username, password)
        self.start_batch(username, password, day_to)
        while True:
            self.wait(2)
            percent = self.get_batch_process()
            if percent == 100: 
                break
            # todo: add check if error occurs
        self.logout()
        self.login(username, password)

    def get_logged_branch_code(self):
        xpath = "//div[contains(@class,'malibu-desktop-uHeaderItemMoreOption-info')]//span[contains(@class,'malibu-desktop-uHeaderItemMoreOption-span')]/span/parent::span"
        element = self.wait_for_element_visibility_by_xpath(xpath)
        return element.text.split('|')[1].strip()

    def assert_search_not_found(self):
        not_found_text = "Data not found"
        self.assert_notification(not_found_text)

    def assert_search_injection(self):
        self.simple_search('`')
        self.assert_search_not_found()
        self.click_close_notification()
        
        self.simple_search('{')
        self.assert_search_not_found()
        self.click_close_notification()
        
        self.simple_search('}')
        self.assert_search_not_found()
        self.click_close_notification()

    def assert_element_enable(self, element):
        try:
            self.assertFalse(element.get_attribute('disabled'), "Element '{}' is not enabled".format(element))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_element_enable for element '{element}' failed. Exception: '{e}'")
    
    def assert_field_disable(self, element):
        try:
            self.assertTrue(element.get_attribute('disabled'), "Element '{}' is not disabled".format(element))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_field_disable for element '{element}' failed. Exception: '{e}'")

    def assert_checkbox_enable(self, element):
        try:
            css_class = element.get_attribute('class')
            self.assertTrue('disable' not in css_class, "Checkbox '{}' is not enabled".format(element))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_checkbox_enable for checkbox element '{element}' failed. Exception: '{e}'")

    def assert_checkbox_disable(self, element):
        try:
            css_class = element.get_attribute('class')
            self.assertTrue('disable' in css_class, "Checkbox {} is not disabled".format(element))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_checkbox_disable for checkbox element '{element}' failed. Exception: '{e}'")

    # chua hien thuc lai
    def ui_input_disabled(self, into = None, index = 0):
        # f = self.get_ui_input(into, index = index)
        # if f is not None: 
        #     return f.get_attribute('disabled') == 'true'
        # return False
        return ''

    # chua hien thuc lai
    def ui_textarea_disabled(into=None):
        # f = get_ui_textarea(into)
        # if f is not None: 
        #     return f.get_attribute('disabled') == 'true'
        # return False
        return ''

    # chua hien thuc lai
    def assert_field_ui_enable(self, elt, index = 0):
        # self.assertFalse(ui_input_disabled(elt, index = index), "Field '{}' is not enabled".format(elt))
        return ''

    # chua hien thuc lai
    def assert_field_ui_disable(self, elt, index = 0):
        # self.assertTrue(ui_input_disabled(elt, index = index), "Field '{}' is not disabled".format(elt))
        return ''

    # chua hien thuc lai
    def assert_field_textarea_disable(self, elt):
        # self.assertTrue(ui_textarea_disabled(elt), "Field '{}' is not disabled".format(elt))
        return ''

    # chua hien thuc lai
    def assert_field_textarea_enable(self, elt):
        # self.assertFalse(ui_input_disabled(elt), "Field '{}' is not enabled".format(elt))
        return ''

    # chua hien thuc lai
    def assert_field_label_require(self, field, below = None, to_right_of = None, to_left_of = None, above = None):
        # t = Text(field, below = below, to_right_of = to_right_of, to_left_of = to_left_of, above = above)
        # a = t.web_element.find_elements(By.XPATH, 'span')
        # if a is not None and len(a) > 0:
        #     spa = a[len(a)-1]
        #     self.assertTrue(len(spa.text) > 0 and spa.text[0] == '*', "Field {} miss asterisk".format(field))
        return ''

    # chua hien thuc lai
    def assert_field_label_not_require(self, field, below = None, to_right_of = None, to_left_of = None, above = None):
        # t = Text(field, below = below, to_right_of = to_right_of, to_left_of = to_left_of, above = above)
        # a = t.web_element.find_elements(By.XPATH, 'span')
        # if a is not None and len(a) > 0:
        #     spa = a[len(a)-1]
        #     self.assertFalse(len(spa.text) > 0 and spa.text[0] == '*', "Field {} have asterisk".format(field))
        return ''

    # chua hien thuc lai
    def assert_field_not_blank(self, field, below = None):
        # validation = 'Can not be blank'
        # self.assert_field_validation(field, validation = validation, below = below)
        return ''

    # chua hien thuc lai
    def assert_field_validation(self, field, validation = '', below = None):
        # t = Text("An error has occurred. Please try again")
        # errors = t.web_element.find_elements(By.XPATH, '../../../div[1]/div/ul/div')
        # msg = '{}: {}'.format(field, validation)
        # has_contain = False 
        # for error in errors: 
        #     print("error.text: ", error.text)
        #     if msg in error.text:
        #         has_contain = True 
        # self.assertTrue(has_contain)
        return ''

    # chua hien thuc lai
    def write_table_cell(self, text, caption, row, column, below = None, to_right_of = None, to_left_of = None, above = None): 
        # t = Text(caption, below = below, to_right_of = to_right_of, to_left_of = to_left_of, above = above)
        # table = t.web_element.find_element(By.XPATH, './..//table')
        # cell = self.get_table_cell(table, row, column)
        # if cell is not None:
        #     icon = cell.find_element(By.TAG_NAME, 'i')
        #     click(icon)
        #     field_input = cell.find_element(By.TAG_NAME, 'input')
        #     field_input.send_keys(Keys.CONTROL + "a")
        #     field_input.send_keys(Keys.BACKSPACE)
        #     field_input.send_keys(text)
        return ''

    # chua hien thuc lai
    def assert_field_text(self, field, text, below = None, to_right_of = None, to_left_of = None, above = None):
        # t = self.get_text(field, below = below, to_right_of = to_right_of, to_left_of = to_left_of, above = above)
        # self.assertTrue(t, text, "Field {} value is {}. Expected: {}".format(field, t, text))
        return ''

    def assert_table_length(self, expected):
        try:
            table_xpath = "//div[@class='malibu-desktop-uForm col-12' and not(@style='display: none;')]//tbody[@class='malibu-desktop-uTable-tbody']/tr[@class='']"
            table_element = self.driver.find_elements(By.XPATH, table_xpath)
            rows = len(table_element)
            self.assertTrue(rows == expected, f"Actual: '{rows}'. Expected: '{expected}'")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_table_length '{expected}' failed. Exception: '{e}'")

    def assert_table_data(self, column_name, index, expected):
        try:
            actual = self.get_text_table_data(column_name, index)
            self.assertEqual(actual, expected, "Data in column [{}] and row [{}] not equal. Actual: '{}'. Expected: '{}'".format(column_name, index, actual, expected))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_table_data for column '{column_name}' failed. Exception: '{e}'")

    def assert_status_table_data(self, column_name, index, expected):
        try:
            actual = self.get_status_table_data(column_name, index)
            self.assertEqual(actual, expected, "Data in column [{}] and row [{}] not equal. Actual: '{}'. Expected: '{}'".format(column_name, index, actual, expected))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_status_table_data for column '{column_name}' failed. Exception: '{e}'")

    def assert_total_fee_table_data(self, expected):
        try:
            actual = self.get_total_fee_table_data()
            self.assertEqual(actual, expected, "Data total fee in table fee not equal. Actual: '{}'. Expected: '{}'".format(actual, expected))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_total_fee_table_data failed. Exception: '{e}'")

    def assert_table_data_posting(self, posting_side, column_name, index, expected):
        try:
            actual = self.get_text_table_data_posting(posting_side, column_name, index)
            self.assertEqual(actual, expected, "Data in column [{}] and row [{}] at posting side [{}] not equal. Actual: '{}'. Expected: '{}'".format(column_name, index, posting_side, actual, expected))
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_table_data_posting for column '{column_name}' failed. Exception: '{e}'")

    def assert_search_results(self, expected):
        try:
            xpath = "//div[@class='malibu-desktop-uForm col-12' and not(@style='display: none;')]//div[@class='malibu-desktop-uPagination row']/div/span[@style]"
            element = self.wait_for_element_unobscured_by_xpath(xpath)
            actual = int(element.text.split()[1])
            self.assertEqual(actual, expected, f"Actual: '{actual}'. Expected: '{expected}'")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_search_results failed. Exception: '{e}'")

    def assert_field_signature(self, title):
        sign_icon_xpath = f"//div[contains(@class,'malibu-desktop-uOfGroup')]//legend[@title='{title}']/ancestor::div[contains(@class,'malibu-desktop-uOfGroup')]//div[contains(@class,'malibu-desktop-uButton-square-content')]/img"
        try:
            sign_icon_element = self.wait_for_element_unobscured_by_xpath(sign_icon_xpath)
            self.assertIsNotNone(sign_icon_element, f"Signature icon for field '{title}' is None, expected: signature icon existed.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Signature icon for field '{title}' not exist. Exception: '{e}'")

    def assert_error_message(self):
        expected = "An error has occurred. Please try again"
        xpath = "//div[@class='malibu-desktop-uFormNotify-span']"
        try:
            element = self.wait_for_element_unobscured_by_xpath(xpath)
            self.assertEqual(element.text, expected, "Form error message not show")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_error_message failed. Exception: '{e}'")

    def get_list_error_message(self):
        xpath = "//div[@id='content']/div/div[@class='malibu-desktop-uForm col-12']/div[contains(@class,'malibu-desktop-uForm-content')]/div[@class='malibu-desktop-uFormNotify']/div/ul[@class='malibu-desktop-uFormNotify-ul']/div/div[@class='malibu-desktop-uFormNotify-li']/li"
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            return elements
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_error_message failed. Exception: '{e}'")

    def assert_list_error_message(self, list_expected):
        try:
            elements = self.get_list_error_message()
            list_actual = []
            for element in elements:
                actual = element.get_attribute('innerText').split('\n')[0].strip()
                list_actual.append(actual)
            for expected in list_expected:
                self.assertIn(expected, list_actual, f"Missing message: {expected}.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_list_error_message failed. Exception: '{e}'")

    def get_list_error_message_multi(self, level_1):
        xpath = f"//div[@id='content']/div/div[@class='malibu-desktop-uForm col-12']/div[contains(@class,'malibu-desktop-uForm-content')]/div[@class='malibu-desktop-uFormNotify']/div/ul[@class='malibu-desktop-uFormNotify-ul']/div/div[@class='malibu-desktop-uFormNotify-li']/li[contains(text(),'{level_1}')]/div/div"
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            return elements
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_error_message failed. Exception: '{e}'")

    def assert_list_error_message_multi(self, level_1, list_expected):
        try:
            elements = self.get_list_error_message_multi(level_1)
            list_actual = []
            for element in elements:
                actual = element.get_attribute('innerText').split('\n')[0].strip()
                list_actual.append(actual)
            for expected in list_expected:
                self.assertIn(expected, list_actual, f"Missing message: {expected}.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_list_error_message_multi failed. Exception: '{e}'")

    def assert_fee_grid_exist(self):
        xpath = "//div[@class='col-sm-12 col-md-12']//div[@class='malibu-desktop-uForm-title']"
        actual = self.common(xpath=xpath, method='unobscured', action='get_text')
        self.assertEqual(actual, "Fee", f"Actual: '{actual}'. Expected: 'Fee'")

    def assert_fee_grid_not_exist(self):
        xpath = "//div[@class='col-sm-12 col-md-12']//div[@class='malibu-desktop-uForm-title']"
        try:
            element = self.wait_for_element_unobscured_by_xpath(xpath, timeout=10)
            self.assertIsNone(element, "Fee grid exist.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Check assert_fee_grid_not_exist failed. Exception: '{e}'")

# ================= handle table =================
    def click_menu(self, level_01, level_02=None, level_03=None):
        menu_xpath = "//i[@class='material-icons-outlined' and text()='menu']"
        self.common(xpath=menu_xpath, method='unobscured', action='click', error=f"Click menu '{menu_xpath}' failed.")
        level_01_xpath = f"//ul[@class='malibu-desktop-uSidebarMenuNew-navbar-list-menu-ul']//label[text()='{level_01}']"
        self.common(xpath=level_01_xpath, method='visibility', action='click', error=f"Click menu level 1 '{level_01_xpath}' failed.")
        if level_02 is not None:
            level_02_xpath = f"//ul[@class='malibu-desktop-uSidebarMenuNew-navbar-list-menu-ul']//label[text()='{level_02}']"
            self.common(xpath=level_02_xpath, method='visibility', action='click', error=f"Click menu level 2 '{level_02_xpath}' failed.")
        if level_03 is not None:
            level_03_xpath = f"//ul[@class='malibu-desktop-uSidebarMenuNew-navbar-list-menu-ul']//label[text()='{level_03}']"
            self.common(xpath=level_03_xpath, method='visibility', action='click', error=f"Click menu level 3 '{level_03_xpath}' failed.")

    def simple_search(self, text, placeholder='Search text'):
        search_xpath = f"//input[@placeholder='{placeholder}']"
        self.common(xpath=search_xpath, method='visibility', action='send_keys', value=text, clear_text='Y', need_enter='Y', error=f"Simple search failed for text '{text}' using placeholder '{placeholder}'.")

    def get_text_table_data(self, column_name, index):
        xpath = f"//tr[{index}]/td[@data-title='{column_name}']/div"
        return self.common(xpath=xpath, method='unobscured', action='get_text', error=f"Get text cell of column '{column_name}' at row {index} failed.")

    def get_status_table_data(self, column_name, index):
        xpath = f"//tr[{index}]/td[@data-title='{column_name}']/div//span"
        return self.common(xpath=xpath, method='unobscured', action='get_text', error=f"Get text status cell of column '{column_name}' at row {index} failed.")

    def get_total_fee_table_data(self):
        xpath = f"//td[contains(@class,'perseus-uTableColumnCalculator')]/div"
        return self.common(xpath=xpath, method='unobscured', action='get_text', error='Get total fee of table fee failed.')

    def get_text_table_data_posting(self, posting_side, column_name, index):
        xpath = f"//div[text()='{posting_side}']/following-sibling::div//tr[{index}]/td[@data-title='{column_name}']/div"
        return self.common(xpath=xpath, method='unobscured', action='get_text', error=f"Get text cell of column '{column_name}' at row {index} at posting table failed.")

    def click_table_menu(self, action=None, row=None):
        if row is None:
            row=1
        is_more_option = self.wait_for_element_visibility_by_xpath(f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//tr[{row}]//div[@class='malibu-desktop-uTableColumnButtonHover-button']/i[text()='more_vert']", timeout=3)
        row_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//tr[{row}]//div[@class='malibu-desktop-uTableColumnButtonHover-button']"
        if is_more_option:
            self.common(xpath=row_xpath, method='visibility', action='click', error=f"Click action in BO search screen failed.")
            if action:
                action_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//tr[{row}]//p[text()='{action}']"
                self.common(xpath=action_xpath, method='visibility', action='click', error=f"Click action in BO search screen failed.")
        else:
            self.common(xpath=row_xpath, method='visibility', action='click', error=f"Click action in BO search screen failed.")

# ================= handle search F8 =================
    def simple_search_f8(self, text):
        input_xpath = f"//input[@placeholder='Search Text']"
        self.common(xpath=input_xpath, method='visibility', action='send_keys', value=text, clear_text='Y', error=f"Enter value simple search F8 failed for text '{text}'.")
        button_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]/div/div/div[contains(@class,'malibu-desktop-uView') and not(contains(@class,'malibu-component-padding'))]//span[@class='malibu-desktop-uButton-title' and text()='Search']"
        self.common(xpath=button_xpath, method='visibility', action='click', info=f"", error=f"Click simple search F8 failed for text '{text}'.")

    def click_button_search_advanced_f8(self):
        """Click button search in advanced search F8 screen"""
        button_name_xpath="//div[@id='content']/div/div/div/div/div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView') and not(contains(@class,'malibu-component-padding')) and not(contains(@class,'malibu-view-border'))]//span[@class='malibu-desktop-uButton-title' and text()='Search']"
        self.common(xpath=button_name_xpath, method='unobscured', action='click', info="Clicked on 'Search' button in advanced search F8 screen.", error=f"Click on '{button_name_xpath}' button failed.")

    def advanced_search_f8(self, title, value, field_type="I", in_group="N"):
        """
        Write value to title in advanced search F8 screen, flexible parameters for click_collap, field_type, in_group. field_type: str, default is 'I'. Valid options are:
            - I: tagname is 'input'. Enter text, date or number to input field (default).
            - A: Textarea, multi-line text input.
            - S: Select, dropdown select field.
        """
        # Validate 'field_type' to be one of 'input', 'textarea' or 'select' (default is 'input')
        valid_field_types = ['I', 'A', 'S']
        if field_type not in valid_field_types:
            raise ValueError(f"Invalid field_type: Expected one of {valid_field_types}, got '{field_type}'")
        # Validate 'in_group' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_group not in ['Y', 'N']:
            raise ValueError(f"Invalid in_group: Expected 'Y' or 'N', got '{in_group}'")
        # Create a dictionary of conditions to corresponding methods
        method_map = {
            ('I', 'N'): self.advanced_search_f8_input,
            ('I', 'Y'): self.advanced_search_f8_input_group,
            ('A', 'N'): self.advanced_search_f8_textarea,
            ('A', 'Y'): self.advanced_search_f8_textarea_group,
            ('S', 'N'): self.advanced_search_f8_select,
            ('S', 'Y'): self.advanced_search_f8_select_group,
        }
        # Get the correct method from the map
        key = (field_type, in_group)
        if key not in method_map:
            raise ValueError(f"Invalid combination of field_type, in_group")
        # Call the corresponding method with title and value as the argument
        return method_map[key](title, value)

    def advanced_search_f8_input(self, title, value):
        """Write text or number or date to 'input' in advanced search F8 screen"""
        xpath = f"//div[@id='content']/div/div/div/div/div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView') and contains(@class,'malibu-component-padding') and contains(@class,'malibu-view-border')]/div/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search F8 screen.", error=f"Write '{value}' at '{title}' in advanced search F8 screen failed.")

    def advanced_search_f8_input_group(self, title, value):
        """Write text or number or date to 'input' in advanced search F8 screen"""
        xpath = f"//div[@id='content']/div/div/div/div/div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView') and contains(@class,'malibu-component-padding') and contains(@class,'malibu-view-border')]/div/div/div[contains(@class,'malibu-desktop-uOfGroup')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search F8 screen.", error=f"Write '{value}' at '{title}' in advanced search F8 screen failed.")

    def advanced_search_f8_textarea(self, title, value):
        """Write text to 'textarea' in advanced search F8 screen"""
        xpath = f"//div[@id='content']/div/div/div/div/div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView') and contains(@class,'malibu-component-padding') and contains(@class,'malibu-view-border')]/div/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search F8 screen.", error=f"Write '{value}' at '{title}' in advanced search F8 screen failed.")

    def advanced_search_f8_textarea_group(self, title, value):
        """Write text to 'textarea' in advanced search F8 screen and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

    def advanced_search_f8_select(self, title, value):
        """Select field in advanced search F8 screen"""
        # self.key_escape()
        fieldset_xpath = f"//div[@id='content']/div/div/div/div/div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView') and contains(@class,'malibu-component-padding') and contains(@class,'malibu-view-border')]/div/div/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked '{title}' in advanced search F8 screen.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[contains(@title,'{value}')]"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in advanced search F8 screen.")

    def advanced_search_f8_select_group(self, title, value):
        """Select field in advanced search F8 screen and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

# ================= handle other methods =================
    def click_checkbox_in_tab(self, title):
        """Click 'check-box' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"Clicked check-box '{title}' in screen have tab.", error=f"Click check-box '{title}' in screen have tab failed.")

    def assert_checked_in_tab(self, title):
        # title_xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']/parent::div"
        title_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']/parent::div"
        try:
            title_element = self.wait_for_element_unobscured_by_xpath(title_xpath)
            css_class = title_element.get_attribute('class')
            if 'change' in css_class:
                log.info(f"Attribute 'change' in class '{css_class}'.")
                return True
            else:
                log.warn(f"Attribute 'change' NOT in class '{css_class}'.")
                return False
        except:
            log.error(f"Check attribute 'change' for element '{title}' failed.")

    def click_checkbox_non_tab(self, title):
        """Click 'check-box' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"Clicked check-box '{title}' in screen NON tab.", error=f"Click check-box '{title}' in screen NON tab failed.")

    def assert_checked_non_tab(self, title):
        # title_xpath = f"//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']/preceding-sibling::i"
        title_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']/preceding-sibling::i"
        is_checked = self.common(xpath=title_xpath, method='unobscured', action='get_text')
        if is_checked == 'check_box':
            log.info(f"Checkbox of element '{title}' have checked. Text is '{is_checked}'.")
            return True
        else:
            log.warn(f"Checkbox of element '{title}' is un-check. Text is '{is_checked}'.")
            return False

    def assert_checked_multi(self, collap_name, title):
        title_xpath=f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']/parent::div/parent::div//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']/preceding-sibling::i"
        is_checked = self.common(xpath=title_xpath, method='unobscured', action='get_text')
        if is_checked == 'check_box':
            log.info(f"Checkbox of element '{title}' and '{collap_name}' have checked. Text is '{is_checked}'.")
            return True
        else:
            log.warn(f"Checkbox of element '{title}' '{collap_name}' is un-check. Text is '{is_checked}'.")
            return False

    def assert_checkbox(self, title, expected, collap_name=None):
        i_xpath = ""
        if collap_name:
            i_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']/parent::div/parent::div//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']/preceding-sibling::i"
        else:
            # i_xpath = f"//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']/preceding-sibling::i"
            i_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]//div[text()='{title}']/preceding-sibling::i"
        is_checked = self.common(xpath=i_xpath, method='unobscured', action='get_text')
        if is_checked == 'check_box':
            self.assertTrue(expected)
        else:
            self.assertFalse(expected)

    def click_checkbox_in_multi(self, collap_name, title):
        """Click 'check-box' in multi"""
        # xpath = f"//span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']/parent::div/parent::div//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']/parent::div/parent::div//div[contains(@class,'malibu-desktop-uCheckBox-haveClass')]/div/div[text()='{title}']"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"Clicked check-box '{title}' in screen have tab.", error=f"Click check-box '{title}' in screen have tab failed.")

    def click_checkbox(self, title, in_tab="Y", in_multi="N", collap_name=None):
        """Click 'check-box' from title, flexible parameters for in_tab"""
        # Validate 'in_tab' to be 'Y': screen have tab or 'N': screen have no tab (default is 'Y')
        if in_tab not in ['Y', 'N']:
            raise ValueError(f"Invalid in_tab: Expected 'Y' or 'N', got '{in_tab}'")
        if in_multi not in ['Y', 'N']:
            raise ValueError(f"Invalid in_multi: Expected 'Y' or 'N', got '{in_multi}'")
        # Create a dictionary of conditions to corresponding methods
        method_map = {
            ('Y', 'N'): self.click_checkbox_in_tab,
            ('N', 'N'): self.click_checkbox_non_tab,
            ('Y', 'Y'): lambda title: self.click_checkbox_in_multi(collap_name, title),
            ('N', 'Y'): lambda title: self.click_checkbox_in_multi(collap_name, title)
        }
        # Get the correct method from the map
        key = (in_tab, in_multi)
        if key not in method_map:
            raise ValueError(f"Invalid combination of in_tab and in_multi")
        # Call the corresponding method with title as the argument
        return method_map[key](title)

    def click_signature(self, form_type="fo"):
        """
        Click signature icon in form. form_type: str, default is 'fo'. Valid options are:
            - fo: form type is fo
            - bo: form type is bo
        """
        sign_icon_xpath = f"//div[contains(@class,'malibu-desktop-uButton-square-content')]/img"
        if form_type == "bo":
            sign_icon_xpath = f"//div[contains(@class,'malibu-desktop-uButton-content')]/*[name()='svg']"
        self.common(xpath=sign_icon_xpath, method='unobscured', action='click', info='Clicked signature icon.', error='Click signature icon failed.')

    def close_all_form(self):
        close_all_xpath = "//div[@title='Close all']/i"
        try:
            close_all_element = self.driver.find_element(By.XPATH, close_all_xpath)
            if close_all_element:
                self.common(xpath=close_all_xpath, method='unobscured', action='click', info='Clicked close all icon.')
            else:
                log.warn("Close all icon not found.")
        except NoSuchElementException:
            log.warn("Close all icon does not exist.")

    def click_close_form(self, index = 1):
        close_form_xpath = f"//span[contains(@class,'malibu-desktop-uTabItem-icon-tab')]/div[text()='{index}']/parent::span/following-sibling::div/span[contains(@class,'malibu-desktop-uTabItem-close-button')]"
        try:
            close_form_element = self.driver.find_element(By.XPATH, close_form_xpath)
            if close_form_element:
                self.common(xpath=close_form_xpath, method='unobscured', action='click', info='Clicked close form icon.')
            else:
                log.warn("Close form icon not found.")
        except NoSuchElementException:
            log.warn("Close form icon does not exist.")

    def get_text_form_title(self):
        title_xpath = "//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[@class='malibu-desktop-uForm-title']"
        return self.common(xpath=title_xpath, method='visibility', action='get_text', error=f"Get text title failed.")

    def assert_form_title(self, expected_title=None):
        if expected_title is None: 
            raise AssertionError("The assertion form title cannot be empty.")
        expected_title = str(expected_title).strip()
        actual_title = self.get_text_form_title()
        self.assertEqual(expected_title, actual_title)

    def assert_page_title(self, expected_title=None):
        if expected_title is None: 
            raise AssertionError("The assertion page title cannot be empty.")
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def get_working_date(self):
        xpath = "//div[contains(@class,'malibu-desktop-uHeaderItemMoreOption-info')]/span[@class='malibu-desktop-uHeaderItemMoreOption-span']/div"
        return self.common(xpath=xpath, method='visibility', action='get_text', error=f"Get working date failed.")

    # Functions used for testcase - BO screen
    def bo_click_tab(self, tab_name):
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[@class='malibu-desktop-uFormTabItem-title' and text()='{tab_name}']"
        # xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[@class='malibu-desktop-uFormTabItem-title' and text()='{tab_name}']"
        xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[@class='malibu-desktop-uForm-title']/parent::div//div[@class='malibu-desktop-uFormTabItem-title' and text()='{tab_name}']"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"", error=f"Click tab '{tab_name}' in BO view screen failed.")

    def bo_click_tab_child(self, tab_name):
        xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[@class='malibu-desktop-uForm-title']/parent::div//div[contains(@class,'malibu-desktop-uFormTab-content') and (@style='opacity: 1;')]//div[@class='malibu-desktop-uFormTabItem-title' and text()='{tab_name}']"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"", error=f"Click tab '{tab_name}' in BO view screen failed.")

    def bo_click_checkbox(self, title):
        if self.assert_checked_in_tab(title):
            log.warn(f"Checkbox '{title}' in bo_click_checkbox checked")
            return ''
        else:
            return self.click_checkbox(title, in_tab="Y")

    def bo_click_checkbox_single(self, title):
        if self.assert_checked_non_tab(title):
            log.warn(f"Checkbox '{title}' in bo_click_checkbox_single checked")
            return ''
        else:
            return self.click_checkbox(title, in_tab="N")

    def bo_click_checkbox_multi(self, collap_name, title):
        if self.assert_checked_multi(collap_name, title):
            log.warn(f"Checkbox '{title}' in bo_click_checkbox_multi checked")
            return ''
        else:
            return self.click_checkbox(title=title, in_tab="Y", in_multi="Y", collap_name=collap_name)

    def bo_click_signature(self):
        self.click_signature(form_type="bo")

    # Functions used for testcase - FO screen
    def fo_click_checkbox(self, title):
        if self.assert_checked_non_tab(title):
            log.warn(f"Checkbox '{title}' in fo_click_checkbox checked.")
            return ''
        else:
            return self.click_checkbox(title, in_tab="N")

    def fo_click_signature(self):
        self.click_signature(form_type="fo")

# ================= handle advanced search =================
    def click_button_search_advanced(self):
        """Click button search in advanced search screen"""
        button_name_xpath="//div[contains(@class,'malibu-desktop-uMultiValue')]//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]/div[contains(@class,'malibu-desktop-uForm-content')]//div[contains(@class,'malibu-desktop-uButton-conten')]/span[@class='malibu-desktop-uButton-title' and text()='Search']"
        self.common(xpath=button_name_xpath, method='unobscured', action='click', info="Clicked on 'Search' button in advanced search screen.", error=f"Click on '{button_name_xpath}' button failed.")

    def advanced_search(self, title, value, click_collap="Y", field_type="I", in_group="N"):
        """
        Write value to title in advanced search screen, flexible parameters for click_collap, field_type, in_group. field_type: str, default is 'I'. Valid options are:
            - I: tagname is 'input'. Enter text, date or number to input field (default).
            - A: Textarea, multi-line text input.
            - S: Select, dropdown select field.
        """
        if click_collap=="Y":
            self.click_collap_multi_non_tab('Advanced search')
        # Validate 'field_type' to be one of 'input', 'textarea' or 'select' (default is 'input')
        valid_field_types = ['I', 'A', 'S']
        if field_type not in valid_field_types:
            raise ValueError(f"Invalid field_type: Expected one of {valid_field_types}, got '{field_type}'")
        # Validate 'in_group' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_group not in ['Y', 'N']:
            raise ValueError(f"Invalid in_group: Expected 'Y' or 'N', got '{in_group}'")
        # Create a dictionary of conditions to corresponding methods
        method_map = {
            ('I', 'N'): self.advanced_search_input,
            ('I', 'Y'): self.advanced_search_input_group,
            ('A', 'N'): self.advanced_search_textarea,
            ('A', 'Y'): self.advanced_search_textarea_group,
            ('S', 'N'): self.advanced_search_select,
            ('S', 'Y'): self.advanced_search_select_group,
        }
        # Get the correct method from the map
        key = (field_type, in_group)
        if key not in method_map:
            raise ValueError(f"Invalid combination of field_type, in_group")
        # Call the corresponding method with title and value as the argument
        return method_map[key](title, value)

    def adv_search(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='I', in_group='N')

    def adv_search_group(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='I', in_group='Y')

    def adv_search_text(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='A', in_group='N')

    def adv_search_text_group(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='A', in_group='Y')

    def adv_search_select(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='S', in_group='N')

    def adv_search_select_group(self, title, value):
        return self.advanced_search(title=title, value=value, field_type='S', in_group='Y')

    def adv_click_checkbox(self, collap_name, title):
        return self.click_checkbox(title=title, in_multi="Y", collap_name=collap_name)

    def advanced_search_input(self, title, value):
        """Write text or number or date to 'input' in advanced search screen"""
        xpath = f"//div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search screen.", error=f"Write '{value}' at '{title}' in advanced search screen failed.")

    def advanced_search_input_group(self, title, value):
        """Write text or number or date to 'input' in advanced search screen"""
        xpath = f"//div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search screen.", error=f"Write '{value}' at '{title}' in advanced search screen failed.")

    def advanced_search_textarea(self, title, value):
        """Write text to 'textarea' in advanced search screen"""
        xpath = f"//div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in advanced search screen.", error=f"Write '{value}' at '{title}' in advanced search screen failed.")

    def advanced_search_textarea_group(self, title, value):
        """Write text to textarea in advanced search screen and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

    def advanced_search_select(self, title, value):
        """Select field in advanced search screen"""
        # self.key_escape()
        fieldset_xpath = f"//div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked '{title}' in advanced search screen.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[contains(@title,'{value}')]"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in advanced search screen.", error=f"Select value '{value}' at '{title}' in advanced search screen failed.")

    def advanced_search_select_group(self, title, value):
        """Select field in advanced search screen and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

# ================= handle get text field =================
    def get_text_by_xpath_input(self, xpath_input):
        """Get text by xpath tagname 'input'"""
        return self.common(xpath=xpath_input, method='unobscured', action='get_value', info=f"Get text from xpath '{xpath_input}'.", error=f"Get text from xpath '{xpath_input}' failed.")

    def get_text_by_xpath_textarea(self, xpath_textarea):
        """Get text by xpath tagname 'textarea'"""
        return self.common(xpath=xpath_textarea, method='unobscured', action='get_text', info=f"Get text from xpath '{xpath_textarea}'.", error=f"Get text from xpath '{xpath_textarea}' failed.")

    def get_text_by_xpath_div(self, xpath_div):
        """Get text by xpath tagname 'div'"""
        try:
            element = self.driver.find_element(By.XPATH, xpath_div)
            log.info(f"Get text from xpath '{xpath_div}'.")
            return element.text
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Get text from xpath '{xpath_div}' failed. Exception: {e}")

    def get_text_input_in_tab(self, title):
        """Get text from 'input' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from input '{title}' in screen have tab.", error=f"Get text from input '{title}' in screen have tab failed.")

    def get_text_input_non_tab(self, title):
        """Get text from 'input' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from input '{title}' in screen NON tab.", error=f"Get text from input '{title}' in screen NON tab failed.")

    def get_text_input_in_tab_group(self, title):
        """Get text from 'input' in screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from input '{title}' in screen have tab.", error=f"Get text from input '{title}' in screen have tab failed.")

    def get_text_input_non_tab_group(self, title):
        """Get text from 'input' in screen non tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from input '{title}' in screen NON tab.", error=f"Get text from input '{title}' in screen NON tab failed.")

    def get_text_input_below_border(self, border_name, title):
        """Get text from 'input' below border in screen"""
        xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from input '{title}' below border in screen.", error=f"Get text from input '{title}' below border in screen failed.")

    def get_text_textarea_below_border(self, border_name, title):
        """Get text from 'textarea' below border in screen"""
        xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.common(xpath=xpath, method='unobscured', action='get_text', info=f"Get text from textarea '{title}' below border in screen.", error=f"Get text from textarea '{title}' below border in screen failed.")

    def get_date_input_in_tab(self, title):
        """Get date from 'input' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get date from input '{title}' in screen have tab.", error=f"Get date from input '{title}' in screen have tab failed.")

    def get_date_input_non_tab(self, title):
        """Get date from 'input' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get date from input '{title}' in screen NON tab.", error=f"Get date from input '{title}' in screen NON tab failed.")

    def get_date_input_in_tab_group(self, title):
        """Get date from 'input' in screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get date from input '{title}' in screen have tab and group.", error=f"Get date from input '{title}' in screen have tab failed.")

    def get_date_input_non_tab_group(self, title):
        """Get date from 'input' in screen non tab and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

    def get_text_select_in_tab(self, title):
        """Get text from field 'select' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from field select '{title}' in screen have tab.", error=f"Get text from field select '{title}' in screen have tab failed.")

    def get_text_select_non_tab(self, title):
        """Get text from field 'select' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from field select '{title}' in screen NON tab.", error=f"Get text from field select '{title}' in screen NON tab failed.")

    def get_text_select_in_tab_group(self, title_front_select, title_select):
        """Get text from field 'select' in screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]//legend[@title='{title_front_select}']/parent::fieldset/parent::div/parent::div/parent::div/parent::div/following-sibling::div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title_select}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]//legend[@title='{title_front_select}']/parent::fieldset/parent::div/parent::div/parent::div/parent::div/following-sibling::div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title_select}']/parent::fieldset/preceding-sibling::input"
        return self.common(xpath=xpath, method='unobscured', action='get_value', info=f"Get text from field select '{title_select}' group with '{title_front_select}' in screen have tab.", error=f"Get text from field select '{title_select}' group with '{title_front_select}' in screen have tab failed.")

    def get_text_select_non_tab_group(self, title_front_select, title_select):
        """Get text from field 'select' in screen non tab and group"""
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

    def get_text_select_multi(self, title):
        """Get text from field 'select_multi' in any screen"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uSelectMulti')]//legend[text()='{title}']/parent::fieldset/preceding-sibling::div/div/div[@class='malibu-desktop-uSelectMulti-item-choose-title']"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uSelectMulti')]//legend[text()='{title}']/parent::fieldset/preceding-sibling::div/div/div[@class='malibu-desktop-uSelectMulti-item-choose-title']"
        actual_text = []
        try:
            elements = self.driver.find_elements(By.XPATH, xpath)
            for element in elements:
                actual_text.append(element.text)
            log.info(f"Get list text from field select_multi '{title}' in any screen.")
        except Exception as e:
            log.error(f"Get text from field select_multi '{title}' in any screen failed. Exception: {e}")
        return actual_text

    def get_text_textarea_in_tab(self, title):
        """Get text from 'textarea' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.common(xpath=xpath, method='unobscured', action='get_text', info=f"Get text from title '{title}' in screen have tab.", error=f"Get text from title '{title}' in screen have tab failed.")

    def get_text_textarea_non_tab(self, title):
        """Get text from 'textarea' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.common(xpath=xpath, method='unobscured', action='get_text', info=f"Get text from title '{title}' in screen NON tab.", error=f"Get text from title '{title}' in screen NON tab failed.")

    def get_text_textarea_in_tab_group(self, title):
        """Get text from 'textarea' in screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.common(xpath=xpath, method='unobscured', action='get_text', info=f"Get text from title '{title}' in screen have tab.", error=f"Get text from title '{title}' in screen have tab failed.")

    def get_text_textarea_non_tab_group(self, title):
        """Get text from 'textarea' in screen non tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.common(xpath=xpath, method='unobscured', action='get_text', info=f"Get text from title '{title}' in screen NON tab.", error=f"Get text from title '{title}' in screen NON tab failed.")

    def get_text(self, title, field_type="I", in_tab="Y", in_group="N", in_multi="N", title_front_select=None):
        """
        Get text from title, flexible parameters for field_type, in_tab, in_group. field_type: str, default is 'I'. Valid options are:
            - I: Input, tagname is 'input' and field type is text (default).
            - D: Date, date input field.
            - A: Textarea, tagname is 'textarea' and field type is text
            - S: Select, tagname is 'input' and field type is dropdown select field.
        """
        # Ensure 'title' is a non-empty string
        if not isinstance(title, str) or not title.strip():
            raise ValueError("The 'title' must be a non-empty string.")
        # Validate 'field_type' to be one of 'input', 'textarea' or 'select' (default is 'input')
        # valid_field_types = ['input', 'textarea', 'select']
        valid_field_types = ['I', 'D', 'A', 'S']
        if field_type not in valid_field_types:
            raise ValueError(f"Invalid field_type: Expected one of {valid_field_types}, got '{field_type}'")
        # Validate 'in_tab' to be 'Y': screen have tab or 'N': screen have no tab (default is 'Y')
        if in_tab not in ['Y', 'N']:
            raise ValueError(f"Invalid in_tab: Expected 'Y' or 'N', got '{in_tab}'")
        # Validate 'in_group' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_group not in ['Y', 'N']:
            raise ValueError(f"Invalid in_group: Expected 'Y' or 'N', got '{in_group}'")
        # Validate 'in_group' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_multi not in ['Y', 'N']:
            raise ValueError(f"Invalid in_multi: Expected 'Y' or 'N', got '{in_multi}'")
        # Create a dictionary of conditions to corresponding methods
        method_map = {
            ('I', 'Y', 'N', 'N'): self.get_text_input_in_tab,
            ('I', 'N', 'N', 'N'): self.get_text_input_non_tab,
            ('I', 'Y', 'Y', 'N'): self.get_text_input_in_tab_group,
            ('I', 'N', 'Y', 'N'): self.get_text_input_non_tab_group,
            ('D', 'Y', 'N', 'N'): self.get_date_input_in_tab,
            ('D', 'N', 'N', 'N'): self.get_date_input_non_tab,
            ('D', 'Y', 'Y', 'N'): self.get_date_input_in_tab_group,
            ('D', 'N', 'Y', 'N'): self.get_date_input_non_tab_group,
            ('S', 'Y', 'N', 'N'): self.get_text_select_in_tab,
            ('S', 'N', 'N', 'N'): self.get_text_select_non_tab,
            ('S', 'Y', 'Y', 'N'): lambda title: self.get_text_select_in_tab_group(title_front_select, title),
            ('S', 'N', 'Y', 'N'): lambda title: self.get_text_select_non_tab_group(title_front_select, title),
            ('A', 'Y', 'N', 'N'): self.get_text_textarea_in_tab,
            ('A', 'N', 'N', 'N'): self.get_text_textarea_non_tab,
            ('A', 'Y', 'Y', 'N'): self.get_text_textarea_in_tab_group,
            ('A', 'N', 'Y', 'N'): self.get_text_textarea_non_tab_group,
        }
        # Get the correct method from the map
        key = (field_type, in_tab, in_group, in_multi)
        if key not in method_map:
            raise ValueError(f"Invalid combination of field_type, in_tab, in_group, and in_multi")
        # Call the corresponding method with title as the argument
        return method_map[key](title)

    def get_value_data(self, title):
        """Get text from 'input' any screen"""
        xpath_input = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.get_text_by_xpath_input(xpath_input)

    def get_text_data(self, title):
        """Get text from 'textarea' any screen"""
        xpath_textarea = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.get_text_by_xpath_textarea(xpath_textarea)

    def get_value_multi(self, collap_name, title):
        """Get value from 'input' in 'multi' any screen"""
        # xpath = f"//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        return self.get_text_by_xpath_input(xpath)

    def get_text_multi(self, collap_name, title):
        """Get text from 'textarea' in 'multi' any screen"""
        # xpath = f"//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        return self.get_text_by_xpath_textarea(xpath)

    def get_text_table(self, colunm_01, value_colunm_01, colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Get the value in a specific column of a table row, based on one or two reference column values.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Returns:
            value of colunm (str): The actual value in the target column.
        Example:
            Get text of the "Status" column where the "IFC code" column is "101":
                get_text_table('IFC code', '101', 'Status')
            Get text of the "Replace by" column where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                get_text_table('System account name', 'DEPOSIT', 'Replace by', colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        if colunm_02 is None:
            xpath = f"//table[@class='malibu-desktop-uTable-info']/tbody/tr/td[@data-title='{colunm_01}']/div[text()='{value_colunm_01}']/parent::td/{xpath_type}-sibling::td[@data-title='{colunm_expected}']/div"
            return self.get_text_by_xpath_div(xpath)
        else:
            xpath = f"//table[@class='malibu-desktop-uTable-info']/tbody/tr/td[@data-title='{colunm_01}']/div[text()='{value_colunm_01}']/parent::td/following-sibling::td[@data-title='{colunm_02}']/div[text()='{value_colunm_02}']/parent::td/{xpath_type}-sibling::td[@data-title='{colunm_expected}']/div"
            return self.get_text_by_xpath_div(xpath)

    def get_text_table_index(self, colunm_01, value_colunm_01, colunm_expected, index, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Get the value in a specific column of a table row, based on one or two reference column values and index of row.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            index (int): the index of row.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Returns:
            value of colunm (str): The actual value in the target column.
        Example:
            Get text of the "Status" column row 1 where the "IFC code" column is "101":
                get_text_table_index('IFC code', '101', 'Status', 1)
            Get text of the "Replace by" column row 2 where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                get_text_table_index('System account name', "DEPOSIT', 'Replace by', 2, colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        if colunm_02 is None:
            xpath = f"//table[@class='malibu-desktop-uTable-info']/tbody/tr[{index}]/td[@data-title='{colunm_01}']/div[text()='{value_colunm_01}']/parent::td/{xpath_type}-sibling::td[@data-title='{colunm_expected}']/div"
            return self.get_text_by_xpath_div(xpath)
        else:
            xpath = f"//table[@class='malibu-desktop-uTable-info']/tbody/tr[{index}]/td[@data-title='{colunm_01}']/div[text()='{value_colunm_01}']/parent::td/following-sibling::td[@data-title='{colunm_02}']/div[text()='{value_colunm_02}']/parent::td/{xpath_type}-sibling::td[@data-title='{colunm_expected}']/div"
            return self.get_text_by_xpath_div(xpath)

    def get_text_multi_line(self, title):
        xpath = f"//span[text()='{title}']/parent::div/following-sibling::textarea"
        return self.get_text_by_xpath_textarea(xpath)

    # Functions used for testcase - BO screen
    def bo_get_value(self, title):
        return self.get_text(title, field_type="I", in_tab="Y", in_group="N", in_multi="N")

    def bo_get_value_single(self, title):
        return self.get_text(title, field_type="I", in_tab="N", in_group="N", in_multi="N")

    def bo_get_value_group(self, title):
        return self.get_text(title, field_type="I", in_tab="Y", in_group="Y", in_multi="N")

    def bo_get_value_group_single(self, title):
        return self.get_text(title, field_type="I", in_tab="N", in_group="Y", in_multi="N")

    def bo_get_date(self, title):
        return self.get_text(title, field_type="D", in_tab="Y", in_group="N", in_multi="N")

    def bo_get_date_single(self, title):
        return self.get_text(title, field_type="D", in_tab="N", in_group="N", in_multi="N")

    def bo_get_date_group(self, title):
        return self.get_text(title, field_type="D", in_tab="Y", in_group="Y", in_multi="N")

    def bo_get_select(self, title):
        return self.get_text(title, field_type="S", in_tab="Y", in_group="N", in_multi="N")

    def bo_get_select_single(self, title):
        return self.get_text(title, field_type="S", in_tab="N", in_group="N", in_multi="N")

    def bo_get_select_group(self, title, title_front_select):
        return self.get_text(title, field_type="S", in_tab="Y", in_group="Y", in_multi="N", title_front_select=title_front_select)

    def bo_get_select_group_single(self, title, title_front_select):
        return self.get_text(title, field_type="S", in_tab="N", in_group="Y", in_multi="N", title_front_select=title_front_select)

    def bo_get_select_multi(self, title):
        return self.get_text_select_multi(title)

    def bo_get_text(self, title):
        return self.get_text(title, field_type="A", in_tab="Y", in_group="N", in_multi="N")

    def bo_get_text_single(self, title):
        return self.get_text(title, field_type="A", in_tab="N", in_group="N", in_multi="N")

    def bo_get_text_group(self, title):
        return self.get_text(title, field_type="A", in_tab="Y", in_group="Y", in_multi="N")

    def bo_get_text_group_single(self, title):
        return self.get_text(title, field_type="A", in_tab="N", in_group="Y", in_multi="N")

    def bo_get_value_data(self, title):
        return self.get_value_data(title)

    def bo_get_text_data(self, title):
        return self.get_text_data(title)

    def bo_get_value_multi(self, collap_name, title):
        return self.get_value_multi(collap_name, title)

    def bo_get_text_multi(self, collap_name, title):
        return self.get_text_multi(collap_name, title)

    def bo_get_text_table(self, colunm_01, value_colunm_01, colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        return self.get_text_table(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type)

    def bo_get_text_table_index(self, colunm_01, value_colunm_01, colunm_expected, index, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        return self.get_text_table_index(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, index=index, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type)

    def bo_get_text_multi_line(self, title):
        return self.get_text_multi_line(title)

    def bo_get_value_border(self, border_name, title):
        return self.get_text_input_below_border(border_name, title)

    def bo_get_text_border(self, border_name, title):
        return self.get_text_textarea_below_border(border_name, title)

    def bo_assert_value(self, title, expected):
        self.assertEqual(self.bo_get_value(title), expected)

    def bo_assert_value_single(self, title, expected):
        self.assertEqual(self.bo_get_value_single(title), expected)

    def bo_assert_value_group(self, title, expected):
        self.assertEqual(self.bo_get_value_group(title), expected)

    def bo_assert_value_group_single(self, title, expected):
        self.assertEqual(self.bo_get_value_group_single(title), expected)

    def bo_assert_date(self, title, expected):
        self.assertEqual(self.bo_get_date(title), expected)

    def bo_assert_date_single(self, title, expected):
        self.assertEqual(self.bo_get_date_single(title), expected)

    def bo_assert_date_group(self, title, expected):
        self.assertEqual(self.bo_get_date_group(title), expected)

    def bo_assert_select(self, title, expected):
        self.assertEqual(self.bo_get_select(title), expected)

    def bo_assert_select_single(self, title, expected):
        self.assertEqual(self.bo_get_select_single(title), expected)

    def bo_assert_select_group(self, title, expected):
        self.assertEqual(self.bo_get_select_group(title), expected)

    def bo_assert_select_group_single(self, title, expected):
        self.assertEqual(self.bo_get_select_group_single(title), expected)

    def bo_assert_select_multi(self, title, expected):
        self.assertEqual(sorted(self.bo_get_select_multi(title)), sorted(expected))

    def bo_assert_text(self, title, expected):
        self.assertEqual(self.bo_get_text(title), expected)

    def bo_assert_text_single(self, title, expected):
        self.assertEqual(self.bo_get_text_single(title), expected)

    def bo_assert_text_group(self, title, expected):
        self.assertEqual(self.bo_get_text_group(title), expected)

    def bo_assert_text_group_single(self, title, expected):
        self.assertEqual(self.bo_get_text_group_single(title), expected)

    def bo_assert_value_data(self, title, expected):
        self.assertEqual(self.bo_get_value_data(title), expected)

    def bo_assert_text_data(self, title, expected):
        self.assertEqual(self.bo_get_text_data(title), expected)

    def bo_assert_value_multi(self, collap_name, title, expected):
        self.assertEqual(self.bo_get_value_multi(collap_name, title), expected)

    def bo_assert_text_multi(self, collap_name, title, expected):
        self.assertEqual(self.bo_get_text_multi(collap_name, title), expected)

    def bo_assert_text_table(self, colunm_01, value_colunm_01, colunm_expected, value_colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Assert the expected value in a specific column of a table row, based on one or two reference column values.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            value_colunm_expected (str): The expected value in the target column.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Example:
            To assert text of the "Status" column with "Normal" where the "IFC code" column is "101":
                bo_assert_text_table('IFC code', '101', 'Status', 'Normal')
            To assert text of the "Replace by" column with "2020302031111" where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                bo_assert_text_table('System account name', 'DEPOSIT', 'Replace by', '2020302031111', colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        self.assertEqual(self.bo_get_text_table(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type), value_colunm_expected, f"{colunm_01}: {value_colunm_01} and {colunm_02}: {value_colunm_02}")

    def bo_assert_text_table_account_gls(self, account_gl_name, expected):
        self.bo_assert_text_table('Sys Account Name', account_gl_name, 'GL Account', expected)

    def bo_assert_text_table_ifc_gls(self, ifc_code, ifc_gl_name, expected):
        self.bo_assert_text_table('IFC Code', ifc_code, 'GL Account', expected, 'Sys Account Name', ifc_gl_name)

    def bo_assert_text_table_index(self, colunm_01, value_colunm_01, colunm_expected, index, value_colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Assert the expected value in a specific column of a table row, based on one or two reference column values and index of row.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            index (int): the index of row.
            value_colunm_expected (str): The expected value in the target column.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Example:
            To assert text of the "Status" column row 1 with "Normal" where the "IFC code" column is "101":
                bo_assert_text_table('IFC code', '101', 'Status', 1, 'Normal')
            To assert text of the "Replace by" column row 2 with "2020302031111" where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                bo_assert_text_table('System account name', 'DEPOSIT', 'Replace by', 2, '2020302031111', colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        self.assertEqual(self.bo_get_text_table_index(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, index=index, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type), value_colunm_expected, f"{colunm_01}: {value_colunm_01} and {colunm_02}: {value_colunm_02}")

    def bo_assert_text_multi_line(self, title, expected):
        self.assertEqual(self.bo_get_text_multi_line(title), expected, title)

    def bo_assert_value_border(self, border_name, title, expected):
        self.assertEqual(self.bo_get_value_border(border_name, title), expected, title)

    def bo_assert_text_border(self, border_name, title, expected):
        self.assertEqual(self.bo_get_text_border(border_name, title), expected, title)

    def bo_assert_checkbox(self, title, expected):
        self.assert_checkbox(title=title, expected=expected)

    def bo_assert_checkbox_multi(self, collap_name, title, expected):
        self.assert_checkbox(title=title, expected=expected, collap_name=collap_name)

    # Functions used for testcase - FO screen
    def fo_get_value(self, title):
        return self.get_text(title, field_type="I", in_tab="N", in_group="N", in_multi="N")

    def fo_get_value_group(self, title):
        return self.get_text(title, field_type="I", in_tab="N", in_group="Y", in_multi="N")

    def fo_get_date(self, title):
        return self.get_text(title, field_type="D", in_tab="N", in_group="N", in_multi="N")

    def fo_get_select(self, title):
        return self.get_text(title, field_type="S", in_tab="N", in_group="N", in_multi="N")

    def fo_get_select_group(self, title, title_front_select):
        return self.get_text(title, field_type="S", in_tab="N", in_group="Y", in_multi="N", title_front_select=title_front_select)

    def fo_get_select_multi(self, title):
        return self.get_text_select_multi(title)

    def fo_get_text(self, title):
        return self.get_text(title, field_type="A", in_tab="N", in_group="N", in_multi="N")

    def fo_get_text_group(self, title):
        return self.get_text(title, field_type="A", in_tab="N", in_group="Y", in_multi="N")

    def fo_get_value_data(self, title):
        return self.get_value_data(title)

    def fo_get_text_data(self, title):
        return self.get_text_data(title)

    def fo_get_value_multi(self, collap_name, title):
        return self.get_value_multi(collap_name, title)

    def fo_get_text_multi(self, collap_name, title):
        return self.get_text_multi(collap_name, title)

    def fo_get_text_table(self, colunm_01, value_colunm_01, colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        return self.get_text_table(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type)

    def fo_get_text_table_index(self, colunm_01, value_colunm_01, colunm_expected, index, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        return self.get_text_table_index(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, index=index, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type)

    def fo_get_text_multi_line(self, title):
        return self.get_text_multi_line(title)

    def fo_get_value_border(self, border_name, title):
        return self.get_text_input_below_border(border_name, title)

    def fo_get_text_border(self, border_name, title):
        return self.get_text_textarea_below_border(border_name, title)

    def fo_assert_value(self, title, expected):
        self.assertEqual(self.fo_get_value(title), expected)

    def fo_assert_value_group(self, title, expected):
        self.assertEqual(self.fo_get_value_group(title), expected)

    def fo_assert_date(self, title, expected):
        self.assertEqual(self.fo_get_date(title), expected)

    def fo_assert_select(self, title, expected):
        self.assertEqual(self.fo_get_select(title), expected)

    def fo_assert_select_group(self, title, title_front_select, expected):
        self.assertEqual(self.fo_get_select_group(title, title_front_select), expected)

    def fo_assert_select_multi(self, title, expected):
        self.assertEqual(sorted(self.fo_get_select_multi(title)), sorted(expected))

    def fo_assert_text(self, title, expected):
        self.assertEqual(self.fo_get_text(title), expected)

    def fo_assert_text_group(self, title, expected):
        self.assertEqual(self.fo_get_text_group(title), expected)

    def fo_assert_value_data(self, title, expected):
        self.assertEqual(self.fo_get_value_data(title), expected)

    def fo_assert_text_data(self, title, expected):
        self.assertEqual(self.fo_get_text_data(title), expected)

    def fo_assert_value_multi(self, collap_name, title, expected):
        self.assertEqual(self.fo_get_value_multi(collap_name, title), expected)

    def fo_assert_text_multi(self, collap_name, title, expected):
        self.assertEqual(self.fo_get_text_multi(collap_name, title), expected)

    def fo_assert_text_table(self, colunm_01, value_colunm_01, colunm_expected, value_colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Assert the expected value in a specific column of a table row, based on one or two reference column values.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            value_colunm_expected (str): The expected value in the target column.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Example:
            To assert text of the "Status" column with "Normal" where the "IFC code" column is "101":
                bo_assert_text_table('IFC code', '101', 'Status', 'Normal')
            To assert text of the "Replace by" column with "2020302031111" where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                bo_assert_text_table('System account name', 'DEPOSIT', 'Replace by', '2020302031111', colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        self.assertEqual(self.fo_get_text_table(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type), value_colunm_expected, f"{colunm_01}: {value_colunm_01} and {colunm_02}: {value_colunm_02}")

    def fo_assert_text_table_index(self, colunm_01, value_colunm_01, colunm_expected, index, value_colunm_expected, colunm_02=None, value_colunm_02=None, xpath_type='following'):
        """
        Assert the expected value in a specific column of a table row, based on one or two reference column values and index of row.
        Args:
            colunm_01 (str): The name of the first reference column.
            value_colunm_01 (str): The expected value in the first reference column to locate the row.
            colunm_expected (str): The name of the target column whose value will be asserted.
            index (int): the index of row.
            value_colunm_expected (str): The expected value in the target column.
            colunm_02 (str, optional): The name of the second reference column (if applicable).
            value_colunm_02 (str, optional): The expected value in the second reference column (if applicable).
            xpath_type (str, optional): Direction of the target column relative to the reference column. Options are:
                'following' (default): The target column is to the right of the reference column.
                'preceding': The target column is to the left of the reference column.
        Example:
            To assert text of the "Status" column row 1 with "Normal" where the "IFC code" column is "101":
                bo_assert_text_table('IFC code', '101', 'Status', 1, 'Normal')
            To assert text of the "Replace by" column row 2 with "2020302031111" where "System account name" is "DEPOSIT" and "Customer Condition" is "C1":
                bo_assert_text_table('System account name', 'DEPOSIT', 'Replace by', 2, '2020302031111', colunm_02='Customer Condition', value_colunm_02='C1', xpath_type='preceding')
        """
        self.assertEqual(self.fo_get_text_table_index(colunm_01=colunm_01, value_colunm_01=value_colunm_01, colunm_expected=colunm_expected, index=index, colunm_02=colunm_02, value_colunm_02=value_colunm_02, xpath_type=xpath_type), value_colunm_expected, f"{colunm_01}: {value_colunm_01} and {colunm_02}: {value_colunm_02}")

    def fo_assert_text_multi_line(self, title, expected):
        self.assertEqual(self.fo_get_text_multi_line(title), expected, title)

    def fo_assert_value_border(self, border_name, title, expected):
        self.assertEqual(self.fo_get_value_border(border_name, title), expected, title)

    def fo_assert_text_border(self, border_name, title, expected):
        self.assertEqual(self.fo_get_text_border(border_name, title), expected, title)

    def fo_assert_checkbox(self, title, expected):
        self.assert_checkbox(title=title, expected=expected)

    def fo_assert_checkbox_multi(self, collap_name, title, expected):
        self.assert_checkbox(title=title, expected=expected, collap_name=collap_name)

# ================= handle click field =================
    def click_collap_multi_in_tab(self, collap_name):
        """Click collap multi in screen have tab"""
        xpath_collap_name = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div/span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']"
        xpath_collap_icon = f"{xpath_collap_name}/preceding-sibling::span/span"
        text_collap_icon = self.common(xpath=xpath_collap_icon, method='unobscured', action='get_text')
        if text_collap_icon == '+':
            self.common(xpath=xpath_collap_name, method='unobscured', action='click', info=f"Clicked '{collap_name}' in screen have tab.", error=f"Click '{collap_name}' in screen have tab failed.")
        else:
            log.warn('Collapse in screen have tab already un-collapsed.')

    def click_collap_multi_non_tab(self, collap_name):
        """Click collap multi in screen non tab"""
        # xpath_collap_name = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div/span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']"
        xpath_collap_name = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div/span[@class='malibu-desktop-uMultiValue-title' and text()='{collap_name}']"
        xpath_collap_icon = f"{xpath_collap_name}/preceding-sibling::span/span"
        xpath_collap_icon = f"{xpath_collap_name}/preceding-sibling::span/span"
        text_collap_icon = self.common(xpath=xpath_collap_icon, method='unobscured', action='get_text')
        if text_collap_icon == '+':
            self.common(xpath=xpath_collap_name, method='unobscured', action='click', info=f"Clicked '{collap_name}' in screen NON tab.", error=f"Click '{collap_name}' in screen NON tab failed.")
        else:
            log.warn('Collapse in screen NON tab already un-collapsed.')

    # Functions used for testcase - BO screen
    def bo_click_collap(self, collap_name):
        return self.click_collap_multi_in_tab(collap_name)

    def bo_click_collap_single(self, collap_name):
        return self.click_collap_multi_non_tab(collap_name)

    # Functions used for testcase - FO screen
    def fo_click_collap(self, collap_name):
        return self.click_collap_multi_non_tab(collap_name)

# ================= handle write_text field =================
    def write_text_input(self, title, value, clear_text=None):
        """Write text to 'input' any screen"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in any screen.", error=f"Write '{value}' at '{title}' in any screen failed.")

    def write_text_input_in_tab(self, title, value, clear_text=None):
        """Write text to 'input' screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in screen have tab.", error=f"Write '{value}' at '{title}' in screen have tab failed.")

    def write_text_input_non_tab(self, title, value, clear_text=None):
        """Write text to 'input' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' in screen NON tab.", error=f"Write '{value}' at '{title}' in screen NON tab failed.")

    def write_text_input_in_tab_group(self, title, value, clear_text=None):
        """Write text to 'input' screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in screen have tab.", error=f"Write '{value}' at '{title}' in screen have tab failed.")

    def write_text_input_non_tab_group(self, title, value, clear_text=None):
        """Write text to 'input' in screen non tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' in screen NON tab.", error=f"Write '{value}' at '{title}' in screen NON tab failed.")

    def write_text_input_multi_in_tab(self, collap_name, title, value, clear_text=None):
        """Write text to 'input' in multi in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' at '{collap_name}' in screen have tab.", error=f"Write '{value}' at '{title}' at '{collap_name}' in screen have tab failed.")

    def write_text_input_multi_non_tab(self, collap_name, title, value, clear_text=None):
        """Write text to 'input' in multi in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' at '{collap_name}' in screen NON tab.", error=f"Write '{value}' at '{title}' at '{collap_name}' in screen NON tab failed.")

    def write_text_input_below_border(self, border_name, title, value, clear_text=None):
        """Write text to 'input' below border in screen"""
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' below border in screen.", error=f"Write '{value}' at '{title}' below border in screen failed.")

    def write_text_textarea(self, title, value, clear_text=None):
        """Write text to 'textarea' any screen"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in any screen.", error=f"Write '{value}' at '{title}' in any screen failed.")

    def write_text_textarea_in_tab(self, title, value, clear_text=None):
        """Write text to 'textarea' in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in screen have tab.", error=f"Write '{value}' at '{title}' in screen have tab failed.")

    def write_text_textarea_non_tab(self, title, value, clear_text=None):
        """Write text to 'textarea' in screen non tab"""
        xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        # xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' in screen NON tab.", error=f"Write '{value}' at '{title}' in screen NON tab failed.")

    def write_text_textarea_in_tab_group(self, title, value, clear_text=None):
        """Write text to 'textarea' in screen have tab and group"""
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' in screen have tab and group.", error=f"Write '{value}' at '{title}' in screen have tab and group failed.")

    def write_text_textarea_non_tab_group(self, title, value, clear_text=None):
        """Write text to 'textarea' in screen non tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]//div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, need_tab='Y', info=f"Wrote '{value}' at '{title}' in screen NON tab.", error=f"Write '{value}' at '{title}' in screen NON tab failed.")

    def write_text_textarea_multi_in_tab(self, collap_name, title, value, clear_text=None):
        """Write text to 'textarea' in multi in screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' at '{collap_name}' in screen have tab.", error=f"Write '{value}' at '{title}' at '{collap_name}' in screen have tab failed.")

    def write_text_textarea_multi_non_tab(self, collap_name, title, value, clear_text=None):
        """Write text to 'textarea' in multi in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uMultiValue')]/div//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' at '{collap_name}' in screen NON tab.", error=f"Write '{value}' at '{title}' at '{collap_name}' in screen NON tab failed.")

    def write_text_textarea_below_border(self, border_name, title, value, clear_text=None):
        """Write text to 'textarea' below border in screen"""
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' below border in screen.", error=f"Write '{value}' at '{title}' below border in screen failed.")

    def write_text_textarea_multi_line(self, title, value, clear_text=None):
        """Write text to textarea multi line"""
        # xpath = f"//span[text()='{title}']/parent::div/following-sibling::textarea"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[text()='{title}']/parent::div/following-sibling::textarea"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' below textarea multi line in screen.", error=f"Write '{value}' at '{title}' below textarea multi line in screen failed.")

    def write_date_input_in_tab(self, title, value):
        """Write date to 'input' screen have tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in screen have tab.", error=f"Write '{value}' at '{title}' in screen have tab failed.")

    def write_date_input_non_tab(self, title, value):
        """Write date to 'input' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' in screen NON tab.", error=f"Write '{value}' at '{title}' in screen NON tab failed.")

    def write_date_below_border(self, border_name, title, value):
        """Write date to 'input' below border in screen"""
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uDate')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value, clear_text='Y', info=f"Wrote '{value}' at '{title}' below border in screen.", error=f"Write '{value}' at '{title}' below border in screen failed.")

    def write_decimal_input_in_tab(self, title, amount):
        """Write decimal to 'input' in screen have tab"""
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        value_amount=str(amount).replace(',', '')
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen have tab first time.", error=f"Write '{amount}' at '{title}' in screen have tab failed.")
        actual_amount = self.common(xpath=xpath, method='unobscured', action='get_value')
        if actual_amount != amount:
            self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen have tab second time.", error=f"Write '{amount}' at '{title}' in screen have tab failed.")

    def write_decimal_input_in_tab_group(self, title, amount):
        """Write decimal to 'input' in screen have tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uForm') and contains(@class,'col-12') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        value_amount=str(amount).replace(',', '')
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen have tab and group first time.", error=f"Write '{amount}' at '{title}' in screen have tab and group failed.")
        actual_amount = self.common(xpath=xpath, method='unobscured', action='get_value')
        if actual_amount != amount:
            self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen have tab and group second time.", error=f"Write '{amount}' at '{title}' in screen have tab and group failed.")

    def write_decimal_input_non_tab(self, title, amount):
        """Write decimal to 'input' in screen non tab"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        value_amount=str(amount).replace(',', '')
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen NON tab first time.", error=f"Write '{amount}' at '{title}' in screen NON tab failed.")
        actual_amount = self.common(xpath=xpath, method='unobscured', action='get_value')
        if actual_amount != amount:
            self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen NON tab second time.", error=f"Write '{amount}' at '{title}' in screen NON tab failed.")

    def write_decimal_input_non_tab_group(self, title, amount):
        """Write decimal to 'input' in screen non tab and group"""
        # xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        value_amount=str(amount).replace(',', '')
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen NON tab and group first time.", error=f"Write '{amount}' at '{title}' in screen NON tab and group failed.")
        actual_amount = self.common(xpath=xpath, method='unobscured', action='get_value')
        if actual_amount != amount:
            self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{amount}' at '{title}' in screen NON tab and group second time.", error=f"Write '{amount}' at '{title}' in screen NON tab and group failed.")

    def write_decimal_below_border(self, border_name, title, value):
        """Write decimal to 'input' below border in screen"""
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        # xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        value_amount=str(value).replace(',', '')
        self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{value}' at '{title}' below border in screen first time.", error=f"Write '{value}' at '{title}' below border in screen failed.")
        actual_amount = self.common(xpath=xpath, method='unobscured', action='get_value')
        if actual_amount != value:
            self.common(xpath=xpath, method='unobscured', action='send_keys', value=value_amount, clear_text='Y', need_tab='Y', info=f"Wrote '{value}' at '{title}' below border in screen second time.", error=f"Write '{value}' at '{title}' below border in screen failed.")

    def write_table(self, column_01, value_column_01, column_expected, value_expected, column_02=None, value_column_02=None):
        xpath = ""
        if column_02:
            xpath = f"//tr/td[contains(@class,'malibu-desktop-uTable-td') and @data-title='{column_01}']/div[text()='{value_column_01}']/parent::td/parent::tr/td[contains(@class,'malibu-desktop-uTable-td') and @data-title='{column_02}']/div[text()='{value_column_02}']/parent::td/parent::tr/td[contains(@class,'malibu-desktop-uTable-td') and @data-title='{column_expected}']/div/div//"
        else:
            xpath = f"//tr/td[contains(@class,'malibu-desktop-uTable-td') and @data-title='{column_01}']/div[text()='{value_column_01}']/parent::td/parent::tr/td[contains(@class,'malibu-desktop-uTable-td') and @data-title='{column_expected}']/div/div//"
        # click icon
        icon_xpath = f"{xpath}i"
        self.common(xpath=icon_xpath, method='find', action='click', info=f"Clicked 'icon' in table.")
        # enter value
        value_xpath = f"{xpath}input"
        self.common(xpath=value_xpath, method='find', action='send_keys', value=value_expected, clear_text='Y', need_tab='Y', info=f"Wrote '{value_expected}' at '{column_expected}' in table.", error=f"Write '{value_expected}' at '{column_expected}' in table failed.")

    def select(self, title, value):
        """Select field in any screen"""
        # self.key_escape()
        fieldset_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked title '{title}' in any screen.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in any screen.", error=f"Select value '{value}' at title '{title}' in any screen failed.")

    def select_multi(self, title, values):
        """Select multi in any screen"""
        fieldset_xpath = f"//div[contains(@class,'malibu-desktop-uSelectMulti')]//legend[text()='{title}']/parent::fieldset/"
        icon_xpath = f"{fieldset_xpath}following-sibling::i"
        self.common(xpath=icon_xpath, method='unobscured', action='click', info=f"Clicked title '{title}' in select multi.")
        for value in values:
            value_xpath = f"{fieldset_xpath}following-sibling::div//ul/li/label[@title='{value}']"
            self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in select multi.")
        self.common(xpath=icon_xpath, method='unobscured', action='click', info=f"Clicked title '{title}' in select multi again.")

    def select_in_tab(self, title, value):
        """Select field in screen have tab"""
        # self.key_escape()
        fieldset_xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked title '{title}' in screen have tab.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in screen have tab.", error=f"Select value '{value}' at title '{title}' in screen have tab failed.")

    def select_in_tab_group(self, title, value):
        """Select field in screen have tab and group"""
        # self.key_escape()
        fieldset_xpath = f"//div[contains(@class,'malibu-desktop-uFormTab-content')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uOfGroup')]/div/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked title '{title}' in screen have tab.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in screen have tab.", error=f"Select value '{value}' at title '{title}' in screen have tab failed.")

    def select_non_tab(self, title, value):
        """Select field in screen non tab"""
        # self.key_escape()
        fieldset_xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked '{title}' in screen NON tab.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' in screen NON tab.", error=f"Select value '{value}' at '{title}' in screen NON tab failed.")

    def select_non_tab_group(self, title, value):
        """Select field in screen non tab and group"""
        # self.key_escape()
        print("The method has not yet been implemented. Please contact NhiDY to do it.")
        return ''

    def select_below_border(self, border_name, title, value):
        """Select field in below border in screen"""
        # self.key_escape()
        # fieldset_xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uSelectItem')]//legend[@title='{title}']/parent::fieldset/"
        fieldset_xpath = f"//span[text()='{border_name}']/following-sibling::div[contains(@class,'malibu-desktop-uView-content-main')]//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked '{title}' below border in screen.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' below border in screen.", error=f"Select value '{value}' at '{title}' below border in screen failed.")

    def select_below_collap(self, collap_name, title, value):
        fieldset_xpath = f"//legend[@class='malibu-desktop-uMultiValue-border-title' and text()='{collap_name}']/parent::fieldset/following-sibling::div//legend[@title='{title}']/parent::fieldset/"
        title_xpath = f"{fieldset_xpath}preceding-sibling::input"
        self.common(xpath=title_xpath, method='unobscured', action='click', info=f"Clicked '{title}' below collap in screen.")
        value_xpath = f"{fieldset_xpath}following-sibling::div/ul/li/label[@title='{value}']"
        self.common(xpath=value_xpath, method='unobscured', action='click', info=f"Clicked value '{value}' below collap in screen.", error=f"Select value '{value}' at '{title}' below collap in screen failed.")

    def choose_file_by_xpath(self, file_path, xpath):
        """
        Upload the file based on bsolute file path
        Args:
            file_path: Provide the file path (Use absolute path). 
                - Windows path: "C:\path\on\your\image.jpg"
                - Mac/Linux path: "/Users/yourname/path/to/image.jpg"
            xpath: Locate the file input field.
        """
        try:
            file_input = self.driver.find_element(By.XPATH, xpath)
            file_input.send_keys(file_path)
        except (NoSuchElementException, ElementNotInteractableException) as e: 
            log.error(f"Choose file failed. Exception: {e}")

    def choose_file(self, file_path):
        xpath = f"//div[@class='malibu-desktop-uView-content']/div/div/input[@type='file']"
        return self.choose_file_by_xpath(file_path, xpath)

    def get_file_name(self):
        xpath = f"//div[contains(@class,'malibu-desktop-uInputFile-div')]/following-sibling::div[contains(@class,'malibu-desktop-uLabel')]/label"
        return self.get_text_by_xpath_div(xpath)

    def get_info_signature(self, title):
        xpath = f"//div[contains(@class,'malibu-desktop-form-003005-key') and text()='{title}']/following-sibling::div[contains(@class,'malibu-desktop-form-003005-value')]"
        return self.get_text_by_xpath_div(xpath)

    def write_all_type(self, title, value, clear_text=None, field_type=None):
        """
        Writes text into an input or textarea field based on the given title.
        Args:
            title (str): Title of the field (legend text).
            value (str): Text to be written in the field.
            clear_text (str, optinal): If "Y", clears existing text before writing.
            field_type (str, optinal): The type of the field ('input' or 'textarea').
        """
        if field_type not in ['input', 'textarea']:
            log.error(f"Invalid field_type: {field_type}. Must be 'input' or 'textarea'.")
            return
        title_xpath = f"//div[@id='content']/div/div[contains(@class,'malibu-desktop-uForm') and not(@style='display: none;')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::{field_type}"
        self.common(xpath=title_xpath, method='unobscured', action='send_keys', value=value, clear_text=clear_text, info=f"Wrote '{value}' at '{title}' in screen.", error=f"Write '{value}' at '{title}' in screen failed.")

    def write_input(self, title, value, clear_text='Y'):
        self.write_all_type(title=title, value=value, clear_text=clear_text, field_type='input')

    def write_textarea(self, title, value, clear_text='Y'):
        self.write_all_type(title=title, value=value, clear_text=clear_text, field_type='textarea')

    def write_text(self, title, value, field_type="T", in_tab="Y", in_group="N", in_multi="N", below_border="N", clear_text=None, collap_name=None, border_name=None):
        """
        write value to title, flexible parameters for field_type, in_tab, in_group, in_multi. field_type: str, default is 'T'. Valid options are:
            - T: Text, plain text input field (default).
            - D: Date, date input field.
            - N: Number, numeric input field.
            - A: Textarea, multi-line text input.
            - S: Select, dropdown select field.
        """
        # Validate 'field_type' to be one of 'input', 'textarea' or 'select' (default is 'input')
        # valid_field_types = ['text', 'date', 'number', 'textarea', 'select']
        valid_field_types = ['T', 'D', 'N', 'A', 'S']
        if field_type not in valid_field_types:
            raise ValueError(f"Invalid field_type: Expected one of {valid_field_types}, got '{field_type}'")
        # Validate 'in_tab' to be 'Y': screen have tab or 'N': screen have no tab (default is 'Y') or 'A': any screen
        if in_tab not in ['Y', 'N', 'A']:
            raise ValueError(f"Invalid in_tab: Expected 'Y' or 'N' or 'A', got '{in_tab}'")
        # Validate 'in_group' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_group not in ['Y', 'N']:
            raise ValueError(f"Invalid in_group: Expected 'Y' or 'N', got '{in_group}'")
        # Validate 'in_multi' to be 'Y': field in group or 'N': field not in group (default is 'N')
        if in_multi not in ['Y', 'N']:
            raise ValueError(f"Invalid in_multi: Expected 'Y' or 'N', got '{in_multi}'")
        # Validate that 'collap_name' is provided if 'in_multi' is 'Y' and field_type is 'A'
        if in_multi == 'Y' and field_type == 'A' and not collap_name:
            raise ValueError("collap_name must be provided when field_type is 'A' and in_multi is 'Y'")
        # Validate 'below_border' to be 'Y': field below border or 'N': field not below border (default is 'N')
        if below_border not in ['Y', 'N']:
            raise ValueError(f"Invalid below_border: Expected 'Y' or 'N', got '{below_border}'")
        # Create a dictionary of conditions to corresponding methods
        method_map = {
            ('T', 'A', 'N', 'N', 'N'): lambda title, value: self.write_text_input(title, value, clear_text),
            ('T', 'Y', 'N', 'N', 'N'): lambda title, value: self.write_text_input_in_tab(title, value, clear_text),
            ('T', 'N', 'N', 'N', 'N'): lambda title, value: self.write_text_input_non_tab(title, value, clear_text),
            ('T', 'Y', 'Y', 'N', 'N'): lambda title, value: self.write_text_input_in_tab_group(title, value, clear_text),
            ('T', 'N', 'Y', 'N', 'N'): lambda title, value: self.write_text_input_non_tab_group(title, value, clear_text),
            ('T', 'Y', 'N', 'Y', 'N'): lambda title, value: self.write_text_input_multi_in_tab(collap_name, title, value, clear_text),
            ('T', 'N', 'N', 'Y', 'N'): lambda title, value: self.write_text_input_multi_non_tab(collap_name, title, value, clear_text),
            ('T', 'N', 'N', 'N', 'Y'): lambda title, value: self.write_text_input_below_border(border_name, title, value, clear_text),
            ('A', 'A', 'N', 'N', 'N'): lambda title, value: self.write_text_textarea(title, value, clear_text),
            ('A', 'Y', 'N', 'N', 'N'): lambda title, value: self.write_text_textarea_in_tab(title, value, clear_text),
            ('A', 'N', 'N', 'N', 'N'): lambda title, value: self.write_text_textarea_non_tab(title, value, clear_text),
            ('A', 'Y', 'Y', 'N', 'N'): lambda title, value: self.write_text_textarea_in_tab_group(title, value, clear_text),
            ('A', 'N', 'Y', 'N', 'N'): lambda title, value: self.write_text_textarea_non_tab_group(title, value, clear_text),
            ('A', 'Y', 'N', 'Y', 'N'): lambda title, value: self.write_text_textarea_multi_in_tab(collap_name, title, value, clear_text),
            ('A', 'N', 'N', 'Y', 'N'): lambda title, value: self.write_text_textarea_multi_non_tab(collap_name, title, value, clear_text),
            ('A', 'N', 'N', 'N', 'Y'): lambda title, value: self.write_text_textarea_below_border(border_name, title, value, clear_text),
            ('A', 'Y', 'N', 'N', 'Y'): lambda title, value: self.write_text_textarea_below_border(border_name, title, value, clear_text),
            ('D', 'Y', 'N', 'N', 'N'): self.write_date_input_in_tab,
            ('D', 'N', 'N', 'N', 'N'): self.write_date_input_non_tab,
            ('D', 'N', 'N', 'N', 'Y'): lambda title, value: self.write_date_below_border(border_name, title, value),
            ('N', 'Y', 'N', 'N', 'N'): self.write_decimal_input_in_tab,
            ('N', 'N', 'N', 'N', 'N'): self.write_decimal_input_non_tab,
            ('N', 'Y', 'Y', 'N', 'N'): self.write_decimal_input_in_tab_group,
            ('N', 'N', 'Y', 'N', 'N'): self.write_decimal_input_non_tab_group,
            ('N', 'N', 'N', 'N', 'Y'): lambda title, value: self.write_decimal_below_border(border_name, title, value),
            ('S', 'A', 'N', 'N', 'N'): self.select,
            ('S', 'Y', 'N', 'N', 'N'): self.select_in_tab,
            ('S', 'N', 'N', 'N', 'N'): self.select_non_tab,
            ('S', 'Y', 'Y', 'N', 'N'): self.select_in_tab_group,
            ('S', 'N', 'Y', 'N', 'N'): self.select_non_tab_group,
            ('S', 'N', 'N', 'N', 'Y'): lambda title, value: self.select_below_border(border_name, title, value),
            ('S', 'Y', 'N', 'N', 'Y'): lambda title, value: self.select_below_border(border_name, title, value),
            ('S', 'N', 'N', 'Y', 'N'): lambda title, value: self.select_below_collap(collap_name, title, value),
            ('S', 'Y', 'N', 'Y', 'N'): lambda title, value: self.select_below_collap(collap_name, title, value),
        }
        # Get the correct method from the map
        key = (field_type, in_tab, in_group, in_multi, below_border)
        if key not in method_map:
            raise ValueError(f"Invalid combination of field_type, in_tab, in_group, in_multi and below_border")
        # Call the corresponding method with title and value as the argument
        return method_map[key](title, value)

    # Functions used for testcase - BO screen
    def bo_write(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="Y", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_data(self, title, value, clear_text="Y"):
        """Write text to 'input' based on 'title' at any BO screen, 'title' must exist only once."""
        return self.write_text(title, value, field_type="T", in_tab="A", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_single(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_group(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="Y", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_group_single(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_text(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="Y", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_text_data(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="A", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_text_single(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_text_group(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="Y", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_text_group_single(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def bo_write_date(self, title, value):
        return self.write_text(title, value, field_type="D", in_tab="Y", in_group="N", in_multi="N", below_border="N")

    def bo_write_date_single(self, title, value):
        return self.write_text(title, value, field_type="D", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def bo_write_number(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="Y", in_group="N", in_multi="N", below_border="N")

    def bo_write_number_single(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def bo_write_number_group(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="Y", in_group="Y", in_multi="N", below_border="N")

    def bo_write_number_group_single(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="N", in_group="Y", in_multi="N", below_border="N")

    def bo_select(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="Y", in_group="N", in_multi="N", below_border="N")

    def bo_select_data(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="A", in_group="N", in_multi="N", below_border="N")

    def bo_select_single(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def bo_select_group(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="Y", in_group="Y", in_multi="N", below_border="N")

    def bo_select_group_single(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="N", in_group="Y", in_multi="N", below_border="N")

    def bo_select_border(self, border_name, title, value):
        return self.write_text(title, value, field_type="S", in_tab="Y", in_group="N", in_multi="N", below_border="Y", border_name=border_name)

    def bo_select_collap(self, collap_name, title, value):
        return self.write_text(title, value, field_type="S", in_tab="Y", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name)

    def bo_select_multi(self, title, values):
        return self.select_multi(title, values)

    def bo_write_multi(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="Y", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def bo_write_multi_single(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def bo_write_text_multi(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="Y", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def bo_write_text_border(self, border_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="Y", in_group="N", in_multi="N", below_border="Y", border_name=border_name, clear_text=clear_text)

    def bo_write_text_multi_single(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def bo_choose_file(self, file_path):
        return self.choose_file(file_path)

    def bo_get_file_name(self):
        return self.get_file_name()

    def bo_assert_file_name(self, expected):
        self.assertEqual(self.bo_get_file_name(), expected)

    def bo_get_info_signature(self, title):
        return self.get_info_signature(title)

    def bo_assert_info_signature(self, title, expected):
        self.assertEqual(self.bo_get_info_signature(title), expected)

    def bo_set_value(self, title, value, clear_text="Y"):
        return self.write_input(title, value, clear_text=clear_text)

    def bo_set_text(self, title, value, clear_text="Y"):
        return self.write_textarea(title, value, clear_text=clear_text)

    def bo_write_text_multi_line(self, title, value, clear_text="Y"):
        return self.write_text_textarea_multi_line(title, value, clear_text=clear_text)

    # Functions used for testcase - FO screen
    def fo_write(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def fo_write_group(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def fo_write_border(self, border_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="N", in_multi="N", below_border="Y", border_name=border_name, clear_text=clear_text)

    def fo_write_text(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="N", in_multi="N", below_border="N", clear_text=clear_text)

    def fo_write_text_group(self, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="Y", in_multi="N", below_border="N", clear_text=clear_text)

    def fo_write_date(self, title, value):
        return self.write_text(title, value, field_type="D", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def fo_write_date_border(self, border_name, title, value):
        return self.write_text(title, value, field_type="D", in_tab="N", in_group="N", in_multi="N", below_border="Y", border_name=border_name)

    def fo_write_number(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def fo_write_number_group(self, title, value):
        return self.write_text(title, value, field_type="N", in_tab="N", in_group="Y", in_multi="N", below_border="N")

    def fo_write_number_border(self, border_name, title, value):
        return self.write_text(title, value, field_type="N", in_tab="N", in_group="N", in_multi="N", below_border="Y", border_name=border_name)

    def fo_select(self, title, value):
        return self.write_text(title, value, field_type="S", in_tab="N", in_group="N", in_multi="N", below_border="N")

    def fo_select_border(self, border_name, title, value):
        return self.write_text(title, value, field_type="S", in_tab="N", in_group="N", in_multi="N", below_border="Y", border_name=border_name)

    def fo_select_collap(self, collap_name, title, value):
        return self.write_text(title, value, field_type="S", in_tab="N", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name)

    def fo_select_data(self, title, value):
        return self.select(title=title, value=value)

    def fo_select_multi(self, title, values):
        return self.select_multi(title=title, values=values)

    def fo_write_multi(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="T", in_tab="N", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def fo_write_text_multi(self, collap_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="N", in_multi="Y", below_border="N", collap_name=collap_name, clear_text=clear_text)

    def fo_write_text_border(self, border_name, title, value, clear_text="Y"):
        return self.write_text(title, value, field_type="A", in_tab="N", in_group="N", in_multi="N", below_border="Y", border_name=border_name, clear_text=clear_text)

    def fo_choose_file(self, file_path):
        return self.choose_file(file_path)

    def fo_set_value(self, title, value, clear_text="Y"):
        return self.write_input(title, value, clear_text=clear_text)

    def fo_set_text(self, title, value, clear_text="Y"):
        return self.write_textarea(title, value, clear_text=clear_text)

    def fo_write_text_multi_line(self, title, value, clear_text="Y"):
        return self.write_text_textarea_multi_line(title, value, clear_text=clear_text)

# ================= handle clear_text field =================
    def clear_text(self, element_input):
        """Clear text for element 'input'"""
        self.key_escape()
        self.switch_to_core_banking()
        self.driver.execute_script("arguments[0].focus();", element_input)
        self.wait(0.1)
        try:
            actions = ActionChains(self.driver)
            actions.click(element_input).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
            log.warn(f"Cleared value.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Clear value failed. Exception: {e}")

# ================= handle check attribute =================
    def check_disable(self, element):
        """Check attribute disable for 'element'"""
        try:
            css_class = element.get_attribute('class')
            if 'disable' in css_class:
                log.info(f"Attribute 'disable' in class '{css_class}'.")
                return True
            else:
                log.warn(f"Attribute 'disable' NOT in class '{css_class}'.")
                return False
        except:
            log.error(f"Check attribute 'disable' for element '{element}' failed.")

    def click_input_non_tab(self, title):
        """Click of 'input' in screen non tab"""
        xpath = f"//div[contains(@class,'malibu-desktop-uLayout')]/div[contains(@class,'malibu-desktop-uView')]/div[contains(@class,'malibu-desktop-uView-content')]/div[contains(@class,'malibu-desktop-uView-content-main')]/div[contains(@class,'malibu-desktop-uInput')]//legend[@title='{title}']/parent::fieldset/preceding-sibling::input"
        self.common(xpath=xpath, method='unobscured', action='click', info=f"Clicked at '{title}' in screen NON tab.", error=f"Click at '{title}' in screen NON tab failed.")

class FirstTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        global _TEST_BROWSER
        if _TEST_BROWSER is None:
            cls.driver = start_browser()
            _TEST_BROWSER = cls.driver
            cls.started_browser = True
        else: 
            cls.driver = _TEST_BROWSER 
            cls.started_browser = False
        cls().go_to(cls().get_url())
        cls().wait_page_login()
        cls().start_class()
    
    @classmethod
    def tearDownClass(cls):
        global _TEST_BROWSER
        cls().end_class()
        # pass
    
class LastTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        global _TEST_BROWSER
        # cls.driver = _TEST_BROWSER
        # cls.started_browser = False
        # cls().start_class()
        cls.driver = get_driver()
    
    @classmethod
    def tearDownClass(cls):
        global _TEST_BROWSER
        cls().end_class()
        kill_browser()
        # pass