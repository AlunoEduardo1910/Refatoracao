from models.cliente import Cliente
from models.pedidos import Pedido
import json

# ESTRUTURA GLOBAL DE DADOS
CLIENTES = {}  # Armazena os clientes por email como chave
PEDIDOS = []   # Lista global de pedidos

# CARDÁPIO PADRÃO
MENU = {
    "Pizza Salgada": 50,
    "Pizza Doce": 30,
    "Refri": 7,
    "Água": 5
}

def novo_cliente(nome, email, vip=False):
    # Cria um novo cliente e o armazena no dicionário usando o email como chave
    cliente = Cliente(nome, email, vip)
    CLIENTES[email] = cliente
    return cliente

def buscar_cliente(email):
    # Retorna o cliente pelo email (ou None se não existir)
    return CLIENTES.get(email)

def criar_pedido(email, nomes_itens):
    # Busca o cliente antes de criar o pedido
    cliente = buscar_cliente(email)
    if not cliente:
        return None  # Cliente inexistente, pedido não é criado

    # Criação dos itens a partir do menu
    itens = []
    for nome in nomes_itens:
        if nome in MENU:
            itens.append({"nome": nome, "preco": MENU[nome], "qtd": 1})

    # Cria o pedido, adiciona à lista global e o retorna
    pedido = Pedido(cliente, itens)
    PEDIDOS.append(pedido)
    return pedido

def listar_pedidos_json():
    # Constrói uma lista de dicionários com informações dos pedidos
    lista = []
    for p in PEDIDOS:
        lista.append({
            "id": p.id,
            "cliente": p.cliente.nome,
            "total": p.total,
            "vip": p.cliente.vip,
            "status": p.status
        })
    return json.dumps(lista, indent=2, ensure_ascii=False)

def excluir_pedido(pedido_id):
    # Procura e remove um pedido pelo ID
    for p in PEDIDOS:
        if p.id == pedido_id:
            PEDIDOS.remove(p)
            return True
    return False

# MELHORIAS GERAIS:
# - Uso de estruturas globais CLIENTES e PEDIDOS para manter os dados disponíveis entre chamadas.
# - Validação de cliente antes da criação de pedidos.
# - Conversão automática dos dados dos pedidos para JSON.
# - Separação clara das responsabilidades em funções.
