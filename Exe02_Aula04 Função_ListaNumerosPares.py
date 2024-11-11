def ListaNumerosPares(Lista:list):
 lista_qualquer = []
 while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
      break
    lista_qualquer.append(numero)
    print(f'Lista Geral: {lista_qualquer}')
    if numero % 2 == 0:
      Lista.append(numero)
      print(f'Lista Pares: {Lista}')
      
Lista = []  
ListaNumerosPares(Lista)