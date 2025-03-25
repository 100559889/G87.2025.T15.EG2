import json
import os
import sys
import unittest

# Project's root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(project_root)

from uc3m_money.account_manager import AccountManager


class TestCalculateBalance(unittest.TestCase):
    """Test cases for AccountManager.calculate_balance() with ordered execution"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        print("\n===== Starting Test Suite =====")
        cls.valid_iban = "ES6721000418450200051339"
        cls.invalid_iban = "NL6721000418450200051339"

        # Use absolute paths for files
        cls.test_dir = os.path.dirname(os.path.abspath(__file__))
        cls.transactions_file = os.path.join(cls.test_dir, "transactions.json")
        cls.balance_file = os.path.join(cls.test_dir, "balance.json")

    def setUp(self):
        """Run before each test"""
        self._test_id = self.id().split('.')[-1]
        print(f"\n=== Preparing for {self._test_id} ===")

        # Create fresh transactions file for tests that need it
        if not self._test_id.startswith(("test_3_missing", "test_5_invalid")):
            with open(self.transactions_file, 'w') as f:
                json.dump([
                    {"IBAN": self.valid_iban, "amount": "+100,50"},
                    {"IBAN": "ES7621000418450200051449", "amount": "-200,75"}
                ], f)
            print(f"Created {self.transactions_file}")

    def tearDown(self):
        """Run after each test"""
        print(f"\n=== Cleaning up after {self._test_id} ===")
        if os.path.exists(self.transactions_file):
            os.remove(self.transactions_file)
            print(f"Removed {self.transactions_file}")
        if os.path.exists(self.balance_file):
            os.remove(self.balance_file)
            print(f"Removed {self.balance_file}")

    def test_1_valid_transaction(self):
        """T1: Valid IBAN with matching transaction"""
        print("\nPath: 1_2_3_4_5_6_8_9_10_11")
        print(f"Testing with valid IBAN: {self.valid_iban}")

        result = AccountManager.calculate_balance(self.valid_iban)
        print(f"Result: {result}")
        self.assertTrue(result)

        with open(self.balance_file) as f:
            balance_data = json.loads(f.readlines()[-1])
            print(f"Balance data: {balance_data}")
            self.assertEqual(balance_data["IBAN"], self.valid_iban)
            self.assertAlmostEqual(balance_data["balance"], 100.50)
        print("PASS: Valid transaction processed")

    def test_2_invalid_iban(self):
        """T2: Invalid IBAN format"""
        print("\nPath: 1_15_Exception")
        print(f"Testing invalid IBAN: {self.invalid_iban}")

        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.invalid_iban)
        print(f"Exception: {str(ctx.exception)}")
        self.assertIn("Invalid IBAN", str(ctx.exception))
        print("PASS: Correctly rejected invalid IBAN")

    def test_3_missing_transactions_file(self):
        """T3: Missing transactions.json"""
        print("\nPath: 1_2_13_Exception")
        if os.path.exists(self.transactions_file):
            os.remove(self.transactions_file)
        print("Transactions file removed")

        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        print(f"Exception: {str(ctx.exception)}")
        self.assertIn("Transactions file not found", str(ctx.exception))
        print("PASS: Detected missing file")

    def test_4_missing_balance_file(self):
        """T4: balance.json is removed after test"""
        print("\nPath: 1_2_3_4_5_6_8_9_10_11")
        print(f"Testing with valid IBAN: {self.valid_iban}")

        # First ensure balance.json doesn't exist
        if os.path.exists(self.balance_file):
            os.remove(self.balance_file)

        result = AccountManager.calculate_balance(self.valid_iban)
        print(f"Result: {result}")
        self.assertTrue(result)

        # Verify balance.json was created
        self.assertTrue(os.path.exists(self.balance_file))
        print("PASS: balance.json was created")

        # Verify it contains correct data
        with open(self.balance_file) as f:
            balance_data = json.loads(f.readlines()[-1])
            print(f"Balance data: {balance_data}")
            self.assertEqual(balance_data["IBAN"], self.valid_iban)
        print("PASS: Contains correct data")

    def test_5_invalid_json(self):
        """T5: Invalid JSON format in transactions.json"""
        print("\nPath: 1_2_14_Exception")
        with open(self.transactions_file, 'w') as f:
            f.write("{invalid json")
        print("Created invalid transactions.json")

        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        print(f"Exception: {str(ctx.exception)}")
        self.assertIn("Invalid JSON format", str(ctx.exception))
        print("PASS: Detected invalid JSON")

    def test_6_no_matching_transactions(self):
        """T6: No matching transactions"""
        print("\nPath: 1_2_3_4_5_7_8_9_10_11")
        non_existent_iban = "ES7621000418450200051448"
        print(f"Testing non-existent IBAN: {non_existent_iban}")

        result = AccountManager.calculate_balance(non_existent_iban)
        print(f"Result: {result}")
        self.assertTrue(result)

        with open(self.balance_file) as f:
            balance_data = json.loads(f.readlines()[-1])
            print(f"Balance data: {balance_data}")
            self.assertEqual(balance_data["balance"], 0.0)
        print("PASS: Handled no matches (balance=0)")


if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)