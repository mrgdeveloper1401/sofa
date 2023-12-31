# Generated by Django 5.0 on 2023-12-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='rate_choose',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=6, verbose_name='نمره'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
