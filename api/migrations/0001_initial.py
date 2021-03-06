# Generated by Django 2.1 on 2018-09-01 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('atualizado_em', models.DateTimeField(null=True)),
                ('cadatrado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('ponto_positivo', models.CharField(blank=True, max_length=255, null=True)),
                ('ponto_negativo', models.CharField(blank=True, max_length=255, null=True)),
                ('cadatrado_em', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voto', to='api.Produto')),
            ],
        ),
    ]
