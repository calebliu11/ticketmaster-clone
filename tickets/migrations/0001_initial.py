# Generated by Django 4.1.6 on 2023-04-05 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tickets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "funds",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                ("account_number", models.CharField(max_length=100)),
                ("routing_number", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("user_email", models.CharField(max_length=100)),
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
                ("image", models.ImageField(blank=True, null=True, upload_to="pics")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("email", models.CharField(max_length=100)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("cost", models.IntegerField(default=0)),
                ("stripe_token", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        default=tickets.models.get_next_integer_value,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("reason", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=300)),
                ("verified", models.BooleanField(default=False)),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="tickets.listing",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("event", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=300)),
                ("price", models.IntegerField(default=0)),
                ("seller_email", models.CharField(max_length=100)),
                ("date", models.DateField(blank=True)),
                ("image_url", models.CharField(max_length=100)),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="tickets.listing",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="tickets.order",
                    ),
                ),
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
