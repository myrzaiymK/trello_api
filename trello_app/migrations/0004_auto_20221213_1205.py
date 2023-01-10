# Generated by Django 3.2.16 on 2022-12-13 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0003_auto_20221213_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('board', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.board')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('board', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.board')),
            ],
        ),
        migrations.CreateModel(
            name='LabelColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='labelcard',
            name='label',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='trello_app.label'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CheckListCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.card')),
                ('checklist', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.checklist')),
            ],
        ),
        migrations.CreateModel(
            name='AttachmentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.attachment')),
                ('card', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='trello_app.card')),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trello_app.labelcolor'),
            preserve_default=False,
        ),
    ]
