# Generated by Django 2.2.6 on 2020-08-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0016_auto_20200807_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_img'),
        ),
    ]