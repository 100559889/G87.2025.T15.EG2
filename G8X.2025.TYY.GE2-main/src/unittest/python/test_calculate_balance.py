import json
import os
import sys
import unittest

# Add the project root directory to Python path
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
        cls.transactions_file = os.path.join(os.path.dirname(__file__), "transactions.json")
        cls.balance_file = os.path.join(os.path.dirname(__file__), "balance.json")

    def setUp(self):
        """Run before each test"""
        self._test_id = self.id().split('.')[-1]
        print(f"\n=== Preparing for {self._test_id} ===")

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
        for file in [self.transactions_file, self.balance_file]:
            if os.path.exists(file):
                os.remove(file)
                print(f"Removed {file}")

    def test_1_valid_transaction(self):
        """T1: Valid IBAN with matching transaction"""
        print("\nPath: 1_2_3_4_5_6_8_9_10_11")
        result = AccountManager.calculate_balance(self.valid_iban)
        self.assertTrue(result)
        with open(self.balance_file) as f:
            balance_data = json.loads(f.readlines()[-1])
            self.assertEqual(balance_data["IBAN"], self.valid_iban)
        print("PASS: Valid transaction processed")

    def test_2_invalid_iban(self):
        """T2: Invalid IBAN format"""
        print("\nPath: 1_15_Exception")
        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.invalid_iban)
        self.assertEqual(str(ctx.exception), "The JSON data does not have valid values")
        print("PASS: Correctly rejected invalid IBAN")

    def test_3_missing_transactions_file(self):
        """T3: Missing transactions.json"""
        print("\nPath: 1_2_13_Exception")
        if os.path.exists(self.transactions_file):
            os.remove(self.transactions_file)
        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        self.assertEqual(str(ctx.exception), "The data file is not found")
        print("PASS: Detected missing file")

    def test_4_invalid_json_structure(self):
        """T4: Invalid JSON structure"""
        print("\nPath: 1_2_14_Exception")
        with open(self.transactions_file, 'w') as f:
            json.dump([{"wrong_key": "value"}], f)
        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        self.assertEqual(str(ctx.exception), "The JSON does not have the expected structure")
        print("PASS: Detected invalid structure")

    def test_5_invalid_json_format(self):
        """T5: Invalid JSON format"""
        print("\nPath: 1_2_14_Exception")
        with open(self.transactions_file, 'w') as f:
            f.write("{invalid json")
        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        self.assertEqual(str(ctx.exception), "The file is not in JSON format")
        print("PASS: Detected invalid JSON")

    def test_6_invalid_amount_format(self):
        """T6: Invalid amount format"""
        print("\nPath: 1_2_3_4_5_6_8_9_10_12_Exception")
        with open(self.transactions_file, 'w') as f:
            json.dump([{"IBAN": self.valid_iban, "amount": "invalid"}], f)
        with self.assertRaises(Exception) as ctx:
            AccountManager.calculate_balance(self.valid_iban)
        self.assertEqual(str(ctx.exception), "The JSON data does not have valid values")
        print("PASS: Detected invalid amount")

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)