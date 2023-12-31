# Generated by Django 4.2.2 on 2023-06-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0005_alter_uploadfile_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boardtb",
            name="brd_content",
            field=models.TextField(verbose_name="게시판 내용"),
        ),
        migrations.AlterField(
            model_name="boardtb",
            name="brd_title",
            field=models.CharField(max_length=200, verbose_name="게시판 제목"),
        ),
        migrations.AlterField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="board/", verbose_name="업로드된 파일"
            ),
        ),
    ]
