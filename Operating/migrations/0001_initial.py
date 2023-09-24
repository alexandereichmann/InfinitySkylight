# Generated by Django 4.2.5 on 2023-09-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DW1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DW1', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DW2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DW2', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GasP1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GasP1', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GasP2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GasP2', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GT11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GT11', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GT12',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GT12', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GT21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GT21', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GT22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GT22', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RW1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='RW1', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RW2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='RW2', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ST10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ST10', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ST20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ST20', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrancT1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='TrancT1', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrancT2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='TrancT2', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuum1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Vacuum1', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuum2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Vacuum2', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('employee', models.CharField(max_length=255)),
            ],
        ),
    ]