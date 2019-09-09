from model.contact import Contact
from random import randrange


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact()
        app.contact.fill_contact_form(Contact(
            firstname="Василий", lastname="Петрович", middlename="Шапошников", nickname="Shapka", address="dfgdfgsfafg",
            company="ghkdflghd", home="dlkfghlsd", title="dfngdgnf", mobile="23", workphone="45", fax="67", email="werw",
            email2="wer", email3="dsfsd", homephone="sdfsdf", bday="4", bmonth="May", byear="1990",
            address2="sdfsdfasdfasdf", phone2="werawdfadf", notes="asdfasdfasdfasdf"))
        app.contact.confirm()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
