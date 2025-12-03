from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from webui_test.logging import log
from webui_test.running.config import BrowserConfig, WaitConfig
from time import sleep

class DriverWrapper:
    def __init__(self, *args, driver: WebDriver = None, **kwargs):
        self.driver: WebDriver = driver
        super().__init__(*args, **kwargs)

    def go_to(self, url):
        log.debug("1. Go to 'go_to'")
        BrowserConfig.url_env = url
        if self.driver:
            log.debug('2. vao if self.driver')
            if BrowserConfig.headless:
                log.debug(f'Headless: [{BrowserConfig.headless}]')
                self.driver.set_window_size(1920, 1080)
            else:
                log.debug(f'NO Headless: [{BrowserConfig.headless}]')
                # self.driver.maximize_window()
                self.driver.set_window_size(1920, 1080)
            size = self.driver.get_window_size()
            log.debug(f'3. window size: {size}')
            self.driver.get(url)
            log.debug(f"4. Go to 'go_to' method, url: {url}")
        else:
            log.error("self.driver is NULL.")

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

    def wait(self, seconds=1):
        sleep(seconds)

    def take_screenshot(self, path):
        try:
            result = self.driver.get_screenshot_as_file(path)
            if result:
                log.info(f"Take screenshot '{path}'.")
            else:
                log.error('Take screenshot failed.')
        except Exception as e:
            log.error(f"Error taking screenshot: {e}")

