import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Đường dẫn tuyệt đối tới file HTML
current_dir = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = f"file:///{os.path.join(current_dir, 'BasicCalculator.html')}"

@pytest.fixture
def driver():
    """Khởi tạo WebDriver (Chrome) cho mỗi test case"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Bỏ comment dòng này nếu muốn chạy ẩn trình duyệt (không hiện UI)
    driver = webdriver.Chrome(options=options)
    driver.get(HTML_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()

def wait_for_calculation(driver):
    """Hàm chờ xử lý tính toán hoàn tất (chờ ảnh GIF calculating biến mất)"""
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "calculatingForm"))
    )

def test_tc01_add_operation(driver):
    """TC01: Kiểm tra phép Cộng (Build 0)"""
    Select(driver.find_element(By.ID, "selectBuild")).select_by_value("0")
    
    driver.find_element(By.ID, "number1Field").send_keys("5")
    driver.find_element(By.ID, "number2Field").send_keys("3")
    Select(driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Add")
    
    driver.find_element(By.ID, "calculateButton").click()
    wait_for_calculation(driver)
    
    answer = driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
    assert answer == "8", f"Kết quả mong đợi là 8 nhưng thực tế là {answer}"

def test_tc04_divide_operation(driver):
    """TC04: Kiểm tra phép Chia (Build 0)"""
    Select(driver.find_element(By.ID, "selectBuild")).select_by_value("0")
    
    driver.find_element(By.ID, "number1Field").send_keys("20")
    driver.find_element(By.ID, "number2Field").send_keys("4")
    Select(driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Divide")
    
    driver.find_element(By.ID, "calculateButton").click()
    wait_for_calculation(driver)
    
    answer = driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
    assert answer == "5", f"Kết quả mong đợi là 5 nhưng thực tế là {answer}"

def test_tc07_divide_by_zero(driver):
    """TC07: Kiểm tra lỗi chia cho 0 (Build 0)"""
    Select(driver.find_element(By.ID, "selectBuild")).select_by_value("0")
    
    driver.find_element(By.ID, "number1Field").send_keys("5")
    driver.find_element(By.ID, "number2Field").send_keys("0")
    Select(driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Divide")
    
    driver.find_element(By.ID, "calculateButton").click()
    # Lỗi chia cho 0 không cần chờ calculatingForm vì nó bắt ngay lập tức
    
    error_msg = driver.find_element(By.ID, "errorMsgField").text
    assert error_msg == "Divide by zero error!", "Không hiển thị đúng thông báo lỗi chia cho 0"

def test_tc08_invalid_input(driver):
    """TC08: Kiểm tra nhập chữ vào phép toán (Build 0)"""
    Select(driver.find_element(By.ID, "selectBuild")).select_by_value("0")
    
    driver.find_element(By.ID, "number1Field").send_keys("abc")
    driver.find_element(By.ID, "number2Field").send_keys("5")
    Select(driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Add")
    
    driver.find_element(By.ID, "calculateButton").click()
    
    error_msg = driver.find_element(By.ID, "errorMsgField").text
    assert error_msg == "Number 1 is not a number", "Không hiển thị đúng thông báo lỗi nhập chữ"

# ==========================================
# TEST CASES CHO CÁC BUILD BỊ LỖI (Để minh họa)
# ==========================================

def test_bug_build_1_missing_validation(driver):
    """Test trên Build 1: Lỗi không validate text nhập vào"""
    Select(driver.find_element(By.ID, "selectBuild")).select_by_value("1")
    
    driver.find_element(By.ID, "number1Field").send_keys("abc")
    driver.find_element(By.ID, "number2Field").send_keys("def")
    Select(driver.find_element(By.ID, "selectOperationDropdown")).select_by_visible_text("Add")
    
    driver.find_element(By.ID, "calculateButton").click()
    wait_for_calculation(driver)
    
    error_msg = driver.find_element(By.ID, "errorMsgField").text
    # Ở Build 1, lập trình viên quên bắt lỗi nên test case mong đợi có lỗi này sẽ THẤT BẠI (Fail)
    assert error_msg == "Number 1 is not a number", "Bug: Build 1 không validate dữ liệu đầu vào!"
