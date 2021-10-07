from os import system

#Class dedicada a trabalhar com a IU

class UI:
    def __init__(self, ops: list):
        self.entrada = ops
        self.ops = ops
        self.colors = {"HEADER": '\033[95m',
                        "OKBLUE": '\033[94m',
                        "OKCYAN": '\033[96m',
                        "OKGREEN": '\033[92m',
                        "WARNING": '\033[33m',
                        "FAIL": '\033[91m',
                        "ENDC": '\033[0m',
                        "BOLD": '\033[1m',
                        "UNDERLINE": '\033[4m'}


    def start(self):
        self.entrada = 0
        system('cls')

        [print(f'{self.ops.index(op) + 1} - {op}\n') for op in self.ops] #For em uma linha, com função de imprimir as opção do usuário
        self.receber_verificar_entrada()

    #Função que verifica se o valor entrado é valido nas opções
    def receber_verificar_entrada(self):
        try:
            self.entrada = int(input('Opção: '))

            if self.entrada > len(self.ops) or self.entrada < 1:
                self.mensagem_color('Valor invalido', self.colors['WARNING'])

        except ValueError:
            self.mensagem_color('Valor invalido', self.colors['WARNING'])

    #Função que imprime mensagens coloridas
    def mensagem_color(self, text: str, color: str):
        print(color + text + self.colors['ENDC'])
        input()