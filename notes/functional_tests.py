from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

#12

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')  # Corrected here
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ellie goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Correct the ID to match the input element
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy flowers')

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # Reduced sleep time for faster test execution

        self.check_for_row_in_list_table('1:Buy flowers')
        self.check_for_row_in_list_table('2:Give a gift to Lisi')

        # table = self.browser.find_element(By.ID, 'id_list_table')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertIn('1: Buy flowers', [row.text for row in rows])
        # self.assertIn('2: Give a gift to List', [row.text for row in rows])

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
