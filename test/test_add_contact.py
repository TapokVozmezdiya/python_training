# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact()
    app.contact.fill_contact_form(Contact(
        firstname="Василий", lastname="Петрович", middlename="Шапошников", nickname="Shapka", address="dfgdfgsfafg",
        company="ghkdflghd", home="dlkfghlsd", title="dfngdgnf", mobile="23", work="45", fax="67", email="werw",
        email2="wer", email3="dsfsd", homepage="sdfsdf", bday="4", bmonth="May", byear="1990",
        address2="sdfsdfasdfasdf", phone2="werawdfadf", notes="asdfasdfasdfasdf"))
    app.contact.confirm()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact()
    app.contact.fill_contact_form(Contact(
        firstname="", lastname="", middlename="",
        nickname="", address="", company="",
        home="", title="", mobile="", work="", fax="",
        email="", email2="", email3="", homepage="", bday="-", bmonth="-",
        byear="", address2="", phone2="", notes=""))
    app.contact.confirm()
    app.session.logout()
