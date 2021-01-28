import random

class Lutador:
    vitorias = 0

    def __init__(self, nome, idade, peso, forca, faixa, arte):
        if(isinstance(nome, str) and isinstance(idade, int) and isinstance(peso, int) and isinstance(forca, int) and isinstance(faixa, str) and isinstance(arte, str)):
            self.nome   = nome
            self.idade  = idade
            self.peso   = peso
            self.forca  = forca
            self.faixa  = faixa
            self.arte   = arte


class Torneio:

    def __init__(self, nome, arte, faixas, pesos):
        if(isinstance(nome, str) and isinstance(arte, str) and isinstance(faixas, list) and isinstance(pesos, list)):
            self.nome   = nome
            self.arte   = arte
            self.faixas = faixas
            self.pesos  = pesos


lutadores = []
torneios = []

while(True):
    print("\nEscolha uma das opções abaixo:")
    print("1 - Menu do Torneio")
    print("2 - Menu de Lutador")
    print("3 - Criar Torneio Aleatório")
    print("4 - Fechar Programa")
    entrada0 = input("Insira apenas um algarismo: ")
    print()

    if(entrada0 == '1'):  # Menu de torneio
        print("MENU DE TORNEIO:")
        print("1 - Criar torneio")
        print("2 - Inscrever lutador")
        print("3 - Ver torneios existentes")
        print("4 - Ver ranking de torneio -> escolhe um torneio existente")
        print("5 - Ver lutadores inscritos em torneio -> escolhe um torneio existente")
        print("6 - Realizar luta -> escolhe um torneio existente -> escolhe dois lutadores inscritos")
        entrada1 = input("Insira apenas um algarismo: ")

        if(entrada1 == '1'):
            print("CRIAR TORNEIO:")
            
            print("\nInsira um nome para o torneio:")
            nome = input()
            print()

            print("Insira a arte marcial do torneio:")
            arte = input()
            
            faixas = []
            print("Para escolha das faixas, insira uma faixa e pressione Enter:")
            faixa = input()
            while (faixa != ''):
                faixas.append(faixa)
                print("Insira a proxima faixa, para terminar pressione Enter com o campo vazio:")
                faixa = input()
            
            print("Deseja incluir categoria livre?")
            faixa_livre = input("Insira 's' para sim e 'n' para não, sem as aspas: ")
            if(faixa_livre == 's'):
                faixas.append("livre")

            pesos = []
            print("Escolhendo os intervalos de peso:")
            menor = int(input("Insira o valor menor do intervalo:"))
            while(menor != ''):
                maior = int(input("Insira o valor maior do intervalo:"))
                if(menor <= maior):
                    pesos.append([menor,maior])
                else:
                    print("o intervalo " + menor + "-" + maior + "não é válido e por isso não foi adicionado.")
                menor = input("Insira o valor menor do intervalo ou enter para terminar:")

            torneios.append(Torneio(nome, arte, faixas, pesos))
            print("Torneio adicionado com sucesso!\n")


        elif(entrada1 == '2'):
            print("INSCREVER LUTADOR:")

        elif(entrada1 == '3'):
            print("TORNEIOS EXISTENTES:")
            for torneio in torneios:
                print(torneio.nome)

        elif(entrada1 == '4'):
            print("RANKING DE TORNEIO:")

        elif(entrada1 == '5'):
            print("LUTADORES INSCRITOS:")

        elif(entrada1 == '6'):
            print("REALIZAR LUTA:")

        else:
            print("Não foi inserida uma opção válida, insira apenas um algarismo de 1 a 6")

    elif(entrada0 == '2'):    # Menu de Lutador
        print("1 - Cadastrar lutador")
        print("2 - Ver lutadores")
        print("3 - Ver detalhes de lutador -> escolhe um lutador existente")
        entrada1 = input("Insira apenas um algarismo: ")


    elif(entrada0 == '3'):    # Criar torneio aleatorio
        print("Criando Torneio Aleatório...")


    elif(entrada0 == '4'):    # Sair
        break

    else:
        print("Não foi inserida uma opção válida, insira apenas um dos algarismos: 1, 2 ou 3")
