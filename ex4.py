def calcular_percentual_representacao(faturamentos):
    total_faturamento = sum(faturamentos.values())
    percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamentos.items()}
    return percentuais

faturamentos_mensais = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais_representacao = calcular_percentual_representacao(faturamentos_mensais)

for estado, percentual in percentuais_representacao.items():
    print(f"{estado}: {percentual:.2f}%")
