# Generated by Django 3.2.8 on 2022-08-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_tablecolumns_column_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablecolumns',
            name='column_type',
            field=models.CharField(choices=[('String', 'String'), ('Boolean', 'Boolean'), ('Number', 'Number'), ('Email', 'Email'), ('DateTime', 'DateTime')], max_length=20),
        ),
    ]
