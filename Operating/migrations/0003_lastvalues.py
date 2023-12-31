# Generated by Django 4.2.5 on 2023-09-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operating', '0002_remove_dw1_name_remove_dw2_name_remove_gasp1_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lastvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gt11', models.CharField(max_length=5)),
                ('Gt12', models.CharField(max_length=5)),
                ('ST10', models.CharField(max_length=5)),
                ('RW1', models.CharField(max_length=5)),
                ('DW1', models.CharField(max_length=5)),
                ('Vacuum1', models.CharField(max_length=5)),
                ('TrancT1', models.CharField(max_length=5)),
                ('GasP1', models.CharField(max_length=5)),
                ('Gt21', models.CharField(max_length=5)),
                ('Gt22', models.CharField(max_length=5)),
                ('ST20', models.CharField(max_length=5)),
                ('RW2', models.CharField(max_length=5)),
                ('DW2', models.CharField(max_length=5)),
                ('Vacuum2', models.CharField(max_length=5)),
                ('TrancT2', models.CharField(max_length=5)),
                ('GasP2', models.CharField(max_length=5)),
            ],
        ),
    ]
