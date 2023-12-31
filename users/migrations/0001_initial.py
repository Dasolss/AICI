# Generated by Django 4.2.2 on 2023-06-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UidTB",
            fields=[
                (
                    "uid",
                    models.CharField(
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="engineer identification number",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="engineer name")),
            ],
        ),
        migrations.CreateModel(
            name="EngineerTB",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "usr_id",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="engineer ID"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="engineer name")),
                (
                    "phonenum",
                    models.CharField(
                        max_length=11, verbose_name="engineer phone number"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="verify a staff"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="verify a engineer active"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, verbose_name="date modified"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "uid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.uidtb"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
