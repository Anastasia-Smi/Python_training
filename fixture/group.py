class GroupHelper:
    def __init__(self,app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        # init group creation
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        # fill in group form
        self.fill_in_group_form(group)
        # submit
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def delete_first_group(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()

    def edit(self,group):
        wd = self.app.wd
        self.select_first_group()
        self.fill_in_group_form(group)
        wd.find_element_by_name("update").click()

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

    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        self.select_first_group()

        self.fill_in_group_form(new_group_data)

        wd.find_element_by_name("update").click()



