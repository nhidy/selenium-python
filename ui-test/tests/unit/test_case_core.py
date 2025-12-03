import unittest
from unittest.mock import MagicMock, patch, ANY, call
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from webui_test.case import TestCase
from webui_test.wrapper import DriverWrapper

class TestCoreFramework(unittest.TestCase):

    def setUp(self):
        self.mock_driver = MagicMock()
        # Patch get_driver to return our mock
        self.patcher = patch('webui_test.case.get_driver', return_value=self.mock_driver)
        self.patcher.start()
        
        # We need to mock start_browser as well if it's called
        self.patcher_start = patch('webui_test.case.start_browser', return_value=self.mock_driver)
        self.patcher_start.start()

        self.test_case = TestCase(methodName='runTest')
        self.test_case.driver = self.mock_driver

    def tearDown(self):
        self.patcher.stop()
        self.patcher_start.stop()

    @patch('webui_test.wrapper.WebDriverWait')
    def test_common_xpath_click(self, mock_wait):
        """Test common method with xpath and click action"""
        mock_element = MagicMock()
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        self.test_case.common(xpath="//div[@id='test']", action="click", method="visibility")
        
        mock_element.click.assert_called_once()

    @patch('webui_test.wrapper.WebDriverWait')
    def test_common_css_send_keys(self, mock_wait):
        """Test common method with css and send_keys action"""
        mock_element = MagicMock()
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        self.test_case.common(css=".my-input", action="send_keys", value="hello", method="visibility")
        
        mock_element.send_keys.assert_any_call("hello")

    @patch('webui_test.wrapper.WebDriverWait')
    def test_common_element_not_found(self, mock_wait):
        """Test common method when element is not found"""
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.side_effect = TimeoutException("Element not found")
        
        result = self.test_case.common(xpath="//missing", action="click", method="visibility")
        
        self.assertIsNone(result)

    @patch('webui_test.wrapper.DriverWrapper.common')
    def test_click_button(self, mock_common):
        """Test click_button wrapper calls common correctly"""
        self.test_case.click_button("Save")
        
        mock_common.assert_called_with(
            xpath=ANY, 
            method='unobscured', 
            action='click', 
            info="Clicked on 'Save' button.", 
            error=ANY
        )

    @patch('webui_test.wrapper.WebDriverWait')
    def test_common_get_text(self, mock_wait):
        """Test common method with get_text action"""
        mock_element = MagicMock()
        mock_element.text = "Sample Text"
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        result = self.test_case.common(xpath="//div", action="get_text", method="visibility")
        
        self.assertEqual(result, "Sample Text")

    @patch('webui_test.wrapper.WebDriverWait')
    def test_common_get_value(self, mock_wait):
        """Test common method with get_value action"""
        mock_element = MagicMock()
        mock_element.get_attribute.return_value = "Sample Value"
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        result = self.test_case.common(xpath="//input", action="get_value", method="visibility")
        
        self.assertEqual(result, "Sample Value")
        mock_element.get_attribute.assert_called_with('value')

    @patch('webui_test.wrapper.WebDriverWait')
    def test_wait_for_element_visibility(self, mock_wait):
        """Test wait_for_element_visibility_by_xpath"""
        mock_element = MagicMock()
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        result = self.test_case.wait_for_element_visibility_by_xpath("//div")
        
        self.assertEqual(result, mock_element)

    @patch('webui_test.wrapper.WebDriverWait')
    def test_wait_for_element_enabled(self, mock_wait):
        """Test wait_for_element_enabled_by_xpath"""
        mock_element = MagicMock()
        mock_wait_instance = mock_wait.return_value
        mock_wait_instance.until.return_value = mock_element
        
        result = self.test_case.wait_for_element_enabled_by_xpath("//button")
        
        self.assertEqual(result, mock_element)

    # New tests for DriverWrapper methods
    @patch('webui_test.wrapper.WebDriverWait')
    def test_accept_alert(self, mock_wait):
        """Test accept_alert"""
        mock_wait_instance = mock_wait.return_value
        # alert_is_present returns a condition, until returns the alert object usually, 
        # but here until returns True/False or the alert? 
        # EC.alert_is_present() returns the alert object if present.
        
        self.test_case.driver.switch_to.alert = MagicMock()
        
        self.test_case.accept_alert()
        
        self.test_case.driver.switch_to.alert.accept.assert_called_once()

    @patch('webui_test.wrapper.WebDriverWait')
    def test_dismiss_alert(self, mock_wait):
        """Test dismiss_alert"""
        self.test_case.driver.switch_to.alert = MagicMock()
        
        self.test_case.dismiss_alert()
        
        self.test_case.driver.switch_to.alert.dismiss.assert_called_once()

    @patch('webui_test.wrapper.WebDriverWait')
    def test_switch_to_frame(self, mock_wait):
        """Test switch_to_frame"""
        self.test_case.switch_to_frame("frame_id")
        
        # EC.frame_to_be_available_and_switch_to_it returns a condition.
        # WebDriverWait.until calls the condition.
        # We just check if WebDriverWait was called correctly.
        mock_wait.assert_called()

    def test_switch_to_default_content(self):
        """Test switch_to_default_content"""
        self.test_case.switch_to_default_content()
        self.test_case.driver.switch_to.default_content.assert_called_once()

if __name__ == '__main__':
    unittest.main()
