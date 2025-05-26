#nome alterado de services para lógica sistema, para melhor identificação
from RefatoracaoDetetive.models.cliente import Cliente
from RefatoracaoDetetive.models.pedido import Pedido
import random, json


#variável global sinalizada com a substituição das letras por maiúsculas
PEDIDOS = []

def novo_cliente(nome, email, vip=False):
    return Cliente(nome, email, vip)
#após return, substituido cliente por Cliente, com a primeira letra maiúscula, visto que queremos chamar a classe.


#para melhor identificação, foi retirado a abreviação de c:, deixando apenas cliente
#pid foi substituido por id_pedido e p por pedido
def criar_pedido(cliente, itens):
    id_pedido = random.randint(1, 9999)
    pedido = Pedido(id_pedido, cliente, itens)
    PEDIDOS.append(pedido)
    return pedido

#substituido a abrevição p por pedido
def listar_pedidos_json():
    lista = []
    for pedido in PEDIDOS:
        lista.append({
            "id": pedido.id,
            "cliente": pedido.cliente.nome,
            "total": pedido.total,
            "vip": pedido.cliente.vip,
            "status": pedido.status
        })
    return json.dumps(lista, indent=2, ensure_ascii=False)

#substituido a abrevição p por pedido
#também foi removido a função que estaria removendo os pedidos após se tornarem concluídos, visto que, se temos a função de concluir, não faz sentido removê-lo logo após
def concluir_todos():
    for pedido in PEDIDOS:
        if pedido.status != "concluído":
            pedido.status = "concluído"
