from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

import time


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()


class ApplicationPage:
    def __init__(self, url, driver: webdriver.Firefox):
        self.url = url
        self.driver = driver
        # self.personal_info = personal_info

    def is_one_page_application(self):
        self.driver.get(self.url)
        time.sleep(0.5)
        submit_btns = self.driver.find_elements(
            By.XPATH,
            f"//button[contains(@id, 'submit') or contains(@name, 'submit') or contains(@class, 'submit')]",
        )
        if submit_btns:
            btn = submit_btns[0]
            if btn.id or btn.accessible_name or btn.get_attribute("class"):
                self.driver.close()
                return True
        else:
            # self.driver.close()
            return False

    def __check_inputs(self, elements, element_name):
        print(f"checking {element_name} inputs\n")
        e = elements[0]
        input_id = e.id
        name = e.accessible_name
        class_name = e.get_attribute("class")
        print(
            "-" * 45
            + f"\nID: {input_id}\nName: {name}\nClass Name: {class_name}\n"
            + "-" * 45
        )
        if input_id or name or class_name:
            # self.driver.close()
            return f"{element_name} can be filled\n"
        else:
            # self.driver.close()
            return "this element was not found"

    def find_info_inputs(self):
        self.driver.get(self.url)
        time.sleep(1)
        first_name_inputs = self.driver.find_elements(
            By.XPATH,
            f"//input[contains(@id, 'first') and contains(@id, 'name') or contains(@name, 'first') and contains(@name, 'name') or contains(@class, 'first') and contains(@class, 'name')]",
        )
        last_name_inputs = self.driver.find_elements(
            By.XPATH,
            f"//input[contains(@id, 'last') and contains(@id, 'name') or contains(@name, 'last') and contains(@name, 'name') or contains(@class, 'last') and contains(@class, 'name')]",
        )

        if first_name_inputs and last_name_inputs:
            # self.driver.close()
            return self.__check_inputs(
                first_name_inputs, "first name"
            ), self.__check_inputs(last_name_inputs, "last name")

        else:
            full_name_input = self.driver.find_elements(
                By.XPATH,
                f"//input[contains(@id, 'name') or contains(@name, 'name') or contains(@class, 'name')]",
            )
            if full_name_input:
                # self.driver.close()
                return self.__check_inputs(full_name_input, "Full Name")
            else:
                # self.driver.close()
                return "Could not find any name info inputs"
