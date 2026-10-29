import os
os.system("cls" if os.name == "nt" else "clear")

alunos = [ 
    {'nome' : 'Ana', 'notas' : [9, 9], 'idade' : 15}, 
    {'nome' : 'Estevan', 'notas' : [10, 8], 'idade' : 15},
    {'nome' : 'Rafael', 'notas' : [10, 10], 'idade' : 15}, 
    {'nome' : 'Eduardo', 'notas' : [8, 9], 'idade' : 15},
    {'nome' : 'Bruno', 'notas' : [9, 10], 'idade' : 16}, 
    {'nome' : 'Yasmin', 'notas' : [10, 8], 'idade' : 16},
    {'nome' : 'Guilherme', 'notas' : [7, 9], 'idade' : 16}, 
    {'nome' : 'Arthur', 'notas' : [9, 10], 'idade' : 16},
    {'nome' : 'Random', 'notas' : [1, 5], 'idade' : 15}

] 

def media(soma, qtde): 
    return soma / qtde 

for aluno in alunos: 
    qtde_notas = len(aluno['notas']) 
    soma = sum(aluno['notas']) 
    nota = media(soma, qtde_notas)
    
    if nota >= 7:
        print(f"Aluno: {aluno['nome']}, Nota: {nota} - APROVADO")
    else:
        print(f"Aluno: {aluno['nome']}, Nota: {nota} - REPROVADO")