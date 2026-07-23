# Teste Técnico – Analista de Gestão de Dados de Pesquisa Pleno

## Como executar o pipeline

1. Instale as dependências:

   `pip install pandas numpy openpyxl pyarrow`

2. Os arquivos CSV originais estão na pasta `02_Base_Original/`. 
O notebook `EDA.ipynb` já está configurado para carregá-los automaticamente a partir dessa pasta.

3. Abra o arquivo `EDA.ipynb` no **Jupyter Notebook**, **VS Code** ou **Google Colab** e execute as células **em ordem sequencial** (de cima para baixo):

   | Célula | Etapa | Descrição |
   | :--- | :--- | :--- |
   | **1** | Carregamento | Leitura das 4 bases a partir da pasta `02_Base_Original/` |
   | **2** | Validação estrutural | Verificação de colunas obrigatórias conforme Dicionário de Dados v2.4 |
   | **3a** | Diagnóstico de qualidade | Identificação de todos os problemas com descrição, impacto e sugestão de ação |
   | **3b** | Decisões e ações | Priorização (Crítico/Alto/Médio/Baixo) e plano de ação com responsáveis |
   | **4** | Tratamento e padronização | Correção automática de campos, marcação de qualidade e padronização |
   | **5** | Exportação final | Geração de CSVs, Excel, Parquet e estatísticas detalhadas |
   | **6** | (Opcional) Renomeação | Correção de nomenclatura de arquivos conforme POP (requer ajuste do caminho da pasta de arquivos) |

> ⚠️ **Atenção:** a **Célula 6** (renomeação de arquivos) exige que você edite a variável `PASTA_RAIZ_ARQUIVOS` dentro do notebook, apontando para o local correto onde os arquivos de campo (termos, fotos e diários) estão armazenados. Recomenda-se executar primeiro em **modo simulação** para verificar as alterações propostas.

## Resultados esperados

- Diagnóstico completo em JSON (`diagnostico_qualidade_*.json`)
- Plano de ação com prioridades (`plano_acao_*.md` e `decisoes_acoes_*.json`)
- Bases tratadas em **CSV**, **Excel** e **Parquet** (pasta `output_tratado/`)
- Estatísticas detalhadas por coluna (pasta `estatisticas/`)
- Relatório de renomeação de arquivos (caso execute a Célula 6)
