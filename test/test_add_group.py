# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.open_group_page()
    app.group.add_group()
    app.group.fill_group_form(Group(name="ndfg", header="asdasd", footer="dasda"))
    app.group.confirm()


def test_add_empty_group(app):
    app.group.open_group_page()
    app.group.add_group()
    app.group.fill_group_form(Group(name="", header="", footer=""))
    app.group.confirm()
