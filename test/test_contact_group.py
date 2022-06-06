import datetime
from model.contact import Contact
from model.group import Group
from random import randrange

from pony.orm import*
from model.group import Group
from model.contact import Contact
from _datetime import datetime
from pymysql.converters import decoders
from fixture.orm import ORMFixture

#task 22

def test_add_contact_to_group(app, group, contact, db, ormDB):

    group_id = int(app.group.select_group_id())
    contact_id = app.contact.select_contact_id()

    app.contact.select_contact(contact_id)

    app.group.select_group_by_id_from_drop_down(group_id)

    app.group.add_contact_to_group()
    group.id=group_id
    contact.id=contact_id
    #A = ORMFixture( "localhost", "addressbook", "root","")
    contacts_in_group_db = ormDB.get_contacts_in_group(group)
    assert(contact in contacts_in_group_db)


def test_delete_contact_from_group(app):

        contact = app.contact.select_contact(0)
        app.group.select_group_from_dropdown(2)

        app.group.select_group_from_upper_dropdown(2)
        app.group.delete_contacts_from_groups_page()

        contacts_in_group_db = ORMFixture.get_contacts_in_group(2)
        assert (contact not  in contacts_in_group_db)
