# Generated by Django 3.2.8 on 2022-09-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_atten_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=150)),
                ('Lname', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Msg', models.CharField(max_length=150)),
            ],
        ),
    ]
