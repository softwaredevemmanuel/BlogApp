# Generated by Django 2.1.5 on 2022-11-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0003_auto_20221125_1101"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(default="coding", max_length=255),
        ),
    ]
