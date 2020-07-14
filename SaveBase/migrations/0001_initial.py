# Generated by Django 3.0.3 on 2020-03-12 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomerKab', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Номер кабинета',
                'verbose_name_plural': 'Номера кабинетов',
            },
        ),
        migrations.CreateModel(
            name='Korpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomKorpusa', models.CharField(max_length=3, verbose_name='Номер корпуса')),
                ('Adres', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Номер корпуса',
                'verbose_name_plural': 'Номера корпусов',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeTech', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип техники',
                'verbose_name_plural': 'Типы техники',
            },
        ),
        migrations.CreateModel(
            name='Techn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvNomer', models.CharField(max_length=50)),
                ('Naimen', models.CharField(max_length=100)),
                ('DataProverki', models.DateField(verbose_name='Дата проверки')),
                ('AktSpis', models.CharField(max_length=30)),
                ('DataUtil', models.DateField(verbose_name='Дата утилизации')),
                ('Prim', models.TimeField(verbose_name='Примечание')),
                ('IDKabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SaveBase.Kabinet')),
                ('IDType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SaveBase.Type')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техника',
            },
        ),
        migrations.AddField(
            model_name='kabinet',
            name='IDKorpus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SaveBase.Korpus'),
        ),
        migrations.AddField(
            model_name='kabinet',
            name='IDSotrud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataPerem', models.DateField(verbose_name='Дата перемещения')),
                ('AktPerem', models.CharField(max_length=30)),
                ('IDKab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SaveBase.Kabinet')),
                ('IDSotrud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('IDTech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SaveBase.Techn')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
            },
        ),
    ]