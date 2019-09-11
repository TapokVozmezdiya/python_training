from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 5),
            middlename=random_string("middlename", 5), nickname=random_string("nickname", 5),
            address=random_string("address", 5), company=random_string("company", 10),
            title=random_string("title", 10),
            mobile=random_string("mobile", 10), workphone=random_string("workphone", 10), fax=random_string("fax", 10),
            email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homephone=random_string("homephone", 10), bday="4", bmonth="May", byear="1990",
            address2=random_string("address2", 10), phone2=random_string("phone2", 10),
            notes=random_string("notes", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
