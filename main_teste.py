from app.logica_sistema import novo_cliente, criar_pedido, listar_pedidos_json, excluir_pedido, MENU
#importa funções principais e o MENU do sistema centralizado em logica_sistema.py


while True:
    comando = input("""
    Escolha uma opção:
    1) Novo cliente
    2) Criar pedido
    3) Listar pedidos
    4) Excluir pedido
    5) Sair
    """)
    #laço principal do sistema que apresenta o menu interativo ao usuário

    match comando:
        case "1":
            nome = input("Nome: ")
            email = input("Email: ")
            vip = input("É VIP? (s/n): ").lower() == 's'
            cliente = novo_cliente(nome, email, vip)
            print(f"Cliente cadastrado: {cliente.mostrar_dados()}")
            #criação de um novo cliente, com verificação se é VIP e exibição dos dados com método da classe

        case "2":
            email = input("Digite o email do cliente: ")
            print("Menu disponível:")
            for nome, preco in MENU.items():
                print(f"- {nome}: R$ {preco}")

            itens = []
            while True:
                item = input("Adicionar item (ou 'sair'): ")
                if item.lower() == "sair":
                    break
                elif item in MENU:
                    itens.append(item)
                else:
                    print("Item não encontrado no menu.")

            pedido = criar_pedido(email, itens)
            if pedido:
                print("Pedido criado com sucesso!")
                pedido.resumo()
            else:
                print("Cliente não encontrado.")
            #criação de pedido com seleção dinâmica de itens do menu e associação ao cliente via email

        case "3":
            print("\nPedidos atuais:")
            print(listar_pedidos_json())
            #exibe todos os pedidos existentes em formato JSON formatado

        case "4":
            pedido_id = input("Digite o ID do pedido a excluir: ")
            if excluir_pedido(pedido_id):
                print("Pedido excluído com sucesso.")
            else:
                print("Pedido não encontrado.")
            #exclusão de pedido com busca pelo ID e confirmação de sucesso ou falha

        case "5":
            print("Saindo do sistema. Até logo!")
            break
            #encerra o loop e finaliza o sistema

        case _:
            print("Opção inválida. Tente novamente.")
            #trata entradas inválidas no menu principal
