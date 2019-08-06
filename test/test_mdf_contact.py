from model.contact import Contact


def test_mdf_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact()
    app.contact.add_string(Contact(
        firstname="Edit", lastname="Edit", middlename="Edit", nickname="Edit", address="Edit",
        company="Edit", home="Edit", title="Edit", mobile="Edit", work="Edit", fax="Edit", email="Edit",
        email2="Edit", email3="Edit", homepage="Edit", bday="-", bmonth="-", byear="Edit",
        address2="Edit", phone2="Edit", notes="Edit"))
    app.contact.update_contact()
    app.session.logout()
