from app.logica_sistema import novo_cliente, criar_pedido, listar_pedidos_json, concluir_todos
#nome das variaveis estão muito simples, dificultando a identificação da função como um todo.

comando = ""
while comando != "6":
    comando = input(f"Escolha uma opção: \n"
                    f"1) Novo cliente\n"
                    f"2) Criar pedido \n"
                    f"3) Listar pedido \n"
                    f"4)  \n"
                    f"5) Sair \n")



itens1 = [{"nome": "Pizza", "preco": 50, "qtd": 2}]
itens2 = [{"nome": "Refri", "preco": 7}]

p1 = criar_pedido(c1, itens1)
p2 = criar_pedido(c2, itens2)

p1.resumo()
p3.resumo()

print("\n== JSON Atual ==")
print(listar_pedidos_json())

concluir_todos()

print("\n== Depois de concluir todos ==")
print(listar_pedidos_json())