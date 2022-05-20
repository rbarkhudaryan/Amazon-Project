import unittest
from TestCases.LoginTestCases import LoginNegativeTestCase, LogOutTestCase, PasswordNegativeTestCase, SignInTestCase
from TestCases.CartSectionTestCases import AllItemsDeleteTestCase, ItemDeleteTestCase
from TestCases.SearchResultsTestCase import ItemSearchTestCase

class GeneralSuiteClass(unittest.TestSuite):
    def generate_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(SignInTestCase.SignInTestClass('test_sign_in_TC'))
        suite.addTest(LogOutTestCase.LogOutTestClass('test_log_out_TC'))
        suite.addTest(LoginNegativeTestCase.NegativeLogInTestClass('test_negative_log_in_TC'))
        suite.addTest(PasswordNegativeTestCase.NegativePasswordTestClass('test_negative_password_TC'))
        suite.addTest(ItemSearchTestCase.ItemSearchTestClass('test_item_search_TC'))
        suite.addTest(ItemDeleteTestCase.ItemDeleteTestClass('test_item_delete_TC'))
        suite.addTest(AllItemsDeleteTestCase.AllItemsDeleteTestClass('test_all_items_delete_TC'))
        return suite


if __name__ == "__main__":
    suiteObject = GeneralSuiteClass()
    runner = unittest.TextTestRunner()
    runner.run(suiteObject.generate_suite())