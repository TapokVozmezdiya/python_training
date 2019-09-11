# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contact):
    contact = json_contact
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact()
    app.contact.fill_contact_form(contact)
    app.contact.confirm()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
