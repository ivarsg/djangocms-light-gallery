# Generated by Django 2.2.11 on 2020-03-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0015_auto_20170617_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightgallery',
            name='fullscreen',
            field=models.BooleanField(default=False, verbose_name='Enable Fullscreen Button'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='zoom',
            field=models.BooleanField(default=False, verbose_name='Enable Zoom Buttons'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='zoomActualSize',
            field=models.BooleanField(default=True, verbose_name='Enable Actual Size Button'),
        ),
    ]
