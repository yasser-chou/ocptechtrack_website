# Generated by Django 4.2.3 on 2023-07-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_employe_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='site',
            field=models.CharField(choices=[('Benguerir', 'Benguerir'), ('Casablanca', 'Casablanca'), ('Jorf Lasfar', 'Jorf Lasfar'), ('Khouribga', 'Khouribga'), ('Boucraâ', 'Boucraâ'), ('Youssoufia', 'Youssoufia'), ('Safi', 'Safi'), ('Laâyoune', 'Laâyoune'), ('Autre', 'Autre')], default='NoName', max_length=120),
        ),
        migrations.AddField(
            model_name='employe',
            name='telephone',
            field=models.CharField(default='0000000000', max_length=30, verbose_name='Contact phone'),
        ),
        migrations.AddField(
            model_name='tech',
            name='email_address',
            field=models.EmailField(default='example@example.com', max_length=254, verbose_name='Employe Email'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='site',
            field=models.CharField(choices=[('Benguerir', 'Benguerir'), ('Casablanca', 'Casablanca'), ('Jorf Lasfar', 'Jorf Lasfar'), ('Khouribga', 'Khouribga'), ('Boucraâ', 'Boucraâ'), ('Youssoufia', 'Youssoufia'), ('Safi', 'Safi'), ('Laâyoune', 'Laâyoune'), ('Autre', 'Autre')], default='NoName', max_length=120),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('in progress', 'in progress'), ('pending', 'pending')], max_length=120),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ticket Date'),
        ),
    ]
