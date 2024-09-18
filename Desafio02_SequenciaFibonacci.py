'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''


def verificar_fibonacci(n):
    # Função para criar a sequencia de Fibonacci
    def fibonacci(n):
        sequencia = [0, 1]
        while sequencia[-1] < n:
            sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia

    # Chama a função para gerar a sequencia Fibonacci
    Fibonacci = fibonacci(n)

    # Verificando se o numero de entrada pertence a sequencia
    if n in Fibonacci:
        print(f'O número {n} pertence a sequência!')
    else:
        print(f'O número {n} não pertence a sequência!')


# Solicitando o numero de entrada para criar a sequencia e verificar se o mesmo pertence a sequencia de Fibonacci
num = int(input("Digite um número para criar uma sequência de Fibonacci e descobrir se ele pertence a sequência: "))
verificar_fibonacci(num)
