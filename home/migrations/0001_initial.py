# Generated by Django 3.1.2 on 2020-10-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=15)),
                ('phone', models.CharField(max_length=10)),
                ('massage', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
