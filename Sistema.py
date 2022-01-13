import os


def imprimeMenuPrincipal():

    '''Funcao que imprime o menu principal que contem as opcoes de comando dentro da plataforma'''
    
    print("\nBem vindo ao sistema da FluxoBus!\n")
    print("Escolha uma das opções abaixo\npara acessar sua respectiva sessão:\n")
    print("1 - Ônibus")
    print("2 - Motoristas")
    print("3 - Fiscais")
    print("4 - Pontos de Parada/Rotas")
    print("5 - Sair do sistema")
    

def imprimeMenuOnibus():

    '''Funcao que imprime o menu que contem as opcoes de comando dentro da sessao dos Onibus'''

    print("Você está no menu dos Ônibus!")
    print("Escolha uma das opções abaixo\npara realizar uma ação:\n")
    print("1 - Criar ônibus")
    print("2 - Mostrar ônibus")
    print("3 - Assignar motorista ao ônibus")
    print("4 - Assignar fiscal ao ônibus")
    print("5 - Alterar dados do ônibus")
    print("6 - Alterar rota do ônibus")
    print("7 - Adicionar ponto de parada ao ônibus")
    print("8 - Deletar ônibus")
    print("9 - Voltar para o Menu principal")


def imprimeMenuMotoristas():

    '''Funcao que imprime o menu que contem as opcoes de comando dentro da sessao dos Motoristas'''

    print("Você está no menu dos Motoristas!")
    print("Escolha uma das opções abaixo\npara realizar uma ação:\n")
    print("1 - Criar motorista")
    print("2 - Mostrar motoristas")
    print("3 - Assignar motorista ao ônibus")
    print("4 - Alterar dados do motorista")
    print("5 - Deletar motorista")
    print("6 - Voltar para o Menu principal")


def imprimeMenuFiscais():

    '''Funcao que imprime o menu que contem as opcoes de comando dentro da sessao dos Fiscais'''

    print("Você está no menu dos Fiscais!")
    print("Escolha uma das opções abaixo\npara realizar uma ação:\n")
    print("1 - Criar fiscal")
    print("2 - Mostrar fiscais")
    print("3 - Assignar fiscal ao ônibus")
    print("4 - Alterar dados do fiscal")
    print("5 - Deletar fiscal")
    print("6 - Voltar para o Menu principal")


def imprimeMenuPontoDeParadaRotas():

    '''Funcao que imprime o menu que contem as opcoes de comando dentro da sessao dos Pontos de Parada e das Rotas'''

    print("Você está no menu dos Pontos de Parada e das Rotas!")
    print("Escolha uma das opções abaixo\npara realizar uma ação:\n")
    print("1 - Criar ponto de parada")
    print("2 - Mostrar rotas")
    print("3 - Adicionar ponto de parada ao ônibus")
    print("4 - Alterar dados da parada")
    print("5 - Alterar rota do ônibus")
    print("6 - Deletar ponto de parada")
    print("7 - Voltar para o Menu principal")  


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#    


def imprimeComandoErrado():

    '''Funcao que imprime uma mensagem de erro caso um comando invalido tenha sido inserido pelo usuario'''

    print('Esse comando não existe :(')
    input('Aperte enter para tentar novamente...')
    limpaTela()


def limpaTela():

    '''Funcao que, por meio do modulo "os", identifica o sistema operacional e executa um comando para limpar o terminal:
    - Windows (os.name = "nt") --> Executa "cls"
    - Linux/Mac OS --> Executa "clear" '''

    if os.name == 'nt':
        comando = 'cls' 
    else:
        comando = 'clear'
    
    os.system(comando)


def criaLoopComandoErrado(string_pergunta_opcoes, qtd_opcoes):

    '''Funcao que, ao receber uma string, correspondente a pergunta e o indice de opcoes de escolha, 
    e a qtd de opcoes de escolha, cria um loop de forma a repetir a interacao com o usuario, 
    caso ele insira um comando invalido, ate que esse insira um comando adequado'''
    
    while True:
        try:
            print()
            print(string_pergunta_opcoes)
            comando = int(input('Opcao: '))

            while comando not in range(qtd_opcoes+1):
                imprimeComandoErrado()
                print(string_pergunta_opcoes)
                comando = int(input('Opcao: '))
            return comando
        except:
            imprimeComandoErrado()

        
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


