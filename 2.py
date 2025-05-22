
if_dic = {}
est = {}
for i in range(0, 2):
    nome = input(f'Digite o NOME do {i+1}º aluno: ')
    notas = []
    for j in range(0, 2):
        n = int(input(f'Digite a NOTA {j+1} do {nome}:'))
        notas.append(n)
    media = sum(notas)/2
    est['notas'] = notas
    est['media'] = media
    if_dic[nome] = est
    print(media)
        

#Pedir para o usuario digitar um nome e vc fazer a busca mostrando a 
#Média do aluno (se n existir, digitar novamente até encontrar ou 0 p sair)



