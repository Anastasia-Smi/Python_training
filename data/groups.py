# -*- coding: utf-8 -*-
from model.group import Group


constant =[
    Group(name="name1", header= "header1", footer ="footer1" ),
    Group(name="name2", header= "header2", footer ="footer2" )
]

#def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + " "*10

     #return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


#testdata = [
       #Group(name=name, header=header, footer=footer)
       #for name in ["", random_string("name", 10)]
       #for header in ["", random_string("header", 20)]
       #for footer in ["", random_string("footer", 20)]
#]
#test framework transfer test data to test(nameof paramer whre to transfer data, source,
# ids ---is a list with text of data, [repr(x) for x in testdata]--means that this data takes a string format )