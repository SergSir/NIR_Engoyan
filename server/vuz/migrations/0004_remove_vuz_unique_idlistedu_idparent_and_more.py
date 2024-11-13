# Generated by Django 4.2.16 on 2024-11-13 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vuz", "0003_alter_main_id_listedu_alter_main_id_parent"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="vuz",
            name="unique_idlistedu_idparent",
        ),
        migrations.AlterField(
            model_name="training",
            name="progid",
            field=models.ForeignKey(
                db_column="progid",
                on_delete=django.db.models.deletion.CASCADE,
                to="vuz.program",
            ),
        ),
    ]
