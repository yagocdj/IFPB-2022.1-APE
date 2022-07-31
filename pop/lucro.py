# Questão "lucro"

n = int(input())  # quantidade de números mostrados pelo CEO
stock_prices = list(map(int, input().split()))
highest_profit = 0

# Percorrendo os valores
for i in range(n):
    buy_price = stock_prices[i]
    # Comparando o valor de compra com os possíveis valores de venda
    for j in range(i + 1, n):
        sell_price = stock_prices[j]
        profit = sell_price - buy_price
        if profit > highest_profit:
            highest_profit = profit

# TEMPO EXCEDIDO (TLE)

print(highest_profit)
