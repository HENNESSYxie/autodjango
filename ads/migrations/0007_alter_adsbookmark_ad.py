# Generated by Django 4.0.3 on 2022-04-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_adsbookmark_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbookmark',
            name='ad',
            field=models.IntegerField(db_column='ad_id', default=1),
            preserve_default=False,
        ),
    ]
