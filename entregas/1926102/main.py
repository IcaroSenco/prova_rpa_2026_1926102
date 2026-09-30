# Importa as 3 funções do módulo mod_estoque
from mod_estoque import (
    cadastrar_item,
    calcular_valor_estoque,
    listar_itens_em_falta,
)


def main():
    # 1. Cadastra pelo menos 3 itens usando cadastrar_item
    item1 = cadastrar_item("Resistor 10k", quantidade=50, preco_unitario=0.15)
    item2 = cadastrar_item("Placa Arduino", quantidade=2, preco_unitario=45.00)
    item3 = cadastrar_item("Sensor Ultrassônico", quantidade=4, preco_unitario=12.50)

    # Junta os itens em uma lista
    estoque = [item1, item2, item3]

    # 2. Exibe o valor total do estoque
    valor_total = calcular_valor_estoque(estoque)
    print(f"Valor total do estoque imobilizado: R$ {valor_total:.2f}")

    # 3. Exibe a lista de itens em falta (escolhendo um valor para 'minimo', ex: 5)
    limite_minimo = 5
    itens_em_falta = listar_itens_em_falta(estoque, minimo=limite_minimo)

    print(f"\nItens em falta (quantidade abaixo de {limite_minimo}):")
    for item in itens_em_falta:
        print(f"- {item['nome']}: {item['quantidade']} unidades (Preço unitário: R$ {item['preco_unitario']:.2f})")


if __name__ == "__main__":
    main()