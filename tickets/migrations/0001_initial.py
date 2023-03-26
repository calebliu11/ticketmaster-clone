# Generated by Django 4.1.6 on 2023-03-24 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=150)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("event", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=300)),
                ("price", models.IntegerField(default=0)),
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("ACTIVE", "Active"),
                            ("SOLD", "Sold"),
                            ("EXPIRED", "Expired"),
                        ],
                        default="ACTIVE",
                    ),
                ),
                ("date", models.DateField(blank=True)),
                ("slug", models.SlugField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
