from pycoingecko import CoinGeckoAPI

def main(n):
  cg = CoinGeckoAPI()
  coins = cg.get_coins()
  result = []
  for i in range(n):
    j = coins[i]
    result.append(j["name"])
  return result