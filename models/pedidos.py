# STATUS_PERMITIDOS é um dicionário com os status possíveis para um pedido.
# A chave é um número inteiro para facilitar a seleção posterior.


STATUS_PERMITIDOS = {
    1: "Novo",
    2: "em andamento",
    3: "concluido",
    4: "cancelado"
}


class Pedido:
    _id_counter = 0  # Atributo de classe usado para gerar IDs únicos automaticamente

    def __init__(self, cliente, itens):
        # MELHORIA: ID agora é gerado automaticamente, não precisa ser passado na criação
        Pedido._id_counter += 1
        self.id = str(Pedido._id_counter)  # ID armazenado como string para facilitar comparação com input()

        self.cliente = cliente  # Cliente associado ao pedido
        self.itens = itens  # Lista de itens no pedido (dicionários com nome, preço, qtd)
        self.total = 0  # Total inicial do pedido
        self.status = STATUS_PERMITIDOS[1]  # Começa com o status "Novo"

        self.calculo_total()  # MELHORIA: total é calculado automaticamente na criação do pedido

    def calculo_total(self):
        # Função que soma o total de todos os itens do pedido
        for item in self.itens:
            self.total += item["preco"] * item["qtd"]

        if self.cliente.vip:
            # MELHORIA: Aplica 10% de desconto se o cliente for VIP
            self.total *= 0.9

    def resumo(self):
        # Exibe um resumo do pedido formatado no terminal
        print("=== PEDIDO", self.id, "===")
        print(f"Cliente: {self.cliente.nome}\nVIP: {self.cliente.vip}")
        print(f"Status: {self.status}")
        print("Itens:", self.itens)
        print("TOTAL: R$", self.total)

    def mudar_status(self, novo_status):
        # Permite mudar o status do pedido apenas se for um valor válido
        if novo_status in STATUS_PERMITIDOS.values():
            self.status = novo_status

# MELHORIA GERAL:
# - Removido o uso de ID manual para evitar repetição/confusão.
# - Status agora é padronizado com um dicionário, evitando erros de digitação.
# - A criação do pedido já realiza o cálculo do total.
# - Desconto VIP é aplicado automaticamente de forma clara.
