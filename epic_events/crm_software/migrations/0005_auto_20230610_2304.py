# Generated by Django 4.2.1 on 2023-06-10 23:04

from django.contrib.auth import get_user_model
from django.db import migrations


def forwards_func(apps, schema_editor):
    """
    Create all three necessary group and assign them the permissions.
    """
    Group = apps.get_model('auth.Group')
    Contentype = apps.get_model('contenttypes.Contenttype')
    User = get_user_model()
    Permission = apps.get_model('auth.Permission')
    Customer = apps.get_model('crm_software.Customer')
    Contract = apps.get_model('crm_software.Contract')
    Events = apps.get_model('crm_software.Events')

    sales_group, _ = Group.objects.get_or_create(name='sales')
    support_group, _ = Group.objects.get_or_create(name='support')
    manager_group, _ = Group.objects.get_or_create(name='manager')

    user_ct = Contentype.objects.get_for_model(User)
    customer_ct = Contentype.objects.get_for_model(Customer)
    contract_ct = Contentype.objects.get_for_model(Contract)
    events_ct = Contentype.objects.get_for_model(Events)
    group_ct = Contentype.objects.get_for_model(Group)
    permission_ct = Contentype.objects.get_for_model(Permission)

    # Creating permission
    # Customer
    customer_add_permission, _ = Permission.objects.get_or_create(
        codename='add_customer', name='Can add Customer', content_type=customer_ct
    )
    customer_view_permission, _ = Permission.objects.get_or_create(
        codename='view_customer', name='Can view Customer', content_type=customer_ct
    )
    customer_change_permission, _ = Permission.objects.get_or_create(
        codename='change_customer', name='Can change Customer', content_type=customer_ct
    )
    # Contract
    contract_add_permission, _ = Permission.objects.get_or_create(
        codename='add_contract', name='Can add contract', content_type=contract_ct
    )
    contract_view_permission, _ = Permission.objects.get_or_create(
        codename='view_contract', name='Can view contract', content_type=contract_ct
    )
    contract_change_permission, _ = Permission.objects.get_or_create(
        codename='change_contract', name='Can change contract', content_type=contract_ct
    )
    # Events
    events_add_permission, _ = Permission.objects.get_or_create(
        codename='add_events', name='Can add events', content_type=events_ct
    )
    events_view_permission, _ = Permission.objects.get_or_create(
        codename='view_customer', name='Can view events', content_type=events_ct
    )
    events_change_permission, _ = Permission.objects.get_or_create(
        codename='change_events', name='Can change events', content_type=events_ct
    )
    # User
    user_add_permission, _ = Permission.objects.get_or_create(
        codename='Can add user', name='add_user', content_type=user_ct
    )
    user_view_permission, _ = Permission.objects.get_or_create(
        codename='Can add user', name='add_user', content_type=user_ct
    )
    user_change_permission, _ = Permission.objects.get_or_create(
        codename='Can change user', name='change_user', content_type=user_ct
    )
    # Group
    group_add_permission, _ = Permission.objects.get_or_create(
        codename='Can add group', name='add_group', content_type=group_ct
    )
    group_view_permission, _ = Permission.objects.get_or_create(
        codename='Can view group', name='view_group', content_type=group_ct
    )
    group_change_permission, _ = Permission.objects.get_or_create(
        codename='Can change group', name='change_group', content_type=group_ct
    )
    group_delete_permission, _ = Permission.objects.get_or_create(
        codename='Can delete group', name='delete_group', content_type=group_ct
    )
    # Permission
    permission_add_permission, _ = Permission.objects.get_or_create(
        codename='Can add permission', name='add_permission', content_type=permission_ct
    )
    permission_view_permission, _ = Permission.objects.get_or_create(
        codename='Can view permission', name='view_permission', content_type=permission_ct
    )
    permission_change_permission, _ = Permission.objects.get_or_create(
        codename='Can change permission', name='change_permission', content_type=permission_ct
    )
    permission_delete_permission, _ = Permission.objects.get_or_create(
        codename='Can delete permission', name='delete_permission', content_type=permission_ct
    )

    # Assigning permissions
    # Only sales can create customer, contract and events
    sales_group.permissions.add(customer_add_permission)
    sales_group.permissions.add(contract_add_permission)
    sales_group.permissions.add(events_add_permission)

    # Read
    sales_group.permissions.add(customer_view_permission)
    sales_group.permissions.add(contract_view_permission)
    sales_group.permissions.add(events_view_permission)

    support_group.permissions.add(customer_view_permission)
    support_group.permissions.add(contract_view_permission)
    support_group.permissions.add(events_view_permission)

    # Update or Delete is handled on object level since only the
    # responsible sales can update his customer for example.

    # Manager :
    manager_group.permissions.add(user_add_permission)
    manager_group.permissions.add(user_view_permission)
    manager_group.permissions.add(user_change_permission)

    manager_group.permissions.add(customer_add_permission)
    manager_group.permissions.add(customer_view_permission)
    manager_group.permissions.add(customer_change_permission)

    manager_group.permissions.add(contract_add_permission)
    manager_group.permissions.add(contract_view_permission)
    manager_group.permissions.add(contract_change_permission)

    manager_group.permissions.add(events_add_permission)
    manager_group.permissions.add(events_view_permission)
    manager_group.permissions.add(events_change_permission)

    manager_group.permissions.add(group_add_permission)
    manager_group.permissions.add(group_view_permission)
    manager_group.permissions.add(group_change_permission)
    manager_group.permissions.add(group_delete_permission)

    manager_group.permissions.add(permission_add_permission)
    manager_group.permissions.add(permission_view_permission)
    manager_group.permissions.add(permission_change_permission)
    manager_group.permissions.add(permission_delete_permission)

    # for user in User.objects.filter(group=manager_group):
    #     user.update()


def reverse_func(apps, schema_editor):
    group_names = ('manager', 'sales', 'support')
    Group = apps.get_model('auth.Group')
    Group.objects.filter(name__in=group_names).delete()


class Migration(migrations.Migration):
    dependencies = [
        (
            "crm_software",
            "0001_initial_squashed_0004_user_groups_user_user_permissions",
        ),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]