from datetime import datetime

class Cliente:
    _id_counter = 0  # Atributo de classe para gerar IDs únicos automaticamente

    def __init__(self, nome, email, vip=False):
        # MELHORIA: ID agora é atribuído automaticamente ao cliente
        Cliente._id_counter += 1
        self.id = Cliente._id_counter

        self.nome = nome
        self.email = email
        self.vip = vip  # Booleano para indicar se é cliente VIP
        self.data_do_cadastro = datetime.now().strftime("%d/%m/%Y")  # Data atual formatada

    def mostrar_dados(self):
        # Retorna uma string formatada com nome e tipo do cliente
        return f"{self.nome} ({'VIP' if self.vip else 'Comum'})"

# MELHORIA GERAL:
# - O ID do cliente agora é único e automático.
# - Adicionado o atributo data_do_cadastro para registrar o momento do cadastro.
# - Método mostrar_dados melhora a legibilidade do status VIP do cliente.