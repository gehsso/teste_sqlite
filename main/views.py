from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    # Cria e salva um novo cliente
    cliente = Cliente(nome='TESTE')
    cliente.save()

    # Busca todos os clientes do banco de dados
    clientes = Cliente.objects.all()

    # Cria uma string com os nomes dos clientes
    clientes_nomes = '<br>'.join([cliente.nome for cliente in clientes])

    # Retorna a resposta com a lista de clientes
    return HttpResponse(f'Página index Main. Clientes: {clientes_nomes}')