# Generated by Django 4.2.7 on 2023-11-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_grammar_bank_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammar_bank',
            name='question_type',
            field=models.CharField(max_length=255),
        ),
    ]
