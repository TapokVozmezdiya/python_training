from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.add_group()
        app.group.fill_group_form(Group(name="test"))
        app.group.confirm()
    app.group.delete_first_group()
