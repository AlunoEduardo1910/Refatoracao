from models import Pedido, Cliente
import random, json

pedidos = []

def novo_cliente(nome, email, vip=False):
    return cliente(nome, email, vip)

def criar_pedido(c: cliente, itens):
    pid = random.randint(1, 9999)
    p = Pedido(pid, c, pedidos)
    pedidos.append(p)
    return p

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
            pedidos.remove(p)