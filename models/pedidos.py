

STATUS_PERMITIDOS = {1 : "Novo", 2 : "em  andamento",3 : "concluido",4 : "cancelado"}

class Pedido:
    ultimo_id = 0

    def __init__(self,cliente,itens,total):
        Pedido.ultimo_id += 1
        self.id = str(Pedido.ultimo_id)
        self.cliente = cliente
        self.itens = itens
        self.total = total
        self.status = STATUS_PERMITIDOS[1] #Como é um novo pedido



    def calculo_total(self):
        for i in self.itens:
            self.total += i["preco"] * i["qtd"]
        if self.cliente.vip:
            self.total = self.total * 0.9

    def resumo(self):
        print("=== PEDIDO", self.id, "===")
        print(f"Cliente: {self.cliente.nome}\n"
              f"VIP: {self.cliente.vip}")
        print(f"Status: {self.status}")
        print("Itens:", self.itens)
        print("TOTAL: R$", self.total)

    def mudar_status(self, novo_status):
        if novo_status in STATUS_PERMITIDOS.values():
            self.status = novo_status

# A classe pedido não tem atributos, foi adicionado os atributos que sejam coerentes com a classe pedido