# Generated by Django 4.2.2 on 2023-06-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0009_alter_uploadfile_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="board", verbose_name="uploaded file"
            ),
        ),
    ]
