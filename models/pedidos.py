

STATUS_PERMITIDOS = {1 : "Novo", 2 : "em  andamento",3 : "concluído", 4 : "cancelado"}

class Pedido:
    id = 0

    def __init__(self,cliente,itens):   #removido o total, visto que não é lógico eu ter que fornecer o valor total e posteriormente ter uma função para calcular
        Pedido.id += 1
        self.id = str(Pedido.id)
        self.cliente = cliente
        self.itens = itens
        self.total = 0
        self.status = STATUS_PERMITIDOS[1] #Como é um novo pedido
        self.calculo_total() #a princípio, quando o objeto for criado, já irá ser feito o cálculo automaticamente do valor total



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