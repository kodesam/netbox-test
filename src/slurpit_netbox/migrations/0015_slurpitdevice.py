# Generated by Django 4.2.8 on 2024-01-19 02:35

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0105_customfield_min_max_values'),
        ('slurpit_netbox', '0014_remove_slurpitplan_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlurpitDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('hostname', models.TextField(max_length=255, null=True)),
                ('plan_id', models.TextField(max_length=10, null=True)),
                ('content', models.JSONField()),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]