from model.group import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="ndfg", header="asdasd", footer="dasda"))
        app.group.confirm()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
