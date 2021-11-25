link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_presence_of_button_for_es_lang(browser):
    browser.get(link)
    a = browser.find_elements_by_css_selector("#add_to_basket_form [type='submit']")
    assert 1 == len(a), 'button is not exist'
