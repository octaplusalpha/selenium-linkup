import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    def __init__(self, driver: str):
        print('Starting up...')
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        print(f'Opening {url}')
        self.browser.get(url)

    def closing_page(self):
        print('Closing Browser ...')
        self.browser.close()

if __name__ == '__main__':
    browser = Browser('chromedriver.exe')
    browser.open_page('https://ogieluconstructions.com')
    time.sleep(5)
    browser.closing_page()