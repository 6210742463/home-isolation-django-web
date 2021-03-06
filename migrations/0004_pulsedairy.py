# Generated by Django 3.2.6 on 2021-09-04 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hs', '0003_alter_status_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PulseDairy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spo2', models.IntegerField(blank=True, null=True)),
                ('temp', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('beat', models.IntegerField(blank=True, null=True)),
                ('gs1', models.CharField(blank=True, max_length=50, null=True)),
                ('gs2', models.CharField(blank=True, max_length=50, null=True)),
                ('gs3', models.CharField(blank=True, max_length=50, null=True)),
                ('gs4', models.CharField(blank=True, max_length=50, null=True)),
                ('gs5', models.CharField(blank=True, max_length=50, null=True)),
                ('ys1', models.CharField(blank=True, max_length=50, null=True)),
                ('ys2', models.CharField(blank=True, max_length=50, null=True)),
                ('ys3', models.CharField(blank=True, max_length=50, null=True)),
                ('ys4', models.CharField(blank=True, max_length=50, null=True)),
                ('rs1', models.CharField(blank=True, max_length=50, null=True)),
                ('rs2', models.CharField(blank=True, max_length=50, null=True)),
                ('rs3', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
