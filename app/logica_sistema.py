from models import Pedido, cliente
import random, json

pedidos = []




def novo_cliente(nome, email, vip=False, data_do_cadastro=None):
        return cliente(nome, email, vip, data_do_cadastro)

def listar_pedidos_json():
    lista = []
    for p in pedidos:
        lista.append({
            "id": p._id,
            "cliente": p.cliente.nome,
            "total": p.total,
            "vip": p.cliente.vip,
            "status": p.status
        })
    return json.dumps(lista, indent=2, ensure_ascii=False)

def concluir_todos():
    for p in pedidos:
        if p.status != "concluido ":
            p.status = "concluido"

#Removido a função de remover os pedidos, visto que os que já estão concluídos, não precisam sair do sistema.

def criar_pedido(c: cliente, itens):
    # gerar o numero do pedido, sem repetir o numero
    pedido_id = random.randint(1, 9999)
    p = Pedido(pedido_id, cliente, pedidos)
    pedidos.append(p)
    return p