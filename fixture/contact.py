from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("photo")) > 0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # FIO & Nickname
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # Secondary
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        # Birthday
        self.change_field_birthday("bday", contact.bday)
        self.change_field_birthday("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # Internet contact
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # Telephone
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # Work
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.home)

    def change_field_birthday(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)

    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def confirm(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@type='submit'])[2]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("All phones")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            firstname = element.find_element_by_css_selector('[name] td:nth-of-type(3)').text
            lastname = element.find_element_by_css_selector('[name] td:nth-of-type(2)').text
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts


