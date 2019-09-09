import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page()
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobile == contact_from_edit_page.mobile
    assert contact_from_home_page.phone2 == contact_from_edit_page.phone2


# def clear(s):
#     return re.sub("[() -]","", s)