import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_an_add_to_cart_button(browser):
    browser.get(link)
    cart_button = browser.find_element_by_xpath("//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert cart_button, "Невозможно добавить товар в корзину"
