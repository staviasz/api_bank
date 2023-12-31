# Generated by Django 4.2.6 on 2023-10-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_cpf_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Numero da Conta'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='number_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accounts'),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='number_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accounts'),
        ),
    ]
