"""
Vinheria Agnello
Caso ficcional criado exclusivamente
para fins acadêmicos. 

RM555206 - Milton Cezar Backanieski 
RM555026 - Vitor Bebiano Mulford 
RM54901 - Lorenzo Hayashi Mangini
"""

import os


def limpar_terminal():
    """
    Limpa o terminal de acordo com o sistema operacional.
    """
    if os.name == "nt":
        _ = os.system("cls")


def criar_lista_de_vinhos():
    """
    Cria e retorna uma lista de vinhos com seus tipos e preços.
    """
    lista_vinhos = {
        "Tintos": [
            ("Cabernet Sauvignon", 100),
            ("Pinot Noir", 115),
            ("Tinto Malbec", 80),
            ("Tinto Merlot", 95),
        ],
        "Brancos": [
            ("Chardonnay", 80),
            ("Sauvignon Blanc", 70),
            ("Riesling", 90),
            ("Pinot Grigio", 60),
        ],
        "Rosés": [
            ("Cabernet Franc", 70),
            ("Syrah", 80),
            ("Grenache", 60),
        ],
    }
    return lista_vinhos


def menu():
    """
    Exibe o menu principal e solicita a opção do usuário.
    """
    limpar_terminal()
    print("MENU PRINCIPAL\n")
    print("1 - Ver lista de vinhos disponíveis")
    print("2 - Comprar vinhos")
    print("3 - Visualizar carrinho de compras")
    print("4 - Finalizar compra")
    print("5 - Sair\n")
    opcao = int(input("Opção: "))
    return opcao


def comprar_vinhos(lista_vinhos, carrinho):
    """
    Permite ao usuário comprar vinhos e adicioná-los ao carrinho.
    """
    while True:
        limpar_terminal()
        print("COMPRAR VINHOS\n")
        print("Escolha um tipo de vinho para comprar:")
        print("1 - Tintos")
        print("2 - Brancos")
        print("3 - Rosés")
        print("4 - Voltar ao menu principal\n")
        opcao_tipo = int(input("Opção: "))

        if opcao_tipo == 4:
            break

        tipo_vinho = None
        if opcao_tipo == 1:
            tipo_vinho = "Tintos"
        elif opcao_tipo == 2:
            tipo_vinho = "Brancos"
        elif opcao_tipo == 3:
            tipo_vinho = "Rosés"
        else:
            print("Opção inválida.")
            continue

        print(f"\nVinhos {tipo_vinho}:")
        for i, (vinho, preco) in enumerate(lista_vinhos[tipo_vinho]):
            print(f"{i+1} - {vinho}: R$ {preco}")

        opcao_vinho = int(
            input("\nEscolha o número do vinho que deseja comprar (ou 0 para voltar): ")
        )
        if opcao_vinho == 0:
            continue

        try:
            vinho_escolhido, preco_vinho = lista_vinhos[tipo_vinho][opcao_vinho - 1]
        except IndexError:
            print("Opção inválida.")
            continue

        quantidade = int(
            input(f"Digite a quantidade de '{vinho_escolhido}' que deseja comprar: ")
        )
        carrinho.append((vinho_escolhido, preco_vinho, quantidade))
        print("Vinho adicionado ao carrinho.")

    return carrinho


def visualizar_carrinho(carrinho):
    """
    Exibe os itens no carrinho de compras e calcula o total com desconto, se aplicável.
    """
    limpar_terminal()
    total = 0
    total_itens = 0
    print("CARRINHO DE COMPRAS\n")
    print("Itens no carrinho:")
    for item in carrinho:
        vinho, preco_unitario, quantidade = item
        subtotal = preco_unitario * quantidade
        total += subtotal
        total_itens += quantidade
        print(f"{vinho}: {quantidade} garrafa(s) - R$ {subtotal}")

    desconto = 0
    if total_itens >= 4:
        desconto = total * 0.20
    elif total_itens == 3:
        desconto = total * 0.10
    elif total_itens == 2:
        desconto = total * 0.05

    total_com_desconto = total - desconto
    print(f"\nValor total da compra: R$ {total}")
    print(f"Desconto aplicado: R$ {desconto}")
    print(f"Total a pagar com desconto: R$ {total_com_desconto}")


def finalizar_compra():
    """
    Finaliza a compra, solicitando e exibindo os dados de cadastro do cliente e o método de pagamento.
    """
    limpar_terminal()
    print("FINALIZAR COMPRA\n")
    nome_completo, email, cpf, data_nascimento, endereco, cep, cidade, estado = (
        cadastro()
    )
    print("\nCadastro do cliente:")
    frase_cadastro = (
        f"Nome: {nome_completo}, Email: {email}, CPF: {cpf}, "
        f"Data de Nascimento: {data_nascimento}, Endereço: {endereco}, "
        f"CEP: {cep}, Cidade: {cidade}, Estado: {estado}"
    )
    print(frase_cadastro)
    metodo_pagamento = input(
        "\nEscolha o método de pagamento ((1) Pix, (2) Boleto, (3) Débito ou (4) Crédito): "
    )
    print("\nCompra finalizada com sucesso!")


def cadastro():
    """
    Solicita e retorna os dados de cadastro do cliente.
    """
    print("-" * 17)
    print("CADASTRO CLIENTE")
    print("-" * 17)
    nome_completo = input("Nome completo: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço (rua, numero, complemento): ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    return nome_completo, email, cpf, data_nascimento, endereco, cep, cidade, estado


carrinho_compras = []

while True:
    opcao = menu()

    if opcao == 1:
        vinhos = criar_lista_de_vinhos()
        for tipo, lista in vinhos.items():
            print(f"\nVinhos {tipo}:")
            for vinho, preco in lista:
                print(f"{vinho}: R$ {preco}")
        input("\nPressione Enter para continuar...")
    elif opcao == 2:
        carrinho_compras = comprar_vinhos(criar_lista_de_vinhos(), carrinho_compras)
    elif opcao == 3:
        visualizar_carrinho(carrinho_compras)
        input("\nPressione Enter para continuar...")
    elif opcao == 4:
        finalizar_compra()
        input("\nPressione Enter para continuar...")
    elif opcao == 5:
        print("\nPrograma finalizado.")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
