# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_delete_first_contact(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
        app.contact.delete()


