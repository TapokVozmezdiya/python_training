# -*- coding: utf-8 -*-
from model.group import Group


def test_mdf_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="Edit", header="", footer="Edit"))
    app.session.logout()
