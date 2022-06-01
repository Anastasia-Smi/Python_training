import datetime
from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture
from pony.orm import*
from model.group import Group
from model.contact import Contact
from _datetime import datetime
from pymysql.converters import decoders

def test_add_contact_to_group(app):
    contact=app.contact.select_contact(0)
    app.group.select_group_from_dropdown(2)
    contacts_in_group_db = ORMFixture.get_contacts_in_group()
    assert(contact in contacts_in_group_db)


def test_delete_contact_from_group(app):

        contact = app.contact.select_contact(0)
        app.group.select_group_from_dropdown(2)

        app.group.select_group_from_upper_dropdown(2)
        app.group.delete_contacts_from_groups_page()

        contacts_in_group_db = ORMFixture.get_contacts_in_group(2)
        assert (contact not  in contacts_in_group_db)
