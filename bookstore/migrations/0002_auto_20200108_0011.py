# Generated by Django 3.0.1 on 2020-01-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstore',
            name='id',
        ),
        migrations.AddField(
            model_name='bookstore',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='code',
            field=models.CharField(default=models.AutoField(primary_key=True), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
