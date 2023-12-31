# Generated by Django 4.2.2 on 2023-06-27 15:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("voc", "0003_rename_voc_id_customertb_voc_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="voctb",
            name="uploaded_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="date uploaded",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="voctb",
            name="voc_desc",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="file name"
            ),
        ),
        migrations.AlterField(
            model_name="voctb",
            name="cent",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="voc.centertb",
            ),
        ),
    ]
