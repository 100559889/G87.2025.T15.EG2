import sys
import os
import unittest

# Add project root to path (corrected to go up 3 levels)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from uc3m_money.account_manager import AccountManager
from uc3m_money.account_management_exception import AccountManagementException

class TestAccountManager(unittest.TestCase):
    """Valid test"""
    def test_valid(self):
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("mytest.json")

    def test_dup_file(self):
        """Duplicate entire file"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupFile.json")

    def test_del_file(self):
        """Delete entire file"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delFile.json")

    def test_dup_begin_obj(self):
        """Duplicate the first bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupBeginObj.json")

    def test_del_begin_obj(self):
        """Delete the first bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delBeginObj.json")

    def test_dup_data(self):
        """Duplicate the data"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupData.json")

    def test_del_data(self):
        """Delete the data"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delData.json")

    def test_dup_end_obj(self):
        """Duplicate the final bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEndObj.json")

    def test_del_end_obj(self):
        """Delete the final bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEndObj.json")

    def test_mod_begin_obj(self):
        """Modify first bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modBeginObj.json")

    def test_dup_field1(self):
        """Duplicate field1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupField1.json")

    def test_del_field1(self):
        """Delete field1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delField1.json")

    def test_dup_comma(self):
        """Duplicate the comma"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupComma.json")

    def test_del_comma(self):
        """Delete the comma"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delComma.json")

    def test_dup_field2(self):
        """Duplicate field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupField2.json")

    def test_del_field2(self):
        """Delete field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delField2.json")

    def test_mod_end_obj(self):
        """Modify the final bracket"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEndObj.json")

    def test_dup_label_field1(self):
        """Duplicate label for field1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupLabelField1.json")

    def test_del_label_field1(self):
        """Delete label for field 1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delLabelField1.json")

    def test_dup_equals1(self):
        """Duplicate first equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEquals1.json")

    def test_del_equals1(self):
        """Delete first equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEquals1.json")

    def test_dup_val_field1(self):
        """Duplicate value for field1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValField1.json")

    def test_del_val_field1(self):
        """Delete value for field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValField1.json")

    def test_mod_comma(self):
        """Modify the comma"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modComma.json")

    def test_dup_label_field2(self):
        """Duplicate label for field 2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupLabelField2.json")

    def test_del_label_field2(self):
        """Delete label for field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delLabelField2.json")

    def test_dup_equals2(self):
        """Duplicate second equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupEquals2.json")

    def test_del_equals2(self):
        """Delete second equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delEquals2.json")

    def test_dup_val_field2(self):
        """Duplicate value for field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValField2.json")

    def test_del_val_field2(self):
        """Delete value for field2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValField2.json")

    def test_dup_quote1(self):
        """Duplicate first quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote1.json")

    def test_del_quote1(self):
        """Delete first quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote1.json")

    def test_dup_val_label1(self):
        """Duplicate value for label1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValLabel1.json")

    def test_del_val_label1(self):
        """Delete value for label1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValLabel1.json")

    def test_dup_quote2(self):
        """Duplicate second quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote2.json")

    def test_del_quote2(self):
        """Delete second quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote2.json")

    def test_mod_equals1(self):
        """Modify first equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEquals1.json")

    def test_dup_quote3(self):
        """Duplicate third quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote3.json")

    def test_del_quote3(self):
        """Delete third quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote3.json")

    def test_dup_val1(self):
        """Duplicate value1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupVal1.json")

    def test_del_val1(self):
        """Delete value1"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delVal1.json")

    def test_dup_quote4(self):
        """Duplicate fourth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote4.json")

    def test_del_quote4(self):
        """Delete fourth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote4.json")

    def test_dup_quote5(self):
        """Duplicate fifth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote5.json")

    def test_del_quote5(self):
        """Delete fifth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote5.json")

    def test_dup_val_label2(self):
        """Duplicate value for label2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupValLabel2.json")

    def test_del_val_label2(self):
        """Delete value for label2"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delValLabel2.json")

    def test_dup_quote6(self):
        """Duplicate sixth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote6.json")

    def test_del_quote6(self):
        """Delete sixth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote6.json")

    def test_mod_equals2(self):
        """Modify second equals"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modEquals2.json")

    def test_dup_quote7(self):
        """Duplicate seventh quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote7.json")

    def test_del_quote7(self):
        """Delete seventh quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote7.json")

    def test_dup_curr(self):
        """Duplicate currency"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupCurr.json")

    def test_del_curr(self):
        """Delete currency"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delCurr.json")

    def test_dup_space(self):
        """Duplicate the space"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupSpace.json")

    def test_del_space(self):
        """Delete the space"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delSpace.json")

    def test_dup_number(self):
        """Duplicate number"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupNumber.json")

    def test_del_number(self):
        """Delete number"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delNumber.json")

    def test_dup_quote8(self):
        """Duplicate eighth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupQuote8.json")

    def test_del_quote8(self):
        """Delete eighth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delQuote8.json")

    def test_mod_quote1(self):
        """Modify first quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote1.json")

    def test_mod_iban(self):
        """Modify the IBAN"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modIban.json")

    def test_mod_quote2(self):
        """Modify the second quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote2.json")

    def test_mod_quote3(self):
        """Modify the third quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote3.json")

    def test_mod_valid_iban(self):
        """Modify the valid IBAN"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modValidIban.json")

    def test_mod_quote4(self):
        """""Modify fourth quote"""""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote4.json")

    def test_mod_quote5(self):
        """Modify fifth quote"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote5.json")

    def test_mod_amount(self):
        """Modify the amount"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modAmount.json")

    def test_mod_quote6(self):
        """Modify the sixth quote"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote6.json")

    def test_mod_quote7(self):
        """Modify the seventh quote"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote7.json")

    def test_mod_curr(self):
        """Modify the currency"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modCurr.json")

    def test_mod_space(self):
        """Modify the space"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modSpace.json")

    def test_dup_whole(self):
        """Duplicate whole numbers"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupWhole.json")

    def test_del_whole(self):
        """Delete whole numbers"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delWhole.json")

    def test_dup_dot(self):
        """Duplicate decimal point"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupDot.json")

    def test_del_dot(self):
        """Delete the decimal point"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delDot.json")

    def test_dup_dec(self):
        """Duplicate decimal numbers"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("dupDec.json")

    def test_del_dec(self):
        """Delete the decimal numbers"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("delDec.json")

    def test_mod_quote8(self):
        """Modify eighth quotation"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modQuote8.json")

    def test_mod_whole(self):
        """Modify whole numbers"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modWhole.json")

    def test_mod_dot(self):
        """Modify decimal point"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modDot.json")

    def test_mod_dec(self):
        """Modify decimal points"""
        manager = AccountManager()
        with self.assertRaises(AccountManagementException):
            manager.deposit_into_account("modDec.json")

if __name__ == '__main__':
    unittest.main()