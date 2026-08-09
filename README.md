# 📊 Gestão de Dados de Pesquisa – Diagnóstico Socioambiental

**Temple | Analista de Gestão de Dados de Pesquisa Pleno**  
**Data da Entrega:** Agosto/2026  
**Candidata:** Joyce Emília O. Mota

---

## 📌 Sobre o Projeto

Este repositório contém a entrega do teste técnico para a posição de **Analista de Gestão de Dados de Pesquisa Pleno**. O projeto aborda um **diagnóstico socioambiental** em uma região composta por **8 municípios**, integrando diferentes estratégias de pesquisa e produção de evidências para subsidiar decisões do cliente.

### A pesquisa contempla:
- Survey com aproximadamente **6.000 respondentes**
- **40 entrevistas** em profundidade
- **12 grupos focais**
- Observação de campo
- Dados secundários (IBGE, CadÚnico, DataSUS)
- Registros de mobilização social
- Evidências diárias de campo (fotos, diários, termos de consentimento)

---

## 🎯 Situação-Problema

O projeto está em andamento em uma **fase piloto**. Após as primeiras semanas, a coordenação identificou diversos problemas:

| Problema | Impacto |
| :--- | :--- |
| **Padronização inconsistente** | Cada pesquisador preenche os campos de forma diferente |
| **Dados duplicados** | Respostas repetidas comprometem a análise |
| **Inconsistências entre bases** | Divergências entre dados e documentos de controle |
| **Documentação ausente** | Parte dos dados coletados não possui registro |
| **Perda de rastreabilidade** | Não se sabe qual é a versão mais atual da base |
| **Conferência manual** | Consome muitas horas da jornada de trabalho |

---

## 🎯 Objetivos do Projeto

1. **Avaliar** as bases disponíveis e identificar inconsistências.
2. **Propor** soluções para os problemas apontados pela equipe.
3. **Estruturar** um processo que garanta:
   - **Qualidade** dos dados
   - **Rastreabilidade** de cada registro
   - **Disponibilidade** para a equipe de pesquisa
4. **Automatizar** o máximo possível das tarefas manuais.

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta / Biblioteca | Finalidade |
| :--- | :--- |
| **Python 3.13** | Linguagem principal do pipeline |
| **Pandas** | Manipulação e análise de dados |
| **NumPy** | Operações numéricas e arrays |
| **Matplotlib / Seaborn** | Visualização de dados |
| **Jupyter Notebook** | Ambiente para análise exploratória (EDA) |
| **Git / GitHub** | Versionamento e entrega do projeto |

---

## 📂 Estrutura do Projeto

```
├── 01_Codigos_Python/
│   ├── Script_1_Carregamento.py              # Carrega as 4 bases com detecção de encoding
│   ├── Script_2_Validacao_Estrutura.py       # Valida colunas obrigatórias
│   ├── Script_3a_Diagnostico_Qualidade.py    # Identifica problemas com impacto e sugestão
│   ├── Script_3b_Decisoes_Acoes.py           # Prioriza problemas e gera plano de ação
│   ├── Script_4_Tratamento_Padronizacao.py   # Corrige e padroniza os dados
│   ├── Script_5_Exportacao_Final.py          # Exporta em CSV, Excel e Parquet
│   └── Script_6_Renomeacao_Arquivos.py       # Corrige nomenclatura (POP)
│
├── 02_Base_Original/
│   ├── 01_Base_Principal_Survey_v2_4.csv
│   ├── 03_Cadastro_Mestre_Municipios_Comunidades.csv
│   ├── 04_Controle_Equipe_Campo.csv
│   └── 05_Controle_Evidencias.csv
│
├── 03_Resultados_Processados/
│   ├── Diagnostico/
│   │   └── diagnostico_qualidade_*.json
│   ├── Plano_Acao/
│   │   ├── plano_acao_*.md
│   │   └── decisoes_acoes_*.json
│   └── Dados_Tratados/
│       ├── tratado_survey_*.csv
│       ├── tratado_cadastro_*.csv
│       ├── tratado_equipe_*.csv
│       ├── tratado_evidencias_*.csv
│       └── estatisticas/
│
├── 04_Documentacao/
│   ├── README.md
│   └── Relatorio_Executivo.md
│
├── 05_Evidencias_Renomeacao/
│   └── relatorio_renomeacao_*.csv
│
└── EDA.ipynb                                 # Notebook com análise exploratória completa
```

---

## 📊 Principais Resultados do Diagnóstico

### Visão Geral

| Indicador | Valor |
| :--- | :--- |
| **Total de problemas identificados** | **864** |
| **Bases analisadas** | 4 (Survey, Cadastro, Equipe, Evidências) |
| **Problemas críticos** | 10 (idade inválida, arquivos faltando, duplicatas) |
| **Problemas de alto impacto** | 42 (pesquisadores não encontrados, campos nulos) |
| **Problemas médios** | 743 (nomenclatura incorreta) |
| **Problemas baixos** | 26 (status inválido, IBGE duplicado) |

### Distribuição por Base

| Base | Problemas | % do Total |
| :--- | :---: | :---: |
| Evidências | 791 | 91,6% |
| Survey | 47 | 5,4% |
| Cadastro | 26 | 3,0% |
| **Total** | **864** | **100%** |

### Principais Tipos de Problemas

