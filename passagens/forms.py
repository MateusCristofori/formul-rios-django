from cProfile import label
from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from .classe_viagem import tipos_de_classes
from passagens.validation import *

class PassagemForm(forms.Form):
  origem = forms.CharField(label='Origem', max_length=100)
  destino = forms.CharField(label='Destino', max_length=100)
  email = forms.EmailField(label='E-mail', max_length=100)
  data_ida = forms.DateField(label='Ida', widget=DatePicker())
  data_volta = forms.DateField(label='Volta', widget=DatePicker())
  data_pesquisa = forms.DateField(label="Data da pesquisa", disabled=True, initial=datetime.today)
  classe_viagem = forms.ChoiceField(label='Classe do voo', choices=tipos_de_classes)
  informacoes = forms.CharField(
    label='Informações extras',
    max_length=200,
    widget=forms.Textarea(),
    required=False
  )

 
def clean(self):
  origem = self.cleaned_data.get('origem')
  destino = self.cleaned_data.get('destino')
  data_ida = self.cleaned_data.get('data_ida')
  data_volta = self.cleaned_data.get('data_volta')
  data_pesquisa = self.cleaned_data.get('data_pesquisa')
  lista_erros = {}
  numeros_campo(origem, 'origem', lista_erros)
  numeros_campo(destino, 'destino', lista_erros)
  origem_destino_iguais(origem, destino, lista_erros)
  data_ida_data_volta(data_ida, data_volta)
  data_ida_data_pesquisa(data_ida, data_pesquisa)
  if lista_erros is not None:
    for error in lista_erros:
      mensagem_erro = lista_erros[error]
      self.add_error(error, mensagem_erro)
      