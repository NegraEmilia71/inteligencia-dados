import os
import shutil
import glob
from pathlib import Path

# ============================================================
# SCRIPT PARA ORGANIZAR A ESTRUTURA DE ENTREGA (VERSÃO ATUALIZADA)
# ============================================================

# Definição da estrutura de pastas e arquivos correspondentes
ESTRUTURA = {
    '01_Codigos': ['*.py', '*.ipynb'],
    '02_Base_Original': [
        '01_Base_Principal_Survey_v2_4.csv',
        '03_Cadastro_Mestre_Municipios_Comunidades.csv',
        '04_Controle_Equipe_Campo.csv',
        '05_Controle_Evidencias.csv'
    ],
    '03_Resultados_Processados/Diagnostico': ['diagnostico_qualidade_*.json'],
    '03_Resultados_Processados/Plano_Acao': [
        'plano_acao_*.md',
        'decisoes_acoes_*.json',
        'diagnostico_resumo_*.md'
    ],
    '03_Resultados_Processados/Dados_Tratados': ['output_tratado'],  # pasta inteira
    '04_Documentacao': [
        'README.md',
        'Relatorio_Executivo.md'
    ],
    '05_Evidencias_Renomeacao': ['relatorio_renomeacao_*.csv']
}

def criar_pastas():
    """Cria todas as pastas definidas na estrutura."""
    for pasta in ESTRUTURA.keys():
        Path(pasta).mkdir(parents=True, exist_ok=True)
        print(f"📁 Criada/verificada: {pasta}")

def mover_arquivos():
    """Move os arquivos para as pastas correspondentes."""
    for destino, padroes in ESTRUTURA.items():
        for padrao in padroes:
            # Se for uma pasta inteira (ex: output_tratado)
            if os.path.isdir(padrao):
                if os.path.exists(padrao):
                    # Verifica se a pasta destino já contém a subpasta
                    destino_path = Path(destino) / padrao
                    if not destino_path.exists():
                        shutil.move(padrao, destino)
                        print(f"📂 Movida pasta: {padrao} -> {destino}")
                    else:
                        print(f"ℹ️  Pasta já existe em {destino}: {padrao}")
                continue

            # Caso contrário, procurar arquivos que correspondam ao padrão
            for arquivo in glob.glob(padrao):
                if os.path.isfile(arquivo):
                    shutil.move(arquivo, destino)
                    print(f"📄 Movido: {arquivo} -> {destino}")

def mover_scripts():
    """Move todos os scripts Python para a pasta de códigos, exceto este."""
    for arquivo in glob.glob('Script_*.py'):
        if arquivo != 'organizar_entrega.py':
            shutil.move(arquivo, '01_Codigos_Python')
            print(f"🐍 Movido script: {arquivo} -> 01_Codigos_Python")
    
    # Move também o próprio script organizador para a raiz (opcional, mas mantido aqui)
    # Se quiser mover o organizador junto, descomente a linha abaixo:
    # if os.path.exists('organizar_entrega.py'):
    #     shutil.move('organizar_entrega.py', '01_Codigos_Python')
    #     print("🐍 Movido: organizar_entrega.py -> 01_Codigos_Python")

def criar_readme():
    """Cria um README.md básico se nenhum for encontrado."""
    if not os.path.exists('04_Documentacao/README.md'):
        with open('04_Documentacao/README.md', 'w', encoding='utf-8') as f:
            f.write("""# Teste Técnico – Analista de Gestão de Dados de Pesquisa Pleno

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
   | **6** | (Opcional) Renomeação | Correção de nomenclatura de arquivos conforme POP (requer ajuste do caminho da pasta de arquivos) |

> ⚠️ **Atenção:** a **Célula 6** (renomeação de arquivos) exige que você edite a variável `PASTA_RAIZ_ARQUIVOS` dentro do notebook, apontando para o local correto onde os arquivos de campo (termos, fotos e diários) estão armazenados. Recomenda-se executar primeiro em **modo simulação** para verificar as alterações propostas.

## Resultados esperados

- Diagnóstico completo em JSON (`diagnostico_qualidade_*.json`)
- Plano de ação com prioridades (`plano_acao_*.md` e `decisoes_acoes_*.json`)
- Bases tratadas em **CSV**, **Excel** e **Parquet** (pasta `output_tratado/`)
- Estatísticas detalhadas por coluna (pasta `estatisticas/`)
- Relatório de renomeação de arquivos (caso execute a Célula 6)
""")

        print("📝 README.md criado em 04_Documentacao/")
    else:
        print("ℹ️  README.md já existe em 04_Documentacao/")


def verificar_arquivos_originais():
    """Verifica se todos os arquivos CSV originais estão presentes na pasta 02_Base_Original/."""   
    pasta_base = Path('02_Base_Original')
    csvs_esperados = [
        '01_Base_Principal_Survey_v2_4.csv',
        '03_Cadastro_Mestre_Municipios_Comunidades.csv',
        '04_Controle_Equipe_Campo.csv',
        '05_Controle_Evidencias.csv'
    ]
    todos_presentes = True
    for csv in csvs_esperados:
        if not (pasta_base / csv).exists():
            todos_presentes = False
            print(f"⚠️  Atenção: {csv} não encontrado em 02_Base_Original/")
    if todos_presentes:
        print("✅ Todos os CSVs originais estão em 02_Base_Original/")

if __name__ == '__main__':
    print("🔄 Organizando estrutura de entrega...")
    print("-" * 50)

    criar_pastas()
    mover_scripts()
    mover_arquivos()
    criar_readme()
    
    print("-" * 50)
    verificar_arquivos_originais()
    
    print("\n" + "=" * 50)
    print("✅ Estrutura organizada com sucesso!")
    print("📂 Pasta raiz: Entrega_Teste_Temple/")
    print("=" * 50)