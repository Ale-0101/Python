quantidade_notas = int(input("Quantas notas voce quer incerrir: "))
notas = []

for cont in range(quantidade_notas):
    
    notas.append(int(input(f"Nota numero {cont+1}: ")))

print(f"A medias dos alunos foi: {sum(notas)/len(notas)}")
