

import unittest
from SeleniumPythonRefactorTestCase import SearchText
from SeleniumPythonMultipleTests import HomePageTest
from unittest import TestLoader, TestSuite, TextTestRunner

# get all tests from SearchText and HomePageTest class

# load the tests
# tests = unittest.TestLoader();
# search_text = tests.loadTestsFromTestCase(SearchText)
# home_page_test = tests.loadTestsFromTestCase(HomePageTest)
#
# # create a test suite combining search_text and home_page_test
# test_suite = unittest.TestSuite([home_page_test, search_text])
#
# # run the suite
# unittest.TextTestRunner(verbosity=2).run(test_suite)


	# create the suite from the test classes
suite = TestSuite()
    # load the tests
tests = unittest.TestLoader()

	# add the tests to the suite
suite.addTests(tests.loadTestsFromTestCase(SearchText))
suite.addTests(tests.loadTestsFromTestCase(HomePageTest))

    # run the suite
runner = unittest.TextTestRunner()
runner.run(suite)
if __name__ == '__main__':
    unittest.main()


