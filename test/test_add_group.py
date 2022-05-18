# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#for  random_string
import random
import string
#test data transfer to test as a parameter

def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + " "*10
     #random lenghts but no longer than maxlen
     return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [
       Group(name=name, header=header, footer=footer)
       for name in ["", random_string("name", 10)]
       for header in ["", random_string("header", 20)]
       for footer in ["", random_string("footer", 20)]
]
#test framework transfer test data to test(nameof paramer whre to transfer data, source,
# ids ---is a list with text of data, [repr(x) for x in testdata]--means that this data takes a string format )

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):

       old_groups = app.group.get_group_list()
       app.group.create(group)
       assert len(old_groups) + 1 == app.group.count()
       new_groups = app.group.get_group_list()
       old_groups.append(group)
       assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
