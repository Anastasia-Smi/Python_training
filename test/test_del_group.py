
# -*- coding: utf-8 -*-

from model.group import  Group

def test_del_first_group(app):
       app.group.open_group_page()
       app.group.delete_first_group()
       app.group.return_to_group_page()
