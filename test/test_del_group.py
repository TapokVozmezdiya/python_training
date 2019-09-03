from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="ndfg", header="asdasd", footer="dasda"))
        app.group.confirm()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
