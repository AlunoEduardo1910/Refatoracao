import datetime as dt

ALLOWED_STATUS = ["Novo", "em  andamento", "concluido", "cancelado"]

class cliente:
    def __init__(self, n, e_mail, vip=False):
        self.nome = n
        self.email = e_mail
        self.vip = vip
        self.CadastradoEm = dt.datetime.now().strftime("%d/%m/%Y")

# A classe pedido deve ser separada em outro arquivo.
# Os arquivos deve estar dentro do diretorio models

class Pedido:
    def calc_total(self):
        for i in self.itens:
            self.total += i["preco"] * i["qtd"]
        if self.cliente.vip:
            self.total = self.total * 0.9

    def resumo(self):
        print("=== PEDIDO", self._id, "===")
        print("Cliente:", self.cliente.nome, "| VIP?", self.cliente.vip)
        print("Status:", self.status)
        print("Itens:", self.itens)
        print("TOTAL: R$", self.total)

    def mudar_status(self, s):
        self.status = s