def eh_numero_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
   
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    
    return False

numero_para_verificar = int(input("Digite um número para verificar se ele está na sequência de Fibonacci: "))

if eh_numero_fibonacci(numero_para_verificar):
    print(f"O número {numero_para_verificar} está na sequência de Fibonacci.")
else:
    print(f"O número {numero_para_verificar} NÃO está na sequência de Fibonacci.")
