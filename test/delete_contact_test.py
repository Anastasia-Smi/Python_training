# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_delete_first_contact(app):
        app.contact.open_home_page()
        app.session.login( username="admin", password=  "secret")
        app.contact.delete()
        app.session.logout()

