# Generated by Django 5.0 on 2023-12-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('image', models.ImageField(height_field='height', upload_to='products/images/%Y/%m/%d', verbose_name='عکس', width_field='width')),
                ('image_hash', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='هش')),
                ('image_size', models.PositiveIntegerField(default=0, verbose_name='حجم عکس')),
                ('alter_image', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن عکس')),
                ('width', models.PositiveIntegerField(default=0, verbose_name='عرض')),
                ('height', models.PositiveIntegerField(default=0, verbose_name='ارتفاع')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]