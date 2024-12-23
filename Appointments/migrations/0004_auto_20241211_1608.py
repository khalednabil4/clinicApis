# Generated by Django 3.2.18 on 2024-12-11 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_specialist_is_deleted'),
        ('Appointments', '0003_alter_doctoravailability_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoravailability',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctoravailability',
            name='Doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='admin', to='User.administrator'),
        ),
        migrations.AlterField(
            model_name='doctoravailability',
            name='Status',
            field=models.CharField(choices=[('Process', 'Process'), ('Cancel', 'Cancel'), ('Rejected', 'Rejected by the administration'), ('waiting', 'waiting'), ('approval', 'approval'), ('AnotherDate', 'AnotherDate')], default=1, max_length=50),
        ),
    ]
