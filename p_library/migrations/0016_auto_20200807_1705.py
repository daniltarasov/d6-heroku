# Generated by Django 2.2.6 on 2020-08-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0015_auto_20200807_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_image',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_img'),
        ),
    ]
