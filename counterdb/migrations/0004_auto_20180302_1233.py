# Generated by Django 2.0.1 on 2018-03-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterdb', '0003_syst_stand_thash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syst_stand',
            name='thash',
            field=models.CharField(blank='True', max_length=1000, null='False', verbose_name='Стенд'),
        ),
    ]