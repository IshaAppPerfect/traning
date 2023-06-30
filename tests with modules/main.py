

import unittest

from unittest import TestLoader, TestSuite

from SeleniumPythonMultipleTests.HomePageTest import HomePageTest
# from SeleniumPythonRefactorTestCase.SearchText import SearchText

# from SeleniumPythonRefactorTestCase import SearchText


# class SearchText(unittest.TestCase):
#     @classmethod
#     def setUp(inst):
#         # create a new Firefox session """
#         inst.driver = webdriver.Edge()
#         inst.driver.implicitly_wait(30)
#         inst.driver.maximize_window()
#
#         # navigate to the application home page """
#         inst.driver.get("http://www.google.com/")
#
#     def test_search_by_text(self):
#         # get the search textbox
#         self.search_field = self.driver.find_element(By.NAME, "q")
#         self.search_field.clear()
#         # enter search keyword and submit
#         self.search_field.send_keys("Selenium Webdriver interview questions")
#         self.search_field.submit()
#         # get the list of elements which are displayed after the search
#         # currently on result page using find_elements_by_class_name method
#         lists = self.driver.find_elements(By.CLASS_NAME, "r")
#         self.assertEqual(11, len(lists))
#
#     def test_search_by_name(self):
#         # get the search textbox
#         self.search_field = self.driver.find_element(By.NAME, "q")
#         # enter search keyword and submit
#         self.search_field.send_keys("Python class")
#         self.search_field.submit()
#         # get the list of elements which are displayed after the search
#         # currently on result page using find_elements_by_class_name method
#         list_new = self.driver.find_elements(By.NAME, "r")
#         self.assertEqual(11, len(list_new))
#
#     @classmethod
#     def tearDownClass(inst):
#         # close the browser window
#         inst.driver.quit()
#
#
#
#
#
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#
#
# class HomePageTest(unittest.TestCase):
#     @classmethod
#     def setUp(inst):
#         # create a new Firefox session """
#         inst.driver = webdriver.Chrome()
#         inst.driver.implicitly_wait(30)
#         inst.driver.maximize_window()
#
#         # navigate to the application home page """
#         inst.driver.get("http://www.google.com/")
#
#     def test_search_box(self):
#         # check search box exists on Home page
#         self.assertTrue(self.is_element_present(By.NAME,"q"))
#
#     def test_language_settings(self):
#         # check language options on Home page
#         self.assertTrue(self.is_element_present(By.ID,"_eEe"))
#
    # def test_images_link(self):
    #     # check images link on Home page
    #     images_link = self.driver.find_element(By.LINK_TEXT,"Images")
    #     images_link.click()
    #     # check search field exists on Images page
    #     self.assertTrue(self.find_element(By.NAME,"q"))
    #     self.search_field = self.driver.find_element(By.NAME,"q")
    #     # enter search keyword and submit
    #     self.search_field.send_keys("Selenium Webdriver framework architecture diagram")
    #     self.search_field.submit()
#
#     @classmethod
#     def tearDown(inst):
#         # close the browser window
#         inst.driver.quit()
#
#     def is_element_present(self, how, what):
#         """
#         Helper method to confirm the presence of an element on page
#         :params how: By locator type
#         :params what: locator value
#         """
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException: return False
#         return True





	# create the suite from the test classes
suite = TestSuite()


	# add the tests to the suite
# suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SearchText))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(HomePageTest))

    # run the suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
if __name__ == '__main__':
    unittest.main()


