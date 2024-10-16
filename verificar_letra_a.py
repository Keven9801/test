def verificar_letra_a(string):
    # Contar a ocorrência de 'a' e 'A'
    count_a = string.count('a')
    count_A = string.count('A')
    
    # Somar as ocorrências de 'a' e 'A'
    total_count = count_a + count_A
    
    # Verificar se a letra 'a' está presente na string
    if total_count > 0:
        print(f"A letra 'a' (ou 'A') ocorre {total_count} vezes na string.")
    else:
        print("A letra 'a' (ou 'A') não está presente na string.")

# Exemplo de uso
string = input("Informe uma string: ")
verificar_letra_a(string)