def interageMenuOnibus(lista_onibus, lista_motoristas_ocupados, lista_motoristas_livres, lista_fiscais_ocupados, lista_fiscais_livres, lista_pontos_parada):

    while True:

        limpaTela()
        imprimeMenuOnibus()
        comando_menu = input("\nOpção: ")
        limpaTela()

        if comando_menu == '1':

            placa = coletaInformacoesCadastroOnibus(lista_onibus)
            
            if placa == None:
                limpaTela()
                continue

            numero_do_onibus = len(lista_onibus) + 1
            exec("Onibus%i = %s" % (numero_do_onibus, "Onibus(placa)"))
            exec("lista_onibus += [Onibus%i]" % numero_do_onibus)

        elif comando_menu == '2':

            imprimeOnibus(lista_onibus)

        elif comando_menu == '3':
            assignaMotoristaOnibus(lista_motoristas_ocupados, lista_motoristas_livres, lista_onibus)
        elif comando_menu == '4':
            assignaFiscalOnibus(lista_fiscais_ocupados, lista_fiscais_livres, lista_onibus)
        elif comando_menu == '5':
            alteraDadosOnibus(lista_onibus)
        elif comando_menu == '6':
            alteraRotaOnibus(lista_onibus)
        elif comando_menu == '7':
            assignaPontoDeParadaOnibus(lista_pontos_parada, lista_onibus)
        elif comando_menu == '8':
            deletaOnibus(lista_onibus)
        elif comando_menu == '9':
            return lista_onibus
            break
        else:
            imprimeComandoErrado()
            continue
        


def interageMenuMotoristas(lista_motoristas_ocupados, lista_motoristas_livres, lista_onibus):

    while True:

        limpaTela()
        imprimeMenuMotoristas()
        comando_menu = input("\nOpção: ")
        limpaTela()

        if comando_menu == '1':

            tupla_nome_cpf = coletaInformacoesCadastroMotorista(lista_motoristas_ocupados, lista_motoristas_livres)

            if tupla_nome_cpf == None:
                limpaTela()
                continue

            numero_do_motorista = len(lista_motoristas_ocupados) + len(lista_motoristas_livres)
            exec("Motorista%i = %s" % (numero_do_motorista, "Motorista(tupla_nome_cpf[0], tupla_nome_cpf[1])"))
            exec("lista_motoristas_livres += [Motorista%i]" % numero_do_motorista)

        elif comando_menu == '2':
            imprimeMotorista(lista_motoristas_ocupados, lista_motoristas_livres)
        elif comando_menu == '3':
            assignaMotoristaOnibus(lista_motoristas_ocupados, lista_motoristas_livres, lista_onibus)
        elif comando_menu == '4':
            alteraDadosMotorista(lista_motoristas_livres, lista_motoristas_ocupados)
        elif comando_menu == '5':
            deletaMotorista(lista_motoristas_livres, lista_motoristas_ocupados)
        elif comando_menu == '6':
            break
        else:
            imprimeComandoErrado()
            continue
  


def interageMenuFiscais(lista_fiscais_ocupados, lista_fiscais_livres, lista_onibus):

    while True:

        limpaTela()
        imprimeMenuFiscais()
        comando_menu = input("\nOpção: ")
        limpaTela()

        if comando_menu == '1':

            tupla_nome_cpf = coletaInformacoesCadastroFiscal(lista_fiscais_ocupados, lista_fiscais_livres)

            if tupla_nome_cpf == None:
                limpaTela()
                continue

            numero_do_fiscal = len(lista_fiscais_ocupados) + len(lista_fiscais_livres)
            exec("Fiscal%i = %s" % (numero_do_fiscal, "Fiscal(tupla_nome_cpf[0], tupla_nome_cpf[1])"))
            exec("lista_fiscais_livres += [Fiscal%i]" % numero_do_fiscal)

        elif comando_menu == '2':
            imprimeFiscal(lista_fiscais_ocupados, lista_fiscais_livres)
        elif comando_menu == '3':
            assignaFiscalOnibus(lista_fiscais_ocupados, lista_fiscais_livres, lista_onibus)
        elif comando_menu == '4':
            alteraDadosFiscal(lista_fiscais_livres, lista_fiscais_ocupados)
        elif comando_menu == '5':
            deletaFiscal(lista_fiscais_livres, lista_fiscais_ocupados)
        elif comando_menu == '6':
            break
        else:
            imprimeComandoErrado()
            continue  



