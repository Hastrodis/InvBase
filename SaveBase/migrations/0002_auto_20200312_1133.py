# Generated by Django 3.0.3 on 2020-03-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaveBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='AktPerem',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='techn',
            name='AktSpis',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='techn',
            name='DataUtil',
            field=models.DateField(blank=True, null=True, verbose_name='Дата утилизации'),
        ),
        migrations.AlterField(
            model_name='techn',
            name='Prim',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
    ]
