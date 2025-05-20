from models.cliente import Cliente
from models.pedidos import Pedido
import json


pedidos = []



def novo_cliente(nome, email, vip=False): #retirado a data como parâmetro, tendo em vista que ela é gerada automaticamente dentro da classe
        return Cliente(nome, email, vip)

def criar_pedido(c: Cliente, itens):
    pedido = Pedido(c, itens)
    pedidos.append(pedido)
    return pedido
#alterado p para pedido, para melhor identificação
#O cliente após o c: estava com o c minúsculo, alterado para maiúsculo, visto que queremos puxar a classe.


def listar_pedidos_json():
    lista = []
    for p in pedidos:
        lista.append({
            "id": p.id,
            "cliente": p.cliente.nome,
            "total": p.total,
            "vip": p.cliente.vip,
            "status": p.status
        })
    return json.dumps(lista, indent=2, ensure_ascii=False)

def excluir_pedido(id):
    for pedido in pedidos:
        if pedido.id == id:
            pedidos.remove(pedido)
            return f"Pedido {id} removido com sucesso."
    return f"Pedido com ID {id} não encontrado."

#Não via a necessidade de concluir todos os pedidos, pois os que não estivessem concluídos eram para estar cancelados
#Então preferimos por adotar a exclusão de pedido, em caso de ter sido feito um pedido errado.


