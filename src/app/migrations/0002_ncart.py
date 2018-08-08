# Generated by Django 2.1 on 2018-08-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=80)),
                ('bookId', models.CharField(max_length=100)),
                ('bookName', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('Quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
