# Generated by Django 5.0 on 2023-12-31 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
                'db_table': 'about_us',
            },
        ),
    ]
