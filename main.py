"""
* APS de Estrutura de Dados *
Integrantes:
Kauan Henrique Santos Simão - 2988987
Pedro Coelho dos Santos Junior – 853528
Victoria Bernardi da Silva – 2751815
Lucas Episcopo Brunoro – 1821695
"""

bd = []
id = 0

print('Programa de cadastro para o auxílio emergencial usando 2 estruturas de dados (Fila e Dicionário)\n')

while True:
    print('* MENU *')
    print("1 - Cadastrar pessoa")
    print("2 - Lista Cadastros")
    print("3 - Procurar Pessoa Específica pelo Id")
    print('4 - Sair\n')
    op = int(input('Digite a opção desejada: '))
    print('')

    if op == 1:
        print('Digite os dados da pessoa à ser cadastrada: ')
        cad = dict()
        cad['id'] = id
        cad['nome'] = input('Digite o nome: ')
        cad['rg'] = input('Digite o RG: ')
        cad['cpf'] = input('Digite o CPF: ')
        cad['telefone'] = input('Digite o telefone: ')
        cad['endereco'] = input('Digite o endereço: ')
        bd.append(cad.copy())
        id = id + 1
        print('Usuário cadastrado!\n')

    elif op == 2:
        for cad in bd:
            for k, v in cad.items():
                print(f'{k}={v}')
            print()

    elif op == 3:
        indentificador = int(input('Insira o Id do usuário cadastrado: '))
        print('')
        b = dict()
        for a in bd:
            if a.get('id') == indentificador:
                b = a
                break
        if not b:
            print('* Id inválido! *')
        for k, v in b.items():
            print(f'{k}={v}')
        print()

    elif op == 4:
        break

    else:
        print('* Digite uma opção válida! *')
