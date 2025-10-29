"""
Initial migration that does not create tables and is based on existing ones.
Following Django's table naming conventions, models resulting from a refactor
will be registered in renamed tables in the database.
"""

from django.db import migrations, models
from django.core import validators
from django.db.models import deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Address',
                    fields=[
                        ('id',
                         models.BigAutoField(auto_created=True,
                                             primary_key=True,
                                             serialize=False,
                                             verbose_name='ID')),
                        ('number',
                         models.PositiveIntegerField(
                            validators=[
                                validators.MaxValueValidator(9999)
                            ]
                         )),
                        ('street', models.CharField(max_length=64)),
                        ('city', models.CharField(max_length=64)),
                        ('state',
                         models.CharField(
                            max_length=2,
                            validators=[
                                validators.MinLengthValidator(2)
                            ]
                         )),
                        ('zip_code',
                         models.PositiveIntegerField(
                            validators=[
                                validators.MaxValueValidator(99999)
                            ]
                         )),
                        ('country_iso_code',
                         models.CharField(
                            max_length=3,
                            validators=[
                                validators.MinLengthValidator(3)
                            ]
                         )),
                    ],
                ),
                migrations.CreateModel(
                    name='Letting',
                    fields=[
                        (
                            'id',
                            models.BigAutoField(auto_created=True,
                                                primary_key=True,
                                                serialize=False,
                                                verbose_name='ID')
                        ),
                        ('title', models.CharField(max_length=256)),
                        (
                            'address',
                            models.OneToOneField(
                                on_delete=deletion.CASCADE,
                                to='lettings.address'
                            ),
                        ),
                    ],
                ),
            ],
            database_operations=[],
        ),
    ]
