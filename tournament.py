import random

class Lutador:
    vitorias = 0
    derrotas = 0

    def __init__(self, nome, idade, peso, forca, faixa, arte):
        if(isinstance(nome, str) and isinstance(idade, int) and isinstance(peso, int) and isinstance(forca, int) and isinstance(faixa, str) and isinstance(arte, str)):
            self.nome   = nome      # str
            self.idade  = idade     # int
            self.peso   = peso      # int
            self.forca  = forca     # int
            self.faixa  = faixa     # str
            self.arte   = arte      # str
            self.poder  = -peso*forca*(((idade-40)**2)-1600)/1600 # aprox. entre 0-10.000
        else:
            print("ERROR: Lutador __init__", nome, idade, peso, forca, faixa, arte)

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nForca: {self.forca}\nFaixa: {self.faixa}\nArte marcial: {self.arte}'

class Participante:
    vitorias = 0
    derrotas = 0
    
    def __init__(self, lutador, peso_index, faixa):
        if(isinstance(lutador, Lutador) and isinstance(peso, int) and isinstance(faixa, str)):
            self.lutador    = lutador       # Lutador
            self.peso       = peso_index    # int(index(peso))
            self.faixa      = faixa         # str
        else:
            print("ERROR: Participante __init__ lutador, peso_index ou faixa invalido", lutador, peso_index, faixa)


