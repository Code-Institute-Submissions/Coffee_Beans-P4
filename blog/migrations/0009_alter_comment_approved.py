# Generated by Django 5.0.4 on 2024-04-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.IntegerField(default=0),
        ),
    ]
