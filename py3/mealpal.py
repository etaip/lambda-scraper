#!/usr/bin/env python

from chrome_utils import HeadlessChromeDriver
from match_image import find_image

class MealpalClient:
    MEALPAL_URL = 'https://www.mealpal.com'
    MEALPAL_USERNAME_CSS_SELECTOR = '#user_email'
    MEALPAL_PASSWORD_CSS_SELECTOR = '#user_password'
    MEALPAL_LOGIN_CSS_SELECTOR = '#new_user > input.mp-red-button-full'
    MEALPAL_LOGIN_PAGE_CSS_SELECTOR = '#app > div.header.usa > div.header-container > a'

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.driver = HeadlessChromeDriver()
        self.driver.navigate(self.MEALPAL_URL)

    def login(self):
        self.driver.navigate_using_css_selector(self.MEALPAL_LOGIN_PAGE_CSS_SELECTOR)
        self.driver.login_using_css_selector(self.MEALPAL_USERNAME_CSS_SELECTOR,
                                             self.MEALPAL_PASSWORD_CSS_SELECTOR,
                                             self.MEALPAL_LOGIN_CSS_SELECTOR, self.username, self.password)
        self.driver.explicit_wait(20)

    def take_screenshot(self, filename: str):
        self.driver.screenshot(filename)

    def order(self, image_path):
        file_path = '/Users/etai/screenshot_before.png'
        self.driver.screenshot(file_path)
        image_coordinates = find_image(image_path, file_path)
        print(image_coordinates)
        self.driver.click_element_from_point(image_coordinates[0], image_coordinates[1])


def main():
    client = MealpalClient('etplush@gmail.com', '')
    client.login()
    client.order('query_image.png')
    client.take_screenshot('/Users/etai/screenshot_after.png')


if __name__ == '__main__':
    main()
