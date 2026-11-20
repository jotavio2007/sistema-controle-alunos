# 🎓 Sistema de Controle de Notas de Alunos

Projeto desenvolvido em Python para gerenciamento de notas escolares via terminal, evoluindo da manipulação básica de estruturas de dados em memória para um sistema **CRUD completo** com persistência em arquivo JSON e validação de entradas.

---

## 🚀 Funcionalidades (Versão 2.0)

* **Cadastrar Aluno (`Create`):** Registra o nome e a nota do aluno em uma lista de dicionários, validando se a nota é um valor numérico entre `0` e `10`.
* **Listar Alunos (`Read`):** Exibe todos os alunos cadastrados, suas respectivas notas e a situação final (`aprovado` para notas $\ge 7$ ou `reprovado`).
* **Calcular Média da Turma:** Soma todas as notas registradas e calcula a média geral da turma (tratando o caso de lista vazia para evitar divisão por zero).
* **Buscar Aluno (`Read`):** Localiza um aluno específico pelo nome (ignorando diferenças entre maiúsculas e minúsculas) e exibe sua nota e situação.
* **Editar Nota (`Update`):** Permite atualizar a nota de um aluno já cadastrado com a mesma validação de intervalo e tipo numérico.
* **Excluir Aluno (`Delete`):** Remove o registro de um aluno da lista pelo nome.
* **Persistência de Dados:** Salva e carrega automaticamente todos os registros no arquivo `alunos.json`, garantindo que os dados não sejam perdidos ao encerrar o programa.

---

## 🛠️ Conceitos Aplicados

* Estruturas de dados: **Listas** e **Dicionários**[cite: 1, 2].
* Modularização com **Funções** (`def`, parâmetros, `return` e escopo local/global)[cite: 1, 2].
* Controle de fluxo com laços (`while`, `for`) e condicionais (`if`, `elif`, `else`)[cite: 1, 2].
* Tratamento de exceções (`try` / `except ValueError` e `FileNotFoundError`).
* Serialização de dados com o módulo nativo `json` (`json.dump` e `json.load`).
* Manipulação de strings com `.lower()` para buscas flexíveis.

---

## 💻 Como Executar

1. Clone este repositório ou abra-o no **GitHub Codespaces**.
2. No terminal, execute o arquivo principal:
   ```bash
   python sistema.py