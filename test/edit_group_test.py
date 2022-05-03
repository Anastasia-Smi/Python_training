import datetime
from model.group import Group

def test_edit_first_group(app):

       app.group.open_group_page()
       app.group.edit(Group(name=f"{datetime.datetime.now().strftime('%M')}group_1",
                            header=f"{datetime.datetime.now().strftime('%M')}header",
                            footer=f"{datetime.datetime.now().strftime('%M')}footer"))
       app.group.return_to_group_page()
