from RefatoracaoDetetive.app.logica_sistema import novo_cliente, criar_pedido, listar_pedidos_json, concluir_todos

#alterado a abreviação c1 para cadastro1, para melhor identificação do que seria a função da variável
cadastro1 = novo_cliente("Ana", "ana@mail", vip=True)
#alterado a abreviação c2 para cadastro2, para melhor identificação do que seria a função da variável
cadastro2 = novo_cliente("Bruno", "bruno@mail")

itens1 = [{"nome": "Pizza", "preco": 50, "qtd": 2}]
#adicionado ("qtd":1) no itens2 para que funcionasse no calculo total, visto que no calculo total tem um multiplicador de quantidade.
itens2 = [{"nome": "Refri", "preco": 7, "qtd": 1}]

#alterado a abreviação
pedido1 = criar_pedido(cadastro1, itens1)
pedido2 = criar_pedido(cadastro2, itens2)

#alterado a abreviação
pedido1.resumo()
pedido2.resumo()

print("\n== JSON Atual ==")
print(listar_pedidos_json())

concluir_todos()

print("\n== Depois de concluir todos ==")
print(listar_pedidos_json())