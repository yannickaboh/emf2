# Generated by Django 2.1.5 on 2019-12-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microfinance', '0002_caisse_depot_retrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depot',
            name='motif',
            field=models.TextField(blank=True, max_length=250, verbose_name='Motif'),
        ),
    ]