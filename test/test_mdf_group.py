# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_mdf_group(app):
    if app.group.count() == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="ndfg", header="asdasd", footer="dasda"))
        app.group.confirm()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edit", header="", footer="Edit")
    group.id = old_groups[index].id
    app.group.edit_group(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
