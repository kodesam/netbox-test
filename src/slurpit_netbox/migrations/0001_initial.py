# Generated by Django 4.2.7 on 2023-12-02 06:19

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0181_rename_device_role_device_role'),
        ('extras', '0098_webhook_custom_field_data_webhook_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='StagedDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('digest', models.TextField(max_length=64, unique=True)),
                ('hostname', models.TextField(max_length=255, unique=True)),
                ('fqdn', models.TextField(max_length=128)),
                ('device_os', models.TextField(max_length=128)),
                ('device_type', models.TextField(max_length=255)),
                ('disabled', models.IntegerField()),
                ('added', models.TextField(max_length=32)),
                ('last_seen', models.DateTimeField(null=True)),
                ('createddate', models.DateTimeField()),
                ('changeddate', models.DateTimeField(null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=200)),
                ('status', models.CharField(default='new', editable=False, max_length=50)),
                ('parameters', models.JSONField(blank=True, null=True)),
                ('last_synced', models.DateTimeField(blank=True, editable=False, null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': "Slurp'it Setting",
                'verbose_name_plural': "Slurp'it Settings",
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ImportedDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('digest', models.TextField(max_length=64, unique=True)),
                ('hostname', models.TextField(max_length=255, unique=True)),
                ('fqdn', models.TextField(max_length=128)),
                ('device_os', models.TextField(max_length=128)),
                ('device_type', models.TextField(max_length=255)),
                ('disabled', models.IntegerField()),
                ('added', models.TextField(max_length=32)),
                ('last_seen', models.DateTimeField(null=True)),
                ('createddate', models.DateTimeField()),
                ('changeddate', models.DateTimeField(null=True)),
                ('mapped_device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.device')),
                ('mapped_devicetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.devicetype')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
