# Generated by Django 3.0.2 on 2020-03-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200318_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='stores',
            field=models.ManyToManyField(to='main_app.Store'),
        ),
    ]
