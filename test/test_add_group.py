
# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
       app.group.open_group_page()
       app.group.create(Group(name="group_1", header="header", footer="footer"))
       app.group.return_to_group_page()

