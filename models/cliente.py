from datetime import datetime

class Cliente:
    def __init__(self, nome, email, vip=False):
        self.nome = nome
        self.email = email
        self.vip = vip
        self.data_do_cadastro = datetime.now().strftime("%d/%m/%Y")

    def mostrar_dados(self):
        return f"{self.nome} ({'VIP' if self.vip else 'Comum'})"

# A classe pedido deve ser separada em outro arquivo.
# Os arquivos devem estar dentro do diretório models
# a classe cliente está sem comportamento, adicionado o comportamento mostrar dados para o cliente, para verificar se ele é vip ou não.
# Nome dos atributos mais claros
#retirado a função de cadastrar clientes do cliente
