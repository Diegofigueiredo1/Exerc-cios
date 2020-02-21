#Função para calcular a taxa metabólica basal.
def calculo_basal(peso, constante):
    return (peso ** 0.75) * constante



#Função para calcular a taxa metabólica específica.
def calculo_especifico(peso, constante):
    return (peso ** 0.25) * constante



def main():
    codigos = [1, 2, 3, 4, 5]
    valores = [129, 78, 70, 49, 10]
    peso_total = float(input('Informe o peso total em Kg do animal: '))
    grupo = int(input('Informe a qual grupo o animal pertence: '))
    while grupo not in codigos:
        grupo = int(input('Por favor informe o grupo corretamente: '))
    objetivo = input('Informe qual calculo você deseja realizar, ["B" para TMB / "E" para TME]: ').upper()
    while objetivo != 'B' and objetivo != 'E':
        objetivo = input('Escolha inválida. Por favor digite uma das opções indicadas, ["B" para TMB / "E" para TME]: ').upper()
    for i in range(len(codigos)):
        if grupo == codigos[i]:
            constante = valores[i]
    if objetivo == 'B':
        print(f'Taxa metabólica basal = {calculo_basal(peso_total, constante):.2f}')
    elif objetivo == 'E':
        print(f'Taxa metabólica específica = {calculo_especifico(peso_total, constante):.2f}')



main()


