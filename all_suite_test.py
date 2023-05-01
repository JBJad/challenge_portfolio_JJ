import unittest

from unittest.loader import makeSuite

from test_cases.failed_login_to_the_system import FailedTestLoginPage
from test_cases.filling_out_add_a_player_form import TestAddingAPlayer
from test_cases.login_to_the_system import TestLoginPage
from test_cases.negative_filling_out_add_a_player_form import NegativeTestAddingAPlayer
from test_cases.test_adding_a_player import TestClickingOnAddAPlayer


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(FailedTestLoginPage))
    test_suite.addTest(makeSuite(TestAddingAPlayer))
    test_suite.addTest(makeSuite(NegativeTestAddingAPlayer))
    test_suite.addTest(makeSuite(TestClickingOnAddAPlayer))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
