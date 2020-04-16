#!/usr/bin/python

'''
So what if we kept track of the current_min_price_so_far and the max_profit_so_far?
'''

# find largest number (max_profit_so_far)
# find smallest (current_min_price)
# check that smallest comes before the largest
# subtract smallest from largest number

# decide on which type of sort to use
# naive solution first - make it work
# optimize


import argparse


def find_max_profit(prices):
    # find largest number (max_profit_so_far)
    for i in range(0, len(prices)-1):
        current_index = i
        smallest = current_index
        largest = current_index + 1
        for j in range(largest, len(prices)):
            if prices[largest] < prices[j]:
                largest = j
        # find smallest (current_min_price)
        for k in range(smallest, largest):
            if prices[smallest] > prices[k]:
                smallest = k
    # subtract largest from smallest number
        return prices[largest] - prices[smallest]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
