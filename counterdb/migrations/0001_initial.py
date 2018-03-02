# Generated by Django 2.0.1 on 2018-03-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Syst_stand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syst', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Система')),
                ('stand', models.CharField(blank='False', max_length=1000, null='False', verbose_name='Стенд')),
                ('tested', models.BooleanField(verbose_name='Тестирование')),
                ('thash', models.CharField(blank='True', max_length=1000, null='False', verbose_name='Хеш')),
            ],
        ),
    ]
