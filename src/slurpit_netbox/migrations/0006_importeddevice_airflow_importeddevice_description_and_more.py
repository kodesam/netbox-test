# Generated by Django 4.2.8 on 2023-12-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slurpit_netbox', '0005_remove_slurpitlog_comments_remove_slurpitlog_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importeddevice',
            name='airflow',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='description',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='location',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='position',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='rack',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='region',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='importeddevice',
            name='tenant',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='airflow',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='description',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='location',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='position',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='rack',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='region',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='stageddevice',
            name='tenant',
            field=models.TextField(max_length=128, null=True),
        ),
    ]