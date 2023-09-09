# Generated by Django 4.2.3 on 2023-09-09 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_modify_author', 'Create/Update/Delete authors'),)},
        ),
    ]
