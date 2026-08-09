# Relatório Executivo 
# Diagnóstico e Tratamento de Dados

**Data de entrega:** [23/07/2023]  
**Versão:** 1.0  
**Responsável:** [Joyce Emília O. Mota]  
**Cargo:** Analista de Gestão de Dados de Pesquisa Pleno  

## 1. Resumo Executivo

Este relatório consolida os resultados do processo de diagnóstico, tratamento e padronização das bases de dados do projeto de diagnóstico socioambiental. Foram analisadas as bases de Survey, Cadastro, Equipe e Evidências totalizando **864 inconsistências** identificadas, das quais **11 foram classificadas como críticas** que precisam ser tratadas prioritariamente.

O pipeline desenvolvido garante:
- **Rastreabilidade:** cada registro mantém seu UUID e metadados de coleta.
- **Qualidade:** campos obrigatórios preenchidos, valores fora de domínio sinalizados.
- **Disponibilidade:** dados exportados em CSV, Excel e Parquet com as estatísticas detalhadas.
- **Conformidade com o POP - Critérios de Qualidade para Validação de Evidências:** uso da nomenclatura de arquivos padronizada.


## 2. Metodologia

O trabalho seguiu um pipeline estruturado em 7 etapas desenvolvido no ambiente EDA.ipynb com uma ação extra de renomeação:

| Etapa | Descrição | Script |
| :--- | :--- | :--- |
| 1. Carregamento | Leitura das 4 bases com detecção automática de encoding. | `Script_1_Configuração e Carregamento das Bases.ipynb` |
| 2. Validação estrutural | Verificação de colunas obrigatórias conforme Dicionário de Dados v2.4. | `Script_2_Validacao_Estrutura.ipynb` |
| 3. Diagnóstico de qualidade | Identificação de todos os problemas com descrição, impacto e sugestão de ação. | `Script_3a_Diagnostico_Qualidade.ipynb` |
| 4. Decisões e ações | Priorização (Crítico/Alto/Médio/Baixo) e plano de ação com responsáveis. | `Script_3b_Decisoes_Acoes.ipynb` |
| 5. Tratamento e padronização | Correção automática de campos, marcação de qualidade e padronização. | `Script_4_Tratamento_Padronizacao.ipynb` |
| 6. Exportação | Geração de CSVs, Excel, Parquet e estatísticas detalhadas. | `Script_5_Exportacao_Final` |
| 7. Renomeação EXTRA | Correção de nomenclatura de arquivos. | `Script_6_Renomeacao_Arquivos.ipynb` |

## Como executar o pipeline

1. Instale as dependências:
   `pip install pandas numpy openpyxl pyarrow`

2. Os arquivos CSV originais estão na pasta `02_Base_Original/`. O notebook `EDA.ipynb` já está configurado para carregá-los automaticamente a partir dessa pasta.

3. Abra o arquivo `EDA.ipynb` no **Jupyter Notebook**, **VS Code** ou **Google Colab** e execute as células **em ordem sequencial** (de cima para baixo):

   | Célula | Etapa | Descrição |
   | :--- | :--- | :--- |
   | **1** | Carregamento | Leitura das 4 bases a partir da pasta `02_Base_Original/` |
   | **2** | Validação estrutural | Verificação de colunas obrigatórias conforme Dicionário de Dados v2.4 |
   | **3a** | Diagnóstico de qualidade | Identificação de todos os problemas com descrição, impacto e sugestão de ação |
   | **3b** | Decisões e ações | Priorização (Crítico/Alto/Médio/Baixo) e plano de ação com responsáveis |
   | **4** | Tratamento e padronização | Correção automática de campos, marcação de qualidade e padronização |
   | **5** | Exportação final | Geração de CSVs, Excel, Parquet e estatísticas detalhadas |
   | **6** | Renomeação [Extra] | Correção de nomenclatura dos arquivos conforme POP que requer ajuste do caminho real da pasta de arquivos |

 ⚠️ **Atenção:** a **Célula 6** (renomeação de arquivos) exige que você edite a variável `PASTA_RAIZ_ARQUIVOS` dentro do notebook, apontando para o local correto onde os arquivos de campo (termos, fotos e diários) estão armazenados. Recomenda-se executar primeiro em **modo simulação** para verificar as alterações propostas.

