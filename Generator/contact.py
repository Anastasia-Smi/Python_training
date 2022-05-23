# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
#test data transfer to test as a parameter

try:
    opts, args= getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n =5
f= "data/contact.json"

for o, a in opts:
    if o =="-n":
        n= int (a)
    elif o=="-f":
        f=a

def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + " "*10
     #random lenghts but no longer than maxlen
     return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [
       Contact(firstname="", lastname="", address="", home_phone="", work_phone="",
               mobile_phone="", email="", e_mail_2="", e_mail_3="")] +[
       Contact(firstname=random_string("firstname",10), lastname= random_string("lastname",20),
               address=random_string("address", 20),home_phone=random_string("", 2),
               work_phone=random_string("", 2),mobile_phone=random_string("", 2),
              email=random_string("", 2),e_mail_2=random_string("", 2),e_mail_3=random_string("", 2))
       for i in range(n)]


file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
    #dumps turms out data into string in json