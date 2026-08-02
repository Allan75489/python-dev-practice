# Calculadora Cientifica

import math

# =========================
# Operações básicas
# =========================

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Não é possível dividir por zero."


# =========================
# Operações científicas
# =========================

def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def logaritmo(a):
    if a > 0:
        return math.log(a)
    else:
        return "Erro: log definido apenas para números positivos"

def log10(a):
    if a > 0:
        return math.log10(a)
    else:
        return "Erro: log definido apenas para números positivos"

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erro: raiz de número negativo"

def fatorial(a):
    if a >= 0 and int(a) == a:
        return math.factorial(int(a))
    else:
        return "Erro: fatorial apenas para inteiros positivos"

def exponencial(a):
    return math.exp(a)

def porcentagem(a, b):
    return (a / 100) * b

def absoluto(a):
    return abs(a)

def arredondar(a):
    return round(a)


# =========================
# Armazenar dados
# =========================

def armazenar_dados():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    grau_academico = input("Qual o seu nível atual de estudo?: ")
    return nome, idade, grau_academico


# =========================
# Calculadora
# =========================

def calculadora():

    nome, idade, grau_academico = armazenar_dados()

    print(f"\nNome: {nome} | Idade: {idade} | Grau Acadêmico: {grau_academico}")

    while True:

        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Seno")
        print("6. Cosseno")
        print("7. Tangente")
        print("8. Logaritmo natural")
        print("9. Logaritmo base 10")
        print("10. Potência")
        print("11. Raiz Quadrada")
        print("12. Fatorial")
        print("13. Exponencial (e^x)")
        print("14. Porcentagem")
        print("15. Valor Absoluto")
        print("16. Arredondar")
        print("Digite 'sair' para encerrar")

        escolha = input("Opção: ").lower()

        if escolha == "sair":
            print("Encerrando calculadora...")
            break

        if escolha in ["1", "2", "3", "4", "10", "14"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolha == "1":
                print("Resultado:", soma(a, b))
            elif escolha == "2":
                print("Resultado:", subtracao(a, b))
            elif escolha == "3":
                print("Resultado:", multiplicacao(a, b))
            elif escolha == "4":
                print("Resultado:", divisao(a, b))
            elif escolha == "10":
                print("Resultado:", potencia(a, b))
            elif escolha == "14":
                print("Resultado:", porcentagem(a, b))

        elif escolha in ["5","6","7","8","9","11","12","13","15","16"]:
            a = float(input("Digite o valor: "))

            if escolha == "5":
                print("Resultado:", seno(a))
            elif escolha == "6":
                print("Resultado:", cosseno(a))
            elif escolha == "7":
                print("Resultado:", tangente(a))
            elif escolha == "8":
                print("Resultado:", logaritmo(a))
            elif escolha == "9":
                print("Resultado:", log10(a))
            elif escolha == "11":
                print("Resultado:", raiz_quadrada(a))
            elif escolha == "12":
                print("Resultado:", fatorial(a))
            elif escolha == "13":
                print("Resultado:", exponencial(a))
            elif escolha == "15":
                print("Resultado:", absoluto(a))
            elif escolha == "16":
                print("Resultado:", arredondar(a))

        else:
            print("Opção inválida!")


calculadora()