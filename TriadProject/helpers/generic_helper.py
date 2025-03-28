"""
Module containing GenericHelper class
"""
# External
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class GenericHelper:
    """
    Class containing general helper functions for assisting testing
    """

    def __init__(self, driver):
        """
        Method to initialise the variables needed in the generic helper
        """
        self.driver = driver
        self.wait = 20

    def enter_text_by(self, identifier, text_to_enter, element):
        """
        A generic method to enter text in an element
        :param identifier: The method of locating the element
        :param element: The element to enter in text
        :param text_to_enter: The text being entered
        """
        element = WebDriverWait(self.driver, self.wait).until(
            expected_conditions.presence_of_element_located((identifier, element)))
        element.send_keys(text_to_enter)

    def enter_text_by_id(self, text_to_enter, field_id):
        """
        Identifies element by a specified ID and enters text into it
        :param text_to_enter: The text to enter
        :param field_id: The field ID of where to enter the text
        """
        self.enter_text_by(By.ID, text_to_enter, field_id)

    def click_by(self, identifier, element):
        """
        A generic method to click an element
        :param identifier: The method of locating the element
        :param element: The element to click
        """
        element = WebDriverWait(self.driver, self.wait).until(
            expected_conditions.presence_of_element_located((identifier, element)))
        element.click()

    def click_by_id(self, field_id):
        """
        Identifies element by a specified ID and clicks on it
        :param field_id: The field ID to click
        """
        self.click_by(By.ID, field_id)

    def get_text_by(self, identifier, element):
        """
        A generic method to get an elements text
        :param identifier: The method to locate the element
        :param element: The element to get the text for
        :return: Element text
        """
        element = WebDriverWait(self.driver, self.wait).until(
            expected_conditions.presence_of_element_located((identifier, element)))
        return element.text

    def get_text_by_id(self, field_id):
        """
        Identifies element by a specified ID and returns it
        :param field_id: The field ID to identify
        :return: The element identified
        """
        return self.get_text_by(By.ID, field_id)

    def get_text_by_class(self, field_id):
        """
        Identifies element by a specified ID and returns it
        :param field_id: The field ID to identify
        :return: The element identified
        """
        return self.get_text_by(By.CLASS_NAME, field_id)

    def get_text_by_css(self, field_id):
        """
        Identifies element by a specified ID and returns it
        :param field_id: The field ID to identify
        :return: The element identified
        """
        return self.get_text_by(By.CSS_SELECTOR, field_id)

    def is_element_visible_by_id(self, locator):
        """
        Checks if an element identified by the locator is visible on the screen
        :param locator: The locator tuple (By, value) of the element to check
        :return: True if the element is visible, False otherwise
        """
        try:
            element = WebDriverWait(self.driver, self.wait).until(
                expected_conditions.visibility_of_element_located((By.ID, locator)))
            return element.is_displayed()
        except TimeoutException:
            return False
