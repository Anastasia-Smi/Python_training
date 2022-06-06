# -*- coding: utf-8 -*-
#function that creates fixture

import pytest
from fixture.Application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.session import SessionHelper
from fixture.db import DbFixture
from fixture.group import Group
from fixture.contact import Contact
from fixture.orm import ORMFixture

fixture = None
target =None


def load_config(file):
    global target
    if target is None:
        f = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(f) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request):
   db_config = load_config(request.config.getoption("--target"))['db']
   dbfixture=DbFixture(host=db_config['host'],user=  db_config['user'],
                       name=db_config['name'],
                       password= db_config['password'])
   def fin():
        dbfixture.destroy()
   request.addfinalizer(fin)
   return dbfixture

@pytest.fixture(scope="session")
def ormDB(request):
   db_config = load_config(request.config.getoption("--target"))['db']
   dbfixture=ORMFixture(host=db_config['host'],user=  db_config['user'],
                       name=db_config['name'],
                       password= db_config['password'])
   def fin():
        dbfixture.destroy()
   request.addfinalizer(fin)
   return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture
def group():
     return Group(name="name", header= "header", footer= "footer", id= str("id"))

@pytest.fixture
def contact():
     return Contact(firstname="firstname", lastname= "lastname",
                    address= "address", all_phones_from_home_page = "all_phones_from_home_page",
                    all_emails_from_home_page= "all_emails_from_home_page",
                    id= str("id"))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata= load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata= load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())