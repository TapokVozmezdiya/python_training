# -*- coding: utf-8 -*-
from model.group import Group


def test_mdf_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="ndfg", header="asdasd", footer="dasda"))
        app.group.confirm()
    group = Group(name="Edit", header="", footer="Edit")
    group.id = old_groups[0].id
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
