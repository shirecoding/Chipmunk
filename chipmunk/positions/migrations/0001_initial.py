# Generated by Django 3.1.7 on 2021-03-11 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('TRADITIONAL', 'Traditional IRA or 401(k)'), ('ROTH', 'Roth IRA or 401(k)'), ('STANDARD', 'Standard Brokerage')], max_length=100)),
                ('cash_balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('shares', models.FloatField()),
                ('cost_basis', models.FloatField(default=0.0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.account')),
            ],
        ),
    ]