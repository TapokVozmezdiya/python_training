# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 5),
            middlename=random_string("middlename", 5), nickname=random_string("nickname", 5),
            address=random_string("address", 5), company=random_string("company", 10),
            title=random_string("title", 10),
            mobile=random_string("mobile", 10), workphone=random_string("workphone", 10), fax=random_string("fax", 10),
            email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homephone=random_string("homephone", 10), bday="4", bmonth="May", byear="1990",
            address2=random_string("address2", 10), phone2=random_string("phone2", 10),
            notes=random_string("notes", 10))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact()
    app.contact.fill_contact_form(contact)
    app.contact.confirm()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
