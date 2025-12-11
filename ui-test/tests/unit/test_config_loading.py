import unittest
import json
import os
import sys
import argparse
from unittest.mock import patch, mock_open

# Add the parent directory to sys.path to import run_by_api
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from tests import run_by_api

class TestConfigLoading(unittest.TestCase):
    def setUp(self):
        self.config_data = {
            "release_version": "1.0",
            "server_name": "TEST_SERVER",
            "browser": "chrome"
        }
        self.config_json = json.dumps(self.config_data)

    def test_load_config_valid(self):
        """Test loading a valid JSON config file."""
        with patch("builtins.open", mock_open(read_data=self.config_json)):
            loaded_config = run_by_api.load_config_from_file("dummy_path.json")
            self.assertEqual(loaded_config, self.config_data)

    def test_load_config_file_not_found(self):
        """Test loading a non-existent config file."""
        with self.assertRaises(FileNotFoundError):
            run_by_api.load_config_from_file("non_existent_file.json")

    def test_load_config_invalid_json(self):
        """Test loading an invalid JSON file."""
        with patch("builtins.open", mock_open(read_data="{invalid_json")):
            with self.assertRaises(json.JSONDecodeError):
                run_by_api.load_config_from_file("dummy_path.json")

    def test_str_to_bool(self):
        """Test str_to_bool function."""
        self.assertTrue(run_by_api.str_to_bool(True))
        self.assertFalse(run_by_api.str_to_bool(False))
        self.assertTrue(run_by_api.str_to_bool("true"))
        self.assertTrue(run_by_api.str_to_bool("True"))
        self.assertTrue(run_by_api.str_to_bool("yes"))
        self.assertTrue(run_by_api.str_to_bool("y"))
        self.assertFalse(run_by_api.str_to_bool("false"))
        self.assertFalse(run_by_api.str_to_bool("False"))
        self.assertFalse(run_by_api.str_to_bool("no"))
        self.assertFalse(run_by_api.str_to_bool("n"))
        self.assertFalse(run_by_api.str_to_bool(None))
        self.assertFalse(run_by_api.str_to_bool("null"))
        self.assertFalse(run_by_api.str_to_bool(""))
        
        with self.assertRaises(argparse.ArgumentTypeError):
            run_by_api.str_to_bool("invalid")

    def test_parse_test_files(self):
        """Test parse_test_files function."""
        # Test with list
        config_list = {"test_files": ["test1", "test2"]}
        self.assertEqual(run_by_api.parse_test_files(config_list), ["test1", "test2"])
        
        # Test with string
        config_str = {"test_files": "test1, test2, test3"}
        self.assertEqual(run_by_api.parse_test_files(config_str), ["test1", "test2", "test3"])
        
        # Test with empty
        config_empty = {}
        self.assertEqual(run_by_api.parse_test_files(config_empty), [])
        
        # Test with None
        config_none = {"test_files": None}
        self.assertEqual(run_by_api.parse_test_files(config_none), [])

if __name__ == '__main__':
    unittest.main()
