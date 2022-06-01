
from model.group import Group
from sys import maxsize

class GroupHelper:
    def __init__(self, app):
        self.app = app

    #NAVIGATION

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")


    #GENERAL METHODS
    def fill_in_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    group_cache=None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


    def select_first_group(self):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_group_from_dropdown(self, index):
        wd = self.app.wd
        groups= self.get_group_list()
        group_id = groups[index].id
        #wd.find_element_by_css_selector(".right:last-child").click()
        wd.find_element_by_xpath("//div[@class='right']/select").click()
        wd.select_by_value(group_id)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()

    def select_group_from_upper_dropdown(self, index):
        wd = self.app.wd
        groups = self.get_group_list()
        group_id = groups[index].id
        wd.find_element_by_name("group").click()
        wd.select.select_by_value(group_id)
        wd.find_element_by_link_text("home").click()

    #CREATE

    def create(self, group):
        # init group creation
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        self.fill_in_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    #EDIT
    def edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        self.fill_in_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_in_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None


    #DELETE #DELETE #DELETE

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self,id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_contacts_from_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//div/input[@type='button']").click()
        wd.find_element_by_link_text("home").click()

