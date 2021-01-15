import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                    action='store',
                    default="chrome",
                    help="Choose browser: chrome, firefox, opera")
    parser.addoption('--language',
                    action='store',
                    default="ru",
                    help="Choose language: en-gb, es, fr, ...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == "chrome":

        # languages for chrome and opera
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":

        # languages for firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)

        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)

    elif browser_name == "opera":

        # languages for chrome and opera
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        print("\nstart opera browser for test..")
        browser = webdriver.Opera(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, opera")
    yield browser
    print("\nquit browser..")
    browser.quit()








