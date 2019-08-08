# -*- coding: utf-8 -*-
from model.group import Group


def test_mdf_group(app):
    if app.group.count() == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="test"))
        app.group.confirm()
    app.group.edit_group(Group(name="Edit", header="", footer="Edit"))
