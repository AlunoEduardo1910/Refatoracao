import datetime

class Cliente:
    def __init__(self, nome, email, vip=False):
        self.nome = nome
        self.email = email
        self.vip = vip
        self.data_do_cadastro = datetime.timezone.now().strftime("%d/%m/%Y")


# A classe pedido deve ser separada em outro arquivo.
# Os arquivos deve estar dentro do diretorio models
# a classe cliente está sem comportamento
# Nome dos atributos mais claros
#retirado a função de cadastrar clientes do cliente
