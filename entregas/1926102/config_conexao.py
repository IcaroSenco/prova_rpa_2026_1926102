def main():
    ENDPOINT_URL = "http://api.exemplo.com"
    PORTA = 8080
    TAXA_AMOSTRAGEM = 1.5
    USA_HTTPS = True

    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS,
    }

    print("=== RELATÓRIO DE VALIDAÇÃO ===")
    for chave, valor in parametros.items():
        print(f"{chave}: {valor} | Tipo: {type(valor)}")


if __name__ == "__main__":
    main()