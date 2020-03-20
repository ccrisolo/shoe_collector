# Generated by Django 3.0.2 on 2020-03-20 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200320_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Shoe')),
            ],
        ),
    ]
