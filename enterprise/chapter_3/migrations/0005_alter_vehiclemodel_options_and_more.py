# Generated by Django 4.0 on 2024-04-12 22:00

from django.db import migrations, models
import django.db.models.expressions
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0004_seller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'ordering': ['name'], 'verbose_name': 'Vehicle Model', 'verbose_name_plural': 'Vehicle Models'},
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['name'], name='chapter_3_v_name_7ccb3d_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['-name'], name='desc_name_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(django.db.models.expressions.OrderBy(django.db.models.functions.text.Lower('name'), descending=True), name='lower_name_idx'),
        ),
    ]
