# Generated by Django 4.2.5 on 2023-12-12 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_myproduct"),
    ]

    operations = [
        migrations.CreateModel(
            name="maincate",
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
                ("Name", models.CharField(max_length=20)),
                (
                    "picture",
                    models.ImageField(null=True, upload_to="static/mcategory/"),
                ),
                ("cdate", models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name="myproduct",
            name="mcategory",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.maincate",
            ),
        ),
    ]