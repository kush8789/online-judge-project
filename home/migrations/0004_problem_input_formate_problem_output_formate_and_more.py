# Generated by Django 4.2 on 2023-05-21 07:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_solution_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="problem",
            name="input_formate",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problem",
            name="output_formate",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problem",
            name="problem_constraint",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problem",
            name="problem_input",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problem",
            name="problem_output",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="problem",
            name="statement",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
