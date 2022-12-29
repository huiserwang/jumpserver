# Generated by Django 3.2.14 on 2022-12-29 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0106_auto_20221228_1838'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accountbackupplan',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='accountbackupplan',
            name='recipients',
        ),
        migrations.DeleteModel(
            name='AccountBackupPlanExecution',
        ),
        migrations.DeleteModel(
            name='CommandFilter',
        ),
        migrations.DeleteModel(
            name='CommandFilterRule',
        ),
        migrations.DeleteModel(
            name='GatheredUser',
        ),
        migrations.DeleteModel(
            name='AccountBackupPlan',
        ),
    ]
