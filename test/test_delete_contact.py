# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_delete_first_contact(app):
        old_contacts = app.contact.get_contact_list()
        if app.contact.count() == 0:
                app.contact.add(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
        app.contact.delete()
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[0:1] = []
        assert old_contacts == new_contacts