def interageMenuPontoDeParadaRotas(lista_pontos_parada, lista_onibus):

    while True:

        limpaTela()
        imprimeMenuPontoDeParadaRotas()
        comando_menu = input("\nOpção: ")
        limpaTela()

        if comando_menu == '1':

            endereco = coletaInformacoesCadastroPontosDeParada(lista_pontos_parada)
            
            if endereco == None:
                limpaTela()
                continue

            numero_do_ponto_parada = len(lista_pontos_parada) + 1
            exec("PontoParada%i = %s" % (numero_do_ponto_parada, "PontosParada(endereco)"))
            exec("lista_pontos_parada += [PontoParada%i]" % numero_do_ponto_parada)

        elif comando_menu == '2':

            imprimePontosDeParada(lista_pontos_parada)

        elif comando_menu == '3':

            assignaPontoDeParadaOnibus(lista_pontos_parada, lista_onibus)

        elif comando_menu == '4':
            alteraDadosPontoParada(lista_pontos_parada)
        elif comando_menu == '5':
            alteraRotaOnibus(lista_onibus)
        elif comando_menu == '6':
            deletaPontoDeParada(lista_pontos_parada)
        elif comando_menu == '7':
            break
        else:
            imprimeComandoErrado()
            continue



#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

def coletaInformacoesCadastroOnibus(lista_onibus):

    while True:

        print("Vamos começar a cadastrar um novo ônibus:\n")
        placa = input("Placa do onibus: ")
        
        if placa in lista_onibus:
            print("Esse onibus ja esta cadastrado!")
            input("Aperte enter para voltar para o menu...")
            break
        
        limpaTela()

        print(f"Onibus cadastrado com sucesso, veja abaixo:\n\nNome: Onibus {len(lista_onibus)+1}\nPlaca: {placa}\n")
        
        input("Aperte enter para voltar para o menu...")

        return placa



def imprimeOnibus(lista_onibus):

    indice = 1
    for onibus in lista_onibus:
        print(f"Onibus {indice}:")
        print(onibus)
        indice += 1

    input("\nAperte enter para prosseguir...")



