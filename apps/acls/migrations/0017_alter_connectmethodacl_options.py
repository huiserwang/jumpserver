# Generated by Django 3.2.19 on 2023-06-13 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acls', '0016_auto_20230606_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connectmethodacl',
            options={'ordering': ('priority', 'name'), 'verbose_name': 'Connect method acl'},
        ),
    ]
