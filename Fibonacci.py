def fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Ingrese el número hasta el cual desea generar la secuencia de Fibonacci: "))

for i in range(num):
    print(fibonacci(i))
