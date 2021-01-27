from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class GerenciarPostagem(models.Manager):
    def get_queryset(self):
        return super (GerenciarPostagem,self).get_queryset().filter(status='publicado')


class Postagem(models.Model):
    STATUS_CHOICE = (('rascunho', 'Rascunho'), ('publicado', 'Publicado'))

    titulo = models.CharField(max_length=250)
    rotulo = models.SlugField(max_length=250, unique_for_date='data_publicacao')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_postagem')
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='rascunho')

    objects = models.Manager()
    publicado = GerenciarPostagem()

    def get_absolute_url(self):
        return reverse('blog:detalhe_postagem', 
                        args=[self.data_publicacao.year,
                        self.data_publicacao.month, 
                        self.data_publicacao.day,
                        self.rotulo])

    class Meta:
        ordering = ("-data_publicacao",)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):

    post = models.ForeignKey(Postagem, verbose_name=("comentario"),on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    ativo = models.BooleanField()

    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")

    def __str__(self):
        return f'Comentario por {self.nome} no {self.post}'
