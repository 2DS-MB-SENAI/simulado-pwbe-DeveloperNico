from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import BibliotecaForm

def listar_livros(request):
    livros = Biblioteca.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def crud_create(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = BibliotecaForm()
    return render(request, 'crud_form.html', {'form': form})

def crud_update(request, pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = BibliotecaForm()
    return render(request, 'crud_form.html', {'form': form})

def crud_delete(request, pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'confirmacao_delete.html', {'livro': livro})
            