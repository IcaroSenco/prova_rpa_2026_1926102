# Lista de leituras fornecida pela questão
leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar_sensores(leituras_sensor: list) -> None:
    soma_validas = 0.0
    qtd_validas = 0

    for leitura in leituras_sensor:
        # 1. Leitura fora da faixa (> 80.0) -> ignora com continue
        if leitura > 80.0:
            print(f"[DESCARTE] Leitura de {leitura}°C fora da faixa: ignorada.")
            continue

        # 2. Sensor corrompido (-999.0) -> interrompe com break
        if leitura == -999.0:
            print(f"[FALHA] Sensor corrompido ({leitura}). Interrompendo monitoramento...")
            break

        # 3. Leitura válida -> exibe e acumula
        print(f"[OK] Leitura de {leitura}°C registrada.")
        soma_validas += leitura
        qtd_validas += 1

    # 4. Cálculo da média evitando divisão por zero
    if qtd_validas > 0:
        media = soma_validas / qtd_validas
        print(f"\nTotal de leituras válidas: {qtd_validas}")
        print(f"Média das leituras válidas: {media:.2f}°C")
    else:
        print("\nNenhuma leitura válida foi registrada.")


if __name__ == "__main__":
    monitorar_sensores(leituras)