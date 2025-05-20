from models import cliente

STATUS_PERMITIDOS = {1 : "Novo", 2 : "em  andamento",3 : "concluido",4 : "cancelado"}
indice = 1 #indice para alterar o status futuramente

class Pedido:
    def __init__(self,id,itens,total):
        self.id = id
        self.itens = itens
        self.total = total
        self.status = STATUS_PERMITIDOS.get(indice)



    def calculo_total(self):
        for i in itens:
            self.total += i["preco"] * i["qtd"]
        if cliente.vip:
            self.total = self.total * 0.9

    def resumo(self):
        print("=== PEDIDO", self._id, "===")
        print(f"Cliente: {cliente.nome}\n"
              f"VIP: {cliente.vip}")
        print(f"Status: {pedido.status}")
        print("Itens:", self.itens)
        print("TOTAL: R$", self.total)

    def mudar_status(self, status):
        self.status = status
        indice += 1

# A classe pedido não tem atributos