# Conversor de moedas para o Real (BRL)

def converter_para_real(valor, taxa_cambio):
    return valor * taxa_cambio


print("=== Conversor de Moedas ===")
print("1 - Dólar")
print("2 - Euro")
print("3 - Libra")
print("4 - Iene")

opcao = input("Escolha a moeda que deseja converter (1-4): ")

if opcao == "1":
    valor = float(input("Digite o valor em dólar: "))
    taxa = float(input("Digite a taxa de câmbio do dólar: "))
    resultado = converter_para_real(valor, taxa)
    print(f"US$ {valor:.2f} equivalem a R$ {resultado:.2f}")

elif opcao == "2":
    valor = float(input("Digite o valor em euro: "))
    taxa = float(input("Digite a taxa de câmbio do euro: "))
    resultado = converter_para_real(valor, taxa)
    print(f"€ {valor:.2f} equivalem a R$ {resultado:.2f}")

elif opcao == "3":
    valor = float(input("Digite o valor em libra: "))
    taxa = float(input("Digite a taxa de câmbio da libra: "))
    resultado = converter_para_real(valor, taxa)
    print(f"£ {valor:.2f} equivalem a R$ {resultado:.2f}")

elif opcao == "4":
    valor = float(input("Digite o valor em iene: "))
    taxa = float(input("Digite a taxa de câmbio do iene: "))
    resultado = converter_para_real(valor, taxa)
    print(f"¥ {valor:.2f} equivalem a R$ {resultado:.2f}")

else:
    print("❌ Opção inválida.")