class Torneio:

    def __init__(self, nome, artes, faixas, pesos):
        if(isinstance(faixas, list) and isinstance(pesos, list)): # Verificando parâmetros mais complexos
            for faixa in faixas:
                if(not isinstance(faixa, str)):
                    print("Erro: Torneio __init__ faixa invalida", faixa)
                    return
            
            for peso_1 in pesos:
                if(not isinstance(peso_1, list)):
                    print("Erro: Torneio __init__ peso_1 invalido", peso_1)
                    return
                
                for peso_2 in peso_1:
                    if(not isinstance(peso_2, int)):
                        print("Erro: Torneio __init__ peso_2 invalido", peso_2)
                        return
        else:
            print("Error: Torneio __init__ faixas ou pesos invalidos", faixas, pesos)
            return

        if(isinstance(nome, str) and isinstance(arte, str) and isinstance(faixas, list) and isinstance(pesos, list)):
            self.nome   = nome      # str
            self.arte   = arte      # str
            self.faixas = faixas    # list(str)
            self.pesos  = pesos     # list(list(int,int))
            self.participantes = []
        else:
            print("ERROR: Torneio __init__ nome ou arte invalido", nome, arte)


    def __str__(self):
        text = f'Nome: {self.nome}\nArte marcial: {self.arte}\nFaixa(s):'
        for faixa in self.faixas:
            text += faixa + ", "
        
        text = text[:-2]
        text += "\n Peso(s):"
        for peso_int in pesos:
            text +=  peso_int[0] + '-' + peso_int[1]

        return text

    def addParticipante(self, lutador, peso_index, faixa):
        if(isinstance(lutador, Lutador) and isinstance(peso_index, int) and peso_index <= len(self.pesos) and isinstance(faixa, str)):
            self.participantes.append(Participante(lutador, peso_index, faixa))
        else:
            print("ERROR: Torneio addParticipante", lutador, peso_index, faixa)

    def ordParticipantes(self):
        indiceMax = 0
        indice = 0
        while(indice < len(self.participantes) - 1): # O indice vai crescendo porém após mudanças ele volta
            if(self.participantes[indice].vitorias > self.participantes[indice+1].vitorias): # Caso mais comum
                indiceMax += 1
                indice = indiceMax
                continue

            if(self.participantes[indice].vitorias < self.participantes[indice+1].vitorias):
                var = self.participantes[indice]
                self.participantes[indice] = self.participantes[indice + 1]
                self.participantes[indice + 1] = var
                indice -= 1

            elif(self.participantes[indice].derrotas < self.participantes[indice+1].derrotas):
                indiceMax += 1
                indice = indiceMax
                continue

            elif(self.participantes[indice].derrotas > self.participantes[indice+1].derrotas):
                var = self.participantes[indice]
                self.participantes[indice] = self.participantes[indice + 1]
                self.participantes[indice + 1] = var
                indice -= 1

            elif(self.participantes[indice].lutador.poder > self.participantes[indice].lutador.poder): # Em um confronto direto quem tem mais poder vence
                var = self.participantes[indice]
                self.participantes[indice] = self.participantes[indice + 1]
                self.participantes[indice + 1] = var
                indice -= 1
            
            else:
                indiceMax += 1
                indice = indiceMax

            if(indice == -1):
                indice = 1

        return self.participantes

    def realizarLuta(self, participanteA, participanteB):
        if(isinstance(participanteA, Participante) and isinstance(participanteB, Participante)):
            if(participanteA.lutador.poder > participanteB.lutador.poder):
                participanteA.vitorias += 1
                participanteB.derrotas += 1
                vitorioso = participanteA
            else:
                participanteB.vitorias += 1
                participanteA.derrotas += 1            
                vitorioso = participanteB
            
            return vitorioso


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
        print("\nMENU DE TORNEIO:")
        print("1 - Criar torneio")
        print("2 - Inscrever lutador")
        print("3 - Ver torneios existentes")
        print("4 - Ver ranking de torneio")
        print("5 - Ver lutadores inscritos em torneio")
        print("6 - Realizar luta")
        entrada1 = input("Insira apenas um algarismo: ")

        if(entrada1 == '1'):    # Criar Torneio
            print("\nCRIAR TORNEIO:")
            
            print("\nInsira um nome para o torneio:")
            nome = input().capitalize()

            print("\nInsira a arte marcial do torneio:")
            arte = input().capitalize()
            
            faixas = []
            print("\nDeseja incluir categoria faixa livre?")
            faixa_livre = input("Insira 's' para sim e 'n' para não, sem as aspas: ")
            if(faixa_livre == 's'):
                faixas.append("Livre")

            print("\nPara escolha das faixas, insira uma faixa e pressione Enter:")
            faixa = input().capitalize()
            while (faixa != ''):
                if(faixa in faixas):
                    print("Essa faixa já está inclusa no torneio")
                else:
                    faixas.append(faixa)
                print("Insira a proxima faixa, para terminar pressione Enter com o campo vazio:")
                faixa = input().capitalize()
            
            pesos = []
            print("\nEscolha os intervalos de pesos:")
            print("Insira o valor menor do intervalo:")
            menor = input()
            while(menor != ''):
                try:
                    menor = int(menor)
                except:
                    print("Erro: Não foi inserido um peso válido")
                    continue

                print("Insira o valor maior do intervalo:")
                
                try:
                    maior = int(input())
                except:
                    print("Erro: Não foi inserido um peso válido")
                    continue

                print()

                if(menor <= maior):
                    pesos.append([menor,maior])
                else:
                    print("Erro: Não foi inserido um intervalo válido")
                    continue

                print("Insira o valor menor do intervalo ou enter para terminar:")
                try:
                    menor = input()
                except:
                    print("Erro: Não foi inserido um peso válido")
                    menor = ''
                

            torneios.append(Torneio(nome, arte, faixas, pesos))
            print("Torneio adicionado com sucesso!\n")

        elif(entrada1 == '2'):  # Inscrever Lutador
            numLutadores = len(lutadores)
            if(numLutadores < 1):
                print("Você primeiro precisa cadastrar um lutador")
                continue

            print("\nINSCREVER LUTADOR:")

            print("\nSelecione um dos lutadores:")
            for c in range(len(lutadores)):
                print(str(c) + " - " + lutadores[c].nome)
            
            try:
                num = int(input("Insira o número do lutador: "))
                lutador = lutadores[num]
            except:
                print("Erro: Não foi insetido um valor válido")
                continue

            print("\nSelecione um dos torneios:")
            torneios_possiveis = []
            for c in range(len(torneios)):
                if(torneios[c].arte == lutador.arte):
                    print(str(len(torneios_possiveis)) + " - " + torneios[c].nome)
                    torneios_possiveis.append(c)
            
            try:
                num = int(input("Insira o número do torneio: "))
                torneio = torneios[torneios_possiveis[num]]
            except:
                print("Erro: Não foi insetido um valor válido")
                continue

            pular = False
            for part in torneio.participantes:
                if(part.lutador == lutador):
                    print("Este lutador já está participando deste torneio")
                    pular = True
                    break
            if(pular):
                continue

            opcoes_peso = []
            for c in range(len(torneio.pesos)):
                if(torneio.pesos[c][0] <= lutador.peso and torneio.pesos[c][1] >= lutador.peso):
                    dic_pesos = {"texto": str(torneio.pesos[c][0]) + " - " + str(torneio.pesos[c][1]), "index": c}
                    opcoes_peso.append(dic_pesos)
            
            if(len(opcoes_peso) == 0):
                print("O peso deste lutador não é aceito por este torneio.")
            
            else:
                opcoes_faixa = []
                if(lutador.faixa in torneio.faixas):
                    opcoes_faixa.append(lutador.faixa)

                if("Livre" in torneio.faixas):
                    opcoes_faixa.append("Livre")

                if(len(opcoes_faixa) == 0):
                    print("O faixa deste lutador não é aceita por este torneio.")

                else:
                    print("AAA")
                    print(opcoes_peso)
                    if(len(opcoes_peso) == 1):
                        print("\nIntervalo de pesos selecionado: " + dic_pesos["texto"])
                        peso_index = opcoes_peso[0]["index"] # outra opcao -> dic_pesos["index"]
                    
                    else:
                        print("\nSelecione o intervalo de pesos desejado:")
                        for c in range(len(opcoes_peso)):
                            print(str(c) + " - " + opcoes_peso[c]["texto"])
                        
                        try:
                            num = int(input("Insira o numero da opção: "))
                        except:
                            print("Não foi inserido um numero válido")
                            continue

                        peso_index = opcoes_peso[num]["index"]
                    

                    if(len(opcoes_faixa) == 1):
                        print("\nFaixa selecionada: " + opcoes_faixa[0])

                    else: 
                        print("\nSelecione a faixa desejada:")
                        for c in range(len(opcoes_faixa)):
                            print(str(c) + " - " + opcoes_faixa[c])
                        
                        try:
                            num = int(input("Insira o numero da opção: "))
                        except:
                            print("Não foi inserido um numero válido")
                            continue

                        faixa = opcoes_faixa[num]          
                      
                    torneio.addParticipante(lutador, peso_index, faixa)            

        elif(entrada1 == '3'):  # Torneios Existentes
            if(len(torneios) < 1):
                print("Não há torneios existentes")
                continue

            print("\nTORNEIOS EXISTENTES:")
            print("Nome \t\t|\t Arte-marcial")
            for torneio in torneios:
                print(torneio.nome, " \t|\t", torneio.arte)

        elif(entrada1 == '4'):  # Ranking Torneio
            if(len(torneios) < 1):
                print("Você primeiro precisa criar um torneio")
                continue

            print("\nRANKING DE TORNEIO:")
            
            print("\nSelecione um torneio:")
            
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)

            try:    
                num = int(input("Insira o numero do torneio: "))
                participantes = torneios[num].ordParticipantes()
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

            print("Nome \t\t\t V/D")
            for part in participantes:
                print(part.lutador.nome + "\t\t" + str(part.vitorias) + "/" + str(part.derrotas))

        elif(entrada1 == '5'):  # Lutadores Inscritos
            print("\nLUTADORES INSCRITOS:")
            print("\nSelecione um torneio:")
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)
                
            try:
                num = int(input("Insira o numero do torneio: "))    
                for part in torneios[num].participantes:
                    print(part.lutador.nome)
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

        elif(entrada1 == '6'):  # Realizar luta
            if(len(torneios) < 1):
                print("Não há torneios disponíveis")

            print("\nREALIZAR LUTA:")
            print("\nSelecione um torneio:")
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)

            try:    
                num = int(input("Insira o numero do torneio: "))
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

            if(num >= len(torneios)):
                print("Id de torneio inválido")
                continue

            if(len(torneios[num].participantes) < 2):
                print("Este toneio não possui participantes suficientes")

            print("\nEscolha os participantes:")
            for c in range(len(torneios[num].participantes)):
                print(str(c) + " - " + torneios[num].participantes[c].lutador.nome)

            try:
                part1 = int(input("Insira o numero do primeiro participante: "))
            except:
                print("Numero de participante inválido")
                continue
            
            print("Participantes da mesma categoria de " + torneios[num].participantes[part1].lutador.nome)

            faixa = torneios[num].participantes[part1].faixa
            peso = torneios[num].participantes[part1].peso
            indices_validos = []
            for c in range(len(torneios[num].participantes)):
                if(torneios[num].participantes[c].faixa == faixa and torneios[num].participantes[c].peso == peso and c != part1):
                    print(str(c) + " - " + torneios[num].participantes[c].lutador.nome)
                    indices_validos.append(c)
                else:
                    print(str(c))

            if(len(indices_validos) == 0):
                print("Não há outros participantes na mesma categoria de " + torneios[num].participantes[part1].lutador.nome)
                continue

            try:
                part2 = int(input("Insira o numero do segundo participante: "))
                p1 = torneios[num].participantes[part1] 
                p2 = torneios[num].participantes[part2]
                if(part2 not in indices_validos):
                    print("Os participantes devem pertencer a mesma categoria de peso e faixa")
                    continue
            except:
                print("Numero de participante inválido")
                continue

            vitorioso = torneios[num].realizarLuta(p1, p2)
            print("E " + vitorioso.lutador.nome + " vence o confronto!!")

        else:
            print("Não foi inserida uma opção válida, insira apenas um algarismo de 1 a 6")

    elif(entrada0 == '2'):    # Menu de Lutador
        print("1 - Cadastrar lutador")
        print("2 - Ver lutadores")
        print("3 - Ver detalhes de lutador")
        entrada1 = input("Insira o numero da opção: ")

        if(entrada1 == '1'):    # Cadastrar Lutador
            print("\nCADASTRAR LUTADOR:")

            print("\nInsira o nome do lutador:")
            nome = input().capitalize()

            pular = False
            for lutador in lutadores:
                if(lutador.nome == nome):
                    print("Já existe um lutador com este nome:")
                    pular = True
                    break
            if(pular):
                continue

            print("\nInsira a idade do lutador:")
            try:
                idade = int(input())
            except:
                print("Não foi inserida uma idade válida")
                continue

            if(idade < 0):
                print("O valor de idade deve ser positivo")

            print("\nInsira o peso do lutador:")
            try:
                peso = int(input())
            except:
                print("Não foi inserida um peso válido")
                continue

            print("\nInsira a forca do lutador:")
            try:
                forca = int(input())
            except:
                print("Não foi inserida uma forca válida")
                continue
            
            print("\nInsira a faixa do lutador")
            faixa = input().capitalize()

            print("\nInsira a arte marcial do lutador:")
            arte = input().capitalize()

            lutadores.append(Lutador(nome, idade, peso, forca, faixa, arte))
            print("Lutador adicionado com sucesso!\n")

        elif(entrada1 == '2'):  # Ver nome dos lutadores
            print("\nVER LUTADORES:")
            for lutador in lutadores:
                print(lutador.nome)

        elif(entrada1 == '3'):  # Detalhes lutador
            print("\nVER DETALHES DE LUTADOR:")
            print("\nSelecione um dos lutadores:")
            for c in range(len(lutadores)):
                print(str(c) + " - " + lutadores[c].nome)
            
            num = int(input("Insira o numero do lutador:"))
            print(lutadores[num])

        else:
            print("Não foi inserida uma opção válida, insira apenas um algarismo de 1 a 3")

    elif(entrada0 == '3'):    # Criar torneio aleatorio
        print("Criando Torneio Aleatório...")

        possiveis_nomes_torneio = ["Os Faixa Preta", "Vem pro X1", "O Melhor da Rua", "Trocação de Soco", "Cai na mão", "Torneio Mundial", "World Championship", "Rei do Ringue", "10min sem perder a amizade"]
        
        possiveis_artes = ["Jiu-jitsu", "Kung Fu", "Muay Thai", "Karate", "Capoeira", "Judo", "Tae Kwon Do", "Boxe", "Ninjutsu"]
        possiveis_faixas = ["Branca", "Cinza", "Azul", "Amarela", "Laranja", "Verde", "Roxa", "Marrom", "Preta"]

        possiveis_nomes_lutador = ["John", "Naruto", "Amanda", "Sakura", "Saitama", "Ryu", "Chun-Li", "Akuma", "Cammy", "Sagat", "Guile", "Goku", "Vegeta", "Bulma", "Mestre", "Itachi", "Madara"]
        possiveis_sobrenomes_lutador = ["Cena", "Uzumaki", "Nunes", "Haruno", "Silva", "Alves", "Ferreira", "Kami", "Tanaka", "Watanabe", "Yamamoto", "Uchiha"]

        var = random.randint( 0, len(possiveis_nomes_torneio) - 1)
        nome_torneio = possiveis_nomes_torneio[var]

        var = random.randint(1, len(possiveis_artes) - 1)
        arte = possiveis_artes[var]

        numFaixas = len(possiveis_faixas)
        faixas = []
        for c in range(random.randint(1, 5)):   # 1 a n categorias de faixas
            var = random.randint( 0, numFaixas - 1 - c)
            faixas.append(possiveis_faixas[var])
            possiveis_faixas.pop(var)

        pesos = []
        for c in range(random.randint(1, 5)):   # 1 a 5 categorias de peso
             peso_menor = random.randint(40, 100)
             peso_maior = peso_menor + random.randint(5, 40)
             pesos.append([peso_menor, peso_maior])
        
        torneios.append(Torneio(nome_torneio, arte, faixas, pesos))    # criação do torneio
        print("Torneio aleatório criado com sucesso!")
        print("Criando Lutadores...")

        nomes_adicionados = []
        for _ in range(random.randint(4, 12)):  # 4 a 12 lutadores por torneio
            var = random.randint(0, len(possiveis_nomes_lutador) - 1)
            nome_lutador = possiveis_nomes_lutador[var]
            var = random.randint(0, len(possiveis_sobrenomes_lutador) - 1)
            nome_lutador += " " + possiveis_sobrenomes_lutador[var]
            
            if(nome_lutador in nomes_adicionados):  # Não cria 2 lutadores com mesmo nome
                continue
                
            nomes_adicionados.append(nome_lutador)

            idade = random.randint(8, 80)   # idade entre 8 e 80 (inclusive)

            peso_index = random.randint(0, len(pesos) - 1)
            peso = random.randint(pesos[peso_index][0], pesos[peso_index][1])

            forca = random.randint(1, 10000)  # forca entre 1 e 10000

            var = random.randint(0, len(faixas) - 1)
            faixa = faixas[var]

            lutadores.append(Lutador(nome_lutador, idade, peso, forca, faixa, arte))

            torneios[-1].addParticipante(lutadores[-1], peso_index, faixa)

            print("Lutador " + nome_lutador + " adicionado!")

        print("O torneio foi criado e os lutadores adicionados!")

    elif(entrada0 == '4'):    # Fecha o programa
        break

    else:
        print("Não foi inserida uma opção válida, insira apenas um algarismos de 1 a 4")
