# Generated by Django 4.2.4 on 2023-08-08 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('consola', models.CharField(choices=[('xbox', 'Xbox'), ('switch', 'Nintendo_Switch'), ('ps4', 'PS4'), ('pc', 'PC'), ('otro', 'Otro')], default='pc', max_length=15)),
                ('producto', models.CharField(choices=[('consola', 'Consola'), ('juego', 'Juego'), ('periferico', 'Periferico')], default='juego', max_length=15)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('año', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-fechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='foro.consola')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
