# Sistema de Controle de Notas de Alunos

Projeto prático desenvolvido em Python para consolidar os conceitos fundamentais de programação. O sistema funciona via terminal e permite gerenciar o cadastro, a situação individual e a média geral de uma turma através de um menu interativo.

## Funcionalidades

- **Cadastrar Aluno:** Registra o nome e a nota do aluno em uma estrutura de dados em memória.
- **Listar Alunos e Situação:** Exibe todos os alunos cadastrados, suas notas e classifica automaticamente cada um como **Aprovado** (nota $\ge 7.0$) ou **Reprovado** (nota $< 7.0$).
- **Calcular Média da Turma:** Soma as notas registradas, verifica se há alunos cadastrados para evitar divisão por zero e retorna a média geral da turma.
- **Menu Interativo:** Permite navegar entre as operações continuamente até que o usuário escolha encerrar o programa.

## Conceitos Aplicados

- **Variáveis e Tipos Primitivos:** Manipulação de textos (`str`) e números decimais (`float`).
- **Entrada, Saída e Conversão de Tipos:** Leitura de dados pelo teclado com `input()`, conversão com `float()` e exibição formatada com `print()`.
- **Estruturas de Dados:** Armazenamento de múltiplos registros utilizando uma **lista de dicionários** (`list` e `dict`) e adição de elementos com `.append()`.
- **Controle de Fluxo:** Tomada de decisões com estruturas condicionais (`if`, `elif`, `else`) e operadores de comparação (`>=`, `==`, `!=`).
- **Laços de Repetição:** Iteração sobre registros com `for` e manutenção do menu interativo com `while`.
- **Funções e Escopo:** Modularização do código com `def` e retorno de valores processados do escopo local para o global com `return`.

## Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe o arquivo `controle_alunos.py` deste repositório.
3. No terminal, navegue até a pasta do arquivo e execute:

```bash
python controle_alunos.py
