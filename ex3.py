import json

def calcular_estatisticas_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        faturamento_data = json.load(file)
    
    faturamentos_validos = [dia["valor"] for dia in faturamento_data if dia["valor"] not in [None, 0]]

    if not faturamentos_validos:
        print("Não há dias com faturamento válido para calcular as estatísticas.")
        return
    
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    dias_acima_da_media = sum(1 for faturamento in faturamentos_validos if faturamento > media_mensal)
    
    print(f"Menor faturamento em um dia do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento em um dia do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

calcular_estatisticas_faturamento('/Users/helena/Documents/unipe2024-2/tecnicas/python/teste1/dados.json')
