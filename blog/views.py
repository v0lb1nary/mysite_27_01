from django.shortcuts import render, get_object_or_404
from .models import Postagem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

def lista_postagem(request):
    lista_objetos = Postagem.publicado.all()
    paginacao = Paginator(lista_objetos, 3)
    pagina = request.GET.get('page')

    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:
        posts = paginacao.page(1)
    except EmptyPage:
        posts = paginacao.page(paginacao.num_pages)
    
    return render(request, 'blog/postagem/lista.html', {'pagina': pagina, 'posts':posts})


def detalhe_postagem(request, ano, mes, dia, rotulo):
    post = get_object_or_404(Postagem, rotulo= rotulo, 
                            status = 'publicado', 
                            data_publicacao__year = ano,
                            data_publicacao__month = mes, 
                            data_publicacao__day = dia)
    return render(request, 'blog/postagem/detalhe.html', { 'post' : post})

def compartilhar_postagem(request, post_id):
    post = get_object_or_404(Postagem, id=post_id, status='publicado')
    sent = False

    if request.method == 'POST':
        form = FormularioPostEmail(request.POST)

        if form.is_valed():
            cd = form.cleaned_data 
            post_url = request.build_absolute_url(post.get_absolute_url())
            assunto = f"{cd['nome']} recomendado que vc leia" f"{ post.titulo }"
            mensagem = f"Leia {post.titulo} em {post.url}\n \n" f"{cd['nome']}\s comentario: " f"{cd['comentarios']}"  
            send_email (assunto, mensagem, 'pyhton.django@gmail.com', [cd['para']])
            sent = True
    
    else:
        form = FormularioPostEmail()

        return render(request, 'blog/postagem/compartilhar.html,' {'post':post, 'form':form, 'sent':sent})