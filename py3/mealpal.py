#!/usr/bin/env python

from chrome_utils import HeadlessChromeDriver

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




def main():
    client = MealpalClient('etplush@gmail.com', '7*Bd6!5EB8zkd3f2')
    client.login()
    print(client.driver.get_element_id_from_point(380, 1200))
    client.take_screenshot('/Users/etai/screenshot.png')


if __name__ == '__main__':
    main()
