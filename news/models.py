from django.db import models

#модель новости
class News(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    link = models.TextField()  # This field type is a guess.
    title = models.TextField()  # This field type is a guess.
    anons = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.TextField(blank=True, null=True)  # This field type is a guess.
    text = models.TextField(blank=True, null=True)
    tables = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'News'
