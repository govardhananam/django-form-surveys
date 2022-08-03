# Generated by Django 4.0.6 on 2022-08-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djf_surveys', '0008_auto_20220721_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['question__ordering']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['ordering']},
        ),
        migrations.AddField(
            model_name='question',
            name='key',
            field=models.CharField(blank=True, default='', max_length=225, null=True, unique=True),
        ),
    ]