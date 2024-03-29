print('\n\n### Olá! Seja bem vindo a calculadora de imposto de renda. ###')
print('-'*62)
nome = input('\nDigite seu nome: ')

while True:
    #solicita o salario do usuário como uma string
    salario_mensal = input('Digite seu salário mensal: R$')

    #verifica se a entrada contem soment numeros e virgulas
    if salario_mensal.replace(',', '', 1).replace('.','',1).isdigit():
        #substitui ',' por '.'
        salario_mensal = float(salario_mensal.replace(',', '.'))
        break
    else:
        print('Entrada Invalida. Digite uma valor numérico')

#calculo do imposto de renda em cima do salario recebido
#obs.: este calculo está sendo realizado em cima dos valores previstos no ano de 2024
#calculados em cima dos recebimentos 2023
def aliquota_imposto():

    if salario_mensal <= 2259.20:
        return 0
    elif salario_mensal >= 2259.20 and salario_mensal < 2826.66:
        return 7.5
    elif salario_mensal >= 2826.66 and salario_mensal < 3751.06:
        return 15
    elif salario_mensal >= 3751.06 and salario_mensal < 4664.68:
        return 22.5
    else:
        return 27.5

imposto_devido = (salario_mensal*aliquota_imposto())/100

if __name__ == '__main__':
    print(f'\n\n{nome}, com o salário recebido de R${salario_mensal:.2f},seu imposto devido será de R${imposto_devido:.2f}')