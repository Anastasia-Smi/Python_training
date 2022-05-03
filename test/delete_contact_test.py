# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact


def test_delete_first_contact(app):
        app.contact.delete()


