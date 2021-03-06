# Generated by Django 2.0.6 on 2019-05-23 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeraddress',
            options={},
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='id',
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='ad_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='add_detail',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='telephone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='territory',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
    ]
