import unittest
from uc3m_money import AccountManager, AccountManagementException

class TestAccountManager(unittest.TestCase):
    def valid_test(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_file(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_file(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_data(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_data(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_end_object(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_end_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_end_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_label_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_label_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_val_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_val_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_label_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_label_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_val_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_val_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_val_label1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_val_label1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_val1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_val1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_val_label2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_val_label2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote6(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote6(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote7(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote7(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_curr(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_curr(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_space(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_space(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_number(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_number(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_quote8(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def del_quote8(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_iban(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_valid_iban(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def mod_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

if __name__ == '__main__':
    unittest.main()