import logging
import pandas as pd

formato = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("1926102", encoding="utf-8")
file_handler.setFormatter(formato)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def importar_notas(caminho: str) -> float:
    """Lê o arquivo CSV com pandas, registra logs das notas e do total,

    e retorna a soma dos valores da coluna 'valor'.
    """
    try:
        
        df = pd.read_csv(caminho, encoding="utf-8")

        
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

        if df.empty or df["valor"].isnull().all():
            raise pd.errors.EmptyDataError("O arquivo CSV está vazio ou sem dados válidos.")

        
        for _, linha in df.iterrows():
            logging.info(
                f"Nota lida: {int(linha['nota'])} | "
                f"Cliente: {linha['cliente']} | "
                f"Valor: R$ {linha['valor']:.2f}"
            )

        
        total_faturado = float(df["valor"].sum())
        logging.info(f"Importação concluída. Total faturado: R$ {total_faturado:.2f}")

        return total_faturado

    except FileNotFoundError:
        logging.error(f"Erro ao importar: Arquivo não encontrado no caminho '{caminho}'.")
        return 0.0

    except pd.errors.EmptyDataError:
        logging.error(f"Erro ao importar: O arquivo CSV em '{caminho}' está vazio.")
        return 0.0

    finally:
        logging.info(f"Processamento/Tentativa de importação para '{caminho}' finalizada.")

if __name__ == "__main__":
    print("--- Teste 1: Importando 'notas.csv' ---")
    total1 = importar_notas("notas.csv")
    print(f"Resultado retornado: {total1}\n")

    print("--- Teste 2: Importando caminho inexistente ---")
    total2 = importar_notas("caminho_invalido.csv")
    print(f"Resultado retornado: {total2}\n")