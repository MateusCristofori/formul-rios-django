from django.shortcuts import render
from django import views
from .forms import PassagemForm

class IndexView(views.View):
  
  def get(self, request):
    form = PassagemForm()
    
    context = {
      'form': form
    }
    return render(request, 'index.html', context)
  
class ExibirDadosView(views.View):
  
    def post(self, request):
      form = PassagemForm(request.POST)
      if form.is_valid():
        context = {
          'form': form
        }
        return render(request, 'exibir_dados.html', context)
      else:
        print('form inválido')
        context = {
          'form': form
        }
        return render(request, 'index.html', context)