## Resultados esperados

- Diagnóstico completo em JSON (`diagnostico_qualidade_*.json`)
- Plano de ação com prioridades (`plano_acao_*.md` e `decisoes_acoes_*.json`)
- Bases tratadas em **CSV**, **Excel** e **Parquet** (pasta `output_tratado/`)
- Estatísticas detalhadas por coluna (pasta `estatisticas/`)
- Relatório de renomeação de arquivos (caso execute a Célula 6)

## 3. Principais Achados do Diagnóstico
### 3.1. Distribuição dos Problemas por Tipo de Base

| Base | Nome Original da Base | Problemas Identificados | % do Total |
| :--- | :---: | :---: | :---: |
| 1. Base de Evidências | 05_Controle_Evidencias | 791 | 91,6% |
| 2. Base de Survey | 01_Base_Principal_Survey_v2_4 | 47 | 5,4% |
| 3. Base de Cadastro | 03_Cadastro_Mestre_Municipios_Comunidades | 26 | 3,0% |
| **Total** | - | **864** | **100%** |

Obs: Não foram encontradas insconsistencias na Base de Equipe 04_Controle_Equipe_Campo e as orientações cabivéis foram explicitadas em 6. Recomendações para a Equipe.  

### 3.2. Distribuição por Tipo de Problema

| Tipo | Ocorrências | Prioridade | Nome da Base |
| :--- | :---: | :---: | :---: |
| 1. Uso de Nomenclatura incorreta | 743 | Médio | Base de Evidências|
| 2. Pesquisador(a) não encontrado | 43 | Alto | Base de Evidências|
| 3. Pesquisador(a) não encontrado | 40 | Alto | Base de Survey|
| 4. Status inválido | 18 | Baixo | Base de Cadastro|
| 5. Código IBGE duplicado | 8 | Baixo | Base de Cadastro|
| 6. Idade inválida | 3 | Crítico | Base de Survey|
| 7. UUID duplicado | 3 | Crítico | Base de Survey|
| 8. Ausência do Diário de campo | 3 | Crítico | Base de Evidências|
| 9. Campo obrigatório nulo | 1 | Alto | Base de Survey|
| 10. Foto da entrevista ausente | 1 | Alto | Base de Evidências|
| 11. Data inconsistente entre Upload e Coleta | 1 | Crítico | Base de Evidências|

### 3.3. Destaques Críticos para Ação Imediata:

- **Idades inválidas:** registros de idade com -4, 15 e 132 – requerem a verificação com os(as) pesquisadores(as), uso da média artimética ou o descarte.
- **UUIDs duplicados:** 3 UUIDs aparecem em 2 registros cada – requerem a verificação com os(as) pesquisadores(as)por impossibilitar a rastreabilidade única.
- **Diário de campo faltando:** 3 entrevistas sem diário – requerem a verificação com os(as) pesquisadores(as) por violar o POP por ser uma evidência obrigatória.
- **Data inconsistente:** upload (30/03/2026) anterior à coleta (25/04/2026) – requerem a verificação com os(as) pesquisadores(as) por ser um possível erro de registro da data.

## 4. Plano de Ação Consolidado
### 4.1. Priorização e Responsáveis

| Prioridade | Problemas | Responsável | Prazo |
| :--- | :--- | :--- | :--- |
| **Crítico** (10) | Idade inválida, UUID duplicado, TC/Diário faltando, Data inconsistente | Supervisor do pesquisador / Analista de Dados | Imediato |
| **Alto** (42) | Pesquisador não encontrado, campos nulos e sem foto | Coordenação de Campo / Analista | Até 3 dias |
| **Médio** (743) | Nomenclatura incorreta de arquivos | Analista de Dados (Executar o Script 6) | Até 2 dias |
| **Baixo** (26) | Status inválido, IBGE duplicado, situação da equipe | Coordenação | Até 5 dias |

