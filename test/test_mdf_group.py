# -*- coding: utf-8 -*-
from model.group import Group


def test_mdf_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group()
    app.group.create(Group(name="Edit", header="Edit", footer="Edit"))
    app.session.logout()
