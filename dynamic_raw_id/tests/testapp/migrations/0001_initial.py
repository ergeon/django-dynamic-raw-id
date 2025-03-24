# Generated by Django 5.0.4 on 2024-04-21 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CharPrimaryKeyModel",
            fields=[
                (
                    "chr",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IntPrimaryKeyModel",
            fields=[
                (
                    "num",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="Number"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ModelToTestInlinesBase",
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
            ],
        ),
        migrations.CreateModel(
            name="UUIDPrimaryKeyModel",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="ModelToTestInlines",
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
                (
                    "dynamic_raw_id_fk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="inline_dynamic_raw_id_fk",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Dynamic RawID ForeignKey",
                    ),
                ),
                (
                    "base",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testapp.modeltotestinlinesbase",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ModelToTest",
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
                (
                    "dynamic_raw_id_fk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dynamic_raw_id_fk",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Dynamic RawID ForeignKey",
                    ),
                ),
                (
                    "dynamic_raw_id_fk_char_pk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dynamic_raw_id_fk_char_pk",
                        to="testapp.charprimarykeymodel",
                        verbose_name="Dynamic RawID Custom Primary Key: Character Field",
                    ),
                ),
                (
                    "dynamic_raw_id_fk_int_pk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dynamic_raw_id_fk_int_pk",
                        to="testapp.intprimarykeymodel",
                        verbose_name="Dynamic RawID Custom Primary Key: Integer Field",
                    ),
                ),
                (
                    "dynamic_raw_id_fk_limited",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_staff": True},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dynamic_raw_id_fk_limited",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Dynamic RawID ForeignKey with limited choices",
                    ),
                ),
                (
                    "dynamic_raw_id_many",
                    models.ManyToManyField(
                        blank=True,
                        related_name="dynamic_raw_id_many",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Dynamic RawID ManyToMany",
                    ),
                ),
                (
                    "rawid_fk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rawid_fk",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Regular RawID ForeignKey",
                    ),
                ),
                (
                    "rawid_fk_limited",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_staff": True},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rawid_fk_limited",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Regular RawID ForeignKey with limited choices",
                    ),
                ),
                (
                    "rawid_many",
                    models.ManyToManyField(
                        blank=True,
                        related_name="rawid_many",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Regular RawID ManyToMany",
                    ),
                ),
                (
                    "dynamic_raw_id_fk_uuid_pk",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dynamic_raw_id_fk_uuid_pk",
                        to="testapp.uuidprimarykeymodel",
                        verbose_name="Dynamic RawID Custom Primary Key: UUID Field",
                    ),
                ),
            ],
        ),
    ]
