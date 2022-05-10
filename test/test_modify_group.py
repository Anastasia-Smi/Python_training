import datetime
from model.group import Group
from random import randrange


def test_modify_name_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = (Group(name=f"{datetime.datetime.now().strftime('%M')}group_1"))
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_name_first_group(app):
    old_groups = app.group.get_group_list()
    group = (Group(name=f"{datetime.datetime.now().strftime('%M')}group_1"))
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_header_first_group(app):
    old_groups = app.group.get_group_list()
    group = (Group(name=f"{datetime.datetime.now().strftime('%M')}header"))
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_all_values_first_group(app):
    old_groups = app.group.get_group_list()
    group = (Group(name=f"{datetime.datetime.now().strftime('%M')}group_1",
                         header=f"{datetime.datetime.now().strftime('%M')}header",
                         footer=f"{datetime.datetime.now().strftime('%M')}footer"))
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
