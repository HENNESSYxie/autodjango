# Generated by Django 4.0.3 on 2022-04-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_adsbookmark_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbookmark',
            name='ad',
            field=models.IntegerField(blank=True, db_column='ad_id', null=True),
        ),
    ]