### 4.2. Ações Automáticas vs. Manuais

| Ação | Automática | Manual |
| :--- | :---: | :---: |
| Padronização de municípios/comunidades | ✅ | |
| Correção de gênero (M/F) | ✅ | |
| Remoção de duplicatas (ID/UUID) | (marcação) | ⚠️ (revisão) |
| Preenchimento de campos nulos | (parcial) | ⚠️ (complementar) |
| Renomeação de arquivos | ✅ (Executar o Script 6) | |
| Validação de pesquisadores | | ✅ (cadastro na equipe) |
| Correção de idades | | ✅ (consulta ao respondente) |


## 5. Qualidade dos Dados comparativo de Antes e Depois do Tratamento

| Indicador | Antes do Tratamento | Depois do Tratamento |
| :--- | :--- | :--- |
| Campos obrigatórios nulos | 1 (Comunidade) | 0 (preenchido via Cadastro) |
| Idades inválidas | 3 (−4, 15, 132) | Identificados e marcados para revisão |
| UUIDs/IDs duplicados | 6 registros afetados | Identificados e marcados para revisão |
| Nomenclatura incorreta | 743 arquivos | Corrigida automaticamente (Script 6) |
| Formato de saída | CSV único | CSV + Excel + Parquet + Estatísticas |
| Rastreabilidade | Parcial | Total (UUID + metadados) |

## 6. Recomendações para a Equipe

1. **Governança de dados:** Adotar o campo `Qualidade_Registro` como filtro para análises. Registrar um “OK” apenas quando todos os problemas forem resolvidos.
2. **Cadastro de equipe:** Atualizar a base `04_Controle_Equipe_Campo` com todos os colaboradores ativos (incluir “Rafaela” e identificar quem é o “Fulano” para inserir seu nome corretamente).
3. **Monitoramento contínuo:** Executar o `Script_3a_Diagnostico_Qualidade` diariamente durante a coleta para detectar problemas precocemente.
4. **Armazenamento:** Utilizar os arquivos **Parquet** (compactos e rápidos) para análises futuras.
5. **Padrão POP:** Manter a nomenclatura de arquivos conforme Seção 4 do POP (TC.#####.pdf, IMG.#####.jpg, DC.#####.pdf).
O Script 6 corrige os atuais após a execução, mas aos novos arquivos devem seguir o padrão ao alimentar a tabela.

## 7. Conclusão

O pipeline implementado entrega um conjunto de dados consolidado, rastreável e documentado estando pronto para uso em análises do diagnóstico socioambiental. Todas as etapas, da identificação de problemas até a exportação final, foram automatizadas o que garantindo a reprodutibilidade, confiabilidade e escalabilidade para futuras rodadas de coleta.

Recomenda-se a correção imediata dos 10 problemas críticos e a atualização da Base de Cadastro de Equipe para que a base atinja 100% de conformidade. Os arquivos finais estão disponíveis no diretório `03_Resultados_Processados/Dados_Tratados/`.

## 8. Anexos

- **Diagnóstico completo:** `diagnostico_qualidade_YYYYMMDD_HHMMSS.json`
- **Plano de ação:** `plano_acao_YYYYMMDD_HHMMSS.md`
- **Bases tratadas:** CSV, Excel e Parquet (pasta `output_tratado/`)
- **Relatório de renomeação:** `relatorio_renomeacao_YYYYMMDD_HHMMSS.csv`
- **Estatísticas por coluna:** `estatisticas/` (JSON e TXT)

**Elaborado por:** [Joyce Emília O. Mota]  
**Data:** [23/07/2026]  
**Aprovação:** (espaço para assinatura do(a) coordenador(a)).
