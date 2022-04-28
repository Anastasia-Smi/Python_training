

from selenium import webdriver


class Application:

 def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

 def destroy(self):
      self.wd.quit()

 def login(self, username, password):
      wd = self.wd
    # login
      wd.find_element_by_name("user").click()
      wd.find_element_by_name("user").clear()
      wd.find_element_by_name("user").send_keys(username)
      wd.find_element_by_name("pass").click()
      wd.find_element_by_name("pass").clear()
      wd.find_element_by_name("pass").send_keys(password)
      wd.find_element_by_xpath("//input[@value='Login']").click()

 def open_home_page(self):
    wd = self.wd
    wd.get("http://localhost/addressbook/index.php")

 def logout(self):
    wd = self.wd
    wd.find_element_by_link_text("Logout").click()
#GROUPS

 def return_to_group_page(self):
    wd = self.wd
    wd.find_element_by_link_text("group page").click()

 def create_group(self, group):
    # init group creation
    wd = self.wd
    wd.get("http://localhost/addressbook/group.php")
    wd.find_element_by_name("new").click()
    # fill in group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # submit
    wd.find_element_by_name("submit").click()

 def open_group_page(self):
    wd = self.wd
    wd.find_element_by_link_text("groups").click()

 def open_home_page(self):
    wd = self.wd
    wd.get("http://localhost/addressbook/index.php")

#CONTACTS
 def return_to_contact_page(self):
        # return to contact page
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

 def submit_add_contact_form(self):
        # submit contact
        wd = self.wd
        wd.find_element_by_name("submit").click()

 def fillin_add_contact_form(self, contact):

        # fill in add contact form
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
