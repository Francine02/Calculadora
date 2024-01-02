#Importando para fazer a raíz quadrada
import math
#Classe calculadora com as operações matemáticas que será utilizada pelo loop

class calculadora ():
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.resposta = 0
        
    def adicao(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 + self.n2
        return self.resposta
    
    def subtracao(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 - self.n2
        return self.resposta
    
    def multiplicacao(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 * self.n2
        return self.resposta
    
    def divisao(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 / self.n2
        return self.resposta
 
    def exponenciacao(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 ** self.n2
        return self.resposta
 
    def resto(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = self.n1 % self.n2
        return self.resposta
    
    def raiz(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resposta = math.sqrt(self.n1 + self.n2)
        return self.resposta

#Função onde fica o menu que irá ser apresentado para o usuário
def menu():
    print('\n -------------')
    print('| CALCULADORA |')
    print(' -------------')
    print('** As opções são: ')
    print('1 - Adição \n'
    '2 - Subtração \n'
    '3 - Multiplicação \n'
    '4 - Divisão \n'
    '5 - Exponenciação \n'
    '6 - Resto \n'
    '7 - Raíz quadrada (da soma dos números) \n'
    '0- Sair ')

#Chamando a classe e a função que irá ser utilizada no loop
calcular=calculadora()
menu()

#Pergunta para o usuário com base no menu
esc = int(input('\n**Escolha uma das opções apresentadas:'))

#Criação de um loop para continuar, caso o usuário escolha uma das opções fornecidas e assim uma das operações da calculadora será executada, ou parar se a opção for desejada
while calcular:
    if esc == 0:
        print('Encerrando...')
        break
    elif esc == 1:
        n1 = int(input('\nDigite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.adicao(n1, n2)
        print(f'**O resultado da adição é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 2:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.subtracao(n1, n2)
        print(f'**O resultado da subtração é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 3:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.multiplicacao(n1, n2)
        print(f'**O resultado da multiplicação é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 4:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.divisao(n1, n2)
        print(f'**O resultado da divisão é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 5:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.exponenciacao(n1, n2)
        print(f'**O resultado da exponenciacão é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 6:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.resto(n1, n2)
        print(f'**O resultado da resto é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))
    elif esc == 7:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
        resposta = calcular.raiz(n1, n2)
        print(f'**O resultado da raíz quadrada é: {resposta}')
        esc = int(input('\nEscolha outra opção:'))