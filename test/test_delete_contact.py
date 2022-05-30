# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
from random import randrange

#task 13
def test_delete_random_contact(app):
        old_contacts = app.contact.get_contact_list()
        if app.contact.count() == 0:
                app.contact.add(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
        index = randrange(len(old_contacts))
        app.contact.delete_by_index(index)
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index:index+1] = []
        assert old_contacts == new_contacts

def test_delete_random_contact_db(app, db, check_ui ):
        old_contacts = db.get_contact_list()
        if len(db.get_contact_list())== 0:
                app.contact.add(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
        index = randrange(len(old_contacts))
        app.contact.delete_by_index(index)
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts[index:index+1] = []
        assert old_contacts == new_contacts
        if check_ui:
                assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.id_or_max)

def test_delete_first_contact(app):
        old_contacts = app.contact.get_contact_list()
        if app.contact.count() == 0:
                app.contact.add(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
        app.contact.delete()
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[0:1] = []
        assert old_contacts == new_contacts
