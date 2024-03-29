# Generated by Django 3.2 on 2023-08-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0008_auto_20230822_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='anneescol_eleveM',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='descr_eleveM',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='frais_eleveM',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='num_tel_parentM',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevecem',
            name='anneescol_eleveMCEM',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='elevecem',
            name='descr_eleveMCEM',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='elevecem',
            name='frais_eleveMCEM',
            field=models.CharField(default='non', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevecem',
            name='nom_profMCEM',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='elevecem',
            name='num_tel_parentMCEM',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevepre',
            name='anneescol_eleveMpre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='elevepre',
            name='descr_eleveMpre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='elevepre',
            name='frais_eleveMpre',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevepre',
            name='nom_profMPre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='elevepre',
            name='num_tel_parentMpre',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eleveprim',
            name='anneescol_eleveMPrim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eleveprim',
            name='descr_eleveMPrim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eleveprim',
            name='frais_eleveMPrim',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eleveprim',
            name='nom_profMPrim',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eleveprim',
            name='num_tel_parentMPrim',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
