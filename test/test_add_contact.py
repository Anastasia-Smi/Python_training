# -*- coding: utf-8 -*-
import datetime

import pytest

from fixture.Application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.open_home_page()
        app.login( username="admin", password=  "secret")
        app.fillin_add_contact_form(Contact(firstname= f"{datetime.datetime.now().strftime('%M')}name",
                                            lastname =f"{datetime.datetime.now().strftime('%M')}lastname",
                                            address=f"{datetime.datetime.now().strftime('%M')}address",
                                            home_phone=f"{datetime.datetime.now().strftime('%M%S')}",
                                            email=f"{datetime.datetime.now().strftime('%M')}email@gmail.com"))
        app.logout()



