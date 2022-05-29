# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange
import random

def test_del_randome_group(app):
       old_groups = app.group.get_group_list()
       if app.group.count() == 0:
              app.group.create(Group(name="test"))
       index =  randrange(len(old_groups))
       app.group.delete_group_by_index(index)
       assert len(old_groups) - 1 == app.group.count()
       new_groups = app.group.get_group_list()
       old_groups[index:index+1] = []
       assert old_groups == new_groups


def test_del_randome_group_db(app,db,check_ui):
       if len(db.get_group_list()) == 0:
              app.group.create(Group(name="test"))
       old_groups = db.get_group_list()
       group=random.choice(old_groups)
       app.group.delete_group_by_id(group.id)
       assert len(old_groups) - 1 == app.group.count()
       new_groups = db.get_group_list()
       old_groups.remove(group)
       assert old_groups == new_groups
       if check_ui:
              assert sorted(new_groups, key= Group.id_or_max)== sorted(app.group.get_group_list(),key= Group.id_or_max )