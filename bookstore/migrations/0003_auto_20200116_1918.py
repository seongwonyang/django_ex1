# Generated by Django 3.0.1 on 2020-01-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20200108_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
