

def main(prices, k):
    total = 0
    for i in range(len(prices)):
        if k - total < prices[i]:
            return i
        else:
            total += prices[i]
    return total


# pseduo code:
# 1. Create a variable to store the total
# 2. For each price in the array, check if the budget minus the total is less than the price
# 3. If the budget minus the total is less than the price, then return the index of the price
# 4. If the budget minus the total is greater than the price, then add the price to the total
# 5. Return the total


# overall equation for running time:
# T = O(n)

# test
if __name__ == '__main__':
    prices = [2, 3, 1, 6, 4, 7]
    budget = 12

    prices2 = [1, 2, 3, 4]
    budget2 = 7

    print(main(prices, budget))
    print(main(prices2, budget2))
