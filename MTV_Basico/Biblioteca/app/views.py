from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import BibliotecaForm

def crud_read(request):
    livros = Biblioteca.objects.all()
    return render(request, 'crud_read.html', {'livros': livros})

def crud_create(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
    else:
        form = BibliotecaForm()
    return render(request, 'crud_form.html', {'form': form})

def crud_update(request, pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
    else:
        form = BibliotecaForm()
    return render(request, 'crud_form.html', {'form': form})

def crud_delete(request, pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('crud_read')
    return render(request, 'confirmacao_delete.html', {'livro': livro})
            