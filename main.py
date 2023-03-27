def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("")
    print(f'Seja Bem-vindo, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Escolha uma das opções abaixo: ')
    print("")

choice = ""

while True:
    print("1) Tirar fundo da imagem")
    print("2) Normalizar imagem")
    print("3) Sair")
    print("")

    choice = input("Digite aqui: ")

    choice = choice.strip()

    if ( choice == "1"):
        print("Voce escolheu: Tirar fundo da imagem")
        print("")

    elif ( choice == "2" ):
        print("Voce escolheu: Normalizar imagem")
        print("")

    elif ( choice == "3" ):
        print("Voce escolheu: Sair")
        print("")
        break

    else:
        print("Opção inválida! Por favor escolha uma das opções abaixo...")
        print("")

