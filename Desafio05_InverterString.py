''' 5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

palavra = input("Digite uma Palavra para Inverte-la: ")


# Função que inverte uma string dada
def inverter_string(texto):
    return texto[::-1]


print(inverter_string(palavra))

