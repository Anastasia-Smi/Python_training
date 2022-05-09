
from model.group import Group
from sys import maxsize

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        # init group creation
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        self.fill_in_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        self.fill_in_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_in_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        self.fill_in_group_form(new_group_data)

        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache=None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            groups = []
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


