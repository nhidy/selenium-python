import sys
import os
import unittest
from unittest.mock import MagicMock

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Mock selenium to avoid browser startup
sys.modules['selenium'] = MagicMock()
sys.modules['selenium.webdriver'] = MagicMock()
sys.modules['selenium.webdriver.common.by'] = MagicMock()
sys.modules['selenium.webdriver.common.keys'] = MagicMock()
sys.modules['selenium.webdriver.common.action_chains'] = MagicMock()
sys.modules['selenium.webdriver.support.ui'] = MagicMock()
sys.modules['selenium.webdriver.support'] = MagicMock()
sys.modules['selenium.common.exceptions'] = MagicMock()

# Mock jwebui_action because it imports selenium
sys.modules['webui_test.jwebui_action'] = MagicMock()

try:
    from webui_test.form_action import FormAction
    print("Successfully imported FormAction")
except ImportError as e:
    print(f"Failed to import FormAction: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred during import: {e}")
    sys.exit(1)

class TestFormActionStructure(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(FormAction)
        print("Successfully imported FormAction")

    def test_methods_exist(self):
        # Check for methods from different mixins
        self.assertTrue(hasattr(FormAction, 'csh_mov'), "csh_mov should exist (from CashActions)")
        self.assertTrue(hasattr(FormAction, 'dpt_opn'), "dpt_opn should exist (from DepositActions)")
        self.assertTrue(hasattr(FormAction, 'common'), "common should exist (from TestCase/CommonActions)")
        self.assertTrue(hasattr(FormAction, 'transaction_view'), "transaction_view should exist")
        self.assertTrue(hasattr(FormAction, 'check_transaction'), "check_transaction should exist")
        self.assertTrue(hasattr(FormAction, 'add_fees'), "add_fees should exist")
        
    def test_inheritance(self):
        from webui_test.case import TestCase
        self.assertTrue(issubclass(FormAction, TestCase), "FormAction should inherit from TestCase")

    def test_attributes(self):
        # Check for methods from Mixins
        self.assertTrue(hasattr(FormAction, 'deposit_catalogue_definition_add_verify'), "Should have deposit method")
        self.assertTrue(hasattr(FormAction, 'credit_catalogue_definition_add_verify'), "Should have credit method")
        self.assertTrue(hasattr(FormAction, 'bo_approval_search'), "Should have common bo method")
        # Check for methods from FormAction
        self.assertTrue(hasattr(FormAction, 'simple_search_f8'), "Should have FormAction method")

if __name__ == '__main__':
    unittest.main()
