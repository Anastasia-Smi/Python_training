# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + " "*10
     #random lenghts but no longer than maxlen
     return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address,
            home_phone=home_phone, work_phone=work_phone,
            mobile_phone=mobile_phone,
            email=email, e_mail_2=e_mail_2,
            e_mail_3=e_mail_3)
    for firstname in ["", random_string("firstname", 4)]
    for lastname in ["", random_string("lastname", 4)]
    for address in ["", random_string("address", 5)]
    for home_phone in ["", random_string("hp", 5)]
    for work_phone in ["", random_string("wp", 5)]
    for mobile_phone in ["", random_string("mp", 5)]
    for email in ["", random_string("hp", 5)]
    for e_mail_2 in ["", random_string("hp", 5)]
    for e_mail_3 in ["", random_string("hp", 5)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_random_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name",
                            lastname=f"{datetime.datetime.now().strftime('%M')}lastname",
                            address=f"{datetime.datetime.now().strftime('%M')}address",
                            home_phone=f"{datetime.datetime.now().strftime('%M%S')}",
                            email=f"{datetime.datetime.now().strftime('%M')}email@gmail.com")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
