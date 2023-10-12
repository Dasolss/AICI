# Generated by Django 4.2.2 on 2023-06-28 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("voc", "0006_alter_voctb_voc_desc"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConstructionTB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cstr_desc",
                    models.CharField(max_length=20, verbose_name="file name"),
                ),
                (
                    "cstr_file",
                    models.FileField(
                        upload_to="construction/%Y/%m/%d", verbose_name="uploaded file"
                    ),
                ),
                (
                    "started_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="construction date"
                    ),
                ),
                (
                    "cstr_location",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="construction location"
                    ),
                ),
                (
                    "cstr_company",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="construction company"
                    ),
                ),
                (
                    "cstr_num",
                    models.CharField(
                        blank=True, max_length=11, verbose_name="company tel number"
                    ),
                ),
                (
                    "cent",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="voc.centertb",
                    ),
                ),
            ],
        ),
    ]