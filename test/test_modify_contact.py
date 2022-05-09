# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name",
                      lastname=f"{datetime.datetime.now().strftime('%M')}lastname",
                      address=f"{datetime.datetime.now().strftime('%M')}address",
                      home_phone=f"{datetime.datetime.now().strftime('%M%S')}",
                      email=f"{datetime.datetime.now().strftime('%M')}email@gmail.com")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.add(contact)
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) ==len(new_contacts)
    old_contacts[0] =contact
    assert sorted(old_contacts, key = Contact.id_or_max)== sorted(new_contacts, key=Contact.id_or_max)