| Tipo | Ocorrências | Prioridade |
| :--- | :---: | :---: |
| Nomenclatura incorreta (arquivos) | 743 | Médio |
| Pesquisador não encontrado | 83 | Alto |
| Status inválido | 18 | Baixo |
| Código IBGE duplicado | 8 | Baixo |
| Idade inválida | 3 | **Crítico** |
| UUID duplicado | 3 | **Crítico** |
| Diário de campo faltando | 3 | **Crítico** |
| Data inconsistente | 1 | **Crítico** |

---

## 🔧 Soluções Implementadas

### 1. Pipeline Automatizado

| Etapa | Script | Descrição |
| :--- | :--- | :--- |
| **1. Carregamento** | Script 1 | Leitura das 4 bases com detecção automática de encoding |
| **2. Validação** | Script 2 | Verificação de colunas obrigatórias conforme Dicionário de Dados |
| **3. Diagnóstico** | Script 3a | Identificação de problemas com descrição, impacto e sugestão |
| **4. Decisões** | Script 3b | Priorização (Crítico/Alto/Médio/Baixo) e plano de ação |
| **5. Tratamento** | Script 4 | Correção automática de campos e padronização |
| **6. Exportação** | Script 5 | Geração de CSVs, Excel, Parquet e estatísticas |
| **7. Renomeação** | Script 6 | Correção de nomenclatura de arquivos conforme POP |

### 2. Critérios de Qualidade (POP)

Baseado no documento **POP – Critérios de Qualidade para Validação de Evidências**:

- **Evidências obrigatórias:** Termo de consentimento, fotografia, diário de campo, metadados
- **Padrão de nomenclatura:** `TC.#####.pdf`, `IMG.#####.jpg`, `DC.#####.pdf`
- **Classificação de não conformidades:** Crítica / Maior / Menor
- **Checklist de validação:** 9 critérios obrigatórios

### 3. Indicadores de Qualidade

- % de entrevistas com conjunto completo de evidências
- % de arquivos com nomenclatura correta
- % de evidências aprovadas na primeira validação
- Tempo médio entre coleta e upload
- Nº de não conformidades críticas por pesquisador
- Nº de retrabalhos por lote

---

## 🚀 Como Executar o Pipeline

### 1. Clone o repositório

```bash
git clone https://github.com/NegraEmilia71/teste-temple-analista-dados.git
cd teste-temple-analista-dados
```

### 2. Instale as dependências

```bash
pip install pandas numpy openpyxl pyarrow
```

### 3. Execute os scripts em ordem

```bash
python 01_Codigos_Python/Script_1_Carregamento.py
python 01_Codigos_Python/Script_2_Validacao_Estrutura.py
python 01_Codigos_Python/Script_3a_Diagnostico_Qualidade.py
python 01_Codigos_Python/Script_3b_Decisoes_Acoes.py
python 01_Codigos_Python/Script_4_Tratamento_Padronizacao.py
python 01_Codigos_Python/Script_5_Exportacao_Final.py
python 01_Codigos_Python/Script_6_Renomeacao_Arquivos.py  # Opcional
```

---

## 📈 Visualizações Geradas

O pipeline gera automaticamente:

- **Gráficos de diagnóstico:** Distribuição de problemas por tipo e prioridade
- **Mapas de calor:** Inconsistências por base e pesquisador
- **Estatísticas descritivas:** Por coluna, com nulos, duplicatas e valores extremos
- **Relatórios em JSON e Markdown:** Para documentação e auditoria

---

## 📄 Documentação

### Relatório Executivo

O relatório consolidado está disponível em `04_Documentacao/Relatorio_Executivo.md` e contém:

- Resumo executivo com os principais números
- Detalhamento dos problemas identificados
- Plano de ação com prioridades e responsáveis
- Recomendações para a equipe

### Dicionário de Dados

Todas as variáveis do survey estão documentadas no Dicionário de Dados v2.4, incluindo:
- Tipo de dado
- Obrigatoriedade
- Valores esperados
- Descrição

---

## 🎯 Recomendações Finais

1. **Corrigir problemas CRÍTICOS** imediatamente (idade inválida, UUID duplicado, arquivos faltando)
2. **Atualizar cadastro de equipe** com todos os pesquisadores ativos
3. **Automatizar a validação diária** com o Script 3a
4. **Adotar o campo `Qualidade_Registro`** para filtrar dados problemáticos
5. **Utilizar os arquivos Parquet** para análises futuras (compactos e rápidos)

---

## 👩‍💻 Sobre a Candidata

**Joyce Emília O. Mota**  
Candidata à vaga de **Analista de Gestão de Dados de Pesquisa Pleno**  
📧 joyce.emilia@email.com  
🔗 [LinkedIn](https://www.linkedin.com/in/joyce-cerqueira/)  
🔗 [GitHub](https://github.com/NegraEmilia71)

---

## 📌 Observações

- Os dados utilizados são **anônimos** e fazem parte de um projeto de diagnóstico socioambiental
- O pipeline foi desenvolvido para ser **reprodutível** e **escalável**
- O projeto está disponível em: [https://github.com/NegraEmilia71/teste-temple-analista-dados](https://github.com/NegraEmilia71/teste-temple-analista-dados)

---

## 📝 Licença

Este projeto é de uso exclusivo para fins de avaliação do processo seletivo da Temple.

---

*Estrutura organizada e pipeline automatizado.* 🚀
