# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
from random import randrange

def test_modify_random_contact(app):
    contact = Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name",
                      lastname=f"{datetime.datetime.now().strftime('%M')}lastname",
                      address=f"{datetime.datetime.now().strftime('%M')}address",
                      home_phone=f"{datetime.datetime.now().strftime('%M%S')}",
                      email=f"{datetime.datetime.now().strftime('%M')}email@gmail.com")

    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] =contact
    assert sorted(old_contacts, key = Contact.id_or_max)== sorted(new_contacts, key=Contact.id_or_max)

def test_modify_random_contact_db(app, db, check_ui):
    contact = Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name",
                      lastname=f"{datetime.datetime.now().strftime('%M')}lastname",
                      address = f"{datetime.datetime.now().strftime('%M')}address",
                      home_phone = f"{datetime.datetime.now().strftime('%M%S')}",
                      email = f"{datetime.datetime.now().strftime('%M')}email@gmail.com")
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(contact))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] =contact
    assert sorted(old_contacts, key = Contact.id_or_max)== sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
