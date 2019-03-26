#!/usr/bin/python

import argparse

def find_max_profit(prices):

  high = prices[0]
  low = prices[0]

  for price in prices:
    if price > high:
      high = price
    elif price < low:
      low = price

  if prices.index(low) < prices.index(high):
    return high - low
  else:
    index = prices.index(high) + 1
    find_max_profit(prices[0:index])




#if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  #parser = argparse.ArgumentParser(description='Find max profit from prices.')
  #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  #args = parser.parse_args()

  #print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


print(find_max_profit([1050, 270, 1540, 3800, 2]))