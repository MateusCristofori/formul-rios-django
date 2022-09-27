from cProfile import label
from dataclasses import field, fields
from datetime import date, datetime
from email.policy import default
from pyexpat import model
from django import forms
from tempus_dominus.widgets import DatePicker
from .classe_viagem import tipos_de_classes
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForm(forms.ModelForm):
  data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
  class Meta:
    model = Passagem
    fields = '__all__'
    labels = {
      'data_ida': 'Data de ida',
      'data_volta': 'Data de volta',
      'informacoes': "Informações",
      'classe_viagem': 'Classe de voo'
    }
    widgets = {
      'data_ida': DatePicker(),
      'data_volta': DatePicker(),
    }


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
      
class PessoaForm(forms.ModelForm):
  class Meta:
    model = Pessoa
    exclude = ['nome']