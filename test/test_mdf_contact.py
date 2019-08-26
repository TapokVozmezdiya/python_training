from model.contact import Contact


def test_mdf_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact()
        app.contact.fill_contact_form(Contact(
            firstname="Василий", lastname="Петрович", middlename="Шапошников", nickname="Shapka", address="dfgdfgsfafg",
            company="ghkdflghd", home="dlkfghlsd", title="dfngdgnf", mobile="23", work="45", fax="67", email="werw",
            email2="wer", email3="dsfsd", homepage="sdfsdf", bday="4", bmonth="May", byear="1990",
            address2="sdfsdfasdfasdf", phone2="werawdfadf", notes="asdfasdfasdfasdf"))
        app.contact.confirm()
    app.contact.edit_contact(Contact(firstname="Edit", lastname="Edit", middlename="Edit", nickname="Edit",
                                     address="Edit", company="Edit", home="Edit", title="Edit", mobile="Edit",
                                     work="Edit", fax="Edit", email="Edit", email2="Edit", email3="Edit",
                                     homepage="Edit", bday="-", bmonth="-", byear="Edit", address2="Edit",
                                     phone2="Edit", notes="Edit"))
    app.contact.update_contact()
