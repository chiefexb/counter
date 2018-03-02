# Generated by Django 2.0.1 on 2018-03-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(blank='False', max_length=1000, null='False', verbose_name='hash')),
                ('job', models.CharField(blank='False', max_length=1000, null='False', verbose_name='job')),
                ('strm', models.DateTimeField()),
                ('endm', models.DateTimeField()),
                ('version', models.CharField(blank='False', max_length=1000, null='False', verbose_name='version')),
                ('status', models.BooleanField(verbose_name='Статус')),
            ],
        ),
    ]