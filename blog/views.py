from django.shortcuts import render, get_object_or_404
from .models import Postagem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

