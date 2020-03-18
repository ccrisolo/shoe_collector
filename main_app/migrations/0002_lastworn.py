# Generated by Django 3.0.2 on 2020-03-18 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastWorn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('activity', models.CharField(choices=[('C', 'Casual'), ('G', 'Gym'), ('S', 'Sport')], default='C', max_length=1)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Shoe')),
            ],
        ),
    ]