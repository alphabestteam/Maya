# Generated by Django 4.2.6 on 2023-10-25 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_unread_messages_user_unread_messages'),
        ('forms', '0004_remove_messagesform_message_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesform',
            name='receiver_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
