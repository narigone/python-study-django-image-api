# Generated by Django 2.2.1 on 2019-05-15 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.FileField(max_length=500, upload_to='../media/images', verbose_name='Imagem'),
        ),
    ]