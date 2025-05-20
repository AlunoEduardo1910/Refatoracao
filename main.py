

#nome das variaveis estão muito simples

c1 = cliente.novo_cliente("Ana", "ana@mail", vip=True)
c2 = novo_cliente("Bruno", "bruno@mail")

itens1 = [{"nome": "Pizza", "preco": 50, "qtd": 2}]
itens2 = [{"nome": "Refri", "preco": 7}]

p1 = criar_pedidos(c1, itens1)
p2 = criar_pedidos(c2, itens2)

p1.resumo()
p3.resumo()

print("\n== JSON Atual ==")
print(listar_pedidos_json())

concluir_todos()

print("\n== Depois de concluir todos ==")
print(listar_pedidos_json())