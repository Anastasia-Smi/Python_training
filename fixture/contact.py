from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    # NAVIGATION
    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    # GENERAL
    def fill_in_contact_form(self, contact):
        wd = self.app.wd

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

    def count(self):
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            row = wd.find_elements_by_xpath("//tr[position() >1]")
            for element in row:
                id = element.find_element_by_xpath(".//td/input[@type='checkbox']").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

    # ADD
    def submit_add_contact_form(self):
        # submit contact
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def add(self, contact):
        # fill in add contact form
        wd = self.app.wd
        self.click_add_contact()
        self.fill_in_contact_form(contact)
        self.submit_add_contact_form()
        self.return_to_contact_page()
        self.contact_cache = None

    def click_add_contact(self):
        # go to add contact page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    # EDIT
    def edit(self, index, contact):
        # fill in add contact form
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_xpath("//tbody/tr/td[8]")[index].click()
        self.fill_in_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    # DELETE
    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div/input[@value ='Delete']").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def delete_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div/input[@value ='Delete']").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

