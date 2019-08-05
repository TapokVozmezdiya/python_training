# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_string(Contact(
        firstname="Василий", lastname="Петрович", middlename="Шапошников", nickname="Shapka", address="dfgdfgsfafg",
        company="ghkdflghd", home="dlkfghlsd", title="dfngdgnf", mobile="23", work="45", fax="67", email="werw",
        email2="wer", email3="dsfsd", homepage="sdfsdf", bday="4", bmonth="May", byear="1990",
        address2="sdfsdfasdfasdf", phone2="werawdfadf", notes="asdfasdfasdfasdf"))

    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_string(Contact(
        firstname="", lastname="", middlename="",
        nickname="", address="", company="",
        home="", title="", mobile="", work="", fax="",
        email="", email2="", email3="", homepage="", bday="-", bmonth="-",
        byear="", address2="", phone2="", notes=""))
    app.session.logout()
