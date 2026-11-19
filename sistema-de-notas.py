alunos=[]
def cadastrar_alunos(nome,nota):
  cadastro={
    'nome':nome,
    'nota':nota
  }
  alunos.append(cadastro)
def listar_alunos():
  for item in alunos:
    if item['nota'] >=7:
     print(item['nome'] ,item['nota'], "aprovado")
    else:
      print(item['nome'], item['nota'] , "reprovado")
def calcular_media():
  soma = 0
  for item in alunos:
   soma= soma + item['nota']
  if len(alunos) == 0:
   return 0  
  else:
     media=soma/len(alunos)
     return media
opcao=""
while opcao != '4':
  print("qual a operação desejada?")
  print("1-cadastrar aluno")
  print("2-listar alunos ")
  print("3-calcular a média da turma")
  print("4-sair")
  opcao=input("digite uma opção: ")
  if opcao =='1':
   nome=input("digite o nome do aluno: ")
   nota=float(input('digite a nota:'))
   cadastrar_alunos(nome, nota)
  elif opcao =='2':
   listar_alunos()
  elif opcao =='3':
    print("média da turma: ",calcular_media())
  elif opcao=='4':
   print('encerrando sessão')
  else:
    print("INVALIDO!")
  
