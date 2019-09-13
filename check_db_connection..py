from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="76"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()


# from fixture.db import DbFixture
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contacts)
#     print(len(contacts))
# finally:
#     db.destroy()


# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()