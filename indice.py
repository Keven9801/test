INDICE = 12
SOMA = 0
K = 1

print("Passo a passo da soma:")
while K < INDICE:
    print(f"K: {K}, SOMA: {SOMA}")
    K = K + 1
    SOMA = SOMA + K
    print(f"Após incrementar K e somar: K: {K}, SOMA: {SOMA}")

print("\nValor final da soma:", SOMA)
