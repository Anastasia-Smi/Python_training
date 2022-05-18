from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, address=None,
                 home_phone=None, work_phone= None,
                 mobile_phone= None,  all_phones_from_home_page = None,
                 email=None, all_emails_from_home_page =None,  e_mail =None,  e_mail_2= None,
                 e_mail_3=None, id=None ):

        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone= mobile_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.e_mail =e_mail,
        self.e_mail_2 = e_mail_2,
        self.e_mail_3 = e_mail_3,
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id


#method returns a string containing a printable representation of an object
    def  __repr__(self):
        return "%s%s%s%s%s%s%s%s%s%s" %(self.id, self.lastname, self.firstname,self.address,
                                       self.home_phone,self.work_phone,self.mobile_phone,
                                       self.email,self.e_mail_2,self.e_mail_3
                                       )



    def __eq__(self,other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.lastname ==other.lastname and self.firstname== other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
