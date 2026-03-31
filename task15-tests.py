import pytest
from pages.login_page import LoginPage
from utilities.excel_utils import ExcelUtils

# Initialize Excel utility
EXCEL_FILE_PATH = "test_data.xlsx"
SHEET_NAME = "LoginTests"
excel = ExcelUtils(EXCEL_FILE_PATH, SHEET_NAME)
test_data = excel.get_test_data()

# Parameterize the test function with data from the Excel file
@pytest.mark.parametrize("test_case", test_data)
def test_login_data_driven(driver, test_case):
    # Get the index of the current test case (used for writing results back)
    row_index = test_data.index(test_case)

    username = test_case["Username"]
    password = test_case["Password"]
    tester_name = test_case["Name of Tester"]

    login_page = LoginPage(driver)
    login_page.login(username, password)

    # 4) The Python code will write whether the Test Passed or Test Failed.
    if login_page.is_login_successful():
        result = "Passed"
        # Optional: Add an assertion here if needed by test requirements, e.g.,
        # assert driver.current_url == "https://orangehrmlive.com"
    else:
        result = "Failed"
        # Optional: Add an assertion here if needed, e.g.,
        # assert "Invalid credentials" in login_page.get_error_message()

    # Write the result, date, time, and tester name back to the Excel file
    excel.write_test_result(row_index, result, tester_name)