# Generated by Django 4.2 on 2023-05-21 07:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_problem_input_formate_problem_output_formate_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="problem",
            name="problem_input",
        ),
        migrations.RemoveField(
            model_name="problem",
            name="problem_output",
        ),
        migrations.AlterField(
            model_name="testcase",
            name="input",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="testcase",
            name="output",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
