# Generated by Django 4.2.7 on 2023-12-01 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(default=8600, unique=True)),
                ('money', models.IntegerField(default=0)),
                ('expired_date', models.DateTimeField()),
                ('card_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
        ),
    ]
