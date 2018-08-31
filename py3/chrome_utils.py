#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class HeadlessChromeDriver:
    def __init__(self, width: int = 1200, height: int = 2400, use_in_headful_mode: bool = False):
        options = webdriver.ChromeOptions()
        if not use_in_headful_mode:
            options.add_argument('headless')

        options.add_argument('window-size={}x{}'.format(width, height))
        self.driver = webdriver.Chrome(chrome_options=options)

    def navigate(self, url: str):
        self.driver.get(url)

    def screenshot(self, filename: str) -> bool:
        return self.driver.get_screenshot_as_file(filename)

    def navigate_using_css_selector(self, css_selector: str):
        elem = self.driver.find_element_by_css_selector(css_selector)
        elem.click()

    def login_using_css_selector(self, username_css: str, password_css: str, login_css: str,
                                 username: str, password: str):
        email_selector = self.driver.find_element_by_css_selector(username_css)
        email_selector.send_keys(username)
        password_selector = self.driver.find_element_by_css_selector(password_css)
        password_selector.send_keys(password)
        login_selector = self.driver.find_element_by_css_selector(login_css)
        login_selector.click()

    def explicit_wait(self, wait_time_seconds: int):
        try:
            WebDriverWait(self.driver, wait_time_seconds).until(lambda x: False)
        except TimeoutException:
            pass

    def click_element_from_point(self, x: int, y: int):
        el = self.driver.execute_script('return document.elementFromPoint({}, {})'.format(x//2, y//2))
        if el:
            print(el.tag_name, el.get_attribute('src'))
            el.click()


def main():
    driver = HeadlessChromeDriver()
    driver.navigate('https://www.mealpal.com')
    driver.screenshot('/Users/etai/screenshot.png')


if __name__ == '__main__':
    main()