def alteraDadosOnibus(lista_onibus):

    imprimeOnibus(lista_onibus)
    onibus_escolhido = int(input("\nDigite o numero do onibus que deseja alterar os dados.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))
    alteracao_placa = input("\nDigite a nova placa do onibus: ")
    limpaTela()

    lista_onibus[onibus_escolhido - 1].placa = alteracao_placa

    print("Os dados do veículo foram alterados com sucesso!")

    input("\nAperte enter para prosseguir...")



def deletaOnibus(lista_onibus):

    imprimeOnibus(lista_onibus)
    onibus_escolhido = int(input("\nDigite o numero do onibus que deseja deletar.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))
    limpaTela()

    del lista_onibus[onibus_escolhido - 1]

    print("O veículo foi deletado com sucesso!")

    input("\nAperte enter para prosseguir...")


def alteraRotaOnibus(lista_onibus):

    imprimeOnibus(lista_onibus)
    onibus_escolhido = int(input("\nDigite o numero do onibus que deseja alterar a rota.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))
    limpaTela()

    comando = input("O que deseja fazer:\n1- Remover os ponto de parada\n2- Adicionar um ponto de parada")
    criaLoopComandoErrado("O que deseja fazer:\n1- Remover um ponto de parada\n2- Adicionar um ponto de parada", 2)

    if comando == 1:
        delattr(lista_onibus[onibus_escolhido - 1], "pontos_de_parada") 

    limpaTela()

    print("A rota foi alterada com sucesso!")

    input("\nAperte enter para prosseguir...")
    
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

def coletaInformacoesCadastroMotorista(lista_motoristas_ocupados, lista_motoristas_livres):

    while True:

        print("Vamos começar a cadastrar um novo motorista:\n")
        nome = input("Nome do motorista: ")
        cpf = input("CPF:")

        if cpf in lista_motoristas_livres or cpf in lista_motoristas_ocupados:
            print("Esse motorista ja esta cadastrado!")
            input("Aperte enter para voltar para o menu...")
            break
        
        limpaTela()

        print(f"Motorista cadastrado com sucesso, veja abaixo:\n\nNome: {nome}\nCPF: {cpf}")
        input("Aperte enter para voltar para o menu...")

        return nome, cpf



def imprimeMotorista(lista_motoristas_ocupados, lista_motoristas_livres):

    lista_geral = lista_motoristas_livres + lista_motoristas_ocupados
    #lista_geral = sorted(lista_geral)
    indice = 1

    for motorista in lista_geral:
        print(f"Motorista {indice}:")
        print(motorista)
        indice += 1

    input("\nAperte enter para prosseguir...")



def assignaMotoristaOnibus(lista_motoristas_ocupados, lista_motoristas_livres, lista_onibus):

    imprimeMotorista(lista_motoristas_ocupados, lista_motoristas_livres)
    motorista_escolhido = int(input("\nDigite o numero do motorista que deseja assignar a um onibus. Ex: 1, caso queira escolher o motorista 1\nEscolhido: "))
    limpaTela()
    
    if motorista_escolhido <= len(lista_motoristas_livres):

        imprimeOnibus(lista_onibus)
        onibus_escolhido = int(input("\nDigite o numero do onibus escolhido.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))

        limpaTela()

        lista_onibus[onibus_escolhido - 1].motorista = lista_motoristas_livres[motorista_escolhido - 1]
        lista_motoristas_ocupados += [lista_motoristas_livres.pop(motorista_escolhido - 1)]

        print("O motorista foi assignado com sucesso!")
        input("\nAperte enter para prosseguir...")

    
    else:
        print("Motorista nao cadastrado ou já assignado a um veículo!")
        input("\nAperte enter para prosseguir...")



def alteraDadosMotorista(lista_motoristas_livres, lista_motoristas_ocupados):

    lista_geral = lista_motoristas_livres + lista_motoristas_ocupados

    imprimeMotorista(lista_motoristas_ocupados, lista_motoristas_livres)
    motorista_escolhido = int(input("\nDigite o numero do motorista que deseja alterar os dados.  Ex: 2, caso queira escolher o motoristas 2\nEscolhido:"))
    alteracao_cpf = input("\nDigite o novo CPF do motorista: ")
    limpaTela()
    alteracao_nome = input("\nDigite o novo nome do motorista: ")

    lista_geral[motorista_escolhido - 1].cpf = alteracao_cpf
    lista_geral[motorista_escolhido - 1].nome = alteracao_nome

    print("Os dados do funcionario foram alterados com sucesso!")

    input("\nAperte enter para prosseguir...")



def deletaMotorista(lista_motoristas_livres, lista_motoristas_ocupados):

    lista_geral = lista_motoristas_livres + lista_motoristas_ocupados

    imprimeMotorista(lista_motoristas_ocupados, lista_motoristas_livres)
    motorista_escolhido = int(input("\nDigite o numero do motorista que deseja deletar.  Ex: 2, caso queira escolher o motorista 2\nEscolhido:"))
    limpaTela()

    del lista_geral[motorista_escolhido - 1]

    print("O funcionario foi deletado com sucesso!")

    input("\nAperte enter para prosseguir...")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

def coletaInformacoesCadastroFiscal(lista_fiscais_ocupados, lista_fiscais_livres):

    while True:

        print("Vamos começar a cadastrar um novo fiscal:\n")
        nome = input("Nome do fiscal: ")
        cpf = input("CPF:")

        if cpf in lista_fiscais_livres or cpf in lista_fiscais_ocupados:
            print("Esse fiscal ja esta cadastrado!")
            input("Aperte enter para voltar para o menu...")
            break
        
        limpaTela()

        print(f"Fiscal cadastrado com sucesso, veja abaixo:\n\nNome: {nome}\nCPF: {cpf}")
        input("Aperte enter para voltar para o menu...")

        return nome, cpf



def imprimeFiscal(lista_fiscais_ocupados, lista_fiscais_livres):

    lista_geral = lista_fiscais_livres + lista_fiscais_ocupados
    #lista_geral = sorted(lista_geral)
    indice = 1

    for fiscal in lista_geral:
        print(f"Fiscal {indice}:")
        print(fiscal)
        indice += 1

    input("\nAperte enter para prosseguir...")



def assignaFiscalOnibus(lista_fiscais_ocupados, lista_fiscais_livres, lista_onibus):

    imprimeFiscal(lista_fiscais_ocupados, lista_fiscais_livres)
    fiscal_escolhido = int(input("\nDigite o numero do fiscal que deseja assignar a um onibus. Ex: 1, caso queira escolher o fiscal 1\nEscolhido: "))
    limpaTela()
    
    if fiscal_escolhido <= len(lista_fiscais_livres):

        imprimeOnibus(lista_onibus)
        onibus_escolhido = int(input("\nDigite o numero do onibus escolhido.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))

        limpaTela()

        lista_onibus[onibus_escolhido - 1].fiscal = lista_fiscais_livres[fiscal_escolhido - 1]
        lista_fiscais_ocupados += [lista_fiscais_livres.pop(fiscal_escolhido - 1)]

        print("O fiscal foi assignado com sucesso!")
        input("\nAperte enter para prosseguir...")

    
    else:
        print("Fiscal nao cadastrado ou já assignado a um veículo!")
        input("\nAperte enter para prosseguir...")



def alteraDadosFiscal(lista_fiscais_livres, lista_fiscais_ocupados):

    lista_geral = lista_fiscais_livres + lista_fiscais_ocupados

    imprimeFiscal(lista_fiscais_ocupados, lista_fiscais_livres)
    fiscal_escolhido = int(input("\nDigite o numero do fiscal que deseja alterar os dados.  Ex: 2, caso queira escolher o fiscal 2\nEscolhido:"))
    alteracao_cpf = input("\nDigite o novo CPF do fiscal: ")
    limpaTela()
    alteracao_nome = input("\nDigite o novo nome do fiscal: ")

    lista_geral[fiscal_escolhido - 1].cpf = alteracao_cpf
    lista_geral[fiscal_escolhido - 1].nome = alteracao_nome

    print("Os dados do funcionario foram alterados com sucesso!")

    input("\nAperte enter para prosseguir...")



def deletaFiscal(lista_fiscais_livres, lista_fiscais_ocupados):

    lista_geral = lista_fiscais_livres + lista_fiscais_ocupados

    imprimeFiscal(lista_fiscais_ocupados, lista_fiscais_livres)
    fiscal_escolhido = int(input("\nDigite o numero do fiscal que deseja deletar.  Ex: 2, caso queira escolher o fiscal 2\nEscolhido:"))
    limpaTela()

    del lista_geral[fiscal_escolhido - 1]

    print("O funcionario foi deletado com sucesso!")

    input("\nAperte enter para prosseguir...")



#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

def coletaInformacoesCadastroPontosDeParada(lista_pontos_parada):

    while True:

        print("Vamos começar a cadastrar um novo ponto de parada:\n")
        endereco = input("Endereco do ponto de parada: ")

        if endereco in lista_pontos_parada:
            print("Esse ponto de parada ja esta cadastrado!")
            input("Aperte enter para voltar para o menu...")
            break
        
        limpaTela()

        print(f"Ponto de parada cadastrado com sucesso, veja abaixo:\n\nEndereco: {endereco}\n")
        input("Aperte enter para voltar para o menu...")

        return endereco



def imprimePontosDeParada(lista_pontos_parada):

    indice = 1

    for ponto_de_parada in lista_pontos_parada:
        print(f"Ponto de parada {indice}:")
        print(ponto_de_parada)
        indice += 1

    input("\nAperte enter para prosseguir...")



def assignaPontoDeParadaOnibus(lista_pontos_parada, lista_onibus):

    imprimePontosDeParada(lista_pontos_parada)
    ponto_de_parada_escolhido = int(input("\nDigite o numero do ponto de parada que deseja assignar a um onibus. Ex: 1, caso queira escolher o ponto de parada 1\nEscolhido: "))
    limpaTela()
    
    if ponto_de_parada_escolhido <= len(lista_pontos_parada):

        imprimeOnibus(lista_onibus)
        onibus_escolhido = int(input("\nDigite o numero do onibus escolhido.  Ex: 2, caso queira escolher o onibus 2\nEscolhido:"))

        limpaTela()

        lista_onibus[onibus_escolhido - 1].pontos_de_parada = lista_pontos_parada[ponto_de_parada_escolhido - 1]

        print("O ponto de parada foi assignado com sucesso!")
        input("\nAperte enter para prosseguir...")

    
    else:
        print("Ponto de parada nao cadastrado!")
        input("\nAperte enter para prosseguir...")



def alteraDadosPontoParada(lista_pontos_parada):

    imprimePontosDeParada(lista_pontos_parada)
    ponto_de_parada_escolhido = int(input("\nDigite o endereco do ponto de parada que deseja alterar os dados.  Ex: 2, caso queira escolher o ponto de parada 2\nEscolhido:"))
    alteracao_endereco = input("\nDigite o novo endereco do ponto de parada: ")
    limpaTela()

    lista_pontos_parada[ponto_de_parada_escolhido - 1].endereco = alteracao_endereco

    print("Os dados do ponto de parada foram alterados com sucesso!")

    input("\nAperte enter para prosseguir...")



def deletaPontoDeParada(lista_pontos_parada):

    imprimePontosDeParada(lista_pontos_parada)
    ponto_parada_escolhido = int(input("\nDigite o numero do ponto de parada que deseja deletar.  Ex: 2, caso queira escolher o ponto de parada 2\nEscolhido:"))
    limpaTela()

    del lista_pontos_parada[ponto_parada_escolhido - 1]

    print("O ponto de parada foi deletado com sucesso!")

    input("\nAperte enter para prosseguir...")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

class Onibus:

    def __init__(self, placa):

        self.placa = placa

    def adicionaMotorista(self, motorista):
        self.motorista = motorista

    def adicionaFiscal(self, fiscal):
        self.fiscal = fiscal

    def adicionaPontosParada(self, pontos_de_parada, preco):
        self.pontos_de_parada = pontos_de_parada
        self.preco = 2.5*len(self.pontos_de_parada)

    def __str__(self):

        try:
            return f"\nPlaca: {self.placa}\n\nMotorista: {self.motorista}\n\nFiscal: {self.fiscal}\n\nRota: {self.pontos_de_parada}\n\nPreco: {self.preco}\n"
        except:
            try:
                return f"\nPlaca: {self.placa}\n\nMotorista: {self.motorista}\n\nFiscal: {self.fiscal}\n"
            except:
                try:
                    return f"\nPlaca: {self.placa}\n\nMotorista: {self.motorista}\n\nRota: {self.pontos_de_parada}\n\nPreco: {self.preco}\n"
                except:
                    try:
                        return f"\nPlaca: {self.placa}\n\nFiscal: {self.fiscal}\n\nRota: {self.pontos_de_parada}\n\nPreco: {self.preco}\n"
                    except:
                        try:
                            return f"\nPlaca: {self.placa}\n\nMotorista: {self.motorista}\n"
                        except:
                            try:
                                return f"\nPlaca: {self.placa}\n\nRota: {self.pontos_de_parada}\n\nPreco: {self.preco}\n"
                            except:
                                 try:
                                    return f"\nPlaca: {self.placa}\n\nFiscal: {self.fiscal}\n"
                                 except:
                                    return f"\nPlaca: {self.placa}"


class Motorista:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"\nNome: {self.nome}\nCPF: {self.cpf}\n"


class Fiscal:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"\nNome: {self.nome}\nCPF: {self.cpf}\n"


class PontosParada:

    def __init__(self, endereco):

        self.endereco = endereco

    def __str__(self):
        return f"\nEndereço: {self.endereco}\n"
        

def main():
    
    lista_onibus = []
    lista_motoristas_ocupados = []
    lista_motoristas_livres = []
    lista_fiscais_ocupados = []
    lista_fiscais_livres = []
    lista_pontos_parada = []

    while True:

        imprimeMenuPrincipal()
        comando_menu = input("\nOpção: ")
        limpaTela()

        if comando_menu == '1':
            interageMenuOnibus(lista_onibus, lista_motoristas_ocupados, lista_motoristas_livres, lista_fiscais_ocupados, lista_fiscais_livres, lista_pontos_parada)
        elif comando_menu == '2':
            interageMenuMotoristas(lista_motoristas_ocupados, lista_motoristas_livres, lista_onibus)
        elif comando_menu == '3':
            interageMenuFiscais(lista_fiscais_ocupados, lista_fiscais_livres, lista_onibus)
        elif comando_menu == '4':
            interageMenuPontoDeParadaRotas(lista_pontos_parada, lista_onibus)
        elif comando_menu == '5':
            break
        else:
            imprimeComandoErrado()
            continue


if __name__ == '__main__':

    main()