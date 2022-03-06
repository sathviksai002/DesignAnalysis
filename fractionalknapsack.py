""" parameters:
1. capacity of the bag to fill the items
2. Weight of all the products
3. Profit of all the products
4. No. of items for the bag
we need to consider the profit/weight which is more
"""


def knapsack(m, w, p):
    ratios = [va/we for va,we in zip(p, w)]        # profit/weight ratio and zip to combine two lists
    n = len(w)                      # the items as no of weights
    index = list(range(n))               # storing from 0 to number of items in list
    index.sort(key=lambda i: ratios[i], reverse=True)    # sorting the list indices according to the profit/weight ratio
    max_value = 0             # initilasing the maxvalue
    fractions = [0]*n        # initialsing the fraction list by 0's, when considered changed to 1
    for i in index:
        if w[i] <= m:              # if weight at that index is less than the max capacity of bag
            max_value += p[i]         # add the profit
            m -= w[i]                # decrease the weight of bag
            fractions[i] = 1        # consider the item
        else:
            fractions[i] = m / w[i]         # if not less or equal then consider only the weight choosen from bag
            max_value += p[i]*fractions[i]        # calulate profit* fraction of weight choosen
            break    # break out from loop
    return max_value


p = list(map(int,input("Enter the profits: ").split())) # enter the profits
w = list(map(int,input("Enter the weights: ").split()))  # enter the weights
m = int(input("Enter the maximum capacity of the bag: "))
print("The maximum profit computed is: ", knapsack(m, w, p))
