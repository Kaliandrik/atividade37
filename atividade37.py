# Ler um vetor com 20 idades e exibir a
# maior e menor.

idades = []

for i in range(1,21):
    idade = int(input("Digite 20 idades: "))
    idades.append(idade)

maioridade = max(idades)
menoridade = min(idades)

print(f"A maior idade digitada é: {maioridade}")
print(f"A menor idade digitada é: {menoridade}")