from selenium import webdriver

browser = webdriver.Firefox(timeout=10)
browser.get('http://localhost:8000')

assert 'Django' in browser.title