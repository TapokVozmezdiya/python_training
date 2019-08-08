from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact()
        app.contact.fill_contact_form(Contact(
            firstname="Василий", lastname="Петрович", middlename="Шапошников", nickname="Shapka", address="dfgdfgsfafg",
            company="ghkdflghd", home="dlkfghlsd", title="dfngdgnf", mobile="23", work="45", fax="67", email="werw",
            email2="wer", email3="dsfsd", homepage="sdfsdf", bday="4", bmonth="May", byear="1990",
            address2="sdfsdfasdfasdf", phone2="werawdfadf", notes="asdfasdfasdfasdf"))
        app.contact.confirm()
    app.contact.delete_contact()
