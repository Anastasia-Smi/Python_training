from model.contact import Contact
import datetime
import re
import functools

def test_contacts_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page= app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#task 20
def test_contacts_ui_match_contacts_db(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname=f"{datetime.datetime.now().strftime('%M')}name"))

    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list_full(), key=Contact.id_or_max)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_db[i])


def clear(s):
    return re.sub("[()', -]","",s)


def clear_email(s):
    return re.sub("[)'(,]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(str(x)),
                                filter(lambda x: x is not None,
                                       [contact.home_phone,contact.mobile_phone,
                                        contact.work_phone,]))))

#def merge_emails_like_on_home_page(contact):
    #return "\n".join(filter(lambda x: x != "",
                            #map(lambda x: clear_email(str(x)),
                                #filter(lambda x: x is not None,
                                       #[contact.e_mail, contact.e_mail_2,
                                       #contact.e_mail_3]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join((filter(lambda x: x != "",
                                    #map(lambda x: clear_email(str(x)),
                             [contact.e_mail, contact.e_mail_2,
                                       contact.e_mail_3])))


