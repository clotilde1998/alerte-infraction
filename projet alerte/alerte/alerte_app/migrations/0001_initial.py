# Generated by Django 4.0 on 2021-12-27 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='localisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=150, verbose_name='Adresse')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='police_centrale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField(verbose_name='Telephone de la police')),
                ('adresse', models.CharField(max_length=150, verbose_name='Adresse de la police')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=120, verbose_name='Prenom')),
                ('adresse', models.CharField(max_length=120, verbose_name=' Adresse')),
                ('tel', models.IntegerField(verbose_name='Telephone')),
            ],
        ),
        migrations.CreateModel(
            name='alerte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.DateTimeField(auto_now_add=True, verbose_name='Date infraction')),
                ('description', models.TextField(blank=True, verbose_name='Description alerte')),
                ('localisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerte_app.localisation')),
                ('police_centrale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerte_app.police_centrale')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerte_app.user')),
            ],
        ),
    ]
