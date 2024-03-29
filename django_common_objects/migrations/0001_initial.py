# Generated by Django 4.1.7 on 2023-03-07 15:13

import django_common_objects.fields
import django_common_objects.models
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonFieldConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30, verbose_name='所属模型')),
                ('key', models.CharField(max_length=20, verbose_name='字段')),
                ('value', models.CharField(blank=True, max_length=200, null=True, verbose_name='值')),
                ('type', models.CharField(choices=[('fixed', '固定值'), ('int', '整数'), ('float', '浮点数'), ('string', '字符串'), ('list', '列表'), ('dict', '字典')], default='string', max_length=10, verbose_name='类型')),
                ('is_required', models.BooleanField(default=False, verbose_name='是否必填')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '通用配置',
                'verbose_name_plural': '通用配置',
                'db_table': 'common_field_config',
            },
        ),
        migrations.CreateModel(
            name='CommonTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30, verbose_name='所属模型')),
                ('name', models.CharField(max_length=50, verbose_name='标签名')),
                ('config', django_common_objects.fields.ConfigField(blank=True, null=True, verbose_name='详细')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '通用标签',
                'verbose_name_plural': '通用标签',
                'db_table': 'common_tag',
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='CommonCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30, verbose_name='所属模型')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('config', django_common_objects.fields.ConfigField(blank=True, null=True, verbose_name='详细')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='django_common_objects.commoncategory', verbose_name='父类别')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '通用类别',
                'verbose_name_plural': '通用类别',
                'db_table': 'common_category',
                'unique_together': {('user', 'name', 'parent')},
            },
        ),
    ]
