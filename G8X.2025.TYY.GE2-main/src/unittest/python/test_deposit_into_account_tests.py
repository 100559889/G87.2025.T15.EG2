import sys
import os
import unittest

# Add project root to path (corrected to go up 3 levels)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from uc3m_money.account_manager import AccountManager
from uc3m_money.account_management_exception import AccountManagementException



class TestAccountManager(unittest.TestCase):
    def valid_test(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def dup_file(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupFile.json")

    def del_file(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delFile.json")

    def dup_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupBeginObj.json")

    def del_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delBeginObj.json")

    def dup_data(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupData.json")

    def del_data(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delData.json")

    def dup_end_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEndObj.json")

    def del_end_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEndObj.json")

    def mod_begin_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modBeginObj.json")

    def dup_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupField1.json")

    def del_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delField1.json")

    def dup_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupComma.json")

    def del_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delComma.json")

    def dup_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupField2.json")

    def del_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delField2.json")

    def mod_end_obj(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEndObj.json")

    def dup_label_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupLabelField1.json")

    def del_label_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delLabelField1.json")

    def dup_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEquals1.json")

    def del_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEquals1.json")

    def dup_val_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValField1.json")

    def del_val_field1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValField1.json")

    def mod_comma(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modComma.json")

    def dup_label_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupLabelField2.json")

    def del_label_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delLabelField2.json")

    def dup_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEquals2.json")

    def del_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEquals2.json")

    def dup_val_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValField2.json")

    def del_val_field2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValField2.json")

    def dup_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote1.json")

    def del_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote1.json")

    def dup_val_label1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValLabel1.json")

    def del_val_label1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValLabel1.json")

    def dup_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote2.json")

    def del_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote2.json")

    def mod_equals1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEquals1.json")

    def dup_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote3.json")

    def del_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote3.json")

    def dup_val1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupVal1.json")

    def del_val1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delVal1.json")

    def dup_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote4.json")

    def del_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote4.json")

    def dup_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote5.json")

    def del_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote5.json")

    def dup_val_label2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValLabel2.json")

    def del_val_label2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValLabel2.json")

    def dup_quote6(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote6.json")

    def del_quote6(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote6.json")

    def mod_equals2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEquals2.json")

    def dup_quote7(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote7.json")

    def del_quote7(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote7.json")

    def dup_curr(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupCurr.json")

    def del_curr(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delCurr.json")

    def dup_space(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupSpace.json")

    def del_space(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delSpace.json")

    def dup_number(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupNumber.json")

    def del_number(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delNumber.json")

    def dup_quote8(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote8.json")

    def del_quote8(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote8.json")

    def mod_quote1(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote1.json")

    def mod_iban(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modIban.json")

    def mod_quote2(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote2.json")

    def mod_quote3(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote3.json")

    def mod_valid_iban(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modValidIban.json")

    def mod_quote4(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote4.json")

    def mod_quote5(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote5.json")

    def mod_amount(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modAmount.json")

    def mod_quote6(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote6.json")

    def mod_quote7(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote7.json")

    def mod_curr(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modCurr.json")

    def mod_space(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modSpace.json")

    def dup_whole(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupWhole.json")

    def del_whole(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delWhole.json")

    def dup_dot(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupDot.json")

    def del_dot(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delDot.json")

    def dup_dec(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupDec.json")

    def del_dec(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delDec.json")

    def mod_quote8(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote8.json")

    def mod_whole(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modWhole.json")

    def mod_dot(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modDot.json")

    def mod_dec(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modDec.json")

if __name__ == '__main__':
    unittest.main()