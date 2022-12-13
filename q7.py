def find_possible_ways(coins, sum):
    size = len(coins)

    # Declaring a 2-D array
    # for storing solutions to subproblems:
    arr = [[0] * (sum + 1) for x in range(size + 1)]

    # Initializing first column of array to 1
    # because a sum of 0 can be made
    # in one possible way: {0}
    for i in range(size + 1):
        arr[i][0] = 1

    # Applying the recursive solution:
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] > j:  # Cannot pick the highest coin:
                arr[i][j] = arr[i - 1][j]
            else:  # Pick the highest coin:
                arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]

    return arr[size][sum]


# pseduo code:
# 1. Create a 2D array of size (n+1)*(sum+1)
# 2. Initialize the first column of the array to 1
# 3. For each coin, for each sum, check if the coin is greater than the sum
# 4. If the coin is greater than the sum, then the number of ways to make the sum is the same as the number of ways to make the sum without the coin
# 5. If the coin is less than the sum, then the number of ways to make the sum is the number of ways to make the sum without the coin plus the number of ways to make the sum with the coin
# 6. Return the last element of the array

# overall equation for running time:
# O(n*sum)

# Big O equation:
# O(n*sum)

if __name__ == '__main__':
    S = [1, 2, 3]
    sum = 5

    sum2 = 10
    coins2 = [2, 5, 3, 6]

    print(find_possible_ways(S, sum))
    print(find_possible_ways(coins2, sum2))
