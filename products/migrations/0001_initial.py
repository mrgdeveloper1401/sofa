# Generated by Django 5.0 on 2023-12-30 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('images', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('attribute_name', models.CharField(max_length=155, verbose_name='ویژگی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'attribute',
                'verbose_name_plural': 'attributes',
                'db_table': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('option_name', models.CharField(max_length=155, unique=True, verbose_name='آپشن')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'option',
                'verbose_name_plural': 'options',
                'db_table': 'options',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('en_name', models.CharField(db_index=True, max_length=155, verbose_name='نام انگلیسی')),
                ('fa_name', models.CharField(max_length=155, verbose_name='نام فارسی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=155, unique=True, verbose_name='اسلاگ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح محصول')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_brands', to='categories.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_categories', to='categories.category')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_images', to='images.images')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_videos', to='videos.movies')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('option_value', models.CharField(max_length=155, verbose_name='نام آپشن')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='option_values', to='products.option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_option_value', to='products.product')),
            ],
            options={
                'verbose_name': 'option value',
                'verbose_name_plural': 'option values',
                'db_table': 'option_values',
            },
        ),
        migrations.AddField(
            model_name='option',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_option', to='products.product'),
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('attribute_value', models.CharField(max_length=155, verbose_name='نام ویژگی')),
                ('attribute_text', models.TextField(blank=True, null=True, verbose_name='توضیح ویژگی')),
                ('attribute_date', models.DateField(blank=True, null=True, verbose_name='تاریخ ویژگی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attribute_values', to='products.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_attribute_value', to='products.product')),
            ],
            options={
                'verbose_name': 'attribute value',
                'verbose_name_plural': 'attribute values',
                'db_table': 'attribute_values',
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_attribute', to='products.product'),
        ),
    ]
