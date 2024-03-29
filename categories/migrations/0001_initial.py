# Generated by Django 5.0 on 2023-12-31 10:29

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categories.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('brand_name', models.CharField(blank=True, db_index=True, max_length=155, null=True, unique=True, verbose_name='نام برند')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_categories', to='categories.category')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'db_table': 'brands',
            },
        ),
    ]
