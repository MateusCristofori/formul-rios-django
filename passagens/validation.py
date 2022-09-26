def origem_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
      lista_erros['destino'] = 'Origem e destino não podem ser iguais.'
    
def numeros_campo(nome_campo, valor_campo, lista_erros):
   if any(char.isdigit() for char in valor_campo):
      lista_erros[nome_campo] = 'Não inclua números nesse campo.'

def data_ida_data_volta(data_ida, data_volta, lista_erros):
   if data_ida > data_volta:
      lista_erros['data_volta'] = 'A data de volta não pode ser menor que a data de ida.'
   
def data_ida_data_pesquisa(data_ida, data_pesquisa, lista_erros):
   if data_ida < data_pesquisa:
      lista_erros['data_ida'] = "A data de ida não pode ser menor que a data atual!"