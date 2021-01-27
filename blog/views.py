from django.shortcuts import render, get_object_or_404
from .models import Postagem, Comentarios
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FormularioPostEmail, FormularioComentarios
from django.core.mail import send_mail

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
    

    #Lista dos comentários ativos para esta postagem
    comentarios = post.comentarios.filter(ativo=True)
    novo_comentario = None
    if request.method == 'POST':
        formulario_comentario = FormularioComentarios(data=request.POST)
        if formulario_comentario.is_valid():
            novo_comentario = formulario_comentario.save(commit=False)
            novo_comentario.post = post
            novo_comentario.save()
    else:
        formulario_comentario = FormularioComentarios()
    return render(request, 'blog/postagem/detalhe.html', { 'post' : post,
                                                            'comentarios': comentarios,
                                                            'novo_comentario': novo_comentario,
                                                            'formulario_comentario': formulario_comentario})

def compartilhar_postagens(request, post_id):
    post = get_object_or_404(Postagem, id=post_id, status='publicado')
    sent = False

    if request.method == 'POST':
        form = FormularioPostEmail(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            assunto = f"{cd['nome']} recomendado que você leia" f"{ post.titulo }"
            mensagem = f"Leia {post.titulo} em {post_url}\n\n" f"{cd['nome']}\'s comentarios: {cd ['comentarios']}"
            send_mail(assunto, mensagem, 'pyhton.django@gmail.com', [cd['para']])
            sent = True
    else:
        form = FormularioPostEmail()
    
    return render(request, 'blog/postagem/compartilhar.html', {'post':post, 'form':form, 'sent':sent}) 