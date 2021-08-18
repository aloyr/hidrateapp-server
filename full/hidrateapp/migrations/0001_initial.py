# Generated by Django 3.2.6 on 2021-08-18 15:36

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import hidrateapp.models
import hidrateapp.sessions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('read', 'read'), ('write', 'write')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('date', models.DateField()),
                ('totalAmount', models.IntegerField(default=0)),
                ('totalBottleAmount', models.IntegerField(default=0)),
                ('isLocationUsed', models.BooleanField(default=False)),
                ('recommendedGoal', models.FloatField(default=0)),
                ('goal', models.FloatField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('altitude', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('rank', models.IntegerField(null=True)),
                ('steps', models.IntegerField(null=True)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HidrateSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='session key')),
                ('session_data', models.TextField(verbose_name='session data')),
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire date')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'db_table': 'hidrate_session',
                'abstract': False,
            },
            managers=[
                ('objects', hidrateapp.sessions.models.HidrateSessionManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('birthday', hidrateapp.models.DateTimeField(null=True)),
                ('wakeUp', hidrateapp.models.DateTimeField(null=True)),
                ('goToSleep', hidrateapp.models.DateTimeField(null=True)),
                ('sipGlow', models.BooleanField()),
                ('gender', models.CharField(max_length=128)),
                ('weight', models.FloatField()),
                ('timeZone', models.CharField(max_length=128)),
                ('fluidInMetric', models.BooleanField()),
                ('elevationInMetric', models.BooleanField()),
                ('heightInMetric', models.BooleanField()),
                ('lightNotificationCount', models.IntegerField()),
                ('degreesInMetric', models.BooleanField()),
                ('appNotificationCount', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('breastfeeding', models.BooleanField(default=False)),
                ('weightInMetric', models.BooleanField()),
                ('pushNotificationCount', models.IntegerField()),
                ('spam', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('activityLevel', models.PositiveSmallIntegerField()),
                ('username', models.CharField(max_length=128, unique=True)),
                ('height', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('agreedToTOS', models.BooleanField(default=False)),
                ('suppressedNotificationTypes', models.JSONField(default=list)),
                ('bottleVendors', models.JSONField(default=dict)),
                ('fitbitUserId', models.CharField(max_length=128)),
                ('goal', models.FloatField(null=True)),
                ('lightType', models.IntegerField(default=0)),
                ('pushNotificationAlways', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=1024)),
                ('acl', models.ManyToManyField(related_name='_hidrateapp_user_acl_+', to='hidrateapp.ACL')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UserHealthStats',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('recentTotal', models.FloatField(default=0)),
                ('recentGoal', models.FloatField(default=0)),
                ('bottlesSaved', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('average', models.FloatField(default=0)),
                ('goalMetCount', models.IntegerField(default=0)),
                ('statDate', hidrateapp.models.DateTimeField(auto_now_add=True)),
                ('volume', models.FloatField(default=0)),
                ('streak', models.IntegerField(default=0)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Sip',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('time', hidrateapp.models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(default=0)),
                ('bottleSerialNumber', models.CharField(max_length=128)),
                ('max', models.IntegerField(default=0)),
                ('min', models.IntegerField(default=0)),
                ('start', models.IntegerField(default=0)),
                ('stop', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('altitude', models.FloatField()),
                ('point', models.JSONField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('deviceType', models.CharField(max_length=128)),
                ('appVersion', models.CharField(max_length=128)),
                ('appName', models.CharField(max_length=128)),
                ('timeZone', models.CharField(max_length=128)),
                ('installationId', models.UUIDField(null=True)),
                ('appIdentifier', models.CharField(max_length=128)),
                ('localeIdentifier', models.CharField(max_length=128)),
                ('deviceName', models.CharField(max_length=128)),
                ('pushType', models.CharField(max_length=128)),
                ('deviceToken', models.CharField(max_length=512)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Glow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('content', models.JSONField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.AddField(
            model_name='day',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hidrateapp.location'),
        ),
        migrations.AddField(
            model_name='day',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.user'),
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('objectId', hidrateapp.models.ObjectIDAutoField(serialize=False)),
                ('lastSynced', hidrateapp.models.DateTimeField(auto_now=True)),
                ('batteryLevel', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('firmwareBootloaderVersion', models.IntegerField(default=0)),
                ('firmwareMinorVersion', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=128)),
                ('serialNumber', models.CharField(max_length=128)),
                ('shouldUpdate', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('description', models.JSONField(default=dict)),
                ('location', models.JSONField(default=dict)),
                ('acl', models.ManyToManyField(to='hidrateapp.ACL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hidrateapp.user')),
            ],
            bases=(hidrateapp.models.SerializableMixin, models.Model),
        ),
        migrations.AddField(
            model_name='acl',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acls', to='hidrateapp.user'),
        ),
        migrations.AlterUniqueTogether(
            name='day',
            unique_together={('user', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='acl',
            unique_together={('user', 'permission')},
        ),
    ]