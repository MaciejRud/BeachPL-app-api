# Generated by Django 5.0.9 on 2024-10-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_tournament_teams_playertournamentresult_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(related_name='tournaments', to='core.team'),
        ),
    ]
