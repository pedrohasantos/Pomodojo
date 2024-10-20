# Generated by Django 5.1.1 on 2024-10-20 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.TextField(default='default@example.com', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.TextField(max_length=50),
        ),
    ]
