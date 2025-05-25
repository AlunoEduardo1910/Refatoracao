from app.logica_sistema import novo_cliente, criar_pedido, MENU, PEDIDOS, PEDIDOS_ITENS, listar_pedidos_json
from models.cliente import Cliente
from models.pedidos import Pedido

#nome das variaveis estão muito simples, dificultando a identificação da função como um todo.
#Criado um dicionário global com os itens disponíveis no cardápio ao invés de um prompt já pré feito com apenas 2 combinações de itens


comando = ""
cardapio = ""
while comando != "6":
    comando = input(f"Escolha uma opção: \n"
                    f"1) Novo cliente\n"
                    f"2) Criar pedido \n"
                    f"3) Listar pedido \n"
                    f"4) Excluir Pedido \n"
                    f"5) Sair \n")

    match comando:
        case "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            vip = input("É VIP? (s/n): ")

            print(novo_cliente(nome, email, vip))

        case "2":
            print(MENU)
            while True:
                itens = input("Selecione os itens que farão parte do pedido:  \n"
                              "Ou 'Sair'\n")

                if itens in MENU:
                    PEDIDOS_ITENS.append(itens)
                elif itens == "Sair":
                    PEDIDOS[Pedido.id]=PEDIDOS_ITENS.copy()
                    print(PEDIDOS)
                    break
                else:
                    print("Item não cadastrado no menu")
                print(PEDIDOS_ITENS)

        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saindo do sistema... Até logo!")
            break
        case _:
            print("Opção inválida! Tente novamente.")


print("\n== JSON Atual ==")
print(listar_pedidos_json())


print("\n== Depois de concluir todos ==")
print(listar_pedidos_json())