"""Cloud Foundry test"""
from flask import Flask
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import os

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    # REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
    driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
    # driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')

    driver.implicitly_wait(5)
    driver.get('http://www.pythonscraping.com/')
    driver.get_screenshot_as_file('tmp/pythonscraping.png')

    return 'Hello World! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)