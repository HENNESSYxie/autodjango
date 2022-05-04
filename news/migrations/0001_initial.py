# Generated by Django 4.0.3 on 2022-04-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('link', models.TextField()),
                ('title', models.TextField()),
                ('anons', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('tables', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'News',
                'managed': False,
            },
        ),
    ]