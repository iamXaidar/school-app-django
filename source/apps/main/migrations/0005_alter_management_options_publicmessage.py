# Generated by Django 4.2 on 2023-11-08 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_management'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'verbose_name_plural': 'Management'},
        ),
        migrations.CreateModel(
            name='PublicMessage',
            fields=[
                ('public_message_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.management')),
            ],
            options={
                'db_table': 'public_message',
            },
        ),
    ]
