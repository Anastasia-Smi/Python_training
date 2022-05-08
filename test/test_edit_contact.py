# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))
    app.contact.edit(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name",
                             lastname=f"{datetime.datetime.now().strftime('%M')}lastname",
                             address=f"{datetime.datetime.now().strftime('%M')}address",
                             home_phone=f"{datetime.datetime.now().strftime('%M%S')}",
                             email=f"{datetime.datetime.now().strftime('%M')}email@gmail.com"))
