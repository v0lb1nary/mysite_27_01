# Generated by Django 3.1.5 on 2021-01-27 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.postagem')),
            ],
            options={
                'ordering': ('data_criacao',),
            },
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
