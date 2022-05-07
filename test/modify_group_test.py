import datetime
from model.group import Group


def test_modify_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name=f"{datetime.datetime.now().strftime('%M')}group_1"))


def test_modify_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header=f"{datetime.datetime.now().strftime('%M')}header"))


def test_edit_all_values_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name=f"{datetime.datetime.now().strftime('%M')}group_1",
                         header=f"{datetime.datetime.now().strftime('%M')}header",
                         footer=f"{datetime.datetime.now().strftime('%M')}footer"))
