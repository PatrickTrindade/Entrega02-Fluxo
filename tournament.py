import random

class Lutador:
    vitorias = 0
    derrotas = 0

    def __init__(self, nome, idade, peso, forca, faixa, arte):
        if(isinstance(nome, str) and isinstance(idade, int) and isinstance(peso, int) and isinstance(forca, int) and isinstance(faixa, str) and isinstance(arte, str)):
            self.nome   = nome
            self.idade  = idade
            self.peso   = peso
            self.forca  = forca
            self.faixa  = faixa
            self.arte   = arte
            self.poder  = peso*forca/(idade+10)
        else:
            print("ERROR: Lutador __init__", nome, idade, peso, forca, faixa, arte)


    def __str__(self):
        return 'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nForca: {self.forca}\nFaixa: {self.faixa}\nArte marcial: {self.arte}'

class Participante:
    vitorias = 0
    derrotas = 0
    
    def __init__(self, lutador, peso_index, faixa):
        self.lutador    = lutador       # Lutador
        self.peso       = peso_index    # int(index(peso))
        self.faixa      = faixa         # str



class Torneio:
    participantes = [] # lista de Participantes

    def __init__(self, nome, artes, faixas, pesos):
        if(isinstance(nome, str) and isinstance(artes, list) and isinstance(faixas, list) and isinstance(pesos, list)):
            self.nome   = nome      # str
            self.arte   = arte      # str
            self.faixas = faixas    # list(str)
            self.pesos  = pesos     # list(list(int,int))
        else:
            print("ERROR: Torneio __init__", nome, artes, faixas, pesos)


    def __str__(self):
        text = 'Nome: {self.nome}\nArte marcial: {self.arte}\nFaixa(s):'
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
        indice = 0
        while(indice < len(self.participantes)): # O indice vai crescendo porém após mudanças ele volta
            if(self.participantes[indice].vitorias > self.participantes[indice+1].vitorias): # Caso mais comum
                indice += 1
                continue

            if(self.participantes[indice].vitorias < self.participantes[indice+1].vitorias):
                var = self.participantes[indice]
                self.participantes[indice] = self.participantes[indice + 1]
                self.participantes[indice + 1] = var
                indice -= 1

            elif(self.participantes[indice].derrotas < self.participantes[indice+1].derrotas):
                indice += 1
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

            return self.participantes

    def realizarLuta(self, participanteA, participanteB):
        if(isinstance(participanteA, Participante) and isinstance(participanteB, Participante)):
            if(participanteA.poder > participanteB.poder):
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

            print("\nInsira a arte marcial do torneio:")
            arte = input()
            
            faixas = []
            print("\nPara escolha das faixas, insira uma faixa e pressione Enter:")
            faixa = input()
            while (faixa != ''):
                faixas.append(faixa)
                print("Insira a proxima faixa, para terminar pressione Enter com o campo vazio:")
                faixa = input()
            
            print("\nDeseja incluir categoria livre?")
            faixa_livre = input("Insira 's' para sim e 'n' para não, sem as aspas: ")
            if(faixa_livre == 's'):
                faixas.append("Livre")

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

        elif(entrada1 == '2'):
            print("INSCREVER LUTADOR:")

            numLutadores = len(lutadores)
            if(numLutadores < 1):
                print("Você primeiro precisa cadastrar um lutador")
                continue

            print("\nSelecione um dos lutadores:")
            for c in range(len(lutadores)):
                print(str(c) + " - " + lutadores[c].nome)
            
            try:
                num = int(input("Insira o número do lutador:"))
                lutador = lutadores[num]
            except:
                print("Erro: Não foi insetido um valor válido")
                continue

            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)
            
            try:
                num = int(input("Insira o número do torneio:"))
                torneio = torneios[num]
            except:
                print("Erro: Não foi insetido um valor válido")
                continue

            opcoes_peso = []
            for c in range(len(torneio.pesos)):
                if(torneio.pesos[c][0] <= lutador.peso and torneio.pesos[c][1] >= lutador.pesos):
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
                    if(len(opcoes_peso) == 1):
                        print("\nIntervalo de pesos selecionado: " + dic_pesos["texto"])
                        peso_index = opcoes_peso[0]["index"] # outra opcao -> dic_pesos["index"]
                    
                    else:
                        print("\nSelecione o intervalo de pesos desejado:")
                        for c in range(len(opcoes_peso)):
                            print(str(c) + " - " + opcoes_peso[c]["texto"])
                        
                        num = input("Insira o numero da opção: ")
                        peso_index = opcoes_peso[num]["index"]
                    

                    if(len(opcoes_faixa) == 1):
                        print("\nFaixa selecionada: " + opcoes_faixa[0])

                    else: 
                        print("\nSelecione a faixa desejada:")
                        for c in range(len(opcoes_faixa)):
                            print(str(c) + " - " + opcoes_faixa[c])
                        
                        num = input("Insira o numero da opção: ")
                        faixa = opcoes_faixa[num]          
                      
                    torneio.addParticipante(lutador, peso_index, faixa)            

        elif(entrada1 == '3'):
            print("TORNEIOS EXISTENTES:")
            for torneio in torneios:
                print(torneio.nome)

        elif(entrada1 == '4'):
            print("RANKING DE TORNEIO:")
            print("\nSelecione um torneio:")
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)

            try:    
                num = int(input("Insira o numero do torneio: "))
                participantes = torneios[num].ordParticipantes()
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

            print("Nome \t\t V/D")
            for part in participantes:
                print(part.lutador.nome + "\t\t" + str(part.vitorias) + "/" + str(part.derrotas))

        elif(entrada1 == '5'):
            print("LUTADORES INSCRITOS:")
            print("\nSelecione um torneio:")
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)
                
            try:
                num = int(input("Insira o numero do torneio: "))    
                for part in torneios[num].participantes:
                    print(part.nome)
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

        elif(entrada1 == '6'):
            print("REALIZAR LUTA:")
            print("\nSelecione um torneio:")
            for c in range(len(torneios)):
                print(str(c) + " - " + torneios[c].nome)

            try:    
                num = int(input("Insira o numero do torneio: "))
            except:
                print("Erro: Não foi inserido um valor válido")
                continue

            print("\nEscolha os participantes:")
            for c in range(len(torneios[num].participantes)):
                print(str(c) + " - " + torneios[num].participantes[c].nome)

            part1 = input("Insira o numero do primeiro participante")
            part2 = input("Insira o numero do segundo participante")

            if(part1 >= c or part2 >= c or part1 < 0 or part2 < 0): # c = quantidade de participantes no torneio
                print("Numero de participante inválido")
                continue
            
            p1 = torneios[num].participantes[part1] 
            p2 = torneios[num].participantes[part2]

            torneios[num].realizarLuta(p1, p2)

        else:
            print("Não foi inserida uma opção válida, insira apenas um algarismo de 1 a 6")

    elif(entrada0 == '2'):    # Menu de Lutador
        print("1 - Cadastrar lutador")
        print("2 - Ver lutadores")
        print("3 - Ver detalhes de lutador -> escolhe um lutador existente")
        entrada1 = input("Insira o numero da opção: ")

        if(entrada1 == '1'):
            print("CADASTRAR LUTADOR:")

            print("\nInsira o nome do lutador:")
            nome = input()

            print("\nInsira a idade do lutador:")
            idade = input()

            print("\nInsira o peso do lutador:")
            peso = input()

            print("\nInsira a forca do lutador:")
            forca = input()

            print("\nInsira a faixa do lutador")
            faixa = input()

            print("\nInsira a arte marcial do lutador:")
            arte = input()

            lutadores.append(Lutador(nome, idade, peso, forca, faixa, arte))
            print("Lutador adicionado com sucesso!\n")

        elif(entrada1 == '2'):    # Printa o nome dos lutadores
            print("VER LUTADORES:")
            for lutador in lutadores:
                print(lutador.nome)

        elif(entrada1 == '3'):    # Seleciona um lutador para printar seus atributos
            print("VER DETALHES DE LUTADOR:")
            print("\nSelecione um dos lutadores:")
            for c in range(len(lutadores)):
                print(c + " - " + lutadores[c].nome)
            
            num = int(input("Insira o numero do lutador:"))
            print(lutadores[num])

        else:
            print("Não foi inserida uma opção válida, insira apenas um algarismo de 1 a 3")

    elif(entrada0 == '3'):    # Criar torneio aleatorio
        print("Criando Torneio Aleatório...")

        possiveis_nomes_torneio = ["Os Faixa Preta", "Vem pro X1", "O Melhor da Rua", "Trocação de Soco", "Cai na mão", "Torneio Mundial", "World Championship", "Rei do Ringue"]
        
        possiveis_artes = ["Jiu-jitsu", "Kung Fu", "Muay Thai", "Karate", "Capoeira", "Judo", "Tae Kwon Do", "Boxe", "Ninjutsu"]
        possiveis_faixas = ["Branca", "Cinza", "Azul", "Amarela", "Laranja", "Verde", "Roxa", "Marrom", "Preta"]

        possiveis_nomes_lutador = ["John", "Naruto", "Amanda", "Sakura", "Saitama", "Ryu", "Chun-Li", "Cammy", "Goku"]
        possiveis_sobrenomes_lutador = ["Cena", "Uzumaki", "Nunes", "Haruno", "Silva", "Alves", "Ferreira"]

        var = random.randint( 0, len(possiveis_nomes_torneio) - 1)
        nome_torneio = possiveis_nomes_torneio[var]

        var = random.randint(1, len(possiveis_artes) - 1)
        arte = possiveis_artes[var]

        numFaixas = len(possiveis_faixas)
        faixas = []
        for c in range(random.randint(1, numFaixas)):   # 1 a n categorias de faixas
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

        for _ in range(random.randint(4, 10)):  # 4 a 10 lutadores por torneio
            var = random.randint(0, len(possiveis_nomes_lutador) - 1)
            nome_lutador = possiveis_nomes_lutador[var]
            var = random.randint(0, len(possiveis_sobrenomes_lutador) - 1)
            nome_lutador += " " + possiveis_sobrenomes_lutador[var]

            idade = random.randint(8, 80)   # idade entre 8 e 80 (inclusive)

            peso_index = random.randint(0, len(pesos) - 1)
            peso = random.randint(pesos[peso_index][0], pesos[peso_index][1])

            forca = random.randint(1, 100)  # forca entre 1 e 100

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
