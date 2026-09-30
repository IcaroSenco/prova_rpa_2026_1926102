# Ficha de Avaliação de Viabilidade de Processo para RPA

## 1. Identificação do Processo
* **Nome do Processo:** Renomeação e Arquivamento Diário de Comprovantes em PDF
* **Cenário Escolhido:** Cenário A
* **Descrição Resumida:** Processo operacional responsável por identificar comprovantes em formato PDF em uma pasta de entrada, extrair a data e o número do documento a partir do nome original do arquivo, renomeá-los seguindo uma regra padronizada e movê-los para a pasta de arquivo final.

---

## 2. Volume e Frequência Estimados
* **Frequência:** Diária (executado ao final do expediente ou em intervalos fixos ao longo do dia).
* **Volume Estimado:** De dezenas a centenas de arquivos PDF por dia.

---

## 3. Estruturação das Entradas
* **As entradas são estruturadas?** **Sim.**
* **Justificativa:** Todos os arquivos de entrada são do mesmo formato (`.pdf`) e os nomes dos arquivos contêm de forma padronizada as informações necessárias (data e número do documento), permitindo extração direta sem ambiguidade.

---

## 4. Regras de Negócio
* **As regras são claras e determinísticas?** **Sim.**
* **Justificativa:** O processo segue uma lógica estritamente baseada em regras condicionais padronizadas e sem subjetividade (ex.: extrair caracteres das posições X a Y, formatar como `AAAA-MM-DD_NUMERO.pdf` e mover para o diretório `/Arquivados`). Não há necessidade de tomada de decisão baseada em julgamento humano.

---

## 5. Veredito Final
* **Elegível para RPA?** **Sim (Altamente Viável).**
* **Justificativa do Veredito:**
  O processo atende a todos os três pilares fundamentais para automação com RPA:
  1. **Dados Estruturados:** Trabalha com arquivos em formato padrão e nomenclatura previsível.
  2. **Regras Determinísticas:** A lógica de renomeação e movimentação é 100% baseada em regras lógicas fixas, sem necessidade de interpretação subjetiva.
  3. **Repetibilidade e Alto Volume:** É uma tarefa rotineira, executada diariamente, com volume considerável, sendo ideal para eliminar trabalho manual repetitivo e reduzir erros de digitação.