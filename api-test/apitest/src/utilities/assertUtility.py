import logging as logger 
import json
import pandas as pd
from decimal import Decimal
from typing import List
from colorama import Fore, Style
from tabulate import tabulate

class AssertUtility(object):

    def assert_equals(assert_key, expected, actual, description=None):
        if description is None:
            assert expected == actual, f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{actual}]."
        else: 
            assert expected == actual, f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{actual}]. {description}"

    def assert_not_equals(assert_key, expected, actual, description=None):
        if description is None:
            assert expected != actual, f"value of [{assert_key}].\nExpected NOT: [{expected}].\nActual: [{actual}]."
        else:
            assert expected != actual, f"value of [{assert_key}].\nExpected NOT: [{expected}].\nActual: [{actual}]. {description}"

    def assert_null(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual is None, f"Expected: value of [{assert_key}] is NULL."
        else:
            assert data_actual is None, f"Expected: value of [{assert_key}] is NULL. {description}"

    def assert_not_null(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual is not None, f"Expected: value of [{assert_key}] is NOT NULL."
        else:
            assert data_actual is not None, f"Expected: value of [{assert_key}] is NOT NULL. {description}"

    def assert_empty(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual == '', f"Expected: value of [{assert_key}] is EMPTY."
        else:
            data_actual == '', f"Expected: value of [{assert_key}] is EMPTY. {description}"

    def assert_not_empty(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual != '', f"Expected: value of [{assert_key}] is NOT EMPTY."
        else:
            assert data_actual != '', f"Expected: value of [{assert_key}] is NOT EMPTY. {description}"

    def assert_true(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual is True, f"Expected: value of [{assert_key}] is TRUE."
        else:
            assert data_actual is True, f"Expected: value of [{assert_key}] is TRUE. {description}"

    def assert_false(assert_key, data_actual, description=None):
        if description is None:
            assert data_actual is False, f"Expected: value of [{assert_key}] is FALSE."
        else:
            assert data_actual is False, f"Expected: value of [{assert_key}] is FALSE. {description}"

    def assert_exists(assert_keys, data_actual):
        """
        Asserts that all keys in `assert_keys` exist in `data_actual`. 
        Logs missing keys and raises a combined error if any are missing.
        
        Parameters:
        - assert_keys: str or list of keys to check.
        - data_actual: dict or similar object to verify keys exist in.
        
        Raises:
        - AssertionError if any key is missing.
        """
        # Ensure assert_keys is a list
        if isinstance(assert_keys, str):
            assert_keys = [assert_keys]
        missing_keys = []  # To store missing keys
        # Check for each key
        for key in assert_keys:
            if key not in data_actual:
                print(f"Missing key: [{key}]")  # Log missing key
                missing_keys.append(key)
        # Raise error if there are missing keys
        if missing_keys:
            missing_keys_str = ", ".join(missing_keys)
            raise AssertionError(f"Expected keys missing: {missing_keys_str}")

    def equals_decimal(assert_key, expected, before_actual, after_actual, description=None):
        if description is None:
            assert Decimal(str(expected)) == (Decimal(str(after_actual)) - Decimal(str(before_actual))), f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{after_actual}] - [{before_actual}]."
        else: 
            assert Decimal(str(expected)) == (Decimal(str(after_actual)) - Decimal(str(before_actual))), f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{after_actual}] - [{before_actual}]. {description}"

    def equals_date(assert_key, expected, actual, description=None):
        if description is None:
            assert pd.Timestamp(expected) == pd.Timestamp(actual), f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{actual}]."
        else: 
            assert pd.Timestamp(expected) == pd.Timestamp(actual), f"value of [{assert_key}].\nExpected: [{expected}].\nActual: [{actual}]. {description}"

    def db_compare_results(table_name: str, data_before: pd.DataFrame, data_after: pd.DataFrame) -> List[str]:
        """
        Compares the differences between two dataframes for a given table name and returns the list of columns with differences.

        Args:
            table_name (str): The name of the table being compared.
            data_before (pd.DataFrame): The dataframe before the update.
            data_after (pd.DataFrame): The dataframe after the update.

        Returns:
            List[str]: A list of column names with differences.
        """
        print('Compare results of table: ', table_name)
        differences = data_before.compare(data_after)
        # Collect columns with differences
        different_columns = list(differences.columns.get_level_values(0).unique())
        # Prepare data for tabular display
        table_data = []
        for col in different_columns:
            before = differences.loc[0, (col, 'self')]
            after = differences.loc[0, (col, 'other')]
            table_data.append([col, before, after])
            # print(f"  Column [{col}]: \tBefore = {before}, \tAfter = {after}")
        # Print the table
        print(tabulate(table_data, headers=["Column", "Before", "After"], tablefmt="grid"))
        return different_columns

    def db_compare_columns(expected_columns, diff_columns):
        """
        Compares two lists of columns and asserts if there are unexpected or missing columns,
        ignoring the order of columns.

        Args:
            expected_columns (list): List of expected column names.
            diff_columns (list): List of columns with differences.

        Returns:
            list: Matched columns if assertions pass.
        """
        # Convert to sets for comparison
        expected_set = set(expected_columns)
        diff_set = set(diff_columns)
        # Find matches, unexpected, and missing columns
        matches = list(expected_set & diff_set)  # Intersection
        unexpected = list(diff_set - expected_set)  # In diff_columns but not in expected_columns
        missing = list(expected_set - diff_set)  # In expected_columns but not in diff_columns
        # Print results with colors
        print(f"{Fore.GREEN}Matched Columns: {matches}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Unexpected Columns: {unexpected}{Style.RESET_ALL}")
        print(f"{Fore.RED}Missing Expected Columns: {missing}{Style.RESET_ALL}")
        # Assert conditions
        assert not unexpected, f"Unexpected columns found: {unexpected}"
        assert not missing, f"Missing expected columns: {missing}"

        # Return matched columns if assertions pass
        return matches

    def db_compare_amount(column_name: str, expected, data_before: pd.DataFrame, data_after: pd.DataFrame, row=0):
        # database - verify value update - o9deposit - DepositAccount - Prepaid FD
        data_before_by_column = data_before[column_name][row]
        data_after_by_column =data_after[column_name][row]
        AssertUtility.equals_decimal(column_name, expected, abs(data_before_by_column), abs(data_after_by_column))

    def db_compare_date(column_name: str, expected, data_after: pd.DataFrame, row=0):
        data_after_by_column = data_after[column_name][row]
        AssertUtility.equals_date(column_name, expected, data_after_by_column)

    def db_compare_value(column_name: str, expected, data_after: pd.DataFrame, row=0):
        data_after_by_column = data_after[column_name][row]
        AssertUtility.assert_equals(column_name, expected, data_after_by_column)
