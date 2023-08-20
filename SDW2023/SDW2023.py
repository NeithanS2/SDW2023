import csv

ids_procurados = []
while True:
    with open('DadosBancarios.csv', 'r') as file:
        ler_dados_bancarios = csv.reader(file)
        next(ler_dados_bancarios)  
        dados_bancarios = {row[0]: row[1:] for row in ler_dados_bancarios}
    
    procurar_id = input("Digite o UserID que você está procurando: ")
    print()
    
    
    if procurar_id in dados_bancarios:
        print(f"Informações do UserID {procurar_id}:")
        print("Nome:", dados_bancarios[procurar_id][0])
        print("Número da Conta:", dados_bancarios[procurar_id][1])
        print("Agência:", dados_bancarios[procurar_id][2])
        print("Número do Cartão:", dados_bancarios[procurar_id][3])
        print()
        ids_procurados.append([procurar_id] + dados_bancarios[procurar_id])
    else:
        print("Esse UserID ainda não foi cadastrado.")
        print()
    
    procura = input('Deseja procurar outro ID? [S]im, [N]ão: ').upper().startswith('S')
    print()
    if procura is True:
        print()
        continue
    else:
        break


with open('IDS_Procurados.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['UserID', 'Nome', 'Número da Conta', 'Agência', 'Número do Cartão'])
    writer.writerows(ids_procurados)

print('IDs que você procurou:')
print()
for informacao in ids_procurados:
    print("UserID:", informacao[0])
    print("Nome:", informacao[1])
    print("Número da Conta:", informacao[2])
    print("Agência:", informacao[3])
    print("Número do Cartão:", informacao[4])
    print()

print('Até a próxima! S2')