def is_fibonacci_number(num):
    if num < 0:
        return False

    # Função para gerar a sequência de Fibonacci até um número limite
    def generate_fibonacci(limit):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < limit:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    # Gerar sequência de Fibonacci até o número informado
    fibonacci_sequence = generate_fibonacci(num)

    # Verificar se o número está na sequência de Fibonacci
    if num in fibonacci_sequence:
        return True
    else:
        return False

# Entrada do usuário
num = int(input("Informe um número: "))

# Verificar se o número pertence à sequência de Fibonacci
if is_fibonacci_number(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
