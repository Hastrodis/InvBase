# Generated by Django 3.0.3 on 2020-05-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaveBase', '0002_auto_20200312_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techn',
            name='AktSpis',
        ),
        migrations.AlterField(
            model_name='techn',
            name='DataUtil',
            field=models.DateField(blank=True, verbose_name='Дата утилизации'),
        ),
        migrations.AlterField(
            model_name='techn',
            name='Prim',
            field=models.TextField(blank=True, default=12.23, verbose_name='Примечание'),
            preserve_default=False,
        ),
    ]
