# conversor de unidade simples

def converter_unidade(valor, unidade_origem, unidade_destino):
    # dicionário de conversão (base: metro)
    conversores = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144
    }

    unidade_origem = unidade_origem.lower()
    unidade_destino = unidade_destino.lower()

    if unidade_origem not in conversores or unidade_destino not in conversores:
        raise ValueError("Unidade de origem ou destino inválida")

    valor_em_metros = valor * conversores[unidade_origem]
    return valor_em_metros / conversores[unidade_destino]


# ===== PROGRAMA PRINCIPAL =====
try:
    print("=== Conversor de Unidades ===")

    valor = float(input("Digite o valor: "))
    origem = input("Unidade de origem (m, cm, mm, km, in, ft, yd): ")
    destino = input("Unidade de destino (m, cm, mm, km, in, ft, yd): ")

    resultado = converter_unidade(valor, origem, destino)

    print(f"\nResultado: {valor} {origem} = {resultado:.4f} {destino}")

except ValueError as e:
    print(f"Erro: {e}")
except Exception:
    print("Entrada inválida. Tente novamente.")