# -*- coding: utf-8 -*-
from model.group import Group


def test_mdf_group(app):
    app.group.edit_group(Group(name="Edit", header="", footer="Edit"))
