class FIO:

    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname


class Work:
    def __init__(self, title, company, address, home):
        self.title = title
        self.company = company
        self.address = address
        self.home = home


class Secondary:
    def __init__(self, address2, phone2, notes):
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes


class Birthday:
    def __init__(self, bday, bmonth, byear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear


class Internet_contact:
    def __init__(self, email, email2, email3, homepage):
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage


class Telephone:
    def __init__(self, mobile, work, fax):
        self.mobile = mobile
        self.work = work
        self.fax = fax

