# Generated by Django 2.2.6 on 2020-06-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20200614_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='p_library.Book'),
        ),
    ]
