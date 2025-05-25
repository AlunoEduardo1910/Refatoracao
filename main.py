from app.logica_sistema import novo_cliente, criar_pedido, listar_pedidos_json, excluir_pedido, MENU
from models.pedidos import STATUS_PERMITIDOS, Pedido
from app.logica_sistema import CLIENTES, PEDIDOS
#importa funções principais e o MENU do sistema centralizado em logica_sistema.py


while True:
    comando = input("""
    Escolha uma opção:
    1) Novo cliente
    2) Criar pedido
    3) Listar pedidos
    4) Mudar status do pedido
    5) Excluir pedido
    6) Excluir Cliente
    7) Sair
    """)
    #laço principal do sistema que apresenta o menu interativo ao usuário

    match comando:
        case "1":
            nome = input("Nome: ")
            email = input("Email: ")
            vip = input("É VIP? (s/n): ").lower() == 's'
            cliente = novo_cliente(nome, email, vip)
            print(f"Cliente cadastrado: {cliente.mostrar_dados()}")
            #criação de um novo cliente, com verificação se é VIP e exibição dos dados

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
            pedido_id = input("Digite o ID do pedido a atualizar: ")
            from app.logica_sistema import buscar_pedido_por_id

            pedido = buscar_pedido_por_id(pedido_id)  # Busca segura do pedido por ID

            if pedido:
                for codigo, status in STATUS_PERMITIDOS.items():
                    print(f"- {codigo}: {status}")
                # exibe os códigos e descrições de status permitidos

                try:
                    novo_codigo = int(input("Selecione o novo status do pedido (número): "))
                    novo_status = STATUS_PERMITIDOS[novo_codigo]

                    pedido.mudar_status(novo_status)
                    print(f"O novo status do pedido é: {novo_status}")
                    # atualiza o status e mostra o novo valor
                except (ValueError, KeyError):
                    print("Código de status inválido.")
                    # trata erro se o valor informado não estiver entre os permitidos
            else:
                print("Pedido não encontrado.")
                # exibe mensagem caso o ID não esteja no banco de pedidos

        case "5":
            pedido_id = input("Digite o ID do pedido a excluir: ")
            if excluir_pedido(pedido_id):
                print("Pedido excluído com sucesso.")
            else:
                print("Pedido não encontrado.")
            #exclusão de pedido com busca pelo ID e confirmação de sucesso ou falha

        case "6":
            for email_cliente, cliente in CLIENTES.items():
                print(f"- {email_cliente}: {cliente.nome}")
            email = input("Digite o email do cliente a excluir: ")
            if email in CLIENTES:
                # Remove pedidos do cliente
                PEDIDOS[:] = [p for p in PEDIDOS if p.cliente.email != email]
                del CLIENTES[email]
                print("Cliente e seus pedidos foram removidos.")
            else:
                print("Cliente não encontrado.")
            # exclui cliente e todos os pedidos associados

        case "7":
            print("Saindo do sistema. Até logo!")
            break
            #encerra o loop e finaliza o sistema

        case _:
            print("Opção inválida. Tente novamente.")
            #trata entradas inválidas no menu principal
