# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.add_group()
    app.group.create(Group(name="ndfg", header="asdasd", footer="dasda"))
    app.group.confirm()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.add_group()
    app.group.create(Group(name="", header="", footer=""))
    app.group.confirm()
    app.session.logout()
