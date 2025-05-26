#igual cliente, pedido foi retirado do arquivo "models" que virou um diretório
ALLOWED_STATUS = ["Novo", "em  andamento", "concluído", "cancelado"]

#adicionado uma inicialização para a classe Pedido
class Pedido:
    def __init__(self, id_pedido, cliente, itens):
        self.id = id_pedido
        self.cliente = cliente
        self.itens = itens
        self.status = "Novo"
        self.total = 0
        self.calculo_total()


    def calculo_total(self):
        for i in self.itens:
            self.total += i["preco"] * i["qtd"]
        if self.cliente.vip:
            self.total = self.total * 0.9

    def resumo(self):
        print("=== PEDIDO", self.id, "===")
        print("Cliente:", self.cliente.nome, "| VIP?", self.cliente.vip)
        print("Status:", self.status)
        print("Itens:", self.itens)
        print("TOTAL: R$", self.total)

    def mudar_status(self, s):
        self.status = s