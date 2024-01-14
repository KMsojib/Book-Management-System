# Generated by Django 5.0 on 2024-01-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStoreModel',
            fields=[
                ('Book_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_Name', models.CharField(max_length=30)),
                ('Catagory', models.CharField(choices=[('Historical fiction', 'Historical fiction'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Comics', 'Comics'), ('Short Story', 'Short Story'), ('Memoir', 'Memoir'), ('Magical Realism', 'Magical Realism'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Biography', 'Biography'), ('Dystopian', 'Dystopian'), ('CookBook', 'CookBook'), ('Paranormal Activity', 'Paranormal Activity'), ('History', 'History')], max_length=30)),
                ('Author', models.CharField(max_length=30)),
                ('First_publication', models.DateTimeField(auto_now_add=True)),
                ('Last_publication', models.DateTimeField()),
            ],
        ),
    ]
