import datetime
import pandas as pd

# Função para calcular a média móvel simples (SMA)
def sma(data, window):
    return data.rolling(window=window).mean()

# Função para verificar a condição de entrada
def verificar_condicao_de_entrada(data, window1, window2):
    last_close = data['Close'].iloc[-1]
    sma1 = sma(data['Close'], window1).iloc[-1]
    sma2 = sma(data['Close'], window2).iloc[-1]
    return last_close > sma1 and last_close > sma2 and sma1 > sma2

# Função para executar a estratégia de scalping
def executar_estrategia_scalping(data, window1, window2):
    capital_inicial = 10000 # Capital inicial
    capital = capital_inicial
    posicao_aberta = False # Indica se há uma posição aberta
    preco_compra = 0 # Preço de compra da posição
    lucro_total = 0 # Lucro total
    comissao = 0.5 # Valor da comissão por contrato negociado

    for i in range(len(data)):
        if verificar_condicao_de_entrada(data.iloc[:i+1], window1, window2) and not posicao_aberta:
            # Condição de entrada satisfeita e não há posição aberta, abrir posição comprada
            posicao_aberta = True
            preco_compra = data['Close'].iloc[i]
            capital -= preco_compra + comissao

        elif posicao_aberta and data['Close'].iloc[i] > preco_compra + 10:
            # Posição aberta e preço atual maior que preço de compra + 10 pontos, fechar posição vendida
            posicao_aberta = False
            preco_venda = data['Close'].iloc[i]
            capital += preco_venda - comissao
            lucro_total += preco_venda - preco_compra - (comissao * 2)

    lucro_total += capital - capital_inicial
    return lucro_total

# Carregar dados históricos do mini índice (exemplo utilizando dados fictícios)
data = pd.DataFrame({'Date': pd.date_range(start='2022-01-01', end='2022-04-14', freq='B'),
                     'Open': [120000, 121000, 122000, 122500, 122300, 122100, 121500, 122200, 122800, 122900, 122800, 123200, 123100, 123000, 122700, 122800],
                     'High': [121500, 122500, 123000, 123000, 123000, 122800, 122600, 123300, 123100, 123100, 123200, 123400, 