# ================================= Using Selenium 4.x =================================
# -------------------------- Wait Methods --------------------------
# ================= xpath =================
    def wait_for_element_visibility_by_xpath(self, xpath, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            # log.info(f"Element with xpath '{xpath}' visible.")
            return element  # The element is visible
        except TimeoutException:
            log.warn(f"The element with xpath '{xpath}' was NOT visible.")
            return None

    def wait_for_element_enabled_by_xpath(self, xpath, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            # log.info(f"Element with xpath '{xpath}' enabled.")
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
                # log.info(f"Element with xpath '{xpath}' disappeared.")
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
            # location = element.location_once_scrolled_into_view
            # self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
            actions = ActionChains(self.driver)
            element = self.wait_for_element_visibility_by_xpath(xpath, timeout=timeout)
            actions.move_to_element(element).perform()
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        # max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        max_wait_time = timeout  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            element = self.wait_for_element_visibility_by_xpath(xpath, timeout=timeout)
            # is_obscured = self.driver.execute_script("""
            #     var element = arguments[0];
            #     var rect = element.getBoundingClientRect();
            #     var x = rect.left + (rect.width / 2);
            #     var y = rect.top + (rect.height / 2);
            #     return document.elementFromPoint(x, y) !== element;
            # """, element)
            try:
                is_obscured = self.driver.execute_script("""
                    var element = arguments[0];
                    var rect = element.getBoundingClientRect();
                    var x = rect.left + (rect.width / 2);
                    var y = rect.top + (rect.height / 2);
                    return document.elementFromPoint(x, y) !== element;
                """, element)
            except StaleElementReferenceException:
                element = self.wait_for_element_visibility_by_xpath(xpath, timeout=timeout)
                continue

            if is_obscured:
                # log.warn(f"Element with xpath {xpath} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                # log.info(f"Element with xpath '{xpath}' is no longer obscured.")
                break
        if not is_obscured:
            # log.info("Element is unobstructed.")
            return element
        else:
            log.error(f"Element with xpath '{xpath}' is still obscured.")
            return None

    def wait_for_element_by_xpath(self, xpath):
        # Get the element you want to interact with
        # element = self.driver.find_element(By.XPATH, xpath)
        try:
            element = self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return None
            
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
            # is_obscured = self.driver.execute_script("""
            #     var element = arguments[0];
            #     var rect = element.getBoundingClientRect();
            #     var x = rect.left + (rect.width / 2);
            #     var y = rect.top + (rect.height / 2);
            #     return document.elementFromPoint(x, y) !== element;
            # """, element)
            try:
                is_obscured = self.driver.execute_script("""
                    var element = arguments[0];
                    var rect = element.getBoundingClientRect();
                    var x = rect.left + (rect.width / 2);
                    var y = rect.top + (rect.height / 2);
                    return document.elementFromPoint(x, y) !== element;
                """, element)
            except StaleElementReferenceException:
                 # If stale, try to find again, or just break/continue
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    continue
                except:
                    break

            if is_obscured:
                # log.warn(f"Element with xpath {xpath} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                # log.info(f"Element with xpath '{xpath}' is no longer obscured.")
                break
        if not is_obscured:
            # log.info("Element is unobstructed.")
            return element
        else:
            log.error(f"Element with xpath '{xpath}' is still obscured.")
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
            return False

# ================= css =================
    def wait_for_element_visibility_by_css(self, css_selector, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            # log.info(f"Element with CSS selector '{css_selector}' visible.")
            return element  # The element is visible
        except TimeoutException:
            log.warn(f"Element with CSS selector '{css_selector}' was NOT visible.")
            return None

    def wait_for_element_enabled_by_css(self, css_selector, timeout=WaitConfig.timeout_explicit):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            # log.info(f"Element with CSS selector '{css_selector}' enabled.")
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
                # log.info(f"Element with CSS selector '{css_selector}' disappeared.")
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
            # location = element.location_once_scrolled_into_view
            # self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
            actions = ActionChains(self.driver)
            element = self.wait_for_element_visibility_by_css(css_selector, timeout=timeout)
            actions.move_to_element(element).perform()
        # While loop to wait until the element is no longer obscured
        is_obscured = True
        # max_wait_time = WaitConfig.timeout_explicit  # Max time to wait (in seconds)
        max_wait_time = timeout  # Max time to wait (in seconds)
        elapsed_time = 0
        interval = 1  # Time to wait between checks (in seconds)
        while is_obscured and elapsed_time < max_wait_time:
            # Execute the JavaScript to check if the element is obscured
            element = self.wait_for_element_visibility_by_css(css_selector, timeout=timeout)
            # is_obscured = self.driver.execute_script("""
            #     var element = arguments[0];
            #     var rect = element.getBoundingClientRect();
            #     var x = rect.left + (rect.width / 2);
            #     var y = rect.top + (rect.height / 2);
            #     return document.elementFromPoint(x, y) !== element;
            # """, element)
            try:
                is_obscured = self.driver.execute_script("""
                    var element = arguments[0];
                    var rect = element.getBoundingClientRect();
                    var x = rect.left + (rect.width / 2);
                    var y = rect.top + (rect.height / 2);
                    return document.elementFromPoint(x, y) !== element;
                """, element)
            except StaleElementReferenceException:
                element = self.wait_for_element_visibility_by_css(css_selector, timeout=timeout)
                continue

            if is_obscured:
                # log.warn(f"Element with CSS selector {css_selector} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                # log.info(f"Element with CSS selector '{css_selector}' is no longer obscured.")
                break
        if not is_obscured:
            # log.info("Element is unobstructed.")
            return element # return True
        else:
            log.error(f"Element with CSS selector '{css_selector}' is still obscured.")
            return None # return False

    def wait_for_element_by_css(self, css_selector):
        # Get the element you want to interact with
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            return None
            
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
            try:
                is_obscured = self.driver.execute_script("""
                    var element = arguments[0];
                    var rect = element.getBoundingClientRect();
                    var x = rect.left + (rect.width / 2);
                    var y = rect.top + (rect.height / 2);
                    return document.elementFromPoint(x, y) !== element;
                """, element)
            except StaleElementReferenceException:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
                    continue
                except:
                    break

            if is_obscured:
                # log.warn(f"Element with css_selector {css_selector} is still obscured after {elapsed_time} seconds, waiting...")
                self.wait(interval)  # Wait for the specified interval before checking again
                elapsed_time += interval
            else:
                # log.info(f"Element with css_selector '{css_selector}' is no longer obscured.")
                break
        if not is_obscured:
            # log.info("Element is unobstructed.")
            return element
        else:
            log.error(f"Element with css_selector '{css_selector}' is still obscured.")
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
            return False

    # -------------------------- Common Interaction --------------------------
    def key_escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()

    def key_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()

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

# ================= handle clear_text field =================
    # def clear_text(self, element: WebElement):
    #     element.clear()
    #     # If text remains, try Ctrl+A + Delete (common fallback)
    #     if element.get_attribute('value'):
    #         element.send_keys(Keys.CONTROL + "a")
    #         element.send_keys(Keys.DELETE)

    def clear_text(self, element_input: WebElement):
        """Clear text for element 'input'"""
        self.key_escape()
        self.switch_to_core_banking()
        self.driver.execute_script("arguments[0].focus();", element_input)
        self.wait(0.1)
        try:
            actions = ActionChains(self.driver)
            actions.click(element_input).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
            # log.warn(f"Cleared value.")
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Clear value failed. Exception: {e}")

# ================= handle check attribute =================
    def check_disable(self, element: WebElement):
        """Check attribute disable for 'element'"""
        try:
            css_class = element.get_attribute('class')
            if 'disable' in css_class:
                # log.info(f"Attribute 'disable' in class '{css_class}'.")
                return True
            else:
                # log.warn(f"Attribute 'disable' NOT in class '{css_class}'.")
                return False
        except:
            log.error(f"Check attribute 'disable' for element '{element}' failed.")

    def check_disabled_field(self, element: WebElement):
        """Check attribute disabled for 'element' is field"""
        try:
            css_class = element.get_attribute('class')
            if 'disabled' in css_class:
                # log.info(f"Attribute 'disabled' in class '{css_class}'.")
                return True
            else:
                # log.warn(f"Attribute 'disabled' NOT in class '{css_class}'.")
                return False
        except:
            log.error(f"Check attribute 'disabled' for element '{element}' failed.")

    def common(self, xpath=None, css=None, method=None, action=None, value=None, clear_text=None, need_tab=None, need_enter=None, info=None, error=None, warn=None, timeout=WaitConfig.timeout_explicit):
        """
        Performs a common interaction with a web element based on provided locators and actions.

        Args:
            xpath (str, optional): XPath locator for the element.
            css (str, optional): CSS selector for the element.
            method (str, optional): Waiting method for the element.
                Possible values: 'unobscured', 'visibility', 'enabled'.
            action (str, optional): Action to perform on the element.
                Possible values: 'send_keys', 'click', 'get_text', 'get_value', 'send_values'.
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
        max_retries = 3
        for attempt in range(max_retries):
            try:
                element = get_element()
                if element is None:
                    if error:
                        log.error(error)
                    if warn:
                        log.warn(warn)
                    return None
                if action == 'send_keys':
                    if clear_text == 'Y':
                        self.clear_text(element)
                        if element.text != '':
                            self.clear_text(element)
                    element.send_keys(value)
                    if need_tab == 'Y':
                        element.send_keys(Keys.TAB)
                    if need_enter == 'Y':
                        element.send_keys(Keys.ENTER)
                    if info:
                        log.info(info)
                    return None
                elif action == 'click':
                    element.click()
                    if info:
                        log.info(info)
                    return None
                elif action == 'get_text':
                    # if info:
                    #     log.info(info)
                    return element.text
                elif action == 'get_value':
                    # if info:
                    #     log.info(info)
                    return element.get_attribute('value')
                elif action == 'send_values':
                    # clear data
                    self.driver.execute_script("arguments[0].value = '';", element)
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", element)
                    log.debug('Clear data.')
                    actions = ActionChains(self.driver)
                    actions.click(element).send_keys(value).perform()
                    log.debug(f"element.get_attribute('value') is: {element.get_attribute('value')}")
                    if element.get_attribute('value') != value:
                        self.driver.execute_script("arguments[0].value = '';", element)
                        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
                        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", element)
                        log.debug("Clear data again in get_attribute('value').")
                        actions = ActionChains(self.driver)
                        actions.click(element).send_keys(value).perform()
                    if info:
                        log.info(info)
                    return None
                break 
            except StaleElementReferenceException:
                if attempt < max_retries - 1:
                    log.debug(f"Encountered StaleElementReferenceException. Retrying... (Times {attempt + 1})")
                    self.wait(0.5)
                    continue
                else:
                    log.error(f"Unable to operate on element due to Stale error after {max_retries} attempts.")
                    return None
            except Exception as e:
                log.error(f"Exception: {str(e)}")
                return None
        return None

    # -------------------------- New Methods gen by BOT --------------------------
    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            log.info("Accepted alert.")
        except TimeoutException:
            log.warn("No alert to accept.")

    def dismiss_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.dismiss()
            log.info("Dismissed alert.")
        except TimeoutException:
            log.warn("No alert to dismiss.")

    def switch_to_frame(self, frame_reference):
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))
            log.info(f"Switched to frame: {frame_reference}")
        except TimeoutException:
            log.error(f"Could not switch to frame: {frame_reference}")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        log.info("Switched to default content.")
