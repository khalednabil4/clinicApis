# Generated by Django 3.2.18 on 2024-12-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0006_specialist_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], max_length=20)),
                ('HourTo', models.TimeField()),
                ('HourFrom', models.TimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('Admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='DaysOpen', to='User.administrator')),
            ],
        ),
    ]
