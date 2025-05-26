#cliente foi separado do pedido, que antes estava em um arquivo "models" tudo junto, "models" foi transformado em diretório

import datetime as dt

class Cliente:
    def __init__(self, nome_cliente, e_mail_cliente, vip=False):
        self.nome = nome_cliente
        self.email = e_mail_cliente
        self.vip = vip
        self.CadastradoEm = dt.datetime.now().strftime("%d/%m/%Y")