# Generated by Django 2.2 on 2019-05-07 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumtopic',
            name='Associated_Topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Topic'),
        ),
    ]