# Generated by Django 5.0.6 on 2024-07-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drink",
            fields=[
                ("drinkId", models.AutoField(primary_key=True, serialize=False)),
                ("drinkName", models.CharField(max_length=128)),
                ("drinkType", models.CharField(max_length=128)),
                ("drinkDescription", models.TextField()),
                ("drinkPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("drinkImage", models.CharField(max_length=100, null=True)),
                ("drinkRegisteredDate", models.DateTimeField(auto_now_add=True)),
                ("drinkUpdatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "drink",
            },
        ),
    ]
