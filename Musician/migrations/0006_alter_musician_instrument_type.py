# Generated by Django 5.0.6 on 2024-06-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0005_rename_phonenumber_field_musician_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('guitar', 'Guitar'), ('piano', 'Piano'), ('drums', 'Drums'), ('violin', 'Violin'), ('saxophone', 'Saxophone')], max_length=50),
        ),
    ]
