import datetime
from model.group import Group


def test_modify_name_first_group(app):
    old_groups = app.group.get_group_list()
    group = (Group(name=f"{datetime.datetime.now().strftime('%M')}group_1"))
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




def test_modify_header_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header=f"{datetime.datetime.now().strftime('%M')}header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_all_values_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name=f"{datetime.datetime.now().strftime('%M')}group_1",
                         header=f"{datetime.datetime.now().strftime('%M')}header",
                         footer=f"{datetime.datetime.now().strftime('%M')}footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
