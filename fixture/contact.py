class ContactHelper:
    def __init__(self,app):
        self.app = app


    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit_add_contact_form(self):
        # submit contact
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fillin_add_contact_form(self, contact):
        # fill in add contact form
        wd = self.app.wd
        self.click_add_contact()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)

        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("152")

        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        self.submit_add_contact_form()
        self.return_to_contact_page()

    def click_add_contact(self):
        # go to add contact page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

