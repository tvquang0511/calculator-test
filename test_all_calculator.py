import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://testsheepnz.github.io/BasicCalculator.html"

class TestBasicCalculator(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') # Chạy ẩn để test nhanh và không ảnh hưởng màn hình
        options.add_argument('--log-level=3')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        
    def tearDown(self):
        self.driver.quit()
        
    def wait_for_calculation(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "calculatingForm"))
        )

    def execute_calc(self, build, num1, num2, operation, wait=True):
        Select(self.driver.find_element(By.ID, "selectBuild")).select_by_value(str(build))
        
        self.driver.find_element(By.ID, "number1Field").clear()
        if num1 is not None:
            self.driver.find_element(By.ID, "number1Field").send_keys(str(num1))
            
        self.driver.find_element(By.ID, "number2Field").clear()
        if num2 is not None:
            self.driver.find_element(By.ID, "number2Field").send_keys(str(num2))
            
        Select(self.driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text(operation)
        self.driver.find_element(By.ID, "calculateButton").click()
        
        if wait:
            self.wait_for_calculation()

    def test_tc01_add(self):
        self.execute_calc(0, 5, 3, "Add")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "8")

    def test_tc02_subtract(self):
        self.execute_calc(0, 10, 4, "Subtract")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "6")

    def test_tc03_multiply(self):
        self.execute_calc(0, 7, 6, "Multiply")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "42")

    def test_tc04_divide(self):
        self.execute_calc(0, 20, 4, "Divide")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "5")

    def test_tc05_concatenate_numbers(self):
        self.execute_calc(0, 5, 3, "Concatenate")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "53")

    def test_tc06_concatenate_text(self):
        self.execute_calc(0, "Hello ", "World", "Concatenate")
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "Hello World")

    def test_tc07_divide_by_zero(self):
        self.execute_calc(0, 5, 0, "Divide", wait=False)
        error_msg = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertEqual(error_msg, "Divide by zero error!")

    def test_tc08_invalid_input_1(self):
        self.execute_calc(0, "abc", 5, "Add", wait=False)
        error_msg = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertEqual(error_msg, "Number 1 is not a number")

    def test_tc09_invalid_input_2(self):
        self.execute_calc(0, 5, "!@#", "Multiply", wait=False)
        error_msg = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertEqual(error_msg, "Number 2 is not a number")

    def test_tc10_max_length(self):
        field1 = self.driver.find_element(By.ID, "number1Field")
        field1.send_keys("1234567890123")
        self.assertEqual(field1.get_attribute("value"), "1234567890")

    def test_tc11_integers_only(self):
        Select(self.driver.find_element(By.ID, "selectBuild")).select_by_value("0")
        self.driver.find_element(By.ID, "number1Field").send_keys("5")
        self.driver.find_element(By.ID, "number2Field").send_keys("2")
        Select(self.driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Divide")
        
        self.driver.find_element(By.ID, "integerSelect").click()
        self.driver.find_element(By.ID, "calculateButton").click()
        self.wait_for_calculation()
        
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "2")

    def test_tc12_integers_only_hidden_on_concat(self):
        Select(self.driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Concatenate")
        is_hidden = not self.driver.find_element(By.ID, "integerSelect").is_displayed()
        self.assertTrue(is_hidden)

    def test_tc13_clear_button(self):
        self.execute_calc(0, 5, 5, "Add")
        self.driver.find_element(By.ID, "clearButton").click()
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        self.assertEqual(answer, "")

if __name__ == '__main__':
    unittest.main()
