import json


def salvar_dados():
  with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo)


def carregar_dados():
  try:
    with open("alunos.json", "r") as arquivo:
      return json.load(arquivo)
  except FileNotFoundError:
    return []


alunos = carregar_dados()


def aluno_existe(nome_busca):
  for item in alunos:
    if item["nome"].lower() == nome_busca.lower():
      return True
  return False


def cadastrar_alunos(nome, nota):
  cadastro = {"nome": nome, "nota": nota}
  alunos.append(cadastro)
  salvar_dados()


def listar_alunos():
  for item in alunos:
    if item["nota"] >= 7:
      print(item["nome"], "-", item["nota"], "- aprovado")
    else:
      print(item["nome"], "-", item["nota"], "- reprovado")


def calcular_media():
  soma = 0
  for item in alunos:
    soma = soma + item["nota"]
  if len(alunos) == 0:
    return 0
  else:
    media = soma / len(alunos)
    return media


def buscar_aluno(nome_busca):
  encontrado = False
  for item in alunos:
    if item["nome"].lower() == nome_busca.lower():
      if item["nota"] >= 7:
        print(item["nome"], "-", item["nota"], "- aprovado")
      else:
        print(item["nome"], "-", item["nota"], "- reprovado")
      encontrado = True
      break
  if not encontrado:
    print("Aluno não encontrado.")


def editar_nota(nome_busca, nova_nota):
  encontrado = False
  for item in alunos:
    if item["nome"].lower() == nome_busca.lower():
      item["nota"] = nova_nota
      salvar_dados()
      print("Nota atualizada com sucesso!")
      encontrado = True
      break
  if not encontrado:
    print("Aluno não encontrado.")


def excluir_aluno(nome_busca):
  encontrado = False
  for item in alunos:
    if item["nome"].lower() == nome_busca.lower():
      alunos.remove(item)
      salvar_dados()
      print("Aluno excluído com sucesso!")
      encontrado = True
      break
  if not encontrado:
    print("Aluno não encontrado.")


opcao = ""
while opcao != "7":
  print("-" * 30)
  print("Qual a operação desejada?")
  print("1 - Cadastrar aluno")
  print("2 - Listar alunos")
  print("3 - Calcular a média da turma")
  print("4 - Buscar aluno")
  print("5 - Editar nota")
  print("6 - Excluir aluno")
  print("7 - Sair")
  opcao = input("Digite uma opção: ").strip()

  if opcao == "1":
    nome = input("Digite o nome do aluno: ").strip()
    if nome == "":
      print("O nome do aluno não pode ficar em branco.")
    elif aluno_existe(nome):
      print("Aluno já cadastrado! Use a opção 5 para editar a nota.")
    else:
      while True:
        try:
          nota = float(input("Digite a nota: ").replace(",", "."))
          if nota < 0 or nota > 10:
            print("Nota deve ser entre 0 e 10.")
          else:
            cadastrar_alunos(nome, nota)
            print("Aluno cadastrado com sucesso!")
            break
        except ValueError:
          print("Valor inválido! Digite um número entre 0 e 10.")

  elif opcao == "2":
    if len(alunos) == 0:
      print("Nenhum aluno cadastrado.")
    else:
      listar_alunos()

  elif opcao == "3":
    if len(alunos) == 0:
      print("Nenhum aluno cadastrado para calcular a média.")
    else:
      print("Média da turma:", round(calcular_media(), 2))

  elif opcao == "4":
    if len(alunos) == 0:
      print("Nenhum aluno cadastrado.")
    else:
      nome = input("Qual aluno deseja buscar? ").strip()
      buscar_aluno(nome)

  elif opcao == "5":
    if len(alunos) == 0:
      print("Nenhum aluno cadastrado.")
    else:
      listar_alunos()
      nome = input("Qual aluno deseja editar? ").strip()
      if not aluno_existe(nome):
        print("Aluno não encontrado.")
      else:
        while True:
          try:
            nova_nota = float(input("Digite a nova nota: ").replace(",", "."))
            if nova_nota < 0 or nova_nota > 10:
              print("Nota deve ser entre 0 e 10.")
            else:
              editar_nota(nome, nova_nota)
              break
          except ValueError:
            print("Valor inválido! Digite um número entre 0 e 10.")

  elif opcao == "6":
    if len(alunos) == 0:
      print("Nenhum aluno cadastrado.")
    else:
      listar_alunos()
      nome = input("Qual aluno deseja excluir? ").strip()
      excluir_aluno(nome)

  elif opcao == "7":
    print("Encerrando sessão...")

  else:
    print("Opção inválida!")